# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **468**
- Unique residual image assets: **466**
- Priority A (`p.im`) placements: **449**
- Missing referenced assets: **49**

### By section

| Section | Placements |
|---|---:|
| `hydronamics` | 152 |
| `fem` | 125 |
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
| 7 | `fem/fem_11_1.html` | 11 | 11 |
| 8 | `hydronamics/hydronamics_12_1.html` | 10 | 10 |
| 9 | `hydronamics/hydronamics_4.html` | 10 | 10 |
| 10 | `hydronamics/hydronamics_9_2.html` | 10 | 10 |
| 11 | `mesh/mesh_2.html` | 10 | 10 |
| 12 | `hydronamics/hydronamics_9_4.html` | 9 | 9 |
| 13 | `mesh/mesh_5.html` | 9 | 9 |
| 14 | `mps/mps_4.html` | 9 | 7 |
| 15 | `physics/physics_4.html` | 9 | 6 |
| 16 | `fem/fem_13.html` | 8 | 8 |
| 17 | `fem/fem_2_1.html` | 8 | 8 |
| 18 | `hydronamics/hydronamics_10_1.html` | 8 | 8 |
| 19 | `hydronamics/hydronamics_12_2.html` | 8 | 6 |
| 20 | `hydronamics/hydronamics_6_1.html` | 8 | 8 |
| 21 | `fem/fem_10.html` | 7 | 7 |
| 22 | `fem/fem_2_3.html` | 7 | 7 |
| 23 | `fem/fem_5.html` | 7 | 7 |
| 24 | `fem/fem_6_2_1.html` | 7 | 7 |
| 25 | `fem/fem_8_2_1.html` | 7 | 7 |
| 26 | `hydronamics/hydronamics_6_2.html` | 7 | 7 |
| 27 | `hydronamics/hydronamics_6_3.html` | 7 | 7 |
| 28 | `hydronamics/hydronamics_6_4.html` | 7 | 6 |
| 29 | `physics/physics_3.html` | 7 | 7 |
| 30 | `physics/physics_6_2_3.html` | 7 | 7 |
| 31 | `fem/fem_1.html` | 6 | 6 |
| 32 | `fem/fem_2_2.html` | 6 | 6 |
| 33 | `fem/fem_6_1_1.html` | 6 | 6 |
| 34 | `fem/fem_6_1_5.html` | 6 | 6 |
| 35 | `hydronamics/hydronamics_9_1.html` | 6 | 6 |
| 36 | `hydronamics/hydronamics_9_5.html` | 6 | 6 |
| 37 | `mesh/mesh_1.html` | 6 | 6 |
| 38 | `column/column_2.html` | 5 | 5 |
| 39 | `fem/fem_12.html` | 5 | 3 |
| 40 | `fem/fem_4.html` | 5 | 5 |
| 41 | `fem/fem_9.html` | 5 | 5 |
| 42 | `hydronamics/hydronamics_9_6.html` | 5 | 5 |
| 43 | `mesh/mesh_3_2.html` | 5 | 5 |
| 44 | `physics/physics_6_1.html` | 5 | 5 |
| 45 | `physics/physics_6_2_1.html` | 5 | 5 |
| 46 | `appendix/appendix_3_1.html` | 4 | 4 |
| 47 | `appendix/appendix_3_2.html` | 4 | 4 |
| 48 | `hydronamics/hydronamics_11.html` | 4 | 4 |
| 49 | `hydronamics/hydronamics_12.html` | 4 | 4 |
| 50 | `mesh/mesh_4.html` | 4 | 4 |
| 51 | `physics/physics_5.html` | 4 | 2 |
| 52 | `fem/fem_6_2_2.html` | 3 | 3 |
| 53 | `fem/fem_6_2_3.html` | 3 | 3 |
| 54 | `fem/fem_6_2_4.html` | 3 | 3 |
| 55 | `fem/fem_6_2_5.html` | 3 | 3 |
| 56 | `physics/physics_6_2_2.html` | 3 | 3 |
| 57 | `physics/physics_6_3_2.html` | 3 | 3 |
| 58 | `fem/fem_3.html` | 2 | 2 |
| 59 | `fem/fem_6_1_2.html` | 2 | 2 |
| 60 | `fem/fem_6_1_3.html` | 2 | 2 |
| 61 | `fem/fem_6_1_4.html` | 2 | 2 |
| 62 | `fem/fem_8.html` | 2 | 2 |
| 63 | `hydronamics/hydronamics_11_6.html` | 2 | 2 |
| 64 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 65 | `hydronamics/hydronamics_5.html` | 2 | 2 |
| 66 | `hydronamics/hydronamics_7.html` | 2 | 2 |
| 67 | `hydronamics/hydronamics_9_3.html` | 2 | 2 |
| 68 | `mps/mps_5.html` | 2 | 2 |
| 69 | `mps/mps_6_1.html` | 2 | 2 |
| 70 | `physics/physics_6_2_4.html` | 2 | 2 |
| 71 | `physics/physics_6_3_3.html` | 2 | 2 |
| 72 | `appendix/appendix_2.html` | 1 | 1 |
| 73 | `counting/counting_1.html` | 1 | 1 |
| 74 | `counting/counting_2.html` | 1 | 1 |
| 75 | `fem/fem.html` | 1 | 1 |
| 76 | `fem/fem_8_1.html` | 1 | 1 |
| 77 | `heat/heat_4_1.html` | 1 | 1 |
| 78 | `heat/heat_4_2.html` | 1 | 1 |
| 79 | `heat/heat_4_3.html` | 1 | 1 |
| 80 | `heat/heat_5.html` | 1 | 1 |
| 81 | `heat/heat_5_1.html` | 1 | 1 |
| 82 | `heat/heat_5_2.html` | 1 | 1 |
| 83 | `heat/heat_5_3.html` | 1 | 1 |
| 84 | `heat/heat_5_4.html` | 1 | 1 |
| 85 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 86 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 87 | `hydronamics/hydronamics_11_1.html` | 1 | 1 |
| 88 | `hydronamics/hydronamics_11_2.html` | 1 | 1 |
| 89 | `hydronamics/hydronamics_11_3.html` | 1 | 1 |
| 90 | `hydronamics/hydronamics_11_4.html` | 1 | 1 |
| 91 | `hydronamics/hydronamics_11_5.html` | 1 | 1 |
| 92 | `mps/mps_1.html` | 1 | 1 |
| 93 | `mps/mps_2.html` | 1 | 1 |
| 94 | `physics/physics_1.html` | 1 | 1 |
| 95 | `physics/physics_6_2_5.html` | 1 | 1 |
| 96 | `physics/physics_6_2_6.html` | 1 | 1 |
| 97 | `physics/physics_6_2_7.html` | 1 | 1 |
| 98 | `physics/physics_6_3_1.html` | 1 | 1 |
| 99 | `physics/physics_7.html` | 1 | 1 |

## Next step

Review Priority A assets page-by-page against the original images, classify each as formula / diagram / other, and only then start exact LaTeX transcription under the existing strict source-image policy.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
