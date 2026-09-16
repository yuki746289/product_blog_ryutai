# v1.5 データ・API・外部連携

## EXT-MATHJAX-001 [KEEP]
数式表示ライブラリはMathJax 4系を維持する。

- 配信元: jsDelivr
- combined component: `tex-mml-chtml.js`
- TeX入力/CHTML出力を利用する。
- `output.displayOverflow = 'linebreak'`
- `output.linebreaks.width = '100%'`
- `output.displayAlign = 'left'`

## デザインサンプル
外部APIやフレームワークを追加しない。サンプル専用HTML/CSSだけで構成し、Webフォント等の外部依存を必須にしない。

その他の外部API・データ連携は変更しない。