# Hydronamics 10_1 Formula Audit — 2026-09-18

## Scope

- Formula targets: **5**
- Retained diagrams: **3**
- Canonical source: original HP images
- Word source is transcription assistance only.

## Pass 1 — source image to LaTeX

Result: **5 / 5 PASS**

Transcription data:
- `.document/formula_reviews/hydronamics_10_1_formulas.json`

Source-visible notation and term order are preserved.

Notable source-visible irregularity:
- `image007` retains `γ r_2 θ_2 θ_1 + γ r_2 θ_1 θ_2` in the intermediate numerator exactly as shown, although the final line uses `γ(r_1+r_2)/(r_1r_2)`.
- `image005` approximation symbol is rendered as `\cong` to match the source-visible `≅`.

## Pass 2 — browser MathJax comparison

- Workflow run: **35338265893**
- Artifact: `hydronamics-10-1-pass2`
- Artifact id: **10543064707**
- Result: **5 / 5 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 5**
- Source image vs MathJax rendering: **5 / 5 visually checked and PASS**

## Diagram policy

Retained unchanged:
- `image001.png`
- `image003.png`
- `image004.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 5 |
| Diagrams retained | 3 |
| Pass 1 | **5 / 5 PASS** |
| Pass 2 | **5 / 5 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 5** |
| Production deployment | Not performed |

**Hydronamics 10_1 formulas are certified for application to the normal page.**
