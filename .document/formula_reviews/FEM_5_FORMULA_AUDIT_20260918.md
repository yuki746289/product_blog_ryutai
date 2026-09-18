# FEM 5 Formula Audit — 2026-09-18

## Scope

- Page: `fem/fem_5.html`
- Source directory: `img/fem_tet_vol.files`
- Source images: `image001.png`–`image007.png`
- Mathematical content blocks: **7**
- Original source images are canonical.

## Reconstruction policy

This page is not a simple sequence of display formulas. `image002.png` contains Japanese explanatory prose together with formulas, so it is reconstructed as **HTML prose + MathJax**. The remaining six images are reconstructed as MathJax display blocks.

The following source-visible details are preserved:

- `image002`: the Japanese four-item sign/permutation explanation.
- `image003`: the source matrix visibly contains `a_{43}` at the lower-left position; it is preserved verbatim rather than silently corrected to `a_{41}`.
- `image003`–`image005`: permutation order, transposition sequence, parity exponents, product order, and final signs are preserved.
- `image006`: the 24-term tetrahedral-volume expansion order is preserved.

## Pass 1

- Result: **7 / 7 PASS**
- Reconstruction data: `.document/formula_reviews/fem_5_formulas.json`

## Pass 2 — browser comparison

- Workflow run: **35317241741**
- Artifact: `fem-5-pass2`
- Artifact id: **10535003963**
- Result: **7 / 7 PASS**
- MathJax errors: **0**
- Formula/render horizontal overflow in audit viewport: **0 / 7**
- Source image vs final MathJax/HTML rendering: **7 / 7 visually checked and PASS**

## Certification

| Check | Result |
|---|---|
| Source blocks | 7 |
| HTML + MathJax mixed block | 1 |
| Pure MathJax blocks | 6 |
| Pass 1 | **7 / 7 PASS** |
| Pass 2 | **7 / 7 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 7** |
| Production deployment | Not performed |

**FEM 5 is certified for application to the normal page.**
