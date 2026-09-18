# FEM Batch 1 Normal Browser QA — 2026-09-18

- Overall: **PASS**
- Viewports: desktop 1440x1000; mobile 390x844
- Formula target: 23 MathJax blocks across 3 pages.
- Classified diagram assets must remain unchanged.

| Page | Viewport | Blocks | Formula images | MathJax errors | Local-scroll | Uncontained | Page overflow |
|---|---|---:|---:|---:|---:|---:|---|
| fem_11_1 | desktop | 11/11 | 0 | 0 | 0 | 0 | NO |
| fem_11_1 | mobile | 11/11 | 0 | 0 | 0 | 0 | NO |
| fem_2_1 | desktop | 6/6 | 0 | 0 | 0 | 0 | NO |
| fem_2_1 | mobile | 6/6 | 0 | 0 | 0 | 0 | NO |
| fem_10 | desktop | 6/6 | 0 | 0 | 0 | 0 | NO |
| fem_10 | mobile | 6/6 | 0 | 0 | 3 | 0 | NO |

## Retained diagrams

- `fem_2_1`: {'001': 1, '008': 1}
- `fem_10`: {'005': 1}

## Failures

- None.

- Production deployment has not been performed.
