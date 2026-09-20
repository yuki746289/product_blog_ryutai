from pathlib import Path
import re, json

ROOT=Path(".").resolve()
SKIP={".git",".github",".document","design_samples"}
AUDIT_SUFFIX=("_mathjax_audit.html","_reaudit.html")
BLOCK=re.compile(r'<div class="math-block"\s+id="([^"]+)"[^>]*>([\s\S]*?)</div>',re.I)
ALIGNED=re.compile(r'\\begin\{aligned\}([\s\S]*?)\\end\{aligned\}',re.I)

issues=[]
pages=0
blocks=0
for p in sorted(ROOT.rglob("*.html")):
    rel=p.relative_to(ROOT)
    s=rel.as_posix()
    if any(part in SKIP or part.startswith(".") for part in rel.parts):
        continue
    if s.endswith(AUDIT_SUFFIX):
        continue
    pages+=1
    text=p.read_text(encoding="utf-8")
    for m in BLOCK.finditer(text):
        blocks+=1
        fid=m.group(1)
        for a in ALIGNED.finditer(m.group(2)):
            body=a.group(1)
            # Old construction puts '=' on the left side of the alignment tab,
            # while continuation + / - are on the right side.
            if "={}&" in body and ("&+" in body or "&-" in body):
                issues.append({"page":s,"id":fid,"reason":"mixed alignment column: ={}& with &+ / &-"})
                break

report=[
"# Operator Alignment Audit — 2026-09-20","",
f"- Public HTML pages scanned: **{pages}**",
f"- Math blocks scanned: **{blocks}**",
f"- Mixed-column operator issues: **{len(issues)}**","",
"| Page | Formula | Reason |","|---|---|---|"
]
if issues:
    report += [f"| {x['page']} | {x['id']} | {x['reason']} |" for x in issues]
else:
    report.append("| - | - | None |")
Path(".document/formula_reviews/OPERATOR_ALIGNMENT_AUDIT_20260920.md").write_text("\n".join(report)+"\n",encoding="utf-8")
Path(".document/formula_reviews/OPERATOR_ALIGNMENT_AUDIT_20260920.json").write_text(json.dumps({"pages":pages,"blocks":blocks,"issues":issues},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"pages":pages,"blocks":blocks,"issues":len(issues)},ensure_ascii=False))
raise SystemExit(1 if issues else 0)
