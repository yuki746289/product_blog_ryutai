# 数式レビュー: fem/fem_6_2_6.html

更新日: 2026-09-19

## 対象

- ページ: `fem/fem_6_2_6.html`
- タイトル: 内挿関数の微分まとめ（4面体1次要素）
- 正本: `img/fem_n_tet.files/image021.png` ～ `image032.png`
- 対象数: **12式**
- MathJaxブロック数: **12**
- 新厳密 Pass 1: **12/12**
- 新厳密 Pass 2: **12/12**
- HOLD: **0**
- Browser QA: **PASS**

## 2026-09-19 新厳密監査

元画像 ↔ MathJax完成描画を12式すべてペア画像化し、直接確認した。

確認項目:

- 左辺 `∂N_i/∂x,y,z` と `∂L_i/∂x,y,z`
- `c_{ix}, c_{iy}, c_{iz}`
- 分母 `6V`
- 右辺6項の変数・節点添字
- 全項の符号
- 項順
- 括弧・等号位置
- `x/y/z` と節点番号 `1..4`

## 結果

`image021～image032` は、元画像とMathJax描画の間に新たな数式内容差・改行差を確認しなかった。

**要修正: 0/12**

## Browser / MathJax Pass 2

| Viewport | Math blocks | Rendered | MathJax error | Unrendered | Uncontained overflow | Page overflow |
|---|---:|---:|---:|---:|---:|---|
| desktop 1440x1000 | 12 | 12 | 0 | 0 | 0 | 0 |
| mobile 390x844 | 12 | 12 | 0 | 0 | 0 | 0 |

- mobileでは4ブロックが `.math-block` 内スクロールになる。
- ページ全体の横overflowはない。
- 旧数式画像要素は通常ページ上 **0**。

## 判定

**fem_6_2_6: 新厳密再監査 完了。**
