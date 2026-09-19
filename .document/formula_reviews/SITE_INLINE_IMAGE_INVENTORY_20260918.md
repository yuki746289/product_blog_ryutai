# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **112**
- Unique residual image assets: **110**
- Priority A (`p.im`) placements: **110**
- Missing referenced assets: **0**

### By section

| Section | Placements |
|---|---:|
| `fem` | 33 |
| `mesh` | 23 |
| `hydronamics` | 21 |
| `physics` | 16 |
| `appendix` | 9 |
| `heat` | 8 |
| `counting` | 2 |

### Missing referenced assets

- **0**

### Pages with residual Word-export images

| No. | Page | Placements | Priority A |
|---:|---|---:|---:|
| 1 | `mesh/mesh_3_1.html` | 10 | 10 |
| 2 | `fem/fem_13.html` | 8 | 8 |
| 3 | `fem/fem_1.html` | 6 | 6 |
| 4 | `fem/fem_12.html` | 5 | 3 |
| 5 | `mesh/mesh_3_2.html` | 5 | 5 |
| 6 | `physics/physics_2.html` | 5 | 5 |
| 7 | `appendix/appendix_3_1.html` | 4 | 4 |
| 8 | `appendix/appendix_3_2.html` | 4 | 4 |
| 9 | `mesh/mesh_4.html` | 4 | 4 |
| 10 | `hydronamics/hydronamics_10_1.html` | 3 | 3 |
| 11 | `physics/physics_4.html` | 3 | 3 |
| 12 | `fem/fem_2_1.html` | 2 | 2 |
| 13 | `fem/fem_2_3.html` | 2 | 2 |
| 14 | `fem/fem_8_2_1.html` | 2 | 2 |
| 15 | `fem/fem_9.html` | 2 | 2 |
| 16 | `hydronamics/hydronamics_14.html` | 2 | 2 |
| 17 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 18 | `hydronamics/hydronamics_9_1.html` | 2 | 2 |
| 19 | `mesh/mesh_5.html` | 2 | 2 |
| 20 | `physics/physics_6_2_3.html` | 2 | 2 |
| 21 | `appendix/appendix_2.html` | 1 | 1 |
| 22 | `counting/counting_1.html` | 1 | 1 |
| 23 | `counting/counting_2.html` | 1 | 1 |
| 24 | `fem/fem.html` | 1 | 1 |
| 25 | `fem/fem_10.html` | 1 | 1 |
| 26 | `fem/fem_2_2.html` | 1 | 1 |
| 27 | `fem/fem_6_1_1.html` | 1 | 1 |
| 28 | `fem/fem_6_2_1.html` | 1 | 1 |
| 29 | `fem/fem_8_1.html` | 1 | 1 |
| 30 | `heat/heat_4_1.html` | 1 | 1 |
| 31 | `heat/heat_4_2.html` | 1 | 1 |
| 32 | `heat/heat_4_3.html` | 1 | 1 |
| 33 | `heat/heat_5.html` | 1 | 1 |
| 34 | `heat/heat_5_1.html` | 1 | 1 |
| 35 | `heat/heat_5_2.html` | 1 | 1 |
| 36 | `heat/heat_5_3.html` | 1 | 1 |
| 37 | `heat/heat_5_4.html` | 1 | 1 |
| 38 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 39 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 40 | `hydronamics/hydronamics_4.html` | 1 | 1 |
| 41 | `hydronamics/hydronamics_5.html` | 1 | 1 |
| 42 | `hydronamics/hydronamics_6_1.html` | 1 | 1 |
| 43 | `hydronamics/hydronamics_6_2.html` | 1 | 1 |
| 44 | `hydronamics/hydronamics_6_3.html` | 1 | 1 |
| 45 | `hydronamics/hydronamics_6_4.html` | 1 | 1 |
| 46 | `hydronamics/hydronamics_7.html` | 1 | 1 |
| 47 | `hydronamics/hydronamics_9_2.html` | 1 | 1 |
| 48 | `hydronamics/hydronamics_9_4.html` | 1 | 1 |
| 49 | `hydronamics/hydronamics_9_5.html` | 1 | 1 |
| 50 | `mesh/mesh_1.html` | 1 | 1 |
| 51 | `mesh/mesh_2.html` | 1 | 1 |
| 52 | `physics/physics_1.html` | 1 | 1 |
| 53 | `physics/physics_3.html` | 1 | 1 |
| 54 | `physics/physics_6_2_1.html` | 1 | 1 |
| 55 | `physics/physics_6_2_2.html` | 1 | 1 |
| 56 | `physics/physics_6_3_2.html` | 1 | 1 |
| 57 | `physics/physics_6_3_3.html` | 1 | 1 |

## Next step

Final residual set contains only confirmed non-formula retained images. MPS formula images are fully replaced by MathJax; image022 is tracked separately as an inferred reconstruction.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
