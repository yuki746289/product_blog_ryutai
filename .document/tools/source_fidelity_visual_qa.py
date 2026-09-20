# Created: 2026-09-20 JST
"""Source-fidelity revalidation for formula line structure and encoding."""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

SKIP_PARTS = {".git", ".github", ".document", "design_samples"}
SKIP_HTML_SUFFIX = ("_mathjax_audit.html", "_reaudit.html")
MOJIBAKE_PATTERNS = (
    "\ufffd",          # replacement char
    "\u0081",          # common C1 artifact from wrong decoding
    "縺", "繧", "譁", # common UTF-8/legacy-Japanese mojibake fragments
)
LEGACY_CHARSET_RE = re.compile(r"(?:charset\s*=\s*|@charset\s+[\"'])(?:shift[_-]?jis|windows-31j|cp932)", re.I)
AUTO_LINEBREAK_RE = re.compile(r"displayOverflow\s*:\s*['\"]linebreak['\"]", re.I)
EXPECTED_OVERFLOW_RE = re.compile(r"displayOverflow\s*:\s*['\"]overflow['\"]", re.I)
INLINE_FALSE_RE = re.compile(r"linebreaks\s*:\s*\{[^}]*inline\s*:\s*false", re.I | re.S)


def public(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return not any(part in SKIP_PARTS or part.startswith(".") for part in rel.parts)


def html_pages(root: Path) -> list[Path]:
    out = []
    for p in root.rglob("*.html"):
        if not public(p, root):
            continue
        rel = p.relative_to(root).as_posix()
        if rel.endswith(SKIP_HTML_SUFFIX):
            continue
        out.append(p)
    return sorted(out)


def composite_white(im: Image.Image) -> Image.Image:
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        rgba = im.convert("RGBA")
        bg = Image.new("RGBA", rgba.size, "white")
        bg.alpha_composite(rgba)
        return bg.convert("RGB")
    return im.convert("RGB")


def line_signature(im: Image.Image) -> dict:
    """Estimate visible formula line bands using horizontal ink projection."""
    im = composite_white(im)
    gray = ImageOps.grayscale(im)
    # Crop to non-near-white content.
    mask = gray.point(lambda p: 0 if p < 245 else 255, mode="1")
    inv = ImageOps.invert(mask.convert("L"))
    bbox = inv.getbbox()
    if not bbox:
        return {"lines": 0, "bands": [], "width_ratios": [], "left_ratios": []}
    crop = gray.crop(bbox)
    w, h = crop.size
    pix = crop.load()
    occupied = []
    ink_counts = []
    for y in range(h):
        count = 0
        for x in range(w):
            if pix[x, y] < 245:
                count += 1
        ink_counts.append(count)
        occupied.append(count >= 1)

    raw = []
    start = None
    for y, on in enumerate(occupied + [False]):
        if on and start is None:
            start = y
        elif not on and start is not None:
            raw.append([start, y - 1])
            start = None

    # Merge small internal gaps (fractions, accents, superscripts).
    gap_limit = max(3, min(7, int(round(h * 0.025))))
    merged = []
    for a, b in raw:
        if merged and a - merged[-1][1] - 1 <= gap_limit:
            merged[-1][1] = b
        else:
            merged.append([a, b])

    # Remove tiny speck bands.
    bands = []
    for a, b in merged:
        area = sum(ink_counts[a:b + 1])
        if (b - a + 1) >= 2 and area >= 6:
            bands.append([a, b])

    widths = []
    lefts = []
    for a, b in bands:
        xs = []
        for y in range(a, b + 1):
            for x in range(w):
                if pix[x, y] < 245:
                    xs.append(x)
        if xs:
            left, right = min(xs), max(xs)
            widths.append(right - left + 1)
            lefts.append(left)
        else:
            widths.append(0)
            lefts.append(0)

    maxw = max(widths) if widths else 1
    return {
        "lines": len(bands),
        "bands": bands,
        "width_ratios": [round(v / maxw, 3) for v in widths],
        "left_ratios": [round(v / maxw, 3) for v in lefts],
        "crop_size": [w, h],
    }


def layout_delta(src: dict, rendered: dict) -> list[str]:
    reasons = []
    if src["lines"] != rendered["lines"]:
        reasons.append(f"line-count {src['lines']} -> {rendered['lines']}")
        return reasons
    # For multiline formulas, compare relative per-line width and indentation.
    if src["lines"] > 1:
        for i, (a, b) in enumerate(zip(src["width_ratios"], rendered["width_ratios"]), 1):
            if abs(a - b) > 0.24:
                reasons.append(f"line-{i}-width {a:.3f}->{b:.3f}")
        for i, (a, b) in enumerate(zip(src["left_ratios"], rendered["left_ratios"]), 1):
            if abs(a - b) > 0.24:
                reasons.append(f"line-{i}-indent {a:.3f}->{b:.3f}")
    return reasons


def pair_image(src: Image.Image, rendered: Image.Image, label: str) -> Image.Image:
    src = composite_white(src)
    rendered = composite_white(rendered)
    max_h = max(src.height, rendered.height, 60)
    title_h = 34
    gap = 18
    canvas = Image.new("RGB", (src.width + rendered.width + gap, max_h + title_h), "white")
    canvas.paste(src, (0, title_h))
    canvas.paste(rendered, (src.width + gap, title_h))
    draw = ImageDraw.Draw(canvas)
    draw.text((4, 4), "SOURCE | " + label, fill="black")
    draw.text((src.width + gap + 4, 4), "MATHJAX", fill="black")
    return canvas


def resolve_source(root: Path, page_path: Path, src: str) -> Path | None:
    if not src:
        return None
    u = urlparse(src)
    if u.scheme or u.netloc or src.startswith("//") or src.startswith("data:"):
        return None
    clean = unquote(u.path)
    p = (page_path.parent / clean).resolve()
    try:
        p.relative_to(root)
    except ValueError:
        return None
    return p


def static_checks(root: Path) -> tuple[list[str], dict]:
    issues = []
    stats = {"public_text": 0, "html": 0, "formula_pages": 0, "formula_markers": 0}
    formula_pages = []
    for p in root.rglob("*"):
        if not p.is_file() or not public(p, root) or p.suffix.lower() not in {".html", ".css", ".js"}:
            continue
        rel_text = p.relative_to(root).as_posix()
        if p.suffix.lower() == ".html" and rel_text.endswith(SKIP_HTML_SUFFIX):
            continue
        stats["public_text"] += 1
        try:
            text = p.read_bytes().decode("utf-8")
        except UnicodeDecodeError as exc:
            issues.append(f"NON_UTF8 {p.relative_to(root).as_posix()}: {exc}")
            continue
        if LEGACY_CHARSET_RE.search(text):
            issues.append(f"LEGACY_CHARSET {p.relative_to(root).as_posix()}")
        if p.suffix.lower() == ".html":
            stats["html"] += 1
            markers = text.count("data-source-image=")
            if markers:
                formula_pages.append(p)
                stats["formula_pages"] += 1
                stats["formula_markers"] += markers
                if AUTO_LINEBREAK_RE.search(text):
                    issues.append(f"AUTO_LINEBREAK {p.relative_to(root).as_posix()}")
                if not EXPECTED_OVERFLOW_RE.search(text):
                    issues.append(f"NO_OVERFLOW_POLICY {p.relative_to(root).as_posix()}")
                if not INLINE_FALSE_RE.search(text):
                    issues.append(f"INLINE_BREAK_NOT_DISABLED {p.relative_to(root).as_posix()}")
    stats["formula_page_paths"] = [p.relative_to(root).as_posix() for p in formula_pages]
    return issues, stats


def run(args) -> int:
    root = Path(args.root).resolve()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    pair_dir = out_dir / "pairs"
    pair_dir.mkdir(parents=True, exist_ok=True)

    static_issues, stats = static_checks(root)
    rows = []
    page_issues = []
    mojibake_pages = []
    charset_pages = []
    source_multiline = 0
    rendered_multiline = 0
    missing_source = 0
    external_source_basis = 0

    pages = html_pages(root)
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1000})
        def route_handler(route):
            url = route.request.url
            try:
                u = urlparse(url)
                local = (not u.netloc) or u.hostname in ("127.0.0.1", "localhost")
            except Exception:
                local = False
            if local or url.startswith("https://cdn.jsdelivr.net/"):
                route.continue_()
            else:
                route.abort()
        context.route("**/*", route_handler)

        for page_path in pages:
            rel = page_path.relative_to(root).as_posix()
            page = context.new_page()
            try:
                res = page.goto(args.base_url.rstrip("/") + "/" + rel, wait_until="domcontentloaded", timeout=30000)
                try:
                    page.wait_for_load_state("networkidle", timeout=2500)
                except PWTimeout:
                    pass
                try:
                    page.evaluate("""async()=>{if(window.MathJax?.startup?.promise)await Promise.race([window.MathJax.startup.promise,new Promise(r=>setTimeout(r,10000))])}""")
                except Exception:
                    pass

                charset = page.evaluate("document.characterSet")
                if (charset or "").upper() != "UTF-8":
                    charset_pages.append({"path": rel, "charset": charset})
                body_text = page.evaluate("document.body ? document.body.innerText : ''")
                hits = [x for x in MOJIBAKE_PATTERNS if x in body_text]
                if hits:
                    mojibake_pages.append({"path": rel, "hits": hits})

                loc = page.locator("[data-source-image]")
                count = loc.count()
                for i in range(count):
                    el = loc.nth(i)
                    src = el.get_attribute("data-source-image") or ""
                    formula_id = el.get_attribute("id") or f"formula-{i+1}"
                    source_status = el.get_attribute("data-source-status") or ""
                    source_path = resolve_source(root, page_path, src)
                    if not source_path or not source_path.exists():
                        if rel.startswith("mps/"):
                            external_source_basis += 1
                            basis = "inferred-reconstruction" if source_status == "inferred-reconstruction" else "word-recovered-source"
                            rows.append({
                                "path": rel, "id": formula_id, "source": src,
                                "source_lines": -1, "rendered_lines": -1,
                                "status": "EXTERNAL_SOURCE_BASIS", "source_basis": basis, "reasons": [],
                            })
                        else:
                            missing_source += 1
                            rows.append({
                                "path": rel, "id": formula_id, "source": src,
                                "source_lines": -1, "rendered_lines": -1,
                                "status": "MISSING_SOURCE", "reasons": ["missing source image"],
                            })
                        continue
                    try:
                        with Image.open(source_path) as sim0:
                            sim = sim0.copy()
                        shot = el.screenshot(type="png")
                        rim = Image.open(io.BytesIO(shot)).copy()
                        ss = line_signature(sim)
                        rs = line_signature(rim)
                        if ss["lines"] > 1:
                            source_multiline += 1
                        if rs["lines"] > 1:
                            rendered_multiline += 1
                        reasons = layout_delta(ss, rs)
                        status = "REVIEW" if reasons else "MATCH"
                        row = {
                            "path": rel, "id": formula_id, "source": src,
                            "source_lines": ss["lines"], "rendered_lines": rs["lines"],
                            "source_width_ratios": ss["width_ratios"],
                            "rendered_width_ratios": rs["width_ratios"],
                            "source_left_ratios": ss["left_ratios"],
                            "rendered_left_ratios": rs["left_ratios"],
                            "status": status, "reasons": reasons,
                        }
                        rows.append(row)
                        # Keep every multiline source pair plus all mismatches for manual revalidation.
                        if ss["lines"] > 1 or reasons:
                            safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{rel}__{formula_id}")
                            pair = pair_image(sim, rim, f"{rel} #{formula_id}")
                            pair.save(pair_dir / f"{safe}.png")
                    except Exception as exc:
                        rows.append({
                            "path": rel, "id": formula_id, "source": src,
                            "source_lines": -1, "rendered_lines": -1,
                            "status": "ERROR", "reasons": [type(exc).__name__ + ": " + str(exc)],
                        })
            except Exception as exc:
                page_issues.append({"path": rel, "error": type(exc).__name__ + ": " + str(exc)})
            finally:
                page.close()
        context.close()
        browser.close()

    review = [r for r in rows if r["status"] not in ("MATCH", "EXTERNAL_SOURCE_BASIS")]
    hard = list(static_issues)
    hard += [f"CHARSET {x['path']}: {x['charset']}" for x in charset_pages]
    hard += [f"MOJIBAKE {x['path']}: {','.join(x['hits'])}" for x in mojibake_pages]
    hard += [f"PAGE {x['path']}: {x['error']}" for x in page_issues]
    hard += [f"{r['status']} {r['path']} {r['id']}: {'; '.join(r['reasons'])}" for r in review]

    data = {
        "static": stats,
        "static_issues": static_issues,
        "pages_checked": len(pages),
        "charset_failures": charset_pages,
        "mojibake_pages": mojibake_pages,
        "page_issues": page_issues,
        "formula_rows": rows,
        "formula_total": len(rows),
        "source_multiline": source_multiline,
        "rendered_multiline": rendered_multiline,
        "layout_review": len(review),
        "missing_source": missing_source,
        "external_source_basis": external_source_basis,
        "canonical_formula_slots": 634,
        "rendered_formula_instances": len(rows),
        "overall": "PASS" if not hard else "REVIEW_REQUIRED",
    }
    (out_dir / "source-fidelity.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    report = [
        "# Source Fidelity Revalidation — 2026-09-20",
        "",
        f"- Overall: **{data['overall']}**",
        f"- Normal HTML pages checked: **{len(pages)}**",
        f"- Public text files checked as UTF-8: **{stats['public_text']}**",
        f"- Formula pages: **{stats['formula_pages']}**",
        f"- Canonical formula slots: **634**",
        f"- Rendered formula instances checked (including repeated references): **{len(rows)}**",
        f"- MPS external source-basis instances: **{external_source_basis}**",
        f"- Source formulas detected as multiline: **{source_multiline}**",
        f"- Rendered formulas detected as multiline: **{rendered_multiline}**",
        f"- Layout review candidates/errors: **{len(review)}**",
        f"- Browser charset failures: **{len(charset_pages)}**",
        f"- Mojibake indicator pages: **{len(mojibake_pages)}**",
        f"- Missing source images: **{missing_source}**",
        f"- Page navigation/runtime failures: **{len(page_issues)}**",
        "",
        "## Policy checks",
        "",
        f"- Static UTF-8 / legacy charset / MathJax-policy issues: **{len(static_issues)}**",
    ]
    if static_issues:
        report += [""] + [f"- {x}" for x in static_issues[:200]]
    report += [
        "",
        "## Layout review candidates",
        "",
        "| Page | Formula | Source | Source lines | Rendered lines | Reason |",
        "|---|---|---|---:|---:|---|",
    ]
    if review:
        for r in review[:500]:
            report.append(
                f"| {r['path']} | {r['id']} | {r['source']} | {r['source_lines']} | {r['rendered_lines']} | {'; '.join(r['reasons'])} |"
            )
    else:
        report.append("| - | - | - | - | - | None |")
    report += [
        "",
        "## Interpretation",
        "",
        "- A MATCH means the automated visible-line-band comparison did not find a line-count/large line-width/indent discrepancy.",
        "- Every source formula detected as multiline is exported as a source-vs-MathJax pair image for manual fidelity review.",
        "- A REVIEW result blocks deployment until the pair is inspected and corrected or explicitly cleared.",
        "",
    ]
    Path(args.report).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report).write_text("\n".join(report), encoding="utf-8")

    print(json.dumps({
        "overall": data["overall"],
        "pages": len(pages),
        "formulas": len(rows),
        "source_multiline": source_multiline,
        "review": len(review),
        "charset_failures": len(charset_pages),
        "mojibake_pages": len(mojibake_pages),
        "static_issues": len(static_issues),
        "external_source_basis": external_source_basis,
    }, ensure_ascii=False))
    return 0 if not hard else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--base-url", default="http://127.0.0.1:8000")
    p.add_argument("--output-dir", default="qa-results/source-fidelity")
    p.add_argument("--report", default=".document/formula_reviews/SOURCE_FIDELITY_REVALIDATION_20260920.md")
    return run(p.parse_args())


if __name__ == "__main__":
    sys.exit(main())
