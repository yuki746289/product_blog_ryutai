# 数式レビュー: fem/fem_8_2_1.html

更新日: 2026-09-19

## 対象
- ページ: `fem/fem_8_2_1.html`
- 正本: `img/fem_bd_2.files/image002.png` ～ `image006.png`
- 数式: **5式**
- 保持図: `image001.png`, `image007.png`
- 新厳密 Pass 1: **5/5**
- 新厳密 Pass 2: **5/5**
- HOLD: **0**
- Browser QA: **PASS**

## 再監査結果
- source image directory の補助JSONが旧名称だったため `img/fem_bd_2.files` へ修正。
- `image002`: `\vec n^*\cdot\vec\sigma^*` から各成分への展開を確認。
- `image003/004`: Laplace圧力式を確認。
- `image005`: **左辺の法線ベクトルの上付き `*` が既存LaTeXで欠落**していたため、元画像どおり `[\vec n^*\cdot\vec\sigma^*]` に修正。
- `image006`: `P_{bd}^*`, `We`, `Oh^2` までの展開を確認。
- 修正後に元画像↔MathJaxを再生成し、5/5一致を確認。

## Browser QA
- desktop/mobileとも5/5 render。
- MathJax error=0、unrendered=0、uncontained overflow=0、page overflow=0。
- 保持図2枚は意図した残置。

## 判定
**fem_8_2_1: 新厳密再監査 完了。**
