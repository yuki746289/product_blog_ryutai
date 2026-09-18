# Heat 7-1 Formula Audit — 2026-09-18

## Scope

- Page: `heat/heat_7_1.html`
- Source directory: `img/heat_discretization_tri.files`
- Formula source images: `image001.png`–`image033.png`
- Formula count: **33**
- Original source images are canonical.

## Classification

All 33 residual Word-export images on this page were visually classified as pure mathematical formulas.

- Formula: **33**
- Diagram / mixed / other: **0**

See `.document/formula_reviews/HEAT_7_IMAGE_CLASSIFICATION_20260918.md`.

## Pass 1 — source image to LaTeX

- Result: **33 / 33 PASS**
- Exact transcription data: `.document/formula_reviews/heat_7_1_formulas.json`
- Signs, term order, factors, indices, superscripts, coefficients and delimiters were checked against the original source images.

During pair review, two transcription differences were found and corrected before certification:

1. `image019`: the source has no standalone `A` after `1/(4A^2)`; the candidate transcription was corrected to match the image.
2. `image021`: the source visibly contains `4/4! V` in the `i=j` line. Although `V` is likely a source typo in this area-integral formula, strict transcription preserves **V** exactly rather than silently correcting it to `A`.

## Pass 2 — browser MathJax comparison

- Final workflow run: **35292202973**
- Final artifact: `heat-7-1-pass2`
- Artifact id: **10527285798**
- Result: **33 / 33 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 33**
- Corrected `image019` and `image021` source/render pairs were rechecked after the final rerun and match the source.

An earlier workflow run failed because the audit page's explicit delimiter configuration prevented MathJax from recognizing the display delimiters. This was an audit-page configuration issue, not a mathematical-content failure. The workflow was corrected to use MathJax's default display delimiters.

## Certification

| Check | Result |
|---|---|
| Image classification | 33 formulas / 0 diagrams |
| Pass 1 transcription | **33 / 33 PASS** |
| Pass 2 source vs MathJax | **33 / 33 PASS** |
| MathJax errors | **0** |
| Formula horizontal overflow | **0 / 33** |
| Source typo handling | Preserved verbatim |
| Production deployment | Not performed |

**Heat 7-1 is certified for application to the normal page.**
