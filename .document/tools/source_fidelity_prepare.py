# Created: 2026-09-20 JST
"""One-time normalization for source-fidelity revalidation.

Public text files must already be UTF-8. This script refuses to guess or transcode
undecodable files. It only aligns declarations/configuration with the UTF-8 bytes
and removes MathJax automatic line breaking.
"""
from pathlib import Path
import re
import sys

ROOT = Path(".").resolve()
SKIP_PARTS = {".git", ".github", ".document", "design_samples"}

html_charset = re.compile(r"charset\s*=\s*(?:shift[_-]?jis|windows-31j|cp932)", re.I)
css_charset = re.compile(r'@charset\s+["\'](?:shift[_-]?jis|windows-31j|cp932)["\']\s*;', re.I)
display_linebreak = re.compile(r"displayOverflow\s*:\s*(['\"])linebreak\1", re.I)
linebreak_block = re.compile(
    r"linebreaks\s*:\s*\{\s*inline\s*:\s*true\s*,\s*width\s*:\s*(['\"])100%\1\s*,\s*lineleading\s*:\s*0?\.2\s*\}",
    re.I,
)


def public(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return not any(part in SKIP_PARTS or part.startswith(".") for part in rel.parts)


def read_utf8(path: Path) -> str:
    data = path.read_bytes()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"NON_UTF8: {path.relative_to(ROOT)}: {exc}") from exc


def write_if_changed(path: Path, old: str, new: str) -> bool:
    if new == old:
        return False
    path.write_text(new, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed = []
    non_utf8 = []

    targets = [p for p in ROOT.rglob("*") if p.is_file() and public(p) and p.suffix.lower() in {".html", ".css", ".js"}]
    for path in targets:
        try:
            text = read_utf8(path)
        except RuntimeError as exc:
            non_utf8.append(str(exc))
            continue

        new = text
        if path.suffix.lower() == ".html":
            new = html_charset.sub("charset=UTF-8", new)
            new = display_linebreak.sub("displayOverflow:'overflow'", new)
            new = linebreak_block.sub("linebreaks:{inline:false}", new)
        elif path.suffix.lower() == ".css":
            new = css_charset.sub('@charset "UTF-8";', new)
            if path.relative_to(ROOT).as_posix() == "css/math.css":
                new = new.replace(
                    "overflow: visible;\n\tmargin: 12px 0 18px 0;",
                    "overflow-x: auto;\n\toverflow-y: hidden;\n\toverscroll-behavior-x: contain;\n\t-webkit-overflow-scrolling: touch;\n\tmargin: 12px 0 18px 0;",
                    1,
                )

        if write_if_changed(path, text, new):
            changed.append(path.relative_to(ROOT).as_posix())

    if non_utf8:
        print("\n".join(non_utf8))
        return 2

    print(f"public_text_files={len(targets)} changed={len(changed)}")
    by_ext = {}
    for name in changed:
        ext = Path(name).suffix.lower()
        by_ext[ext] = by_ext.get(ext, 0) + 1
    print("changed_by_ext=" + repr(by_ext))
    for name in changed:
        print("CHANGED " + name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
