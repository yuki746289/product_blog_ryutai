# 数式再監査進捗（Word基準 + 元画像最終照合）

開始日: 2026-09-19
更新日: 2026-09-19

## 正本・優先順位

1. **元HP画像**
2. Word数式（元画像から貼り付けたもの）
3. 現在のLaTeX
4. 旧監査記録

旧監査の Pass 1 = OK は今回の新厳密再監査では未確認扱いとする。

## 新厳密再監査ルール

- Word数式を高速な転記・比較元として使い、既存LaTeXは差分再利用する。
- 最終判定は必ず元HP画像で行う。
- 元画像 ↔ Word は 1:1 に限定しない。1:N / N:1 の分割・結合を許容する。
- 元画像 ↔ MathJax完成描画をペア画像化し、式範囲・項順・符号・添字・改行を比較する。
- `t / τ`, `i / j`, `x / y / z`, 大小文字、添字、上付き、`∂ / d`, `+ / -` は重点確認する。
- 全体類似度が高くても紛らわしい1文字差を自動合格にしない。
- 判断不能は HOLD とし、推測修正しない。

## ページ進捗

| No. | ページ | 式数 | 新Pass 1 | 新Pass 2 | Browser QA | 状態 |
|---:|---|---:|---:|---:|---|---|
| 1 | `fem/fem_7_2_2.html` | 49 | **49/49** | **49/49** | **PASS** | **DONE** |
| 2 | `fem/fem_7_2_1.html` | 20 | **20/20** | **20/20** | **PASS** | **DONE** |
| 3 | `fem/fem_7_1_2.html` | 42 | **42/42** | **42/42** | **PASS** | **DONE** |
| 4 | `fem/fem_7_1_1.html` | 20 | **20/20** | **20/20** | **PASS** | **DONE** |
| 5 | `fem/fem_6_2_6.html` | 12 | **12/12** | **12/12** | **PASS** | **DONE** |
| 6 | `fem/fem_6_2_1.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 7 | `fem/fem_6_1_5.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 8 | `fem/fem_6_1_1.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 9 | `fem/fem_6_1_2.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 10 | `fem/fem_6_1_3.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 11 | `fem/fem_6_1_4.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 12 | `fem/fem_6_2_2.html` | 3 | **3/3** | **3/3** | **PASS** | **DONE** |
| 13 | `fem/fem_6_2_3.html` | 3 | **3/3** | **3/3** | **PASS** | **DONE** |
| 14 | `fem/fem_6_2_4.html` | 3 | **3/3** | **3/3** | **PASS** | **DONE** |
| 15 | `fem/fem_6_2_5.html` | 3 | **3/3** | **3/3** | **PASS** | **DONE** |
| 16 | `fem/fem_2_1.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 17 | `fem/fem_2_2.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 18 | `fem/fem_2_3.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 19 | `fem/fem_5.html` | 7 | **7/7** | **7/7** | **PASS** | **DONE** |
| 20 | `fem/fem_10.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 21 | `fem/fem_11_1.html` | 11 | **11/11** | **11/11** | **PASS** | **DONE** |
| 22 | `fem/fem_8_2_1.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 23 | `fem/fem_3.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 24 | `fem/fem_4.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 25 | `fem/fem_8.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 26 | `fem/fem_9.html` | 3 | **3/3** | **3/3** | **PASS** | **DONE** |
| 27 | `heat/heat_6.html` | 13 | **13/13** | **13/13** | **PASS** | **DONE** |
| 28 | `heat/heat_3.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 29 | `heat/heat_4_1.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 30 | `heat/heat_4_2.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 31 | `heat/heat_4_3.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 32 | `heat/heat_5_1.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 33 | `heat/heat_5_2.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 34 | `heat/heat_5_3.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 35 | `heat/heat_5_4.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 36 | `heat/heat_7_1.html` | 33 | **33/33** | **33/33** | **PASS** | **DONE** |
| 37 | `heat/heat_7_2.html` | 32 | **32/32** | **32/32** | **PASS** | **DONE** |
| 38 | `hydronamics/hydronamics_5.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 39 | `hydronamics/hydronamics_6_1.html` | 7 | **7/7** | **7/7** | **PASS** | **DONE** |
| 40 | `hydronamics/hydronamics_6_2.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 41 | `hydronamics/hydronamics_6_3.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 42 | `hydronamics/hydronamics_6_4.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 43 | `hydronamics/hydronamics_7.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 44 | `hydronamics/hydronamics_9_1.html` | 4 | **4/4** | **4/4** | **PASS** | **DONE** |
| 45 | `hydronamics/hydronamics_9_2.html` | 9 | **9/9** | **9/9** | **PASS** | **DONE** |
| 46 | `hydronamics/hydronamics_9_3.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 47 | `hydronamics/hydronamics_9_4.html` | 8 | **8/8** | **8/8** | **PASS** | **DONE** |
| 48 | `hydronamics/hydronamics_9_5.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 49 | `hydronamics/hydronamics_9_6.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 50 | `hydronamics/hydronamics_10_1.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 51 | `hydronamics/hydronamics_11.html` | 4 | **4/4** | **4/4** | **PASS** | **DONE** |
| 52 | `hydronamics/hydronamics_11_1.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 53 | `hydronamics/hydronamics_11_2.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 54 | `hydronamics/hydronamics_11_3.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 55 | `hydronamics/hydronamics_11_4.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 56 | `hydronamics/hydronamics_11_5.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 57 | `hydronamics/hydronamics_11_6.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 58 | `hydronamics/hydronamics_12.html` | 4 | **4/4** | **4/4** | **PASS** | **DONE** |
| 59 | `hydronamics/hydronamics_12_1.html` | 10 | **10/10** | **10/10** | **PASS** | **DONE** |
| 60 | `hydronamics/hydronamics_12_2.html` | 8 | **8/8** | **8/8** | **PASS** | **DONE** |
| 61 | `hydronamics/hydronamics_14.html` | 12 | **12/12** | **12/12** | **PASS** | **DONE** |
| 62 | `hydronamics/hydronamics_4.html` | 9 | **9/9** | **9/9** | **PASS** | **DONE** |
| 63 | `hydronamics/hydronamics_8.html` | 12 | **12/12** | **12/12** | **PASS** | **DONE** |
| 64 | `physics/physics_2.html` | 7 | **7/7** | **7/7** | **PASS** | **DONE** |
| 65 | `physics/physics_3.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 66 | `physics/physics_4.html` | 6 | **6/6** | **6/6** | **PASS** | **DONE** |
| 67 | `physics/physics_5.html` | 4 | **4/4** | **4/4** | **PASS** | **DONE** |
| 68 | `physics/physics_6_1.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 69 | `physics/physics_6_2_1.html` | 4 | **4/4** | **4/4** | **PASS** | **DONE** |
| 70 | `physics/physics_6_2_2.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 71 | `physics/physics_6_2_3.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 72 | `physics/physics_6_2_4.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 73 | `physics/physics_6_2_5.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 74 | `physics/physics_6_2_6.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 75 | `physics/physics_6_2_7.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 76 | `physics/physics_6_3_1.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 77 | `physics/physics_6_3_2.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 78 | `physics/physics_6_3_3.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 79 | `physics/physics_7.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 80 | `appendix/appendix_1.html` | 14 | **14/14** | **14/14** | **PASS** | **DONE** |
| 81 | `appendix/appendix_2.html` | 11 | **11/11** | **11/11** | **PASS** | **DONE** |
| 82 | `appendix/appendix_3_1.html` | 8 | **8/8** | **8/8** | **PASS** | **DONE** |
| 83 | `appendix/appendix_3_2.html` | 8 | **8/8** | **8/8** | **PASS** | **DONE** |
| 84 | `column/column_2.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 85 | `mesh/mesh_1.html` | 5 | **5/5** | **5/5** | **PASS** | **DONE** |
| 86 | `mesh/mesh_2.html` | 9 | **9/9** | **9/9** | **PASS** | **DONE** |
| 87 | `mesh/mesh_3_1.html` | 9 | **9/9** | **9/9** | **PASS** | **DONE** |
| 88 | `mesh/mesh_5.html` | 7 | **7/7** | **7/7** | **PASS** | **DONE** |
| 89 | `mps/mps_1.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 90 | `mps/mps_2.html` | 1 | **1/1** | **1/1** | **PASS** | **DONE** |
| 91 | `mps/mps_3.html` | 12 | **12/12** | **12/12** | **PASS** | **DONE** |
| 92 | `mps/mps_4.html` | 9 | **9/9** | **9/9** | **PASS** | **DONE** |
| 93 | `mps/mps_5.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 94 | `mps/mps_6_1.html` | 2 | **2/2** | **2/2** | **PASS** | **DONE** |
| 95 | `mps/mps_6_2.html` | 22 | **21 source-exact + 1 inferred** | **22/22** | **PASS** | **DONE*** |

## fem_7_2_2 完了結果

- 元画像: `image001～image049`
- MathJaxブロック: 51（image031 / image037 の再掲を含む）
- HOLD: 0
- MathJax error: 0
- unrendered: 0
- uncontained overflow: 0
- page-wide overflow: 0
- 元画像 ↔ MathJax比較ペア: 49/49生成・確認
- 通常HTML反映: 完了
- レビュー正本: `.document/formula_reviews/fem_7_2_2_review.md`

### 再監査で修正した主な差異

- image005: Vx式の改行、不要な行末記号。
- image006 / 007: 式の境界を元画像どおり分離。時間記号は **τ**。
- image010: 表面応力積分・重力積分の行構成。
- image011 / 012: 表面張力項を **単一負号 `-2K^*/We`** に確定。
- image011～015: 表面張力項と重力項の改行。
- image016: 元画像注記「蓄積量」をHTMLへ復元。
- image043 / 044: 項ごとの改行を元画像へ合わせた。
- image047～049: 圧力項を元画像どおり粘性項と同じ行へ戻した。
- `P_{z,*}`, `X_i`, `i/j`, `τ`, 最終式交差項を重点確認。

## fem_7_2_1 完了結果

- 元画像: `image001～image020`
- 新Pass 1: **20/20**
- 新Pass 2: **20/20**
- HOLD: 0
- Browser QA: **PASS**
- 通常HTML反映: 完了
- レビュー正本: `.document/formula_reviews/fem_7_2_1_review.md`

## fem_7_1_2 完了結果

- 元画像: `image001～image042`
- 新Pass 1: **42/42**
- 新Pass 2: **42/42**
- HOLD: 0
- Browser QA: **PASS**
- 通常HTML反映: 完了
- レビュー正本: `.document/formula_reviews/fem_7_1_2_review.md`

## fem_7_1_1 完了結果

- 対象元画像: 20式（image019は対象外）
- 新Pass 1: **20/20**
- 新Pass 2: **20/20**
- HOLD: 0
- Browser QA: **PASS**
- 通常HTML反映: 完了
- レビュー正本: `.document/formula_reviews/fem_7_1_1_review.md`

## fem_6_2_6 完了結果

- 対象元画像: image021～image032 = **12式**
- 新Pass 1: **12/12**
- 新Pass 2: **12/12**
- 要修正: **0**
- HOLD: 0
- Browser QA: **PASS**
- レビュー正本: `.document/formula_reviews/fem_6_2_6_review.md`

## fem_6_2_1 完了結果

- 数式元画像: image002～image007 = **6式**
- 保持図: image001
- 新Pass 1: **6/6**
- 新Pass 2: **6/6**
- 要修正: **0**
- HOLD: 0
- Browser QA: **PASS**
- 補助JSONの source image directory metadata を修正
- レビュー正本: `.document/formula_reviews/fem_6_2_1_review.md`

## fem_6_1_5 完了結果

- 元画像: image013～image018 = **6式**
- 新Pass 1: **6/6**
- 新Pass 2: **6/6**
- 要修正: **0**
- HOLD: 0
- Browser QA: **PASS**
- レビュー正本: `.document/formula_reviews/fem_6_1_5_review.md`

## fem_6_1_1 完了結果
- 数式: image002～image006 = **5式**
- 保持図: image001
- 新Pass 1/2: **5/5**
- Browser QA: **PASS**
- HOLD: 0

## fem_6_1_2 完了結果
- 数式: image007～image008 = **2式**
- 新Pass 1/2: **2/2**
- Browser QA: **PASS**
- HOLD: 0

## fem_6_1_3 ～ fem_6_2_5 完了結果
- `fem_6_1_3`: 2/2、source anomaly（y微分途中の `∂/∂x`）を原文どおり保持。
- `fem_6_1_4`: 2/2、同様の source anomaly を保持。
- `fem_6_2_2～6_2_5`: 各3/3、4面体形状関数 N1～N4 の x/y/z 微分を元画像と直接照合。
- 全6ページ Browser QA: **PASS**
- HOLD: 0

## FEM追加6ページ完了結果
- fem_2_1: 6/6
- fem_2_2: 5/5
- fem_2_3: 5/5
- fem_5: 7/7（rich blockを含む）
- fem_10: 6/6
- fem_11_1: 11/11
- 全ページ元画像↔MathJax直接比較済み
- HOLD: 0

## fem_8_2_1 完了結果
- 数式: image002～image006 = **5式**
- 保持図: image001 / image007
- 新Pass 1/2: **5/5**
- image005 の `n^*` 欠落を修正後に再QA
- Browser QA: **PASS**
- HOLD: 0

## FEM追加4ページ完了結果
- fem_3: 2/2
- fem_4: 5/5（日本語説明＋MathJax rich blockを含む）
- fem_8: 2/2
- fem_9: 3/3、図2枚は保持
- 全ページ Browser QA: **PASS**
- HOLD: 0

## FEMカテゴリ最終QA

- 数式新厳密再監査: **235式 / 26ページ**
- 非数式ページ最終QA: **17/17 PASS**
- ローカル図画像: **21枚 / broken 0**
- PC/mobile page-wide overflow: **0**
- FEMカテゴリ: **COMPLETE**
- 最終レポート: `.document/formula_reviews/FEM_FINAL_QA_20260919.md`

## heat_6 完了結果
- 元画像: image001～image013 = **13式**
- display 11式 / inline 2式
- 新Pass 1/2: **13/13**
- Browser QA: **PASS**
- HOLD: 0

## Heat小規模8ページ完了結果
- heat_3: 1/1
- heat_4_1: 1/1
- heat_4_2: 1/1
- heat_4_3: 2/2
- heat_5_1: 1/1
- heat_5_2: 2/2
- heat_5_3: 2/2
- heat_5_4: 6/6
- 全対象で元画像↔MathJax直接比較済み
- Browser QA: 全ページ **PASS**
- HOLD: 0

## heat_7_1 / heat_7_2 完了結果
- heat_7_1: **33/33**
  - image021 の source-visible `4/4! V` を保持
- heat_7_2: **32/32**
  - image014 の source-visible `N_4 ∂N_2/∂Z` を保持
- 両ページとも元画像↔MathJax直接比較済み
- Browser QA: **PASS**
- HOLD: 0

## Heatカテゴリ最終QA

- 数式新厳密再監査: **94式 / 11ページ**
- 非数式ページ最終QA: **7/7 PASS**
- 保持図: **8/8**
- broken image: 0
- PC/mobile page-wide overflow: 0
- Heatカテゴリ: **COMPLETE**
- 最終レポート: `.document/formula_reviews/HEAT_FINAL_QA_20260919_STRICT.md`

## Hydronamics小規模6ページ完了結果
- hydronamics_5: 1/1
- hydronamics_6_1: 7/7
- hydronamics_6_2: 6/6
- hydronamics_6_3: 6/6
- hydronamics_6_4: 6/6
- hydronamics_7: 1/1
- 全対象で元画像↔MathJax直接比較済み
- Browser QA: 全ページ **PASS**
- HOLD: 0

## Hydronamics 9系～11 完了結果
- hydronamics_9_1: 4/4
- hydronamics_9_2: 9/9
- hydronamics_9_3: 2/2
- hydronamics_9_4: 8/8
- hydronamics_9_5: 5/5
- hydronamics_9_6: 5/5
- hydronamics_10_1: 5/5
- hydronamics_11: 4/4
- 全対象で元画像↔MathJax直接比較済み
- Browser QA: 全ページ **PASS**
- HOLD: 0

## Hydronamics 11詳細～14 完了結果
- hydronamics_11_1～11_5: 各1/1
- hydronamics_11_6: 2/2
- hydronamics_12: 4/4
- hydronamics_12_1: 10/10
- hydronamics_12_2: 8/8
- hydronamics_14: 12/12
- inline式を含むページは selector 拡張後に再QA
- 全対象で元画像↔MathJax直接比較済み
- Browser QA: 全ページ **PASS**
- HOLD: 0

## Hydronamicsカテゴリ最終QA

- 数式新厳密再監査: **131式 / 26ページ**
- 非数式ページ最終QA: **10/10 PASS**
- 数式ページ内保持図: **17枚**
- 非数式ページ内ローカル図: **4枚**
- broken image: 0
- PC/mobile page-wide overflow: 0
- Hydronamicsカテゴリ: **COMPLETE**
- 最終レポート: `.document/formula_reviews/HYDRONAMICS_FINAL_QA_20260919_STRICT.md`

## Hydronamics 11_1～14 完了結果
- 11_1～11_6: **7/7**
- 12: **4/4**
- 12_1: **10/10**
- 12_2: **8/8**
- 14: **12/12**
- 全対象で元画像↔MathJax直接比較済み
- Browser QA: 全ページ **PASS**
- HOLD: 0

## Physics数式ページ完了結果
- 新厳密再監査: **49式 / 16ページ**
- 元画像↔MathJax直接比較: **49/49**
- Browser QA: 全ページ **PASS**
- HOLD: 0
- レビュー正本: `.document/formula_reviews/PHYSICS_STRICT_REAUDIT_20260919.md`

## Physicsカテゴリ最終QA

- 数式新厳密再監査: **49式 / 16ページ**
- 非数式ページ最終QA: **6/6 PASS**
- broken image: 0
- PC/mobile page-wide overflow: 0
- Physicsカテゴリ: **COMPLETE**
- 最終レポート: `.document/formula_reviews/PHYSICS_FINAL_QA_20260919_STRICT.md`

## Appendix / Column / Mesh 数式ページ完了結果
- 新厳密再監査: **76式 / 9ページ**
- 元画像↔MathJax直接比較: **76/76**
- 現HTML↔source-certified JSON: **76/76一致**
- Browser QA: 全ページ **PASS**
- HOLD: 0
- レビュー正本: `.document/formula_reviews/APPENDIX_COLUMN_MESH_STRICT_REAUDIT_20260919.md`

## Appendix / Column / Mesh 最終QA

- 数式新厳密再監査: **76式 / 9ページ**
- 非数式ページ最終QA: **11/11 PASS**
- broken image: 0
- PC/mobile page-wide overflow: 0
- Appendix / Column / Mesh: **COMPLETE**
- 最終レポート: `.document/formula_reviews/APPENDIX_COLUMN_MESH_FINAL_QA_20260919_STRICT.md`

## Appendix / Column / Mesh カテゴリ最終QA

- Appendix: **COMPLETE**
- Column: **COMPLETE**
- Mesh: **COMPLETE**
- 非数式ページQA: **11/11 PASS**
- Broken image: 0
- PC/mobile page-wide overflow: 0

## MPSカテゴリ最終QA

- MathJax: **49式 / 7ページ**
- source-exact / recovered: **48式**
- user-approved inferred reconstruction: **1式**
- inferred対象: `mps/mps_6_2.html -> former image022.gif`
- residual formula images: **0**
- MathJax error: 0
- unrendered: 0
- page-wide overflow: 0
- Browser QA: **PASS**
- HOLD: 0
- 詳細: `.document/formula_reviews/MPS_FINAL_BROWSER_QA_20260919.md`
- 注: inferred 1式は source-exact の633式には含めず、operational total 634式にのみ含める。

## Countingカテゴリ最終QA

- 数式画像: **0**
- 保持フローチャート: **2/2**
- 通常ページ: **3/3**
- desktop/mobile: **PASS**
- broken image: 0
- page-wide overflow: 0
- Countingカテゴリ: **COMPLETE**
- 詳細: `.document/formula_reviews/COUNTING_FINAL_QA_20260919_STRICT.md`

## Mesh数式ページ完了結果
- 新厳密再監査: **30式 / 4ページ**
- Browser QA: 全ページ **PASS**
- HOLD: 0
- レポート: `.document/formula_reviews/MESH_STRICT_REAUDIT_20260919.md`

## Column / Appendix数式ページ完了結果
- 新厳密再監査: **46式 / 5ページ**
- Browser QA: 全ページ **PASS**
- HOLD: 0
- レポート: `.document/formula_reviews/COLUMN_APPENDIX_STRICT_REAUDIT_20260919.md`

## 累計

- source-exact / source-recovered 新厳密再監査完了: **633式**
- 数式ページ完了: **95ページ**
- inferred reconstruction: **1式**
- operational MathJax total: **634式**
- Counting: 数式0、フローチャート2枚保持
- 旧564式監査結果とは分離して管理する。

## 次回再開位置

**全対象カテゴリの新厳密再監査・最終表示QA完了。**
最終サマリ: `.document/formula_reviews/FORMULA_STRICT_REAUDIT_FINAL_SUMMARY_20260919.md`
