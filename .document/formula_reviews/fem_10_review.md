# 数式レビュー: fem/fem_10.html

更新日: 2026-09-19

## 対象
- ページ: `fem/fem_10.html`
- 正本: `img/fem_d_matrix.files/image001.png ～ image004.png / image006.png / image007.png`
- 数式: **6式**
- 新厳密 Pass 1: **6/6**
- 新厳密 Pass 2: **6/6**
- HOLD: **0**
- Browser QA: **PASS**

## 元画像 ↔ MathJax 直接比較
離散化行列式。τ/Δτ、x/y/z成分、節点自由度、最終大型行列の添字配置を直接比較。QA artifact manifestはPASS。旧runのfailureはレポートpush競合によるもの。保持図 image005。
- 元画像とMathJax完成描画のペア画像を全対象で確認。
- 内容、符号、添字、項順について修正必要な差異なし。

## Browser QA
- desktop/mobileとも全対象render。
- MathJax error=0、unrendered=0、uncontained overflow=0、page overflow=0。

## 判定
**fem_10: 新厳密再監査 完了。**
