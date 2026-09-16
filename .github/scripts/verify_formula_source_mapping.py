#!/usr/bin/env python3
# Created: 2026-09-16
# Purpose: Verify that every MathJax conversion block is traceable to its original formula image.
from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

MATH_BLOCK_RE = re.compile(
    r"<(?P<tag>div|p|span)\b(?P<attrs>[^>]*\bclass\s*=\s*[\"'][^\"']*\bmath-block\b[^\"']*[\"'][^>]*)>"
    r"(?P<body>.*?)</(?P=tag)>",
    re.IGNORECASE | re.DOTALL,
)
ATTR_RE = re.compile(
    r"(?P<name>[A-Za-z_:][-A-Za-z0-9_:.]*)\s*=\s*(?P<quote>[\"'])(?P<value>.*?)(?P=quote)",
    re.DOTALL,
)
FORMULA_IMAGE_RE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*[\"'](?P<src>[^\"']*(?:\.files/)?image\d+\.(?:png|gif|jpg|jpeg))[\"'][^>]*>",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Issue:
    page: Path
    message: str


def decode_html(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "cp932", "shift_jis"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def attrs_dict(raw_attrs: str) -> dict[str, str]:
    return {
        match.group("name").lower(): html.unescape(match.group("value"))
        for match in ATTR_RE.finditer(raw_attrs)
    }


def resolve_source_image(page: Path, source: str) -> Path:
    source = source.split("?", 1)[0].split("#", 1)[0]
    return (page.parent / source).resolve()


def iter_html_files(root: Path) -> Iterable[Path]:
    excluded_roots = {".git"}
    for path in root.rglob("*.html"):
        if any(part in excluded_roots for part in path.parts):
            continue
        yield path


def audit(root: Path) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    seen_ids: dict[str, Path] = {}
    stats = {
        "html_pages": 0,
        "math_blocks": 0,
        "mapped_math_blocks": 0,
        "formula_images_remaining": 0,
        "pages_with_math_blocks": 0,
        "pages_with_formula_images": 0,
    }

    root = root.resolve()

    for page in iter_html_files(root):
        stats["html_pages"] += 1
        text = decode_html(page)
        matches = list(MATH_BLOCK_RE.finditer(text))
        image_matches = list(FORMULA_IMAGE_RE.finditer(text))

        if matches:
            stats["pages_with_math_blocks"] += 1
        if image_matches:
            stats["pages_with_formula_images"] += 1
            stats["formula_images_remaining"] += len(image_matches)

        for match in matches:
            stats["math_blocks"] += 1
            attrs = attrs_dict(match.group("attrs"))
            formula_id = attrs.get("id", "").strip()
            source = attrs.get("data-source-image", "").strip()

            if not formula_id:
                issues.append(Issue(page, "math-block has no id"))
            elif formula_id in seen_ids:
                issues.append(
                    Issue(
                        page,
                        f"duplicate formula id '{formula_id}' (first: {seen_ids[formula_id].relative_to(root)})",
                    )
                )
            else:
                seen_ids[formula_id] = page

            if not source:
                issues.append(Issue(page, f"{formula_id or '[no id]'} has no data-source-image"))
                continue

            stats["mapped_math_blocks"] += 1
            source_path = resolve_source_image(page, source)
            try:
                source_path.relative_to(root)
            except ValueError:
                issues.append(
                    Issue(page, f"{formula_id or '[no id]'} source escapes repository: {source}")
                )
                continue

            if not source_path.is_file():
                issues.append(
                    Issue(page, f"{formula_id or '[no id]'} source image not found: {source}")
                )

            body = match.group("body")
            if "\\[" not in body and "\\(" not in body:
                issues.append(
                    Issue(page, f"{formula_id or '[no id]'} has no MathJax delimiter")
                )

    return issues, stats


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check structural traceability of MathJax formula conversions. "
            "This does NOT certify visual/content equality with the source image."
        )
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="repository root (default: current directory)",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"ERROR: root directory not found: {root}", file=sys.stderr)
        return 2

    issues, stats = audit(root)

    print("Formula source mapping audit")
    print("----------------------------")
    for key, value in stats.items():
        print(f"{key}: {value}")

    if issues:
        print("\nStructural issues:")
        for issue in issues:
            try:
                page = issue.page.resolve().relative_to(root.resolve())
            except ValueError:
                page = issue.page
            print(f"- {page}: {issue.message}")
        print(
            "\nFAILED: structural mapping issues found. "
            "Source-image equality must still be checked manually with CHECKLIST_FORMULA_CONVERSION.md."
        )
        return 1

    print(
        "\nOK: every detected math-block has an id and an existing source-image mapping. "
        "This is only a structural check; Pass 1/Pass 2 visual comparison is still mandatory."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
