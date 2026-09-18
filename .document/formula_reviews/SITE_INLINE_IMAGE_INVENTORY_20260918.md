# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **413**
- Unique residual image assets: **411**
- Priority A (`p.im`) placements: **394**
- Missing referenced assets: **49**

### By section

| Section | Placements |
|---|---:|
| `hydronamics` | 152 |
| `fem` | 70 |
| `physics` | 65 |
| `mesh` | 53 |
| `mps` | 49 |
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
| 3 | `hydronamics/hydronamics_14.html` | 14 | 14 |
| 4 | `hydronamics/hydronamics_8.html` | 12 | 11 |
| 5 | `mps/mps_3.html` | 12 | 8 |
| 6 | `physics/physics_2.html` | 12 | 12 |
| 7 | `hydronamics/hydronamics_12_1.html` | 10 | 10 |
| 8 | `hydronamics/hydronamics_4.html` | 10 | 10 |
| 9 | `hydronamics/hydronamics_9_2.html` | 10 | 10 |
| 10 | `mesh/mesh_2.html` | 10 | 10 |
| 11 | `hydronamics/hydronamics_9_4.html` | 9 | 9 |
| 12 | `mesh/mesh_5.html` | 9 | 9 |
| 13 | `mps/mps_4.html` | 9 | 7 |
| 14 | `physics/physics_4.html` | 9 | 6 |
| 15 | `fem/fem_13.html` | 8 | 8 |
| 16 | `hydronamics/hydronamics_10_1.html` | 8 | 8 |
| 17 | `hydronamics/hydronamics_12_2.html` | 8 | 6 |
| 18 | `hydronamics/hydronamics_6_1.html` | 8 | 8 |
| 19 | `fem/fem_5.html` | 7 | 7 |
| 20 | `hydronamics/hydronamics_6_2.html` | 7 | 7 |
| 21 | `hydronamics/hydronamics_6_3.html` | 7 | 7 |
| 22 | `hydronamics/hydronamics_6_4.html` | 7 | 6 |
| 23 | `physics/physics_3.html` | 7 | 7 |
| 24 | `physics/physics_6_2_3.html` | 7 | 7 |
| 25 | `fem/fem_1.html` | 6 | 6 |
| 26 | `hydronamics/hydronamics_9_1.html` | 6 | 6 |
| 27 | `hydronamics/hydronamics_9_5.html` | 6 | 6 |
| 28 | `mesh/mesh_1.html` | 6 | 6 |
| 29 | `column/column_2.html` | 5 | 5 |
| 30 | `fem/fem_12.html` | 5 | 3 |
| 31 | `fem/fem_4.html` | 5 | 5 |
| 32 | `fem/fem_9.html` | 5 | 5 |
| 33 | `hydronamics/hydronamics_9_6.html` | 5 | 5 |
| 34 | `mesh/mesh_3_2.html` | 5 | 5 |
| 35 | `physics/physics_6_1.html` | 5 | 5 |
| 36 | `physics/physics_6_2_1.html` | 5 | 5 |
| 37 | `appendix/appendix_3_1.html` | 4 | 4 |
| 38 | `appendix/appendix_3_2.html` | 4 | 4 |
| 39 | `hydronamics/hydronamics_11.html` | 4 | 4 |
| 40 | `hydronamics/hydronamics_12.html` | 4 | 4 |
| 41 | `mesh/mesh_4.html` | 4 | 4 |
| 42 | `physics/physics_5.html` | 4 | 2 |
| 43 | `fem/fem_6_2_2.html` | 3 | 3 |
| 44 | `fem/fem_6_2_3.html` | 3 | 3 |
| 45 | `fem/fem_6_2_4.html` | 3 | 3 |
| 46 | `fem/fem_6_2_5.html` | 3 | 3 |
| 47 | `physics/physics_6_2_2.html` | 3 | 3 |
| 48 | `physics/physics_6_3_2.html` | 3 | 3 |
| 49 | `fem/fem_2_1.html` | 2 | 2 |
| 50 | `fem/fem_2_3.html` | 2 | 2 |
| 51 | `fem/fem_3.html` | 2 | 2 |
| 52 | `fem/fem_6_1_2.html` | 2 | 2 |
| 53 | `fem/fem_6_1_3.html` | 2 | 2 |
| 54 | `fem/fem_6_1_4.html` | 2 | 2 |
| 55 | `fem/fem_8.html` | 2 | 2 |
| 56 | `fem/fem_8_2_1.html` | 2 | 2 |
| 57 | `hydronamics/hydronamics_11_6.html` | 2 | 2 |
| 58 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 59 | `hydronamics/hydronamics_5.html` | 2 | 2 |
| 60 | `hydronamics/hydronamics_7.html` | 2 | 2 |
| 61 | `hydronamics/hydronamics_9_3.html` | 2 | 2 |
| 62 | `mps/mps_5.html` | 2 | 2 |
| 63 | `mps/mps_6_1.html` | 2 | 2 |
| 64 | `physics/physics_6_2_4.html` | 2 | 2 |
| 65 | `physics/physics_6_3_3.html` | 2 | 2 |
| 66 | `appendix/appendix_2.html` | 1 | 1 |
| 67 | `counting/counting_1.html` | 1 | 1 |
| 68 | `counting/counting_2.html` | 1 | 1 |
| 69 | `fem/fem.html` | 1 | 1 |
| 70 | `fem/fem_10.html` | 1 | 1 |
| 71 | `fem/fem_2_2.html` | 1 | 1 |
| 72 | `fem/fem_6_1_1.html` | 1 | 1 |
| 73 | `fem/fem_6_2_1.html` | 1 | 1 |
| 74 | `fem/fem_8_1.html` | 1 | 1 |
| 75 | `heat/heat_4_1.html` | 1 | 1 |
| 76 | `heat/heat_4_2.html` | 1 | 1 |
| 77 | `heat/heat_4_3.html` | 1 | 1 |
| 78 | `heat/heat_5.html` | 1 | 1 |
| 79 | `heat/heat_5_1.html` | 1 | 1 |
| 80 | `heat/heat_5_2.html` | 1 | 1 |
| 81 | `heat/heat_5_3.html` | 1 | 1 |
| 82 | `heat/heat_5_4.html` | 1 | 1 |
| 83 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 84 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 85 | `hydronamics/hydronamics_11_1.html` | 1 | 1 |
| 86 | `hydronamics/hydronamics_11_2.html` | 1 | 1 |
| 87 | `hydronamics/hydronamics_11_3.html` | 1 | 1 |
| 88 | `hydronamics/hydronamics_11_4.html` | 1 | 1 |
| 89 | `hydronamics/hydronamics_11_5.html` | 1 | 1 |
| 90 | `mps/mps_1.html` | 1 | 1 |
| 91 | `mps/mps_2.html` | 1 | 1 |
| 92 | `physics/physics_1.html` | 1 | 1 |
| 93 | `physics/physics_6_2_5.html` | 1 | 1 |
| 94 | `physics/physics_6_2_6.html` | 1 | 1 |
| 95 | `physics/physics_6_2_7.html` | 1 | 1 |
| 96 | `physics/physics_6_3_1.html` | 1 | 1 |
| 97 | `physics/physics_7.html` | 1 | 1 |

## Next step

Review Priority A assets page-by-page against the original images, classify each as formula / diagram / other, and only then start exact LaTeX transcription under the existing strict source-image policy.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
