from pathlib import Path
import re

ROOT=Path(".")
SKIP_PARTS={".git",".github",".document","design_samples"}
SKIP_SUFFIX=("_mathjax_audit.html","_reaudit.html")
MATH_BLOCK_RE=re.compile(r'(<div class="math-block"[^>]*>)([\s\S]*?)(</div>)',re.I)

TARGET_ENVS=("aligned","alignedat","gathered","split")
BEGIN_RE=re.compile(r'\\begin\{([A-Za-z*]+)\}')
END_RE=re.compile(r'\\end\{([A-Za-z*]+)\}')

def public_htmls():
    for p in sorted(ROOT.rglob("*.html")):
        rel=p.relative_to(ROOT)
        s=rel.as_posix()
        if any(part in SKIP_PARTS or part.startswith(".") for part in rel.parts):
            continue
        if s.endswith(SKIP_SUFFIX):
            continue
        yield p

def normalize_env_body(body:str)->tuple[str,int]:
    out=[]
    i=0
    nested=0
    changed=0
    while i<len(body):
        bm=BEGIN_RE.match(body,i)
        if bm:
            nested+=1
            out.append(bm.group(0)); i=bm.end(); continue
        em=END_RE.match(body,i)
        if em:
            nested=max(0,nested-1)
            out.append(em.group(0)); i=em.end(); continue
        if body.startswith(r"\\",i):
            out.append(r"\\"); i+=2
            if nested==0:
                # normalize explicit row spacing or add it
                m=re.match(r'\[[^\]]*\]',body[i:])
                if m:
                    old=m.group(0)
                    if old!="[6pt]":
                        out.append("[6pt]")
                        changed+=1
                    else:
                        out.append(old)
                    i+=len(old)
                else:
                    out.append("[6pt]")
                    changed+=1
            continue
        out.append(body[i]); i+=1
    return "".join(out),changed

def normalize_target_envs(text:str)->tuple[str,int]:
    total=0
    for env in TARGET_ENVS:
        pattern=re.compile(r'(\\begin\{'+re.escape(env)+r'\})([\s\S]*?)(\\end\{'+re.escape(env)+r'\})')
        def repl(m):
            nonlocal total
            nb,n=normalize_env_body(m.group(2))
            total+=n
            return m.group(1)+nb+m.group(3)
        text=pattern.sub(repl,text)
    return text,total

files_changed=0
rows_changed=0
for p in public_htmls():
    original=p.read_text(encoding="utf-8")
    file_rows=0
    def block_repl(m):
        nonlocal_dummy=None
        global_placeholder=0
        body,n=normalize_target_envs(m.group(2))
        nonlocal_holder[0]+=n
        return m.group(1)+body+m.group(3)
    nonlocal_holder=[0]
    updated=MATH_BLOCK_RE.sub(block_repl,original)
    file_rows=nonlocal_holder[0]
    if updated!=original:
        p.write_text(updated,encoding="utf-8")
        files_changed+=1
        rows_changed+=file_rows

print(f"files_changed={files_changed} rows_changed={rows_changed}")
