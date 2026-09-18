# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **278**
- Unique residual image assets: **276**
- Priority A (`p.im`) placements: **263**
- Missing referenced assets: **49**

### By section

| Section | Placements |
|---|---:|
| `physics` | 65 |
| `hydronamics` | 54 |
| `mesh` | 53 |
| `mps` | 49 |
| `fem` | 33 |
| `appendix` | 9 |
| `heat` | 8 |
| `column` | 5 |
| `counting` | 2 |

### Missing referenced assets

These references exist in HTML but the corresponding image file is absent from this repository checkout. They must be recovered or separately verified before formula conversion.

| Section | Missing placements |
|---|---:|
| `mps` | 49 |

<details><summary>Missing asset references</summary>

- `mps/mps_1.html` → `img/mps_weight.files/image001.gif`
- `mps/mps_2.html` → `img/mps_num.files/image001.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image001.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image002.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image003.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image004.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image005.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image006.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image007.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image008.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image009.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image010.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image011.gif`
- `mps/mps_3.html` → `img/mps_nabra.files/image012.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image001.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image002.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image003.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image004.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image005.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image006.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image007.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image008.gif`
- `mps/mps_4.html` → `img/mps_dot.files/image009.gif`
- `mps/mps_5.html` → `img/mps_rap.files/image001.gif`
- `mps/mps_5.html` → `img/mps_rap.files/image002.gif`
- `mps/mps_6_1.html` → `img/mps_fluid_eq.files/image001.gif`
- `mps/mps_6_1.html` → `img/mps_fluid_eq.files/image002.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image001.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image002.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image003.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image004.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image005.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image006.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image007.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image008.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image009.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image010.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image011.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image012.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image013.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image014.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image015.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image016.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image017.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image018.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image019.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image020.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image021.gif`
- `mps/mps_6_2.html` → `img/mps_fluid_count.files/image022.gif`

</details>

### Pages with residual Word-export images

| No. | Page | Placements | Priority A |
|---:|---|---:|---:|
| 1 | `mps/mps_6_2.html` | 22 | 22 |
| 2 | `mesh/mesh_3_1.html` | 19 | 17 |
| 3 | `mps/mps_3.html` | 12 | 8 |
| 4 | `physics/physics_2.html` | 12 | 12 |
| 5 | `mesh/mesh_2.html` | 10 | 10 |
| 6 | `mesh/mesh_5.html` | 9 | 9 |
| 7 | `mps/mps_4.html` | 9 | 7 |
| 8 | `physics/physics_4.html` | 9 | 6 |
| 9 | `fem/fem_13.html` | 8 | 8 |
| 10 | `physics/physics_3.html` | 7 | 7 |
| 11 | `physics/physics_6_2_3.html` | 7 | 7 |
| 12 | `fem/fem_1.html` | 6 | 6 |
| 13 | `hydronamics/hydronamics_9_1.html` | 6 | 6 |
| 14 | `hydronamics/hydronamics_9_5.html` | 6 | 6 |
| 15 | `mesh/mesh_1.html` | 6 | 6 |
| 16 | `column/column_2.html` | 5 | 5 |
| 17 | `fem/fem_12.html` | 5 | 3 |
| 18 | `hydronamics/hydronamics_9_6.html` | 5 | 5 |
| 19 | `mesh/mesh_3_2.html` | 5 | 5 |
| 20 | `physics/physics_6_1.html` | 5 | 5 |
| 21 | `physics/physics_6_2_1.html` | 5 | 5 |
| 22 | `appendix/appendix_3_1.html` | 4 | 4 |
| 23 | `appendix/appendix_3_2.html` | 4 | 4 |
| 24 | `hydronamics/hydronamics_11.html` | 4 | 4 |
| 25 | `hydronamics/hydronamics_12.html` | 4 | 4 |
| 26 | `mesh/mesh_4.html` | 4 | 4 |
| 27 | `physics/physics_5.html` | 4 | 2 |
| 28 | `hydronamics/hydronamics_10_1.html` | 3 | 3 |
| 29 | `physics/physics_6_2_2.html` | 3 | 3 |
| 30 | `physics/physics_6_3_2.html` | 3 | 3 |
| 31 | `fem/fem_2_1.html` | 2 | 2 |
| 32 | `fem/fem_2_3.html` | 2 | 2 |
| 33 | `fem/fem_8_2_1.html` | 2 | 2 |
| 34 | `fem/fem_9.html` | 2 | 2 |
| 35 | `hydronamics/hydronamics_11_6.html` | 2 | 2 |
| 36 | `hydronamics/hydronamics_14.html` | 2 | 2 |
| 37 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 38 | `hydronamics/hydronamics_5.html` | 2 | 2 |
| 39 | `hydronamics/hydronamics_7.html` | 2 | 2 |
| 40 | `hydronamics/hydronamics_9_3.html` | 2 | 2 |
| 41 | `mps/mps_5.html` | 2 | 2 |
| 42 | `mps/mps_6_1.html` | 2 | 2 |
| 43 | `physics/physics_6_2_4.html` | 2 | 2 |
| 44 | `physics/physics_6_3_3.html` | 2 | 2 |
| 45 | `appendix/appendix_2.html` | 1 | 1 |
| 46 | `counting/counting_1.html` | 1 | 1 |
| 47 | `counting/counting_2.html` | 1 | 1 |
| 48 | `fem/fem.html` | 1 | 1 |
| 49 | `fem/fem_10.html` | 1 | 1 |
| 50 | `fem/fem_2_2.html` | 1 | 1 |
| 51 | `fem/fem_6_1_1.html` | 1 | 1 |
| 52 | `fem/fem_6_2_1.html` | 1 | 1 |
| 53 | `fem/fem_8_1.html` | 1 | 1 |
| 54 | `heat/heat_4_1.html` | 1 | 1 |
| 55 | `heat/heat_4_2.html` | 1 | 1 |
| 56 | `heat/heat_4_3.html` | 1 | 1 |
| 57 | `heat/heat_5.html` | 1 | 1 |
| 58 | `heat/heat_5_1.html` | 1 | 1 |
| 59 | `heat/heat_5_2.html` | 1 | 1 |
| 60 | `heat/heat_5_3.html` | 1 | 1 |
| 61 | `heat/heat_5_4.html` | 1 | 1 |
| 62 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 63 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 64 | `hydronamics/hydronamics_11_1.html` | 1 | 1 |
| 65 | `hydronamics/hydronamics_11_2.html` | 1 | 1 |
| 66 | `hydronamics/hydronamics_11_3.html` | 1 | 1 |
| 67 | `hydronamics/hydronamics_11_4.html` | 1 | 1 |
| 68 | `hydronamics/hydronamics_11_5.html` | 1 | 1 |
| 69 | `hydronamics/hydronamics_4.html` | 1 | 1 |
| 70 | `hydronamics/hydronamics_6_1.html` | 1 | 1 |
| 71 | `hydronamics/hydronamics_6_2.html` | 1 | 1 |
| 72 | `hydronamics/hydronamics_6_3.html` | 1 | 1 |
| 73 | `hydronamics/hydronamics_6_4.html` | 1 | 1 |
| 74 | `hydronamics/hydronamics_9_2.html` | 1 | 1 |
| 75 | `hydronamics/hydronamics_9_4.html` | 1 | 1 |
| 76 | `mps/mps_1.html` | 1 | 1 |
| 77 | `mps/mps_2.html` | 1 | 1 |
| 78 | `physics/physics_1.html` | 1 | 1 |
| 79 | `physics/physics_6_2_5.html` | 1 | 1 |
| 80 | `physics/physics_6_2_6.html` | 1 | 1 |
| 81 | `physics/physics_6_2_7.html` | 1 | 1 |
| 82 | `physics/physics_6_3_1.html` | 1 | 1 |
| 83 | `physics/physics_7.html` | 1 | 1 |

## Next step

Review Priority A assets page-by-page against the original images, classify each as formula / diagram / other, and only then start exact LaTeX transcription under the existing strict source-image policy.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
