# 数式レビュー: fem/fem_6_1_5.html

更新日: 2026-09-19

## 対象

- ページ: `fem/fem_6_1_5.html`
- 正本: `img/fem_n_tri.files/image013.png` ～ `image018.png`
- 対象数: **6式**
- 新厳密 Pass 1: **6/6**
- 新厳密 Pass 2: **6/6**
- HOLD: **0**
- Browser QA: **PASS**
- 通常ページ反映: **完了**

## 元画像 ↔ MathJax 直接比較

6式すべてについて元HP画像とMathJax完成描画をペア画像化して目視確認した。

- `image013`: `c_{1x}`, `∂N_1/∂x`, `∂L_1/∂x`, `(-y_3+y_2)/(2S)`
- `image014`: `c_{1y}`, `(x_3-x_2)/(2S)`
- `image015`: `c_{2x}`, `(y_3-y_1)/(2S)`
- `image016`: `c_{2y}`, `(-x_3+x_1)/(2S)`
- `image017`: `c_{3x}`, `(-y_2+y_1)/(2S)`
- `image018`: `c_{3y}`, `(x_2-x_1)/(2S)`

添字 `1/2/3`、`x/y`、負号位置を重点確認し、差異なし。

## Browser / MathJax Pass 2

| Viewport | Math blocks | Rendered | MathJax error | Unrendered | Uncontained overflow | Page overflow |
|---|---:|---:|---:|---:|---:|---|
| desktop 1440x1000 | 6 | 6 | 0 | 0 | 0 | 0 |
| mobile 390x844 | 6 | 6 | 0 | 0 | 0 | 0 |

- mobile内部スクロール: 0
- 未変換数式画像: 0

## 判定

**fem_6_1_5: 新厳密再監査 完了。**
