# Column 2 Formula Audit — 2026-09-19

Created: 2026-09-19T08:55:00+09:00

## Scope

- Formula targets: **5**
- Retained diagrams: **0**
- Canonical source: original HP images

## Pass 1 — source image to LaTeX

Result: **5 / 5 PASS**

Checked directly against source images:
- square-bracketed unit symbols
- numerator/denominator placement in `m/s^2` and `J/s`
- superscripts `2` and `-2`
- source-visible approximate-equality symbol in `image003`
- coefficient `0.239`
- line and unit order

Transcription:
- `.document/formula_reviews/column_2_formulas.json`

## Pass 2

Result: **5 / 5 PASS**

- Final workflow run: **35406325865**
- Artifact: `column-2-pass2`
- Artifact id: **10572875026**
- MathJax errors: **0**
- Unrendered formulas: **0**
- Browser page errors: **0**

Initial Pass 2 run **35406153509** exposed one source-symbol mismatch in `image003`: `\\fallingdotseq` did not match the source glyph. The transcription was corrected to `\\cong`, then the full five-formula Pass 2 was rerun. Final result: 5/5 source/render matches.

Normal-page application is prohibited until Pass 2 is complete.

**Column 2 is certified for normal-page application.**
