# Mesh 1 Formula Audit — 2026-09-19

Created: 2026-09-19T08:31:00+09:00

## Scope

- Formula targets: **5**
- Retained graph: **1**
- Canonical source: original HP images

## Pass 1 — source image to LaTeX

Result: **5 / 5 PASS**

Checked directly against source images:
- least-squares objective and all expansion lines
- summation limits `i=1..n`
- repeated intermediate terms and their order
- derivatives with respect to `a` and `b`
- factors 2 and signs
- final two-equation system

Transcription:
- `.document/formula_reviews/mesh_1_formulas.json`

## Pass 2

Result: **5 / 5 PASS**

- Workflow run: **35404960517**
- Artifact: `mesh-1-pass2`
- Artifact id: **10572152251**
- MathJax errors: **0**
- Unrendered formulas: **0**
- Pair-page horizontal overflow: **0 / 5**
- Browser page errors: **0**

All five source/render pairs were visually inspected. The long least-squares expansion, repeated intermediate terms, summation limits, derivative equations, signs, factors, and final two-equation system match the source.

Normal-page application is prohibited until Pass 2 is complete.

**Mesh 1 is certified for normal-page application.**
