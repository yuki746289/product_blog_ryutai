# Hydronamics Batch 1 Formula Audit — 2026-09-18

## Scope

| Page | Formula targets | Retained diagrams |
|---|---:|---:|
| `hydronamics/hydronamics_14.html` | 12 | 2 |
| `hydronamics/hydronamics_8.html` | 12 | 0 |
| `hydronamics/hydronamics_12_1.html` | 10 | 0 |
| `hydronamics/hydronamics_4.html` | 9 | 1 |
| **Total** | **43** | **3** |

Classification reference:
`.document/formula_reviews/HYDRONAMICS_BATCH_1_IMAGE_CLASSIFICATION_20260918.md`

Original source images are canonical.

## Pass 1 — source image to LaTeX

Result: **43 / 43 PASS**

Transcription data:
- `.document/formula_reviews/hydronamics_14_formulas.json`
- `.document/formula_reviews/hydronamics_8_formulas.json`
- `.document/formula_reviews/hydronamics_12_1_formulas.json`
- `.document/formula_reviews/hydronamics_4_formulas.json`

Source-visible irregularities were preserved rather than corrected. Examples:

- `hydronamics_4/image005`: source-visible `F_z` labels and duplicated `F_{z|z+Δz}` term are retained exactly.
- `hydronamics_12_1/image009`: source-visible minus signs between the velocity-divergence terms are retained.
- `hydronamics_8/image002`: the source's location-index notation is retained as shown.
- `hydronamics_8/image011`: the small `\vec\sigma` image is treated as inline math, not a display block.

## Pass 2 — browser MathJax comparison

- Workflow run: **35322786714**
- Artifact: `hydronamics-batch-1-pass2`
- Artifact id: **10537518583**
- Result: **43 / 43 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow in audit viewport: **0 / 43**
- Source image vs MathJax rendering: **43 / 43 visually checked and PASS**

## Diagram policy

Retained unchanged:

- `hydronamics_14/image001.png`
- `hydronamics_14/image002.png`
- `hydronamics_4/image001.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 43 |
| Diagrams retained | 3 |
| Pass 1 | **43 / 43 PASS** |
| Pass 2 | **43 / 43 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 43** |
| Production deployment | Not performed |

**Hydronamics batch 1 formulas are certified for application to the normal pages.**
