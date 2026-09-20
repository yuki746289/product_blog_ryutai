# Final Site Browser QA — 2026-09-19

- Overall: **FAIL**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Discovered normal HTML pages: **205**
- QA checks: **410**
- Hard-failure rows: **2**
- MPS known missing references: **0/0**
- Production deployment: not performed.

## Global metrics

| Metric | Count |
|---|---:|
| MathJax errors | 0 |
| Unrendered | 2 |
| Page overflow rows | 0 |
| Uncontained overflow | 0 |
| Page errors | 0 |
| Charset failures | 0 |
| Mojibake indicator rows | 0 |
| Automatic MathJax linebreak rows | 0 |
| Non-MPS missing images (desktop) | 0 |
| Allowed local math scroll | 240 |

## MPS SOURCE BLOCKED / HOLD

| Page | Expected | Actual |
|---|---:|---:|

## Failures

- mps/mps_1.html [desktop]: unrendered=1
- mps/mps_1.html [mobile]: unrendered=1

## Acceptance criteria

- MPS known missing references = 0.
- MathJax errors = 0.
- Unrendered = 0.
- Charset failures = 0.
- Mojibake indicator rows = 0.
- Automatic MathJax linebreak rows = 0.
- Page overflow = 0.
- Uncontained overflow = 0.
- Missing images outside MPS HOLD = 0.
