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

## 累計

- 新厳密再監査完了: **356式**
- 完了ページ: **43**
- 旧564式監査結果とは分離して管理する。

## 次回再開位置

**Hydronamicsカテゴリの残りページを継続する。**
