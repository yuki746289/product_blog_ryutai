# Site Final Browser QA — 2026-09-19

- Scope: normal HTML pages on develop
- Browser: Chromium / Playwright
- Viewports: desktop 1440x1000, mobile 390x844
- Pages: **205**
- Total viewport checks: **410**
- Hard failures: **2**
- MathJax errors: **0**
- Unrendered formula containers: **0**
- Uncontained formula overflow: **0**
- Viewport checks with whole-page horizontal overflow: **2**
- Unexpected broken local images: **0**
- Expected MPS missing placements (desktop): **49**
- Expected MPS missing placements (mobile): **49**
- Production deployment: not performed.

## Failure details

| Viewport | Page | Nav | Page errors | MathJax | Unrendered | Uncontained | Page overflow | Broken local images |
|---|---|---|---:|---:|---:|---:|---|---:|
| mobile | ad_amazon.html | OK | 0 | 0 | 0 | 0 | YES | 0 |
| mobile | questionnaire.html | OK | 0 | 0 | 0 | 0 | YES | 0 |

## Interpretation

- MPS source GIF references are a documented HOLD and are counted separately from unexpected broken images.
- Whole-page horizontal overflow is a failure.
- Formula-local scroll is allowed only when contained by the formula element.
- External ads, trackers, and video embeds are blocked during this local structural QA.
