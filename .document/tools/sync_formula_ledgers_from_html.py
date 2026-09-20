# Created: 2026-09-20 JST
"""Synchronize formula-review JSON LaTeX with the current audited HTML.

Only formula entries that already have a 'latex' field are updated.
Rich HTML entries and non-formula metadata are left untouched.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT=Path(".").resolve()
REV=ROOT/".document"/"formula_reviews"

BLOCK_RE=re.compile(
    r'<(?P<tag>div|span)\b(?P<attrs>[^>]*\bdata-source-image="(?P<src>[^"]+)"[^>]*)>'
    r'(?P<body>[\s\S]*?)</(?P=tag)>',
    re.I,
)

def formulas_from_html(page: Path):
    text=page.read_text(encoding="utf-8")
    out={}
    for m in BLOCK_RE.finditer(text):
        src=m.group("src")
        body=m.group("body").strip()
        if body.startswith(r"\[") or body.startswith(r"\("):
            out[Path(src).name]=body
    return out

def page_objects(data):
    if isinstance(data,dict) and isinstance(data.get("page"),str) and isinstance(data.get("formulas"),list):
        yield data
    if isinstance(data,dict) and isinstance(data.get("pages"),list):
        for p in data["pages"]:
            if isinstance(p,dict) and isinstance(p.get("page"),str) and isinstance(p.get("formulas"),list):
                yield p

def main():
    changed_files=[]
    updated=0
    missing=[]
    for jf in sorted(REV.glob("*_formulas.json")):
        data=json.loads(jf.read_text(encoding="utf-8"))
        file_changed=False
        for obj in page_objects(data):
            page=ROOT/obj["page"]
            if not page.exists():
                continue
            current=formulas_from_html(page)
            for f in obj["formulas"]:
                if not isinstance(f,dict) or "latex" not in f or "image" not in f:
                    continue
                image=Path(str(f["image"])).name
                if image not in current:
                    # Inline/rich/special entries can legitimately lack a direct block.
                    missing.append(f"{obj['page']}::{image}")
                    continue
                if f["latex"] != current[image]:
                    f["latex"]=current[image]
                    file_changed=True
                    updated+=1
        if file_changed:
            jf.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
            changed_files.append(jf.relative_to(ROOT).as_posix())
    print(f"ledger_files_changed={len(changed_files)} formula_entries_updated={updated} unmatched_entries={len(missing)}")
    for p in changed_files:
        print("LEDGER_CHANGED "+p)
    return 0

if __name__=="__main__":
    sys.exit(main())
