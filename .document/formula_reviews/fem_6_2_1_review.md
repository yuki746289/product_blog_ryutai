# 数式レビュー: fem/fem_6_2_1.html

更新日: 2026-09-19

## 対象

- ページ: `fem/fem_6_2_1.html`
- タイトル: 4面体要素の体積
- 正本: `img/fem_n_tet.files/image002.png` ～ `image007.png`
- 数式画像: **6式**
- 保持図: `image001.png`（4面体図）
- 新厳密 Pass 1: **6/6**
- 新厳密 Pass 2: **6/6**
- HOLD: **0**
- Browser QA: **PASS**
- 通常ページ反映: **完了**

## 新厳密監査結果

元HP画像とMathJax完成描画を6式すべてペア画像化して比較した。

- `image002`: 体積行列式と24項の展開を確認。
- `image003`: `a_{11}～a_{44}` の対応を確認。
- `image004～007`: `V_1～V_4` の行列式、節点添字、符号、x/y/z置換位置を確認。
- `x_1/x`, `y_1/y`, `z_1/z` 等の紛らわしい置換位置を重点確認。
- 元画像と異なる理論的簡略化・項順変更は行っていない。
- 数式内容の修正は不要だった。

## 補助データ修正

`.document/formula_reviews/fem_6_2_1_formulas.json` の `image_dir` が
`img/fem_vcoord.files` となっていたが、実際の正本は
`img/fem_n_tet.files` のためメタデータのみ修正した。

## Browser / MathJax Pass 2

| Viewport | Math blocks | Rendered | MathJax error | Unrendered | Uncontained overflow | Page overflow | 保持図 |
|---|---:|---:|---:|---:|---:|---|---:|
| desktop 1440x1000 | 6 | 6 | 0 | 0 | 0 | 0 | 1 |
| mobile 390x844 | 6 | 6 | 0 | 0 | 0 | 0 | 1 |

- mobileでは5式が `.math-block` 内スクロール。
- ページ全体の横overflowはない。
- `image001` は数式画像ではなく図として意図的に保持。
- QAワークフローは保持図を許容し、未変換数式画像だけを失敗扱いするよう改善済み。

## 判定

**fem_6_2_1: 新厳密再監査 完了。**
