# FEM Batch 1 Formula Audit — 2026-09-18

## Scope

Strict source-image audit for:

| Page | Formula targets | Retained diagrams |
|---|---:|---:|
| `fem/fem_11_1.html` | 11 | 0 |
| `fem/fem_2_1.html` | 6 | 2 |
| `fem/fem_10.html` | 6 | 1 |
| **Total** | **23** | **3** |

`fem/fem_13.html` was also reviewed in this batch; all eight residual images are mesh / numbering diagrams, so no formula conversion is performed on that page.

## Pass 1 — source image to LaTeX

- Result after correction: **23 / 23 PASS**
- Exact transcription data:
  - `.document/formula_reviews/fem_11_1_formulas.json`
  - `.document/formula_reviews/fem_2_1_formulas.json`
  - `.document/formula_reviews/fem_10_formulas.json`
- Original source images are canonical.
- Source-visible notation and apparent irregularities are preserved rather than silently normalized.

### Corrections found during Pass 2 review

Two off-diagonal matrix indices in `fem_10` were initially transcribed with symmetric counterparts rather than the source-visible order:

- `image002`: corrected `[S_xy]` → `[S_yx]`, and `[S_xz]` → `[S_zx]`.
- `image003`: corrected `[S_yz]` → `[S_zy]`.

No normal production page had been replaced before these corrections.

## Pass 2 — browser MathJax comparison

- Final successful workflow run: **35311609362**
- Artifact: `fem-batch-1-pass2`
- Artifact id: **10533650808**
- Result: **23 / 23 PASS**
- MathJax rendering errors: **0**
- Formula-level horizontal overflow in audit viewport: **0 / 23**
- Source image vs MathJax rendering: **23 / 23 visually checked and PASS**

## Retained diagram assets

- `fem/fem_2_1.html`: `image001.png`, `image008.png`
- `fem/fem_10.html`: `image005.png`
- `fem/fem_13.html`: all eight residual images

## Certification

| Check | Result |
|---|---|
| Formula targets | 23 |
| Pass 1 | **23 / 23 PASS** |
| Pass 2 | **23 / 23 PASS** |
| MathJax errors | **0** |
| Audit horizontal overflow | **0 / 23** |
| Diagrams retained | **11 across the reviewed 4 pages** |
| Production deployment | Not performed |

**FEM Batch 1 formula targets are certified for application to their normal pages.**
