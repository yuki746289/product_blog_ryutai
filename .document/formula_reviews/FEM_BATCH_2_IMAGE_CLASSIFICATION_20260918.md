# FEM Batch 2 Image Classification — 2026-09-18

## Scope

- `fem/fem_2_3.html`: 7 placements
- `fem/fem_5.html`: 7 placements
- `fem/fem_6_2_1.html`: 7 placements
- `fem/fem_8_2_1.html`: 7 placements
- Total: **28**

Review workflow run: **35314195840**  
Artifact: `fem-batch-2-review`  
Artifact id: **10534048130**

## Classification

| Page | Placements | Formula / mathematical text | Diagram / mixed diagram |
|---|---:|---:|---:|
| `fem/fem_2_3.html` | 7 | **5** | **2** |
| `fem/fem_5.html` | 7 | **7** | 0 |
| `fem/fem_6_2_1.html` | 7 | **6** | **1** |
| `fem/fem_8_2_1.html` | 7 | **5** | **2** |
| **Total** | **28** | **23** | **5** |

## Diagram / mixed-diagram assets retained unchanged

### fem_2_3
- `image001.png`: tetrahedral interpolation geometry
- `image007.png`: volume-coordinate geometry

### fem_6_2_1
- `image001.png`: tetrahedral / volume-coordinate geometry

### fem_8_2_1
- `image001.png`: free-surface droplet diagram
- `image007.png`: droplet mesh diagram with an embedded force expression; retain as a mixed diagram

## Formula targets

- `fem_2_3`: `image002.png`–`image006.png` (5)
- `fem_6_2_1`: `image002.png`–`image007.png` (6)
- `fem_8_2_1`: `image002.png`–`image006.png` (5)

Subtotal for immediate strict conversion: **16 formulas**.

## fem_5 handling

All seven `fem_5` assets are mathematical content. `image002.png` includes Japanese explanatory prose together with determinant/permutation formulas, so the page should be reconstructed as **HTML prose + MathJax**, not forced into a single pure-display-math block. The `fem_5` set is therefore separated from the immediate 16-formula conversion batch.

Original source images remain canonical. Production deployment has not been performed.
