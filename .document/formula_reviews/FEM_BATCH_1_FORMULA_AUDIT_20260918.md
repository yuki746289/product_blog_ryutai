# FEM Batch 1 Formula Audit — 2026-09-18

## Scope

Target pages:

| Page | Formula targets | Retained diagrams |
|---|---:|---:|
| `fem/fem_11_1.html` | 11 | 0 |
| `fem/fem_2_1.html` | 6 | 2 |
| `fem/fem_10.html` | 6 | 1 |
| `fem/fem_13.html` | 0 | 8 |
| **Total** | **23** | **11** |

Classification reference:
`.document/formula_reviews/FEM_BATCH_1_IMAGE_CLASSIFICATION_20260918.md`

Original source images are canonical.

## Pass 1 — source image to LaTeX

Final result: **23 / 23 PASS**

Transcription data:
- `.document/formula_reviews/fem_11_1_formulas.json`
- `.document/formula_reviews/fem_2_1_formulas.json`
- `.document/formula_reviews/fem_10_formulas.json`

During visual comparison, the following candidate differences were found and corrected before certification:

- `fem_10/image002`
  - source cross terms are `[S_yx]` and `[S_zx]`;
  - source surface vector contains four entries `[1,1,1,1]^T`.
- `fem_10/image003`
  - source z-cross term is `[S_zy]`;
  - source surface vector contains four entries.
- `fem_10/image004`
  - source surface vector contains four entries.
- `fem_2_1/image005`
  - an enlarged source check confirmed ordinary `N_1,N_2,N_3` with no overbar; the temporary overbar interpretation was reverted before certification.

No corrected candidate had been applied to a normal page before these checks.

## Pass 2 — browser MathJax comparison

- Final workflow run: **35312438146**
- Artifact: `fem-batch-1-pass2`
- Artifact id: **10533424955**
- Result: **23 / 23 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 23**
- Source image vs final MathJax rendering: **23 / 23 visually checked and PASS**

## Diagram policy

The following assets remain images and are not reconstructed:

- `fem_2_1`: `image001.png`, `image008.png`
- `fem_10`: `image005.png`
- `fem_13`: `image001.png`–`image008.png`

## Certification

| Check | Result |
|---|---|
| Formula classification | 23 |
| Diagram/mixed retained | 11 |
| Pass 1 | **23 / 23 PASS** |
| Pass 2 | **23 / 23 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 23** |
| Production deployment | Not performed |

**FEM batch 1 formulas are certified for application to the normal pages.**
