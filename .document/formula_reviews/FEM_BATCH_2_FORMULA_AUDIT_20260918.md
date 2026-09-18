# FEM Batch 2 Formula Audit — 2026-09-18

## Scope

Immediate strict-conversion subset from FEM batch 2:

| Page | Formula targets | Retained diagrams |
|---|---:|---:|
| `fem/fem_2_3.html` | 5 | 2 |
| `fem/fem_6_2_1.html` | 6 | 1 |
| `fem/fem_8_2_1.html` | 5 | 2 |
| **Total** | **16** | **5** |

`fem_5.html` is handled separately because its mathematical images include dense determinant expansions and Japanese explanatory prose.

Classification reference:
`.document/formula_reviews/FEM_BATCH_2_IMAGE_CLASSIFICATION_20260918.md`

Original source images are canonical.

## Pass 1 — source image to LaTeX

Final result: **16 / 16 PASS**

Transcription data:
- `.document/formula_reviews/fem_2_3_formulas.json`
- `.document/formula_reviews/fem_6_2_1_formulas.json`
- `.document/formula_reviews/fem_8_2_1_formulas.json`

Source-visible notation is preserved even where it is unusual. In particular, `fem_2_3/image004.png` visibly writes `φ(x,y)` on a 3-D tetrahedral interpolation page; it is preserved verbatim rather than silently changed to `φ(x,y,z)`.

## Pass 2 — browser MathJax comparison

- Workflow run: **35314818685**
- Artifact: `fem-batch-2-pass2`
- Artifact id: **10534324596**
- Result: **16 / 16 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 16**
- Source image vs MathJax rendering: **16 / 16 visually checked and PASS**

## Diagram policy

Retained unchanged:
- `fem_2_3`: `image001.png`, `image007.png`
- `fem_6_2_1`: `image001.png`
- `fem_8_2_1`: `image001.png`, `image007.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 16 |
| Diagrams retained | 5 |
| Pass 1 | **16 / 16 PASS** |
| Pass 2 | **16 / 16 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 16** |
| Production deployment | Not performed |

**The immediate FEM batch 2 formula set is certified for application to the normal pages.**
