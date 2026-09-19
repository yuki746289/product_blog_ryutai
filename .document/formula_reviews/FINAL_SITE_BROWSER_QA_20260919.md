# Final Site Browser QA — 2026-09-19

- Overall: **FAIL**
- Browser: Chromium / Playwright
- Viewports: desktop 1440×1000, mobile 390×844
- Discovered normal HTML pages: **205**
- QA checks: **410**
- Hard-failure rows: **191**
- MPS known missing references: **49/49**
- Production deployment: not performed.

## Global metrics

| Metric | Count |
|---|---:|
| MathJax errors | 0 |
| Unrendered | 0 |
| Page overflow rows | 0 |
| Uncontained overflow | 56741 |
| Page errors | 1 |
| Non-MPS missing images (desktop) | 0 |
| Allowed local math scroll | 146 |

## MPS SOURCE BLOCKED / HOLD

| Page | Expected | Actual |
|---|---:|---:|
| mps/mps_1.html | 1 | 1 |
| mps/mps_2.html | 1 | 1 |
| mps/mps_3.html | 12 | 12 |
| mps/mps_4.html | 9 | 9 |
| mps/mps_5.html | 2 | 2 |
| mps/mps_6_1.html | 2 | 2 |
| mps/mps_6_2.html | 22 | 22 |

## Failures

- appendix/appendix.html [mobile]: uncontained=307
- appendix/appendix_3_1.html [mobile]: uncontained=307
- column/column.html [mobile]: uncontained=307
- column/column_4.html [mobile]: uncontained=307
- counting/counting_2.html [mobile]: uncontained=307
- design_samples/v1.5/technical-clean.html [mobile]: uncontained=7
- fem/fem_11.html [mobile]: uncontained=307
- fem/fem_13.html [mobile]: uncontained=307
- fem/fem_2_3.html [mobile]: uncontained=307
- fem/fem_6.html [mobile]: uncontained=307
- fem/fem_6_1_3.html [mobile]: uncontained=311
- fem/fem_6_2_1.html [mobile]: uncontained=309
- fem/fem_6_2_5.html [mobile]: uncontained=311
- fem/fem_7_1_1.html [mobile]: uncontained=308
- fem/fem_7_2_2.html [mobile]: uncontained=309
- fem/fem_8_2_1.html [mobile]: uncontained=307
- fortran/fortran_11.html [mobile]: uncontained=307
- fortran/fortran_2.html [mobile]: uncontained=307
- fortran/fortran_6.html [mobile]: uncontained=307
- graph.html [mobile]: uncontained=2
- heat/heat_2.html [mobile]: uncontained=307
- heat/heat_4_2.html [mobile]: uncontained=307
- heat/heat_5_2.html [mobile]: uncontained=307
- heat/heat_7.html [mobile]: pageerror=1; uncontained=307
- hydronamics/hydronamics.html [mobile]: uncontained=307
- hydronamics/hydronamics_10_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_6.html [mobile]: uncontained=307
- hydronamics/hydronamics_13.html [mobile]: uncontained=307
- hydronamics/hydronamics_4.html [mobile]: uncontained=307
- hydronamics/hydronamics_6_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_8.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_3.html [mobile]: uncontained=307
- index.html [mobile]: uncontained=307
- library/library_buble.html [mobile]: uncontained=307
- mail/introduce.html [mobile]: uncontained=307
- mesh/mesh_3.html [mobile]: uncontained=307
- mesh/mesh_5.html [mobile]: uncontained=307
- mps/mps_3.html [mobile]: uncontained=307
- mps/mps_6_1.html [mobile]: uncontained=307
- physics/physics_1.html [mobile]: uncontained=307
- physics/physics_5.html [mobile]: uncontained=307
- physics/physics_6_2_1.html [mobile]: uncontained=307
- physics/physics_6_2_5.html [mobile]: uncontained=307
- physics/physics_6_3_1.html [mobile]: uncontained=307
- physics/physics_8.html [mobile]: uncontained=307
- sitemap/sitemap.html [mobile]: uncontained=307
- appendix/appendix_1.html [mobile]: uncontained=307
- appendix/appendix_3_2.html [mobile]: uncontained=307
- column/column_1.html [mobile]: uncontained=307
- column/column_5.html [mobile]: uncontained=307
- design_samples/v1.5/academic-minimal.html [mobile]: uncontained=7
- fem/fem.html [mobile]: uncontained=307
- fem/fem_11_1.html [mobile]: uncontained=307
- fem/fem_2.html [mobile]: uncontained=307
- fem/fem_3.html [mobile]: uncontained=307
- fem/fem_6_1.html [mobile]: uncontained=307
- fem/fem_6_1_4.html [mobile]: uncontained=311
- fem/fem_6_2_2.html [mobile]: uncontained=311
- fem/fem_6_2_6.html [mobile]: uncontained=309
- fem/fem_7_1_2.html [mobile]: uncontained=309
- fem/fem_8.html [mobile]: uncontained=307
- fem/fem_8_2_2.html [mobile]: uncontained=307
- fortran/fortran.html [mobile]: uncontained=307
- fortran/fortran_12.html [mobile]: uncontained=307
- fortran/fortran_3.html [mobile]: uncontained=307
- fortran/fortran_7.html [mobile]: uncontained=307
- graph_2.html [mobile]: uncontained=2
- heat/heat_3.html [mobile]: uncontained=307
- heat/heat_4_3.html [mobile]: uncontained=307
- heat/heat_5_3.html [mobile]: uncontained=307
- heat/heat_7_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_10_3.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_3.html [mobile]: uncontained=307
- hydronamics/hydronamics_12.html [mobile]: uncontained=307
- hydronamics/hydronamics_14.html [mobile]: uncontained=307
- hydronamics/hydronamics_5.html [mobile]: uncontained=307
- hydronamics/hydronamics_6_3.html [mobile]: uncontained=307
- hydronamics/hydronamics_9.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_4.html [mobile]: uncontained=307
- introduce/introduce.html [mobile]: uncontained=307
- library/library_delauney.html [mobile]: uncontained=307
- mail/mail.html [mobile]: uncontained=307
- mesh/mesh.html [mobile]: uncontained=307
- mesh/mesh_3_1.html [mobile]: uncontained=307
- mps/mps.html [mobile]: uncontained=307
- mps/mps_4.html [mobile]: uncontained=307
- mps/mps_6_2.html [mobile]: uncontained=307
- physics/physics_2.html [mobile]: uncontained=307
- physics/physics_6.html [mobile]: uncontained=307
- physics/physics_6_2_2.html [mobile]: uncontained=307
- physics/physics_6_2_6.html [mobile]: uncontained=307
- physics/physics_6_3_2.html [mobile]: uncontained=307
- profile/profile.html [mobile]: uncontained=307
- appendix/appendix_2.html [mobile]: uncontained=307
- book/book.html [mobile]: uncontained=307
- column/column_2.html [mobile]: uncontained=307
- counting/counting.html [mobile]: uncontained=307
- design_samples/v1.5/gray/mega-menu-preview.html [mobile]: uncontained=123
- fem/fem_1.html [mobile]: uncontained=307
- fem/fem_11_2.html [mobile]: uncontained=307
- fem/fem_2_1.html [mobile]: uncontained=307
- fem/fem_4.html [mobile]: uncontained=307
- fem/fem_6_1_1.html [mobile]: uncontained=309
- fem/fem_6_1_5.html [mobile]: uncontained=309
- fem/fem_6_2_3.html [mobile]: uncontained=311
- fem/fem_7.html [mobile]: uncontained=307
- fem/fem_7_2.html [mobile]: uncontained=307
- fem/fem_8_1.html [mobile]: uncontained=307
- fem/fem_8_3.html [mobile]: uncontained=307
- fortran/fortran_1.html [mobile]: uncontained=307
- fortran/fortran_13.html [mobile]: uncontained=307
- fortran/fortran_4.html [mobile]: uncontained=307
- fortran/fortran_8.html [mobile]: uncontained=307
- heat/heat.html [mobile]: uncontained=307
- heat/heat_4.html [mobile]: uncontained=307
- heat/heat_5.html [mobile]: uncontained=307
- heat/heat_5_4.html [mobile]: uncontained=307
- heat/heat_7_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_10.html [mobile]: uncontained=307
- hydronamics/hydronamics_11.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_4.html [mobile]: uncontained=307
- hydronamics/hydronamics_12_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_6.html [mobile]: uncontained=307
- hydronamics/hydronamics_6_4.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_5.html [mobile]: uncontained=307
- library/library.html [mobile]: uncontained=307
- library/library_renum.html [mobile]: uncontained=307
- mail/mail_base.html [mobile]: uncontained=307
- mesh/mesh_1.html [mobile]: uncontained=307
- mesh/mesh_3_2.html [mobile]: uncontained=307
- mps/mps_1.html [mobile]: uncontained=307
- mps/mps_5.html [mobile]: uncontained=307
- pdf/pdf.html [mobile]: uncontained=307
- physics/physics_3.html [mobile]: uncontained=307
- physics/physics_6_1.html [mobile]: uncontained=307
- physics/physics_6_2_3.html [mobile]: uncontained=307
- physics/physics_6_2_7.html [mobile]: uncontained=307
- physics/physics_6_3_3.html [mobile]: uncontained=307
- appendix/appendix_3.html [mobile]: uncontained=307
- book/library.html [mobile]: uncontained=307
- column/column_3.html [mobile]: uncontained=307
- counting/counting_1.html [mobile]: uncontained=307
- design_samples/v1.5/gray/mega-menu-themes.html [mobile]: uncontained=63
- design_samples/v1.5/modern-dashboard.html [mobile]: uncontained=7
- fem/fem_10.html [mobile]: uncontained=307
- fem/fem_12.html [mobile]: uncontained=307
- fem/fem_2_2.html [mobile]: uncontained=307
- fem/fem_5.html [mobile]: uncontained=307
- fem/fem_6_1_2.html [mobile]: uncontained=311
- fem/fem_6_2.html [mobile]: uncontained=307
- fem/fem_6_2_4.html [mobile]: uncontained=311
- fem/fem_7_1.html [mobile]: uncontained=307
- fem/fem_7_2_1.html [mobile]: uncontained=308
- fem/fem_8_2.html [mobile]: uncontained=307
- fem/fem_9.html [mobile]: uncontained=307
- fortran/fortran_10.html [mobile]: uncontained=307
- fortran/fortran_14.html [mobile]: uncontained=307
- fortran/fortran_5.html [mobile]: uncontained=307
- fortran/fortran_9.html [mobile]: uncontained=307
- heat/heat_1.html [mobile]: uncontained=307
- heat/heat_4_1.html [mobile]: uncontained=307
- heat/heat_5_1.html [mobile]: uncontained=307
- heat/heat_6.html [mobile]: uncontained=307
- heat/heat_8.html [mobile]: uncontained=307
- hydronamics/hydronamics_10_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_11_5.html [mobile]: uncontained=307
- hydronamics/hydronamics_12_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_3.html [mobile]: uncontained=307
- hydronamics/hydronamics_6_1.html [mobile]: uncontained=307
- hydronamics/hydronamics_7.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_2.html [mobile]: uncontained=307
- hydronamics/hydronamics_9_6.html [mobile]: uncontained=307
- library/library_1.html [mobile]: uncontained=307
- link/link.html [mobile]: uncontained=307
- math/math.html [mobile]: uncontained=307
- mesh/mesh_2.html [mobile]: uncontained=307
- mesh/mesh_4.html [mobile]: uncontained=307
- mps/mps_2.html [mobile]: uncontained=307
- mps/mps_6.html [mobile]: uncontained=307
- physics/physics.html [mobile]: uncontained=307
- physics/physics_4.html [mobile]: uncontained=307
- physics/physics_6_2.html [mobile]: uncontained=307
- physics/physics_6_2_4.html [mobile]: uncontained=307
- physics/physics_6_3.html [mobile]: uncontained=307
- physics/physics_7.html [mobile]: uncontained=307
- revision_history.html [mobile]: uncontained=307

## Acceptance criteria

- MPS 49 known missing references remain SOURCE BLOCKED / HOLD.
- MathJax errors = 0.
- Unrendered = 0.
- Page overflow = 0.
- Uncontained overflow = 0.
- Missing images outside MPS HOLD = 0.
