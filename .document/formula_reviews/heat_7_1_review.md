# 数式レビュー: heat/heat_7_1.html

更新日: 2026-09-19

## 対象
- ページ: `heat/heat_7_1.html`
- 正本: `img/heat_discretization_tri.files/image001.png` ～ `image033.png`
- 数式: **33式**
- 新厳密 Pass 1: **33/33**
- 新厳密 Pass 2: **33/33**
- HOLD: **0**
- Browser QA: **PASS**

## 元画像 ↔ MathJax 直接比較
- 33式すべてを元画像とMathJax完成描画のペア画像で再確認。
- 現HTMLは source-certified JSON と **33/33一致**。
- `τ/Δτ`, `Θ`, `q_x^*/q_y^*`, `X/Y`, `i/j`, `A/V`, `Nu`, `Pe` を重点確認。
- `image019`: 元画像どおり `1/(4A^2)` の後に不要な単独Aを置かない。
- `image021`: `i=j` 行の **`4/4! V`** は原画像の表記をそのまま保持。理論的にAへ修正しない。
- 数式内容の追加修正は不要。

## Browser QA
- desktop: 33/33 render、MathJax error=0、page overflow=0。
- mobile: 33/33 render、内部スクロール7式、uncontained overflow=0、page overflow=0。

## 判定
**heat_7_1: 新厳密再監査 完了。**
