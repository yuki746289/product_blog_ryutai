# Mesh 1 Normal Browser QA — 2026-09-19

- Overall: **PASS**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Expected display formulas: 5
- Expected retained graph: 1
- Production deployment: not performed.

| Viewport | Display | Retained | MathJax errors | Unrendered | Local scroll | Uncontained | Page overflow |
|---|---:|---:|---:|---:|---:|---:|---|
| desktop | 5/5 | 1/1 | 0 | 0 | 0 | 0 | NO |
| mobile | 5/5 | 1/1 | 0 | 0 | 1 | 0 | NO |

## Failures

- None.
