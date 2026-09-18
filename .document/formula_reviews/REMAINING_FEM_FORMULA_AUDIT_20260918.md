# Remaining FEM Formula Audit — 2026-09-18

## Scope

Final unclassified FEM mathematical-content subset after FEM batches 1–3 and FEM 5.

| Page | Pure MathJax | HTML prose + MathJax |
|---|---:|---:|
| `fem/fem_3.html` | 2 | 0 |
| `fem/fem_6_1_2.html` | 2 | 0 |
| `fem/fem_6_1_3.html` | 2 | 0 |
| `fem/fem_6_1_4.html` | 2 | 0 |
| `fem/fem_8.html` | 2 | 0 |
| `fem/fem_4.html` | 0 | 1 |
| **Total** | **10** | **1** |

Classification reference:
`.document/formula_reviews/REMAINING_FEM_IMAGE_CLASSIFICATION_20260918.md`

Original source images are canonical.

## Pass 1

- Result: **11 / 11 PASS**
- Reconstruction data: `.document/formula_reviews/remaining_fem_formulas.json`

Source-visible anomalies are intentionally preserved:

- `fem_6_1_3/image010.png`: the left side is a y derivative, but the intermediate source line visibly uses `∂/∂x`.
- `fem_6_1_4/image012.png`: the same source-visible `∂/∂x` appears in the intermediate line.
- `fem_4/image002.png`: Japanese explanatory prose is reconstructed as HTML text while all mathematical expressions remain MathJax.

## Pass 2 — browser MathJax / HTML comparison

- Workflow run: **35318416381**
- Artifact: `remaining-fem-pass2`
- Artifact id: **10535833433**
- Result: **11 / 11 PASS**
- MathJax errors: **0**
- Formula/render horizontal overflow in audit viewport: **0 / 11**
- Source image vs final MathJax/HTML rendering: **11 / 11 visually checked and PASS**

## Diagram policy

The remaining unclassified FEM images that are diagrams or mixed diagrams remain unchanged:

- `fem_12`: 5 images
- `fem_9`: 2 images
- `fem_8_1`: 1 image
- `fem.html`: 1 image

## Certification

| Check | Result |
|---|---|
| Pure MathJax blocks | 10 |
| HTML + MathJax mixed block | 1 |
| Pass 1 | **11 / 11 PASS** |
| Pass 2 | **11 / 11 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 11** |
| Production deployment | Not performed |

**The remaining FEM mathematical-content blocks are certified for application to the normal pages.**
