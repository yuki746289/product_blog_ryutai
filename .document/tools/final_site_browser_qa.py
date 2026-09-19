# Created: 2026-09-19 09:50 JST
"""Sharded final browser QA for product_blog_ryutai."""
import argparse, json, sys
from pathlib import Path
from urllib.parse import quote
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

VPS={"desktop":{"width":1440,"height":1000},"mobile":{"width":390,"height":844}}
MPS={}
SKIP=("_mathjax_audit.html","_reaudit.html")

def pages(root):
    out=[]
    for p in root.rglob("*.html"):
        rel=p.relative_to(root)
        s=rel.as_posix()
        if any(x.startswith(".") for x in rel.parts) or s.endswith(SKIP): continue
        out.append(s)
    return sorted(out)

def inspect(page):
    return page.evaluate(r"""() => {
      const imgs=[...document.images];
      const isLocalSrc=s=>s && !/^https?:/i.test(s) && !s.startsWith('//') && !/^data:/i.test(s);
      const miss=imgs.filter(x=>{
        const s=x.getAttribute('src')||'';
        return isLocalSrc(s) && (!x.complete||x.naturalWidth===0);
      }).map(x=>x.getAttribute('src')||'');
      const formulaTargets=[...document.querySelectorAll('[data-source-image]')];
      const unrenderedTargets=formulaTargets.filter(e=>!e.querySelector('mjx-container')).length;
      const w=document.documentElement.clientWidth;
      const pageOverflow=document.documentElement.scrollWidth>w+2;
      const unc=pageOverflow?[...(document.body?document.body.querySelectorAll('*'):[])].filter(e=>{
        if(e.closest('.math-block')) return false;
        const s=getComputedStyle(e); if(s.position==='fixed'||s.position==='sticky') return false;
        const r=e.getBoundingClientRect(); return r.width>0&&r.height>0&&(r.right>w+2||r.left<-2);
      }).length:0;
      return {matherr:document.querySelectorAll('mjx-merror,.mjx-merror,.MathJax_Error').length,
        unrendered:unrenderedTargets,
        overflow:pageOverflow, uncontained:unc,
        local:[...document.querySelectorAll('.math-block')].filter(e=>e.scrollWidth>e.clientWidth+2).length,
        missing:miss};
    }""")

def issues(r):
    x=[]; exp=MPS.get(r["path"],0); miss=r["missing"]
    if r["status"] and r["status"]>=400: x.append("HTTP "+str(r["status"]))
    if r["nav"]: x.append("navigation")
    if r["console"]: x.append("MathJax console="+str(len(r["console"])))
    if r["matherr"]: x.append("MathJax DOM="+str(r["matherr"]))
    if r["unrendered"]: x.append("unrendered="+str(r["unrendered"]))
    if r["overflow"]: x.append("page overflow")
    if r["uncontained"]: x.append("uncontained="+str(r["uncontained"]))
    if exp:
        if len(miss)!=exp: x.append(f"MPS HOLD expected={exp} actual={len(miss)}")
        if any(s and not s.lower().endswith('.gif') for s in miss): x.append("unexpected MPS missing asset")
    elif miss: x.append("missing images="+str(len(miss)))
    return x

def run(a):
    root=Path(a.root).resolve(); allp=pages(root); todo=allp[a.shard_index::a.shard_count]; rows=[]
    with sync_playwright() as p:
      b=p.chromium.launch(headless=True)
      try:
       for vn,vp in VPS.items():
        c=b.new_context(viewport=vp)
        try:
         for rel in todo:
          pg=c.new_page(); pe=[]; ce=[]
          pg.on("pageerror",lambda e,d=pe:d.append(str(e)))
          pg.on("console",lambda m,d=ce:d.append(m.text) if m.type=="error" and "mathjax" in (m.text or "").lower() else None)
          st=None; nav=""
          try:
           res=pg.goto(a.base_url.rstrip('/')+'/'+quote(rel,safe='/'),wait_until="domcontentloaded",timeout=30000); st=res.status if res else None
           try: pg.wait_for_load_state("networkidle",timeout=2000)
           except PWTimeout: pass
           try: pg.evaluate("async()=>{if(window.MathJax?.startup?.promise)await Promise.race([window.MathJax.startup.promise,new Promise(r=>setTimeout(r,8000))])}")
           except Exception: pass
           try:
            pg.wait_for_function("""() => {
              const t=[...document.querySelectorAll('[data-source-image]')];
              return t.length===0 || t.every(e=>e.querySelector('mjx-container'));
            }""", timeout=8000)
           except PWTimeout: pass
           m=inspect(pg)
          except Exception as e:
           nav=type(e).__name__+": "+str(e); m={"matherr":0,"unrendered":0,"overflow":False,"uncontained":0,"local":0,"missing":[]}
          pg.close(); r={"path":rel,"viewport":vn,"status":st,"nav":nav,"pageerr":pe,"console":ce,**m}; r["issues"]=issues(r); rows.append(r)
        finally: c.close()
      finally: b.close()
    out={"shard":a.shard_index,"shards":a.shard_count,"discovered":len(allp),"rows":rows}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
    bad=sum(bool(r["issues"]) for r in rows); print(f"shard={a.shard_index} pages={len(todo)} checks={len(rows)} failures={bad}"); return bool(bad)

def merge(a):
    fs=sorted(Path(a.merge_dir).glob("shard-*.json")); probs=[]; data=[]
    if len(fs)!=a.expected_shards: probs.append(f"shards expected={a.expected_shards} actual={len(fs)}")
    for f in fs:
      try: data.append(json.loads(f.read_text(encoding="utf-8")))
      except Exception as e: probs.append(f"cannot read {f.name}: {e}")
    rows=[r for d in data for r in d.get("rows",[])]; bad=[r for r in rows if r.get("issues")]
    dc={d.get("discovered") for d in data}; n=next(iter(dc)) if len(dc)==1 else None
    if len(dc)>1: probs.append("inconsistent discovered counts")
    if a.expected_pages and n!=a.expected_pages: probs.append(f"pages expected={a.expected_pages} actual={n}")
    desk=[r for r in rows if r["viewport"]=="desktop"]; actual={}
    for p,e in MPS.items():
      r=next((x for x in desk if x["path"]==p),None); actual[p]=len(r["missing"]) if r else -1
      if not r or actual[p]!=e: probs.append(f"MPS {p} expected={e} actual={actual[p]}")
    if sum(v for v in actual.values() if v>=0)!=0: probs.append("MPS total is not 0")
    mj=sum(r["matherr"]+len(r["console"]) for r in rows); ur=sum(r["unrendered"] for r in rows)
    ov=sum(bool(r["overflow"]) for r in rows); uc=sum(r["uncontained"] for r in rows); pe=sum(len(r["pageerr"]) for r in rows)
    nonm=sum(len(r["missing"]) for r in desk if r["path"] not in MPS); ls=sum(r["local"] for r in rows)
    fail=bool(bad or probs); status="FAIL" if fail else "PASS"
    L=["# Final Site Browser QA — 2026-09-19","",f"- Overall: **{status}**","- Browser: Chromium / Playwright",
       "- Viewports: desktop 1440×1000, mobile 390×844",f"- Discovered normal HTML pages: **{n}**",f"- QA checks: **{len(rows)}**",
       f"- Hard-failure rows: **{len(bad)}**",f"- MPS known missing references: **{sum(v for v in actual.values() if v>=0)}/0**",
       "- Production deployment: not performed.","","## Global metrics","","| Metric | Count |","|---|---:|",
       f"| MathJax errors | {mj} |",f"| Unrendered | {ur} |",f"| Page overflow rows | {ov} |",f"| Uncontained overflow | {uc} |",
       f"| Page errors | {pe} |",f"| Non-MPS missing images (desktop) | {nonm} |",f"| Allowed local math scroll | {ls} |","",
       "## MPS SOURCE BLOCKED / HOLD","","| Page | Expected | Actual |","|---|---:|---:|"]
    for p,e in MPS.items(): L.append(f"| {p} | {e} | {actual[p]} |")
    L += ["","## Failures",""]
    if not fail: L.append("- None outside the documented MPS HOLD.")
    else:
      L += ["- GLOBAL: "+x for x in probs]
      L += [f"- {r['path']} [{r['viewport']}]: {'; '.join(r['issues'])}" for r in bad[:200]]
    L += ["","## Acceptance criteria","","- MPS known missing references = 0.","- MathJax errors = 0.",
          "- Unrendered = 0.","- Page overflow = 0.","- Uncontained overflow = 0.","- Missing images outside MPS HOLD = 0."]
    p=Path(a.report); p.parent.mkdir(parents=True,exist_ok=True); p.write_text("\n".join(L)+"\n",encoding="utf-8"); print(status); return fail

def main():
    q=argparse.ArgumentParser(); q.add_argument("--root",default="."); q.add_argument("--base-url",default="http://127.0.0.1:8000")
    q.add_argument("--shard-index",type=int,default=0); q.add_argument("--shard-count",type=int,default=1); q.add_argument("--output",default="qa-results/shard-0.json")
    q.add_argument("--merge-dir"); q.add_argument("--report",default=".document/formula_reviews/FINAL_SITE_BROWSER_QA_20260919.md")
    q.add_argument("--expected-shards",type=int,default=4); q.add_argument("--expected-pages",type=int,default=205); a=q.parse_args()
    if not a.merge_dir and (a.shard_count<1 or not 0<=a.shard_index<a.shard_count): q.error("invalid shard")
    return 1 if (merge(a) if a.merge_dir else run(a)) else 0
if __name__=="__main__": sys.exit(main())
