# FEM Batch 4 Formula Audit — 2026-09-18

## Scope

Immediate strict-conversion subset:

| Page | Formula targets | Retained diagrams / mixed |
|---|---:|---:|
| `fem/fem_4.html` | 4 | 1 mixed math-text image |
| `fem/fem_9.html` | 3 | 2 diagrams |
| `fem/fem_6_2_2.html` | 3 | 0 |
| `fem/fem_6_2_3.html` | 3 | 0 |
| `fem/fem_6_2_4.html` | 3 | 0 |
| `fem/fem_6_2_5.html` | 3 | 0 |
| **Total** | **19** | **3 retained assets on target pages** |

Additional batch-4 diagrams on `fem_12.html` remain unchanged.

Classification reference:
`.document/formula_reviews/FEM_BATCH_4_IMAGE_CLASSIFICATION_20260918.md`

Original source images are canonical.

## Pass 1 — source image to LaTeX

- Result: **19 / 19 PASS**
- Transcription data: `.document/formula_reviews/fem_batch_4_formulas.json`
- The 12 tetrahedral derivative formulas preserve the full source-visible determinant expansion term order and the final six-term derivative expressions.
- `fem_4/image003` preserves each permutation/sign expansion stage rather than replacing it with a simplified determinant identity.
- Vector arrows and bracket notation on `fem_9` are preserved.

## Pass 2 — browser MathJax comparison

- Workflow run: **35317362082**
- Artifact: `fem-batch-4-pass2`
- Artifact id: **10535172664**
- Result: **19 / 19 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 19**
- Source image vs MathJax rendering: **19 / 19 visually checked and PASS**

## Retained assets

- `fem_4/image002.png`: Japanese explanatory prose + determinant/permutation formulas; handled separately as HTML prose + MathJax.
- `fem_9/image003.png`, `image005.png`: concept diagrams.
- `fem_12/image001.png`–`image005.png`: bandwidth / node-numbering / matrix-layout diagrams.

## Certification

| Check | Result |
|---|---|
| Formula targets | 19 |
| Pass 1 | **19 / 19 PASS** |
| Pass 2 | **19 / 19 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 19** |
| Production deployment | Not performed |

**FEM batch 4 pure formulas are certified for application to the normal pages.**
