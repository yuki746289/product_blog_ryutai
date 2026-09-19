# MPS Source Recovery and Formula Audit — 2026-09-19

## 1. Recovery result

MPS 49 missing image references were re-investigated using the archived original material.

### Archive recovery path

Direct Library raw-byte materialization was denied by the Project file boundary.
The source archive was recovered without modifying the original Library file by:

1. Copy `HP(1).7z` from Library to Google Drive.
2. Download the copied non-native 7z as a raw file through the connected Google Drive API.
3. Read/extract the 7z with the system `libarchive.so`.

Recovered archive size: **30,415,485 bytes**.

## 2. Original MPS materials found in the archive

### HTML / backup

- `HP/source/mps/mps.html`
- `HP/source/mps/mps_1.html` ... `mps_6_2.html`
- corresponding `.BAK` files

### Word source

- `HP/資料/粒子法_重み関数.doc`
- `HP/資料/粒子法_粒子の数密度.doc`
- `HP/資料/粒子法_勾配モデル.doc`
- `HP/資料/粒子法_発散モデル.doc`
- `HP/資料/粒子法_ラプラシアンモデル.doc`
- `HP/資料/粒子法_非圧縮性流れ_支配方程式.doc`
- `HP/資料/粒子法_非圧縮性流れ_計算の流れ.doc`

### Visio source

- `HP/資料/粒子法.vsd`
- `HP/HP図.vsd`
- `HP/公式.vsd`
- other VSD files were also checked.

## 3. Original GIF search

The archive was searched for the site-referenced directories/files:

- `mps_weight.files`
- `mps_num.files`
- `mps_nabra.files`
- `mps_dot.files`
- `mps_rap.files`
- `mps_fluid_eq.files`
- `mps_fluid_count.files`

The original site GIF binaries were **not present** in the 7z.

Therefore the recovered Word Equation.3 source plus Word-rendered output is used as the strongest available source substitute.
Visio is used as a secondary corroborating source when the corresponding formula exists there.

## 4. Word equation mapping

LibreOffice conversion of the Word files exported Equation.3 objects and also converted them to ODT/MathML.

| Page | Site refs | Recoverable from Word | Status |
|---|---:|---:|---|
| `mps_1.html` | 1 | 1 | recovered |
| `mps_2.html` | 1 | 1 | recovered |
| `mps_3.html` | 12 | 12 | recovered |
| `mps_4.html` | 9 | 9 | recovered |
| `mps_5.html` | 2 | 2 | recovered |
| `mps_6_1.html` | 2 | 2 | recovered |
| `mps_6_2.html` | 22 | 21 | 21 recovered / image022 HOLD |
| **Total** | **49** | **48** | **48 recovered / 1 HOLD** |

The first six pages match their Word equation occurrence counts exactly.

## 5. Visio investigation

`粒子法.vsd` opens successfully in LibreOffice Draw and contains five embedded equation objects.
It corroborates key formulas including:

- weight function
- particle number density / related density equation
- gradient model
- divergence model

`HP図.vsd` contains many OLE objects and pressure-related material. Relevant pages were inspected, including pressure-gradient-related content, but no object could be identified with sufficient confidence as `mps_6_2/image022.gif`.

Searches across the VSD files for the surrounding wording:
- 数値安定性
- 圧力の勾配モデル
- 圧力勾配
did not yield a source that can be safely mapped to image022.

## 6. image022 status

Current HTML context:

> ここで、圧力の勾配モデルは数値安定性のため、次式を使用します。

followed by:

`img/mps_fluid_count.files/image022.gif`

The corresponding Word document contains the sentence but no recoverable Equation.3 object at that position.
The Word document has 21 embedded Equation.3 objects, while the site HTML has 22 formula-image references.

No separate authoritative source for image022 was found in the archive Word/PDF/Visio material.

Therefore:

**`mps/mps_6_2.html image022.gif` = SOURCE BLOCKED / HOLD**

No formula is inferred or reconstructed for this one item.

## 7. develop reflection

The 48 recoverable formulas were converted to MathJax on `develop`.

Current formula counts:

- mps_1: 1
- mps_2: 1
- mps_3: 12
- mps_4: 9
- mps_5: 2
- mps_6_1: 2
- mps_6_2: 21

Total: **48**

Actual remaining MPS `<img>` formula references:
- only `mps/mps_6_2.html -> img/mps_fluid_count.files/image022.gif`

The original image path is retained in `data-source-image` for converted formulas as traceability metadata; those attributes are not residual image elements.

## 8. Source-preservation rule

Recovered source-visible notation is preserved even where theoretically unusual.
No silent normalization or theoretical correction is applied.

## 9. Browser QA

Targeted MPS Browser QA is run separately for the seven MPS pages on:
- desktop 1440×1000
- mobile 390×844

Acceptance:
- formula count = 48
- MathJax errors = 0
- unrendered formulas = 0
- page overflow = 0
- uncontained math overflow = 0
- only one known missing MPS image: image022

Final QA result is recorded in:
`.document/formula_reviews/MPS_FINAL_BROWSER_QA_20260919.md`
