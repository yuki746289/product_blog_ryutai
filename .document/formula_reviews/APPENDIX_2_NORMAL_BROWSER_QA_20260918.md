# Appendix 2 Normal Browser QA — 2026-09-18

- Overall: **PASS**
- Viewports: desktop 1440x1000; mobile 390x844
- Formula target: 11 MathJax blocks (image002-image012).
- Mixed geometry diagram image001 must remain exactly once.

| Viewport | Blocks | Formula images | image001 | MathJax errors | Local-scroll | Uncontained | Page overflow |
|---|---:|---:|---:|---:|---:|---:|---|
| desktop | 11/11 | 0 | 1 | 0 | 0 | 0 | NO |
| mobile | 11/11 | 0 | 1 | 0 | 7 | 0 | NO |

## Failures

- None.

- Production deployment has not been performed.
