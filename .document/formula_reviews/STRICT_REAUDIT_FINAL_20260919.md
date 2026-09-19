# Strict Formula Re-audit Final Summary — 2026-09-19

## 1. Current strict inventory

The 2026-09-19 strict re-audit uses the current page/source mapping as its inventory.
It is intentionally kept separate from the older "564 converted formulas" count because the old count used a different inventory scope and predates later source recovery / remapping.

### Source-image / formula pages

| Category | Formulas | Formula pages | Status |
|---|---:|---:|---|
| FEM | 235 | 26 | COMPLETE |
| Heat | 94 | 11 | COMPLETE |
| Hydronamics | 131 | 26 | COMPLETE |
| Physics | 49 | 16 | COMPLETE |
| Mesh | 30 | 4 | COMPLETE |
| Column | 5 | 1 | COMPLETE |
| Appendix | 41 | 4 | COMPLETE |
| **Core subtotal** | **585** | **88** | **COMPLETE** |

### MPS

- Formula slots: **49 / 7 pages**
- source-exact / recovered: **48**
- inferred reconstruction: **1**
- HOLD: **0**
- Browser QA: **PASS**
- inferred item: `mps/mps_6_2.html / image022`
- reconstruction is explicitly marked `data-source-status="inferred-reconstruction"`

### Current total

- Current strict formula slots: **634**
- Formula pages: **95**
- source-exact / source-audited formula slots: **633**
- explicitly inferred formula slots: **1**
- unresolved HOLD: **0**

## 2. Strict verification method

1. Original source image is the final authority where available.
2. Word / recovered Equation.3 is used as a machine-readable transcription source where relevant.
3. Existing LaTeX is reused only after comparison.
4. Source image and final MathJax rendering are paired and directly checked.
5. Browser QA is performed on desktop and mobile.
6. `t/τ`, `i/j/k`, x/y/z, upper/lower case, signs, subscripts, superscripts, equation boundaries and line breaks are treated as high-risk checks.
7. Source-visible notation is preserved even where theoretically unusual.
8. No silent theoretical normalization is permitted.

## 3. Browser acceptance

Across completed strict formula pages:

- MathJax error: **0**
- unrendered formula: **0**
- uncontained math overflow: **0**
- page-wide horizontal overflow: **0**
- unresolved formula image: **0**
- HOLD: **0**

Long formulas may scroll only inside `.math-block` on mobile.

## 4. Nonformula / retained-image QA

Completed category-level nonformula QA:

- FEM: PASS
- Heat: PASS
- Hydronamics: PASS
- Physics: PASS
- Mesh / Column / Appendix: PASS
- Counting: PASS

Counting contains no formula images; its two flowcharts are intentionally retained.

## 5. Important corrections detected by the strict re-audit

Examples include:

- FEM formula boundaries and source line breaks
- `τ` / time-symbol checks
- missing starred normal vector in `fem_8_2_1/image005`
- pressure / tensor term positioning
- source-visible unusual FEM/Heat notation retained without theoretical correction
- MPS `P_i/P_j` source correction
- retained diagram / mixed-image classification corrections

## 6. Final status

**Strict formula re-audit: COMPLETE WITH ONE EXPLICITLY INFERRED MPS FORMULA.**

No unresolved HOLD remains.
