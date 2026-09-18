# Remaining Heat Formula Audit — 2026-09-18

## Scope

Strict source-image audit for the remaining Heat formula images after Heat 6 / Heat 7.

Target pages and formula counts:

| Page | Formula count |
|---|---:|
| `heat/heat_3.html` | 1 |
| `heat/heat_4_1.html` | 1 |
| `heat/heat_4_2.html` | 1 |
| `heat/heat_4_3.html` | 2 |
| `heat/heat_5_1.html` | 1 |
| `heat/heat_5_2.html` | 2 |
| `heat/heat_5_3.html` | 2 |
| `heat/heat_5_4.html` | 6 |
| **Total** | **16** |

The diagram assets classified previously remain images and are excluded from formula replacement.

## Pass 1 — source image to LaTeX

- Result: **16 / 16 PASS**
- Exact transcription data: `.document/formula_reviews/remaining_heat_formulas.json`
- Original source images are canonical.
- Source-visible irregular notation is preserved exactly; no algebraic normalization or silent correction was applied.

## Pass 2 — browser MathJax comparison

- Workflow run: **35296027681**
- Artifact: `remaining-heat-pass2`
- Artifact id: **10527452419**
- Result: **16 / 16 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow in audit viewport: **0 / 16**
- Source image vs MathJax rendering: **16 / 16 visually checked and PASS**

## Diagram assets retained unchanged

- `img/heat_conduction.files/image001.png`
- `img/heat_convection.files/image001.png`
- `img/heat_emission.files/image001.png`
- `img/heat_eq.files/image001.png`
- `img/heat_eq_accumulation.files/image001.png`
- `img/heat_eq_convection.files/image001.png`
- `img/heat_eq_conduction.files/image001.png`
- `img/heat_eq_derivation.files/image001.png`

## Certification

| Check | Result |
|---|---|
| Formula classification | 16 formulas |
| Diagrams retained | 8 |
| Pass 1 | **16 / 16 PASS** |
| Pass 2 | **16 / 16 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 16** |
| Production deployment | Not performed |

**The remaining Heat formula set is certified for application to the normal pages.**
