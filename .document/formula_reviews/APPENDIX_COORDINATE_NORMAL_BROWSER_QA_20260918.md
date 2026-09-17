# Appendix Coordinate Normal Browser QA — 2026-09-18

- Overall: **PASS**
- Viewports: desktop 1440x1000; mobile 390x844
- Formula target: 8 blocks per page; diagrams image001/image002/image004 remain 1/1/2 placements.

| Page | Viewport | Blocks | Formula images | MathJax errors | Local-scroll | Uncontained | Page overflow | Diagrams preserved |
|---|---|---:|---:|---:|---:|---:|---|---|
| appendix_3_1 | desktop | 8/8 | 0 | 0 | 0 | 0 | NO | {'001': 1, '002': 1, '004': 2} |
| appendix_3_1 | mobile | 8/8 | 0 | 0 | 0 | 0 | NO | {'001': 1, '002': 1, '004': 2} |
| appendix_3_2 | desktop | 8/8 | 0 | 0 | 0 | 0 | NO | {'001': 1, '002': 1, '004': 2} |
| appendix_3_2 | mobile | 8/8 | 0 | 0 | 1 | 0 | NO | {'001': 1, '002': 1, '004': 2} |

## Failures

- None.

- Production deployment has not been performed.
