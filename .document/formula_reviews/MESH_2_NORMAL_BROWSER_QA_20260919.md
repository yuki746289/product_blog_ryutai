# Mesh 2 Normal Browser QA — 2026-09-19

- Overall: **PASS**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Expected display formulas: 9
- Expected retained diagram: 1
- Production deployment: not performed.

| Viewport | Display | Retained | MathJax errors | Unrendered | Local scroll | Uncontained | Page overflow |
|---|---:|---:|---:|---:|---:|---:|---|
| desktop | 9/9 | 1/1 | 0 | 0 | 0 | 0 | NO |
| mobile | 9/9 | 1/1 | 0 | 0 | 2 | 0 | NO |

## Failures

- None.
