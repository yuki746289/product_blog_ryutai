# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **603**
- Unique residual image assets: **601**
- Priority A (`p.im`) placements: **582**
- Missing referenced assets: **49**

### By section

| Section | Placements |
|---|---:|
| `hydronamics` | 152 |
| `fem` | 125 |
| `heat` | 102 |
| `physics` | 65 |
| `mesh` | 53 |
| `appendix` | 50 |
| `mps` | 49 |
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
| 1 | `heat/heat_7_1.html` | 33 | 33 |
| 2 | `heat/heat_7_2.html` | 32 | 32 |
| 3 | `mps/mps_6_2.html` | 22 | 22 |
| 4 | `mesh/mesh_3_1.html` | 19 | 17 |
| 5 | `appendix/appendix_1.html` | 14 | 14 |
| 6 | `hydronamics/hydronamics_14.html` | 14 | 14 |
| 7 | `heat/heat_6.html` | 13 | 11 |
| 8 | `appendix/appendix_2.html` | 12 | 12 |
| 9 | `appendix/appendix_3_1.html` | 12 | 12 |
| 10 | `appendix/appendix_3_2.html` | 12 | 12 |
| 11 | `hydronamics/hydronamics_8.html` | 12 | 11 |
| 12 | `mps/mps_3.html` | 12 | 8 |
| 13 | `physics/physics_2.html` | 12 | 12 |
| 14 | `fem/fem_11_1.html` | 11 | 11 |
| 15 | `hydronamics/hydronamics_12_1.html` | 10 | 10 |
| 16 | `hydronamics/hydronamics_4.html` | 10 | 10 |
| 17 | `hydronamics/hydronamics_9_2.html` | 10 | 10 |
| 18 | `mesh/mesh_2.html` | 10 | 10 |
| 19 | `hydronamics/hydronamics_9_4.html` | 9 | 9 |
| 20 | `mesh/mesh_5.html` | 9 | 9 |
| 21 | `mps/mps_4.html` | 9 | 7 |
| 22 | `physics/physics_4.html` | 9 | 6 |
| 23 | `fem/fem_13.html` | 8 | 8 |
| 24 | `fem/fem_2_1.html` | 8 | 8 |
| 25 | `hydronamics/hydronamics_10_1.html` | 8 | 8 |
| 26 | `hydronamics/hydronamics_12_2.html` | 8 | 6 |
| 27 | `hydronamics/hydronamics_6_1.html` | 8 | 8 |
| 28 | `fem/fem_10.html` | 7 | 7 |
| 29 | `fem/fem_2_3.html` | 7 | 7 |
| 30 | `fem/fem_5.html` | 7 | 7 |
| 31 | `fem/fem_6_2_1.html` | 7 | 7 |
| 32 | `fem/fem_8_2_1.html` | 7 | 7 |
| 33 | `heat/heat_5_4.html` | 7 | 7 |
| 34 | `hydronamics/hydronamics_6_2.html` | 7 | 7 |
| 35 | `hydronamics/hydronamics_6_3.html` | 7 | 7 |
| 36 | `hydronamics/hydronamics_6_4.html` | 7 | 6 |
| 37 | `physics/physics_3.html` | 7 | 7 |
| 38 | `physics/physics_6_2_3.html` | 7 | 7 |
| 39 | `fem/fem_1.html` | 6 | 6 |
| 40 | `fem/fem_2_2.html` | 6 | 6 |
| 41 | `fem/fem_6_1_1.html` | 6 | 6 |
| 42 | `fem/fem_6_1_5.html` | 6 | 6 |
| 43 | `hydronamics/hydronamics_9_1.html` | 6 | 6 |
| 44 | `hydronamics/hydronamics_9_5.html` | 6 | 6 |
| 45 | `mesh/mesh_1.html` | 6 | 6 |
| 46 | `column/column_2.html` | 5 | 5 |
| 47 | `fem/fem_12.html` | 5 | 3 |
| 48 | `fem/fem_4.html` | 5 | 5 |
| 49 | `fem/fem_9.html` | 5 | 5 |
| 50 | `hydronamics/hydronamics_9_6.html` | 5 | 5 |
| 51 | `mesh/mesh_3_2.html` | 5 | 5 |
| 52 | `physics/physics_6_1.html` | 5 | 5 |
| 53 | `physics/physics_6_2_1.html` | 5 | 5 |
| 54 | `hydronamics/hydronamics_11.html` | 4 | 4 |
| 55 | `hydronamics/hydronamics_12.html` | 4 | 4 |
| 56 | `mesh/mesh_4.html` | 4 | 4 |
| 57 | `physics/physics_5.html` | 4 | 2 |
| 58 | `fem/fem_6_2_2.html` | 3 | 3 |
| 59 | `fem/fem_6_2_3.html` | 3 | 3 |
| 60 | `fem/fem_6_2_4.html` | 3 | 3 |
| 61 | `fem/fem_6_2_5.html` | 3 | 3 |
| 62 | `heat/heat_4_3.html` | 3 | 3 |
| 63 | `heat/heat_5_2.html` | 3 | 3 |
| 64 | `heat/heat_5_3.html` | 3 | 3 |
| 65 | `physics/physics_6_2_2.html` | 3 | 3 |
| 66 | `physics/physics_6_3_2.html` | 3 | 3 |
| 67 | `fem/fem_3.html` | 2 | 2 |
| 68 | `fem/fem_6_1_2.html` | 2 | 2 |
| 69 | `fem/fem_6_1_3.html` | 2 | 2 |
| 70 | `fem/fem_6_1_4.html` | 2 | 2 |
| 71 | `fem/fem_8.html` | 2 | 2 |
| 72 | `heat/heat_4_1.html` | 2 | 2 |
| 73 | `heat/heat_4_2.html` | 2 | 2 |
| 74 | `heat/heat_5_1.html` | 2 | 2 |
| 75 | `hydronamics/hydronamics_11_6.html` | 2 | 2 |
| 76 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 77 | `hydronamics/hydronamics_5.html` | 2 | 2 |
| 78 | `hydronamics/hydronamics_7.html` | 2 | 2 |
| 79 | `hydronamics/hydronamics_9_3.html` | 2 | 2 |
| 80 | `mps/mps_5.html` | 2 | 2 |
| 81 | `mps/mps_6_1.html` | 2 | 2 |
| 82 | `physics/physics_6_2_4.html` | 2 | 2 |
| 83 | `physics/physics_6_3_3.html` | 2 | 2 |
| 84 | `counting/counting_1.html` | 1 | 1 |
| 85 | `counting/counting_2.html` | 1 | 1 |
| 86 | `fem/fem.html` | 1 | 1 |
| 87 | `fem/fem_8_1.html` | 1 | 1 |
| 88 | `heat/heat_3.html` | 1 | 1 |
| 89 | `heat/heat_5.html` | 1 | 1 |
| 90 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 91 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 92 | `hydronamics/hydronamics_11_1.html` | 1 | 1 |
| 93 | `hydronamics/hydronamics_11_2.html` | 1 | 1 |
| 94 | `hydronamics/hydronamics_11_3.html` | 1 | 1 |
| 95 | `hydronamics/hydronamics_11_4.html` | 1 | 1 |
| 96 | `hydronamics/hydronamics_11_5.html` | 1 | 1 |
| 97 | `mps/mps_1.html` | 1 | 1 |
| 98 | `mps/mps_2.html` | 1 | 1 |
| 99 | `physics/physics_1.html` | 1 | 1 |
| 100 | `physics/physics_6_2_5.html` | 1 | 1 |
| 101 | `physics/physics_6_2_6.html` | 1 | 1 |
| 102 | `physics/physics_6_2_7.html` | 1 | 1 |
| 103 | `physics/physics_6_3_1.html` | 1 | 1 |
| 104 | `physics/physics_7.html` | 1 | 1 |

## Next step

Review Priority A assets page-by-page against the original images, classify each as formula / diagram / other, and only then start exact LaTeX transcription under the existing strict source-image policy.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
