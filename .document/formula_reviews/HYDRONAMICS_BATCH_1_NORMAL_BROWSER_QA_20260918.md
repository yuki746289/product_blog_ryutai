# Hydronamics Batch 1 Normal Browser QA — 2026-09-18

- Overall: **PASS**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Expected formulas: display 40 + inline 3 = 43
- Expected retained diagrams: 3
- Production deployment: not performed.

| Page | Viewport | Display | Inline | Retained images | MathJax errors | Unrendered | Local scroll | Uncontained | Page overflow |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `hydronamics_14` | desktop | 10/10 | 2/2 | 2/2 | 0 | 0 | 0 | 0 | NO |
| `hydronamics_14` | mobile | 10/10 | 2/2 | 2/2 | 0 | 0 | 2 | 0 | NO |
| `hydronamics_8` | desktop | 11/11 | 1/1 | 0/0 | 0 | 0 | 0 | 0 | NO |
| `hydronamics_8` | mobile | 11/11 | 1/1 | 0/0 | 0 | 0 | 0 | 0 | NO |
| `hydronamics_12_1` | desktop | 10/10 | 0/0 | 0/0 | 0 | 0 | 0 | 0 | NO |
| `hydronamics_12_1` | mobile | 10/10 | 0/0 | 0/0 | 0 | 0 | 1 | 0 | NO |
| `hydronamics_4` | desktop | 9/9 | 0/0 | 1/1 | 0 | 0 | 0 | 0 | NO |
| `hydronamics_4` | mobile | 9/9 | 0/0 | 1/1 | 0 | 0 | 3 | 0 | NO |

## Failures

- None.
