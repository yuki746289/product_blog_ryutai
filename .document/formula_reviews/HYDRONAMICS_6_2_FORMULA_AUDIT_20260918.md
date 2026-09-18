# Hydronamics 6_2 Formula Audit — 2026-09-18

## Scope

- Formula targets: **6**
- Retained diagrams: **1**
- Canonical source: original HP images
- Word source is transcription assistance only.

## Pass 1 — source image to LaTeX

Result: **6 / 6 PASS**

Transcription data:
- `.document/formula_reviews/hydronamics_6_2_formulas.json`

Source-visible term order, signs, products, stress subscripts, and evaluation-position bars are preserved.

Notable source-visible irregularity:
- The middle product in `image002`–`image007` is visibly `ΔzxΔz`. It is retained exactly rather than normalized to the theoretically expected `ΔzΔx`.

## Pass 2 — browser MathJax comparison

- Workflow run: **35341075511**
- Artifact: `hydronamics-6-2-pass2`
- Artifact id: **10544843010**
- Result: **6 / 6 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 6**
- Source image vs MathJax rendering: **6 / 6 visually checked and PASS**

## Diagram policy

Retained unchanged:
- `image001.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 6 |
| Diagram retained | 1 |
| Pass 1 | **6 / 6 PASS** |
| Pass 2 | **6 / 6 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 6** |
| Production deployment | Not performed |

**Hydronamics 6_2 formulas are certified for application to the normal page.**
