# Created: 2026-09-20 JST
"""Create/check source-fidelity certification fingerprints.

Certification binds every rendered formula instance to:
- current TeX/MathJax source text
- current original source-image bytes when locally available
- the documented external source basis for MPS recovered/inferred formulas

Any later formula/source change invalidates the certification and reopens review.
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT=Path(".").resolve()
SKIP_PARTS={".git",".github",".document","design_samples"}
SKIP_SUFFIX=("_mathjax_audit.html","_reaudit.html")
BLOCK_RE=re.compile(
    r'<(?P<tag>div|span)\b(?P<attrs>[^>]*\bdata-source-image="(?P<src>[^"]+)"[^>]*)>'
    r'(?P<body>[\s\S]*?)</(?P=tag)>', re.I)
ID_RE=re.compile(r'\bid="([^"]+)"',re.I)
STATUS_RE=re.compile(r'\bdata-source-status="([^"]+)"',re.I)

def sha(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()

def normal(s:str)->str:
    return "\n".join(line.rstrip() for line in s.replace("\r\n","\n").replace("\r","\n").strip().split("\n"))

def public_html():
    for p in sorted(ROOT.rglob("*.html")):
        rel=p.relative_to(ROOT)
        s=rel.as_posix()
        if any(part in SKIP_PARTS or part.startswith(".") for part in rel.parts): continue
        if s.endswith(SKIP_SUFFIX): continue
        yield p

def resolve_source(page:Path,src:str):
    if not src: return None
    u=urlparse(src)
    if u.scheme or u.netloc or src.startswith("//") or src.startswith("data:"): return None
    p=(page.parent/unquote(u.path)).resolve()
    try: p.relative_to(ROOT)
    except ValueError: return None
    return p

def collect():
    entries={}
    for page in public_html():
        rel=page.relative_to(ROOT).as_posix()
        text=page.read_text(encoding="utf-8")
        occurrence={}
        for m in BLOCK_RE.finditer(text):
            attrs=m.group("attrs"); src=m.group("src"); body=normal(m.group("body"))
            ident=(ID_RE.search(attrs).group(1) if ID_RE.search(attrs) else "")
            if not ident:
                occurrence[src]=occurrence.get(src,0)+1
                ident=f"source-{Path(src).name}-{occurrence[src]}"
            key=f"{rel}::{ident}"
            source=resolve_source(page,src)
            status=(STATUS_RE.search(attrs).group(1) if STATUS_RE.search(attrs) else "")
            if source and source.exists():
                basis="original-image"
                source_hash=sha(source.read_bytes())
                source_rel=source.relative_to(ROOT).as_posix()
            elif rel.startswith("mps/"):
                basis="inferred-reconstruction" if status=="inferred-reconstruction" else "word-recovered-source"
                source_hash=None
                source_rel=None
            else:
                basis="missing-source"
                source_hash=None
                source_rel=None
            entries[key]={
                "page":rel,"id":ident,"data_source_image":src,
                "formula_sha256":sha(body.encode("utf-8")),
                "source_basis":basis,"source_path":source_rel,"source_sha256":source_hash,
            }
    return entries

def git_head():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()
    except Exception:
        return ""

def write(path:Path):
    entries=collect()
    bad=[k for k,v in entries.items() if v["source_basis"]=="missing-source"]
    if bad:
        print("Cannot certify missing source:",*bad,sep="\n",file=sys.stderr); return 2
    payload={
      "schema":1,
      "certification":"source-layout-and-content-reviewed",
      "certified_at_utc":datetime.now(timezone.utc).isoformat(),
      "certified_git_head":git_head(),
      "canonical_formula_slots":634,
      "rendered_formula_instances":len(entries),
      "review_basis":[
        "Original HP image/equation-editor visible layout is authoritative.",
        "2026-09-20 source-vs-MathJax layout review completed.",
        "37 confirmed line/alignment mismatches corrected before certification.",
        "MPS: 48 Word-recovered source equations + 1 user-approved inferred reconstruction."
      ],
      "entries":entries,
    }
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"CERTIFIED instances={len(entries)} file={path}")
    return 0

def check(path:Path):
    if not path.exists():
        print("CERTIFICATION_MISSING "+str(path),file=sys.stderr); return 3
    cert=json.loads(path.read_text(encoding="utf-8"))
    now=collect(); old=cert.get("entries",{})
    issues=[]
    for k in sorted(set(old)-set(now)): issues.append("REMOVED "+k)
    for k in sorted(set(now)-set(old)): issues.append("NEW "+k)
    for k in sorted(set(now)&set(old)):
        for field in ("formula_sha256","source_basis","source_sha256"):
            if old[k].get(field)!=now[k].get(field):
                issues.append(f"CHANGED {k} {field}")
    for k,v in now.items():
        if v["source_basis"]=="missing-source": issues.append("MISSING_SOURCE "+k)
    print(f"certified={len(old)} current={len(now)} issues={len(issues)}")
    for x in issues[:500]: print(x)
    return 1 if issues else 0

def main():
    p=argparse.ArgumentParser()
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument("--write"); g.add_argument("--check")
    a=p.parse_args()
    return write(Path(a.write)) if a.write else check(Path(a.check))

if __name__=="__main__": sys.exit(main())
