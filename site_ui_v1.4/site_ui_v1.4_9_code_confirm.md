# site_ui v1.4 コード確認

確認日: 2026-09-16
対象ブランチ: `develop`

## 1. 対象
- `css/math.css`
- `css/responsive.css`
- `menu.html`
- `index.html`
- `footer.html`
- `revision_history.html`
- `fem/fem_6_2_6.html`
- `fem/fem_7_1_1.html`
- `fem/fem_7_1_2.html`
- `fem/fem_7_2_1.html`
- `fem/fem_7_2_2.html`
- `site_ui_v1.4/site_ui_v1.4_7_detail.json`

## 2. 実装確認
- [x] [L101] `.math-block` の横スクロール指定を廃止。
- [x] [L102] FEM主要5ページをMathJax 4へ更新し、`displayOverflow: 'linebreak'` と幅100%の自動改行を設定。
- [x] [L103] 既存TeX式の数式内容は変更していない。
- [x] [L201] トップページ「お知らせ等」に2026-09-16の更新内容と修正履歴リンクを追加。
- [x] [L202] footerから修正履歴リンクを削除。
- [x] [L203] menuの「お気に入りに追加」直下へ修正履歴リンクを追加。
- [x] [L301] `refreshMobileNavigation()` でmenu iframeの`scrolling`を`auto`へ変更。
- [x] [L302] モバイルmenu iframeを縦スクロール可能に変更。
- [x] [L303] メニュー・スマホ本文の旧背景画像を無効化し、白背景へ統一。
- [x] モバイル用ヘッダー・ヒーロー・float指定が旧PC用CSSに上書きされないよう補正。
- [x] `revision_history.html` にR-UI-001〜003を追加。

## 3. 既存動作保護
- [x] `Init()` は変更なし。
- [x] `updateMobileMenuState()` は変更なし。
- [x] `disp()` は変更なし。
- [x] `set_height()` は変更なし。
- [x] PC幅768px以上の左メニュー構成を維持。
- [x] 既存メニューhrefは維持し、修正履歴リンク1件のみ追加。
- [x] 数式の係数・添字・式順序を本v1.4で変更していない。
- [x] 本番FTPへの接続・更新なし。

## 4. 自動・ブラウザ検証

### 実装検証run
GitHub Actions run `35067399307`: **SUCCESS**

確認内容:
- MathJax 4読込と自動改行設定
- 390px幅でFEM主要5ページの数式ブロックはみ出し0件
- 390px幅でページ全体の横スクロールなし
- menu iframe `scrolling=auto`
- マウスホイール相当の実操作でiframe内scrollYが増加
- menu背景色が白
- 修正履歴リンク位置
- トップページのお知らせ表示
- PC/スマホスクリーンショット取得

主要5ページの390px検証はすべて `bad=[]`、`docScrollWidth=375`、`innerWidth=390` で合格。

### 最終視覚検証run
GitHub Actions run `35068283541`: **SUCCESS**

追加確認:
- 日本語フォントを導入した状態でスクリーンショットを再取得。
- `#wrapper` のモバイル背景画像が `none` であることをDOMで確認。
- menu `#sub-wrapper` の背景画像が `none` であることを確認。
- ヘッダー・ヒーローのモバイルCSSを目視確認。
- ハンバーガーメニュー開状態・スクロール後を目視確認。

最終スクリーンショットartifact: `site-ui-v1-4-final-evidence-rerun` / artifact ID `10435465903`。

## 5. 目視確認結果
- PC: 既存の920px系レイアウトと左メニューを維持。
- スマホ: 背景の境界ずれなし。
- スマホ: ヘッダー文字はハンバーガーボタンと干渉せず表示。
- スマホ: ヒーロー見出しはモバイル用サイズで表示。
- スマホ: 数式は横スクロールバーなしで画面内に改行表示。
- スマホ: メニューは白背景で、縦スクロールバーおよびホイール操作を確認。

## 6. 判定

**総合判定: 合格**

v1.4詳細設計に対する実装、既存動作保護、自動検証、実ブラウザ検証、スクリーンショット目視確認を完了した。