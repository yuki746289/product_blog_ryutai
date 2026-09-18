# Physics 4 Formula Audit — 2026-09-18

Created: 2026-09-18T23:47:03+09:00

## Scope

- Formula targets: **6**
  - Display: **3**
  - Inline: **3**
- Retained diagrams / mixed illustrations: **3**
- Canonical source: original HP images
- Word source: unavailable in current working context; not used as evidence

## Pass 1 — source image to LaTeX

Result: **6 / 6 PASS**

Transcription data:
- `.document/formula_reviews/physics_4_formulas.json`

The source images were inspected directly. Arrows, indices, summation bounds, component order, signs, parentheses, and equality order are preserved.

Source-visible nonstandard notation is intentionally preserved:
- `image004.png`: `\\sum_{i=3}^{3}`
- `image004.png`: middle term `\\vec{\\delta}_y v_i`
- `image008.png`: summation bounds `i=0..3`, `j=0..3`

## Pass 2 — source image to browser MathJax

Result: **6 / 6 PASS**

- Workflow run: **35358712499**
- Artifact: `physics-4-pass2`
- Artifact id: **10553611379**
- MathJax errors: **0**
- Unrendered formulas: **0**
- Pair-page horizontal overflow: **0 / 6**
- Browser page errors: **0**

All six source/render pairs were inspected visually after the workflow completed. The MathJax transcription matches the source-visible symbols, indices, summation bounds, term order, signs, and parentheses.

## Diagram policy

Retain unchanged:
- `image001.png`
- `image006.png`
- `image009.png`

## Certification

| Check | Result |
|---|---|
| Formula targets | 6 |
| Retained images | 3 |
| Pass 1 | **6 / 6 PASS** |
| Pass 2 | **6 / 6 PASS** |
| MathJax errors | **0** |
| Production deployment | Not performed |

**Physics 4 is certified for normal-page application.**
