# FEM Batch 2 Normal Browser QA — 2026-09-18

- Overall: **PASS**
- Viewports: desktop 1440x1000; mobile 390x844
- Formula target: 16 MathJax blocks across 3 pages.
- Classified diagram assets must remain unchanged.

| Page | Viewport | Blocks | Formula images | MathJax errors | Local-scroll | Uncontained | Page overflow |
|---|---|---:|---:|---:|---:|---:|---|
| fem_2_3 | desktop | 5/5 | 0 | 0 | 0 | 0 | NO |
| fem_2_3 | mobile | 5/5 | 0 | 0 | 1 | 0 | NO |
| fem_6_2_1 | desktop | 6/6 | 0 | 0 | 0 | 0 | NO |
| fem_6_2_1 | mobile | 6/6 | 0 | 0 | 5 | 0 | NO |
| fem_8_2_1 | desktop | 5/5 | 0 | 0 | 0 | 0 | NO |
| fem_8_2_1 | mobile | 5/5 | 0 | 0 | 2 | 0 | NO |

## Retained diagrams

- `fem_2_3`: {'001': 1, '007': 1}
- `fem_6_2_1`: {'001': 1}
- `fem_8_2_1`: {'001': 1, '007': 1}

## Failures

- None.

- Production deployment has not been performed.
