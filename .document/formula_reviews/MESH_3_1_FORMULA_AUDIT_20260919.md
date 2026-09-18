# Mesh 3_1 Formula Audit — 2026-09-19

Created: 2026-09-19T07:12:00+09:00

## Scope

- Formula targets: **9**
  - Display: **5**
  - Inline: **4**
- Retained images: **10**
- Canonical source: original HP images

## Pass 1 — source image to LaTeX

Result: **9 / 9 PASS**

Checked directly against source images:
- vector arrows and subscripts
- force indices and negative sign
- summation limits
- weight-function arguments
- absolute-value bars and fraction structure
- source-visible `|p_2-p_2|` denominator in `image006`
- scalar factors `c r`
- node-density inequalities
- weighted-average numerator/denominator
- exponent `10^{-3}`

`image012` and `image013` are mixed Japanese-text/formula images; their formula components are certified while their Japanese labels remain existing HTML text.

Transcription:
- `.document/formula_reviews/mesh_3_1_formulas.json`

## Pass 2

Result: **9 / 9 PASS**

- Workflow run: **35400903542**
- Artifact: `mesh-3-1-pass2`
- Artifact id: **10570805617**
- MathJax errors: **0**
- Unrendered formulas: **0**
- Pair-page horizontal overflow: **0 / 9**
- Browser page errors: **0**

All nine source/render pairs were visually inspected. Vector marks, indices, sums, signs, fraction structures, inequalities, `10^{-3}`, and the source-visible `|p_2-p_2|` denominator match the source.

Normal-page application is prohibited until Pass 2 is complete.

**Mesh 3_1 is certified for normal-page application.**
