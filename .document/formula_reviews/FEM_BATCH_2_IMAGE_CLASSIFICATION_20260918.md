# FEM Batch 2 Image Classification — 2026-09-18

## Scope

- `fem/fem_2_3.html`: 7 placements
- `fem/fem_5.html`: 7 placements
- `fem/fem_6_2_1.html`: 7 placements
- `fem/fem_8_2_1.html`: 7 placements
- Total: **28**

Review workflow run: **35312926665**  
Artifact: `fem-batch-2-review`  
Artifact id: **10533647410**

## Classification

| Page | Placements | Formula / mathematical text | Diagram / mixed |
|---|---:|---:|---:|
| `fem/fem_2_3.html` | 7 | **5** | **2** |
| `fem/fem_5.html` | 7 | **7** | 0 |
| `fem/fem_6_2_1.html` | 7 | **6** | **1** |
| `fem/fem_8_2_1.html` | 7 | **5** | **2** |
| **Total** | **28** | **23** | **5** |

## Diagram / mixed assets retained

### fem_2_3
- `image001.png`: tetrahedral interpolation geometry
- `image007.png`: volume-coordinate geometry

### fem_6_2_1
- `image001.png`: tetrahedral / volume-coordinate geometry

### fem_8_2_1
- `image001.png`: free-surface stress diagram
- `image007.png`: droplet mesh + surface-force callout (mixed figure)

## Formula targets

- `fem_2_3`: `image002.png`–`image006.png` = 5
- `fem_5`: `image001.png`–`image007.png` = 7
- `fem_6_2_1`: `image002.png`–`image007.png` = 6
- `fem_8_2_1`: `image002.png`–`image006.png` = 5

Because `fem_5` contains very long determinant/permutation expansions, conversion is split operationally:
1. Batch 2A: `fem_2_3`, `fem_6_2_1`, `fem_8_2_1` — 16 formulas.
2. Batch 2B: `fem_5` — 7 formulas.

Original images remain canonical. Production deployment has not been performed.
