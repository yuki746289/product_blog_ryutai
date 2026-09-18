# Heat 7-2 Formula Audit — 2026-09-18

## Scope

- Page: `heat/heat_7_2.html`
- Source directory: `img/heat_discretization_tet.files`
- Formula source images: `image001.png`–`image032.png`
- Formula count: **32**
- Original source images are canonical.

## Classification

All 32 residual Word-export images on this page were visually classified as pure mathematical formulas.

- Formula: **32**
- Diagram / mixed / other: **0**

See `.document/formula_reviews/HEAT_7_IMAGE_CLASSIFICATION_20260918.md`.

## Pass 1 — source image to LaTeX

- Result: **32 / 32 PASS**
- Exact transcription data: `.document/formula_reviews/heat_7_2_formulas.json`
- Signs, term order, factors, indices, superscripts, coefficients, matrices, integration domains and boundary terms were checked against the original source images.

### Source-visible notation preserved

`image014.png` contains a source-visible anomalous entry in the Y-derivative matrix: row 4, column 2 is

`N_4 ∂N_2/∂Z`

rather than the surrounding Y derivatives. Under the strict source-image policy this is preserved exactly; it is not silently corrected.

## Pass 2 — browser MathJax comparison

- Final successful workflow run: **35293474594**
- Artifact: `heat-7-2-pass2`
- Artifact id: **10526538366**
- Result: **32 / 32 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow in audit viewport: **0 / 32**
- Source image vs MathJax rendering: **32 / 32 visually checked and PASS**

Earlier failed workflow runs were tooling issues only:
- wrong source-image directory name;
- audit loop attempted nonexistent `image033`.

Neither failure represented a mathematical-content failure.

## Certification

| Check | Result |
|---|---|
| Image classification | 32 formulas / 0 diagrams |
| Pass 1 transcription | **32 / 32 PASS** |
| Pass 2 source vs MathJax | **32 / 32 PASS** |
| MathJax errors | **0** |
| Formula horizontal overflow | **0 / 32** |
| Source anomaly handling | Preserved verbatim |
| Production deployment | Not performed |

**Heat 7-2 is certified for application to the normal page.**
