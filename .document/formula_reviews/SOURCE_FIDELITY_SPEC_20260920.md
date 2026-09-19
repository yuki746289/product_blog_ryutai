# Source Fidelity Specification — 2026-09-20

## Status

**CANONICAL — supersedes any implementation that relies on automatic MathJax line breaking.**

This specification applies to all formula conversions in this repository.

## 1. Source of truth

Priority:
1. Original HP formula image / original equation-editor rendering
2. Recovered Word equation object when it represents the same source
3. Current LaTeX / MathJax
4. Previous audit records

The final comparison is always **source rendering ↔ completed MathJax rendering**.

## 2. What “matching the source” means

A formula is source-faithful only when all of the following agree with the source:

- formula scope / omitted or included terms
- term order
- signs and operators
- symbols, case, subscripts and superscripts
- fractions, roots, vectors, derivatives and delimiters
- **number of displayed lines**
- **line-break positions**
- **line grouping and alignment**
- source-visible annotations that belong to the formula

A mathematically equivalent expression is not sufficient if its visible line structure differs from the source.

## 3. Line-break policy

- MathJax automatic display line breaking must **not** be used to decide formula line structure.
- Browser width must **not** introduce a different mathematical line break from the source.
- Source line breaks must be encoded explicitly in TeX (`aligned`, `split`, `array`, `multline`, `\\`, etc.) as appropriate.
- If an unbreakable source-faithful formula is wider than the viewport, keep the original line structure and allow **horizontal scrolling inside `.math-block` only**.
- Page-wide horizontal overflow is not allowed.
- Inline mathematics must not be automatically split by MathJax when doing so changes the source presentation.

Canonical MathJax overflow policy:
- `displayOverflow: 'overflow'`
- `linebreaks.inline: false`
- `.math-block` handles local horizontal scrolling when required.

## 4. Character encoding policy

Public text assets are standardized to **UTF-8**.

- HTML bytes: UTF-8
- HTML charset declaration: UTF-8
- CSS bytes: UTF-8
- CSS `@charset` when present: UTF-8
- JavaScript/text files used by the site: UTF-8

A file whose byte encoding and declared charset disagree is a hard failure.

## 5. QA gates

A final PASS requires all of the following:

1. Public HTML/CSS/JS text assets decode as UTF-8.
2. No legacy `charset=shift_jis` / `@charset "Shift_JIS"` remains in public assets.
3. Browser reports UTF-8 for normal HTML pages.
4. No visible mojibake indicators are detected.
5. No formula page enables MathJax automatic line breaking.
6. Each source formula is revalidated for visible line count, break positions and alignment against its source image/equation-editor rendering.
7. MathJax errors = 0.
8. Unrendered formulas = 0.
9. Missing public images = 0.
10. Page-wide overflow = 0; formula-local horizontal scroll is allowed.
11. Any undecidable source/layout case is HOLD, not PASS.

## 6. Effect on previous QA

The 2026-09-19 browser PASS verified rendering/error/overflow behavior but did not gate source-faithful line structure or UTF-8/declaration consistency. Therefore it is **not sufficient for deployment approval under this specification**.

Deployment remains blocked until this specification's revalidation is complete.
