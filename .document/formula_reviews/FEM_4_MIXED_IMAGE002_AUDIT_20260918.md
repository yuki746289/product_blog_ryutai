# FEM 4 Mixed Image002 Audit — 2026-09-18

## Scope

- Page: `fem/fem_4.html`
- Source: `img/fem_tri_area.files/image002.png`
- Type: Japanese explanatory prose + mathematical notation/formulas
- Original image is canonical.

## Reconstruction

The image was decomposed into:

1. determinant/permutation display formula,
2. Japanese sentence `ε(σ)を σ∈σ_n の符号とすると`,
3. four sign-rule lines.

All mathematical fragments, including the inline `σ∈σ_n`, are rendered by MathJax. Japanese prose remains normal HTML text.

## Browser comparison

- Final workflow run: **35318297184**
- Artifact: `fem-4-mixed-pass2`
- Artifact id: **10536002973**
- MathJax errors: **0**
- Horizontal overflow: **0**
- Source image vs reconstructed browser rendering: **PASS**

An initial candidate left `σ∈σ_n` as plain text; the missing subscript rendering was detected during visual comparison and corrected before normal-page application.

## Certification

**`fem_4/image002.png` is certified for replacement by HTML prose + MathJax.**

Production deployment has not been performed.
