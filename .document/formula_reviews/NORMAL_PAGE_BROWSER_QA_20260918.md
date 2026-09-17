# Normal Page Browser QA — 2026-09-18

- Overall: **PASS**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Mobile policy: MathJax line breaking first; irreducibly wide matrices may scroll inside `.math-block`, but the page itself must never overflow horizontally.

| Page | Viewport | Blocks | Unrendered | Formula images | MathJax errors | Local-scroll formulas | Uncontained overflow | Page overflow |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `fem_6_2_6` | desktop | 12/12 | 0 | 0 | 0 | 0 | 0 | NO |
| `fem_6_2_6` | mobile | 12/12 | 0 | 0 | 0 | 4 | 0 | NO |
| `fem_7_1_1` | desktop | 20/20 | 0 | 0 | 0 | 0 | 0 | NO |
| `fem_7_1_1` | mobile | 20/20 | 0 | 0 | 0 | 13 | 0 | NO |
| `fem_7_1_2` | desktop | 45/45 | 0 | 0 | 0 | 0 | 0 | NO |
| `fem_7_1_2` | mobile | 45/45 | 0 | 0 | 0 | 11 | 0 | NO |
| `fem_7_2_1` | desktop | 20/20 | 0 | 0 | 0 | 0 | 0 | NO |
| `fem_7_2_1` | mobile | 20/20 | 0 | 0 | 0 | 8 | 0 | NO |
| `fem_7_2_2` | desktop | 51/51 | 0 | 0 | 0 | 0 | 0 | NO |
| `fem_7_2_2` | mobile | 51/51 | 0 | 0 | 0 | 19 | 0 | NO |

## Failures

- None.

Screenshots and the machine-readable manifest are stored in the workflow artifact `normal-fem-browser-qa`.
