# site_ui v1.4 詳細設計

## S001 数式表示改善
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S001] MathJax表示をスクロール方式から自動改行方式へ変更する。
### 2. メイン関数
該当なし（CSS/MathJax設定）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. メイン変数
該当なし。
### 6. 処理フロー
- <span style="color:blue">[MOD]</span> [L101] `.math-block` の `overflow-x:auto` と `min-width:max-content` を撤去する (S001)
- <span style="color:blue">[MOD]</span> [L102] MathJax 4を読み込み `output.displayOverflow='linebreak'`、幅100%で自動改行する (S001)
- <span style="color:blue">[MOD]</span> [L103] FEM主要5ページの既存TeX式内容は変更しない (S001)
### 7. 特記事項
数式の係数・添字・式順序は不変。

## S002 告知・修正履歴導線
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S002] トップ告知と修正履歴リンク配置を更新する。
### 2. メイン関数
該当なし（HTML）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. メイン変数
該当なし。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L201] `index.html` お知らせに2026-09-16更新内容と履歴リンクを追加する (S002)
- <span style="color:blue">[MOD]</span> [L202] `footer.html` から修正履歴リンクを削除する (S002)
- <span style="color:green">[ADD]</span> [L203] `menu.html` の「お気に入りに追加」直下へ修正履歴リンクを追加する (S002)
### 7. 特記事項
リンク先は既存 `revision_history.html`。

## S003 モバイルメニュー操作・背景改善
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S003] 固定iframeメニューを縦スクロール可能にし背景を統一する。
### 2. メイン関数
<span style="color:blue">[MOD]</span> [F001] `refreshMobileNavigation`
### 3. 引数
該当なし。
### 4. 戻り値
該当なし（既存どおり値を返さない）。
### 5. メイン変数
- <span style="color:green">[ADD]</span> [V001] `scrollingAttribute`: iframe scrolling属性名。
- <span style="color:green">[ADD]</span> [V002] `scrollingValue`: `auto`。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L301] `refreshMobileNavigation()` 初期化時にmenu iframeのscrolling属性をautoへ設定する (S003)
- <span style="color:blue">[MOD]</span> [L302] モバイルiframeを `overflow-y:auto` / overscroll contain とする (S003)
- <span style="color:blue">[MOD]</span> [L303] menu文書のhtml/body/sub-wrapperを白背景かつ100%最小高に統一する (S003)
### 7. 特記事項
親bodyはメニュー開状態で固定し、スクロールはiframe内だけで行う。

## S004 PC/既存動作維持
### 1. 処理概要
[KEEP] [S004] PC左メニュー、既存href、`disp()`、`set_height()`、既存URLを維持する。
### 2. メイン関数
[KEEP] [F002] `updateMobileMenuState`
### 3. 引数
既存定義を維持。
### 4. 戻り値
既存定義を維持。
### 5. メイン変数
既存定義を維持。
### 6. 処理フロー
- [KEEP] [L401] PC幅ではスマホUIを非表示とする (S004)
- [KEEP] [L402] `disp()` / `set_height()` を変更しない (S004)
### 7. 特記事項
既存メニューhref一覧を変更しない（修正履歴の新規1件追加のみ）。

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|[ADD]|5|L201,L203,L301,V001,V002|
|[MOD]|9|S001,S002,S003,L101,L102,L103,L202,L302,L303,F001を含む（管理上10要素）|
|[KEEP]|4|S004,F002,L401,L402|
|[DEL]|0|なし|
