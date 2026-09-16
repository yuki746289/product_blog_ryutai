# v1.6 データ・API・外部連携

## EXT-MATHJAX-001 [KEEP]
数式表示ライブラリはMathJax 4系を維持する。

- 配信元: jsDelivr
- combined component: `tex-mml-chtml.js`
- TeX入力/CHTML出力を利用する。
- `output.displayOverflow = 'linebreak'`
- `output.linebreaks.width = '100%'`
- `output.displayAlign = 'left'`

MathJaxを通常ページへ使用するかどうかは数式元画像完全一致監査の完了状態に従う。v1.6デザイン実装を理由としてMathJax変換を追加しない。

## EXT-DESIGN-001 [KEEP]
本体デザイン・ナビゲーションに新しい外部UIフレームワーク、CDN CSS、Webフォントを必須導入しない。既存静的HTML/CSS/JavaScriptで成立させる。

## データ/API
新規API、データベース、外部データ連携は追加しない。

## 既存外部リンク
`menu.html` 等に存在する既存外部リンクは、v1.6実装でURLを変更しない。新ナビへ複製する場合も既存hrefをそのまま使用する。
