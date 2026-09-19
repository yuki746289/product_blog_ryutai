# 数式レビュー: heat/heat_7_2.html

更新日: 2026-09-19

## 対象
- ページ: `heat/heat_7_2.html`
- 正本: `img/heat_discretization_tet.files/image001.png` ～ `image032.png`
- 数式: **32式**
- 新厳密 Pass 1: **32/32**
- 新厳密 Pass 2: **32/32**
- HOLD: **0**
- Browser QA: **PASS**

## 元画像 ↔ MathJax 直接比較
- 32式すべてを元画像とMathJax完成描画のペア画像で再確認。
- 現HTMLは source-certified JSON と **32/32一致**。
- `τ/Δτ`, `Θ`, `X/Y/Z`, `q_x^*/q_y^*/q_z^*`, 節点1～4、行列成分を重点確認。
- `image014`: Y微分行列の4行2列は元画像どおり **`N_4 ∂N_2/∂Z`**。周囲がY微分でも推測修正しない。
- 数式内容の追加修正は不要。

## Browser QA
- desktop: 32/32 render、MathJax error=0、page overflow=0。
- mobile: 32/32 render、内部スクロール12式、uncontained overflow=0、page overflow=0。

## 判定
**heat_7_2: 新厳密再監査 完了。**
