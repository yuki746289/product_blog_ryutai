# Appendix 2 Formula Audit — 2026-09-18

## Scope

- Page: `appendix/appendix_2.html`
- Formula source images: `img/appendix_sphere.files/image002.png`–`image012.png`
- Formula count: **11**
- `image001.png` is a mixed geometry diagram and is intentionally excluded from formula replacement.
- Original source images are the canonical transcription reference.

## Pass 1 — source image to LaTeX

- Result: **11 / 11 PASS**
- Exact transcription data: `.document/formula_reviews/appendix_2_formulas.json`
- Signs, term ordering, factors, indices, exponents, coefficients and delimiters were preserved from the source images.
- Long expansions `image009`–`image012` were checked against the enlarged source images term by term.

## Pass 2 — browser MathJax comparison

- Workflow run: **35288931238**
- Artifact: `appendix-2-pass2` (artifact id **10525283036**)
- Result: **11 / 11 PASS**
- Browser MathJax errors: **0**
- Formula-level horizontal overflow: **0 / 11**
- `image002`–`image008`: source/render pairs visually checked.
- `image009`–`image012`: source/render pairs visually checked individually; term sequence, signs, indices and exponents match the source.

### image007 technical correction

An earlier browser audit failed because the display-only LaTeX used `\\[6pt]` row spacing, which MathJax 4 parsed as an invalid display delimiter sequence in this context. It was changed to ordinary row breaks `\\`.

This was a rendering-syntax correction only. **No mathematical content was changed.**

## Certification

| Check | Result |
|---|---|
| Pass 1 transcription | 11 / 11 PASS |
| Pass 2 source vs MathJax | 11 / 11 PASS |
| MathJax browser errors | 0 |
| Formula horizontal overflow | 0 / 11 |
| Mixed diagram `image001` excluded | PASS |
| Production deployment | Not performed |

**Appendix 2 formula set is certified for application to the normal page.**
