# 数式レビュー: hydronamics/hydronamics_8.html

更新日: 2026-09-19

## 対象
- ページ: `hydronamics/hydronamics_8.html`
- 正本ディレクトリ: `img/hydronamics_e_momentum.files`
- 数式: **12式**
- 新厳密 Pass 1: **12/12**
- 新厳密 Pass 2: **12/12**
- HOLD: **0**
- Browser QA: **PASS**

## 元画像 ↔ MathJax 直接比較
- 運動量収支式。ρ, vx/vy/vz, τ成分, p, g, σij, δij、ベクトル式まで直接確認。image011はinline式のためselector拡張で監査。
- 現HTMLとsource-certified JSONは全対象一致。
- 元画像とMathJax完成描画のペア画像を全式確認。
- 数式内容・符号・添字・評価位置・改行に修正必要な差異なし。

## Browser QA
- desktop/mobileとも全対象render。
- MathJax error=0、unrendered=0、uncontained overflow=0、page overflow=0。

## 判定
**hydronamics_8: 新厳密再監査 完了。**
