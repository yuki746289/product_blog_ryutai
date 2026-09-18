# Hydronamics 9_2 Formula Audit — 2026-09-18

## Scope

- Formula targets: **9**
- Retained diagrams: **1**
- Canonical source: original HP images
- Word source is transcription assistance only.

## Pass 1 — source image to LaTeX

Result: **9 / 9 PASS**

Transcription data:
- `.document/formula_reviews/hydronamics_9_2_formulas.json`

Source-visible notation is preserved without theoretical correction, including:
- `image009`: `σ_x+σ_y+σ_z=(p_x+p_y+p_z)/3`
- `image010`: divergence term is written as `(∇·v)` with no added vector arrow.

## Pass 2 — browser MathJax comparison

- Workflow run: **35336615932**
- Artifact: `hydronamics-9-2-pass2`
- Artifact id: **10542847777**
- Result: **9 / 9 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow: **0 / 9**
- Source image vs MathJax rendering: **9 / 9 visually checked and PASS**

## Diagram policy

Retained unchanged:
- `hydronamics_9_2/image001.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 9 |
| Diagram retained | 1 |
| Pass 1 | **9 / 9 PASS** |
| Pass 2 | **9 / 9 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 9** |
| Production deployment | Not performed |

**Hydronamics 9_2 formulas are certified for application to the normal page.**
