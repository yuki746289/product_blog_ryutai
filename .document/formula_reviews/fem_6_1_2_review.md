# 数式レビュー: fem/fem_6_1_2.html

更新日: 2026-09-19

## 対象
- ページ: `fem/fem_6_1_2.html`
- 正本: `img/fem_n_tri.files/image007.png`, `image008.png`
- 数式: **2式**
- 新厳密 Pass 1: **2/2**
- 新厳密 Pass 2: **2/2**
- HOLD: **0**
- Browser QA: **PASS**

## 元画像 ↔ MathJax 直接比較
- `image007`: `∂N_1/∂x`、`∂L_1/∂x`、`∂(S_1/S)/∂x`、途中展開、最終 `(-y_3+y_2)/(2S)` を確認。
- `image008`: y微分系列と最終 `(x_3-x_2)/(2S)` を確認。
- `x/y`、添字1/2/3、負号位置を重点確認。
- 元画像との差異なし。HTML修正不要。

## Browser / MathJax Pass 2
- desktop/mobileとも2/2 render。
- MathJax error=0、unrendered=0、uncontained overflow=0、page overflow=0。

## 判定
**fem_6_1_2: 新厳密再監査 完了。**
