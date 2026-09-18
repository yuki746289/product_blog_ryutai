# Site Inline Image Inventory — 2026-09-18

## Scope and interpretation

- Scope: normal `.html` pages on `develop`; strict audit/re-audit pages and tooling/docs are excluded.
- Target: direct `<img>` references to Word-export style assets matching `img/*.files/imageNNN.(png|gif|jpg|jpeg)`.
- Already converted MathJax formulas referenced only by `data-source-image` are not counted as residual images.
- Priority A means the image is inside `<p class="im">`; this is a **review priority only**, not an automatic assertion that the image is a formula.
- Formula/diagram classification must be confirmed visually before conversion.

## Summary

- HTML pages scanned: **205**
- Residual inline-image placements: **226**
- Unique residual image assets: **224**
- Priority A (`p.im`) placements: **214**
- Missing referenced assets: **49**

### By section

| Section | Placements |
|---|---:|
| `mesh` | 53 |
| `mps` | 49 |
| `physics` | 46 |
| `fem` | 33 |
| `hydronamics` | 21 |
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
| 4 | `mesh/mesh_2.html` | 10 | 10 |
| 5 | `mesh/mesh_5.html` | 9 | 9 |
| 6 | `mps/mps_4.html` | 9 | 7 |
| 7 | `fem/fem_13.html` | 8 | 8 |
| 8 | `physics/physics_6_2_3.html` | 7 | 7 |
| 9 | `fem/fem_1.html` | 6 | 6 |
| 10 | `mesh/mesh_1.html` | 6 | 6 |
| 11 | `column/column_2.html` | 5 | 5 |
| 12 | `fem/fem_12.html` | 5 | 3 |
| 13 | `mesh/mesh_3_2.html` | 5 | 5 |
| 14 | `physics/physics_2.html` | 5 | 5 |
| 15 | `physics/physics_6_1.html` | 5 | 5 |
| 16 | `physics/physics_6_2_1.html` | 5 | 5 |
| 17 | `appendix/appendix_3_1.html` | 4 | 4 |
| 18 | `appendix/appendix_3_2.html` | 4 | 4 |
| 19 | `mesh/mesh_4.html` | 4 | 4 |
| 20 | `physics/physics_5.html` | 4 | 2 |
| 21 | `hydronamics/hydronamics_10_1.html` | 3 | 3 |
| 22 | `physics/physics_4.html` | 3 | 3 |
| 23 | `physics/physics_6_2_2.html` | 3 | 3 |
| 24 | `physics/physics_6_3_2.html` | 3 | 3 |
| 25 | `fem/fem_2_1.html` | 2 | 2 |
| 26 | `fem/fem_2_3.html` | 2 | 2 |
| 27 | `fem/fem_8_2_1.html` | 2 | 2 |
| 28 | `fem/fem_9.html` | 2 | 2 |
| 29 | `hydronamics/hydronamics_14.html` | 2 | 2 |
| 30 | `hydronamics/hydronamics_2.html` | 2 | 2 |
| 31 | `hydronamics/hydronamics_9_1.html` | 2 | 2 |
| 32 | `mps/mps_5.html` | 2 | 2 |
| 33 | `mps/mps_6_1.html` | 2 | 2 |
| 34 | `physics/physics_6_2_4.html` | 2 | 2 |
| 35 | `physics/physics_6_3_3.html` | 2 | 2 |
| 36 | `appendix/appendix_2.html` | 1 | 1 |
| 37 | `counting/counting_1.html` | 1 | 1 |
| 38 | `counting/counting_2.html` | 1 | 1 |
| 39 | `fem/fem.html` | 1 | 1 |
| 40 | `fem/fem_10.html` | 1 | 1 |
| 41 | `fem/fem_2_2.html` | 1 | 1 |
| 42 | `fem/fem_6_1_1.html` | 1 | 1 |
| 43 | `fem/fem_6_2_1.html` | 1 | 1 |
| 44 | `fem/fem_8_1.html` | 1 | 1 |
| 45 | `heat/heat_4_1.html` | 1 | 1 |
| 46 | `heat/heat_4_2.html` | 1 | 1 |
| 47 | `heat/heat_4_3.html` | 1 | 1 |
| 48 | `heat/heat_5.html` | 1 | 1 |
| 49 | `heat/heat_5_1.html` | 1 | 1 |
| 50 | `heat/heat_5_2.html` | 1 | 1 |
| 51 | `heat/heat_5_3.html` | 1 | 1 |
| 52 | `heat/heat_5_4.html` | 1 | 1 |
| 53 | `hydronamics/hydronamics_10.html` | 1 | 1 |
| 54 | `hydronamics/hydronamics_10_2.html` | 1 | 1 |
| 55 | `hydronamics/hydronamics_4.html` | 1 | 1 |
| 56 | `hydronamics/hydronamics_5.html` | 1 | 1 |
| 57 | `hydronamics/hydronamics_6_1.html` | 1 | 1 |
| 58 | `hydronamics/hydronamics_6_2.html` | 1 | 1 |
| 59 | `hydronamics/hydronamics_6_3.html` | 1 | 1 |
| 60 | `hydronamics/hydronamics_6_4.html` | 1 | 1 |
| 61 | `hydronamics/hydronamics_7.html` | 1 | 1 |
| 62 | `hydronamics/hydronamics_9_2.html` | 1 | 1 |
| 63 | `hydronamics/hydronamics_9_4.html` | 1 | 1 |
| 64 | `hydronamics/hydronamics_9_5.html` | 1 | 1 |
| 65 | `mps/mps_1.html` | 1 | 1 |
| 66 | `mps/mps_2.html` | 1 | 1 |
| 67 | `physics/physics_1.html` | 1 | 1 |
| 68 | `physics/physics_3.html` | 1 | 1 |
| 69 | `physics/physics_6_2_5.html` | 1 | 1 |
| 70 | `physics/physics_6_2_6.html` | 1 | 1 |
| 71 | `physics/physics_6_2_7.html` | 1 | 1 |
| 72 | `physics/physics_6_3_1.html` | 1 | 1 |
| 73 | `physics/physics_7.html` | 1 | 1 |

## Next step

Review Priority A assets page-by-page against the original images, classify each as formula / diagram / other, and only then start exact LaTeX transcription under the existing strict source-image policy.

Detailed per-image data is stored in:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.csv`
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.json`
