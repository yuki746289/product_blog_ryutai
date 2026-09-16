# site_ui v1.4 詳細設計

## 実装関数対応表

|ID|区分|対象ファイル|対象関数/対象|変更内容|
|---|---|---|---|---|
|F001|[KEEP]|`menu.html`|`Init()`|変更なし。|
|F002|<span style="color:blue">[MOD]</span>|`menu.html`|`refreshMobileNavigation()`|menu iframe の `scrolling` を `auto` に設定する。|
|F003|[KEEP]|`menu.html`|`updateMobileMenuState()`|変更なし。|
|F004|[KEEP]|`menu.html`|`disp()`|変更なし。|
|F005|[KEEP]|`menu.html`|`set_height()`|変更なし。|
|STATIC001|<span style="color:blue">[MOD]</span>|`css/math.css` / FEM主要5ページ|MathJax表示|横スクロールを廃止しMathJax 4自動改行へ変更。|
|STATIC002|<span style="color:blue">[MOD]</span>|`index.html` / `menu.html` / `footer.html`|告知・導線|更新告知追加、修正履歴リンク移動。|
|STYLE001|<span style="color:blue">[MOD]</span>|`css/responsive.css` / `menu.html`|モバイルメニュー|iframe内縦スクロールと背景統一。|

## S001 数式表示改善
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S001] MathJax表示をスクロール方式からコンテナ幅内の自動改行方式へ変更する。
### 2. メイン関数
該当なし（CSS/MathJax設定）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- <span style="color:blue">[MOD]</span> [L101] `.math-block` の `overflow-x:auto` と `min-width:max-content` を撤去し、横スクロールを発生させない (S001)
- <span style="color:blue">[MOD]</span> [L102] FEM主要5ページをMathJax 4へ更新し、`output.displayOverflow='linebreak'`、`linebreaks.width='100%'` を設定する (S001)
- [KEEP] [L103] FEM主要5ページの既存TeX式本文・係数・添字・式順序は変更しない (S001)
### 7. 特記事項
MathJax 4公式仕様のdisplayOverflow=linebreakを使用する。横スクロールや切り捨てではなく自動改行を優先する。

## S002 告知・修正履歴導線
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S002] トップページ告知と修正履歴リンク配置を更新する。
### 2. メイン関数
該当なし（HTML）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L201] `index.html` の「お知らせ等」に2026-09-16のレスポンシブ対応・数式修正/MathJax化と `revision_history.html` へのリンクを追加する (S002)
- <span style="color:blue">[MOD]</span> [L202] `footer.html` から修正履歴リンクを削除し、著作権表示のみへ戻す (S002)
- <span style="color:green">[ADD]</span> [L203] `menu.html` の「お気に入りに追加」直下へ `revision_history.html` の修正履歴リンクを追加する (S002)
### 7. 特記事項
既存URLは変更しない。修正履歴リンクの新規1件追加以外のメニューhrefは維持する。

## S003 モバイルメニュー操作・背景改善
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S003] 固定iframeメニューをマウスホイール/タッチで縦スクロール可能にし、背景色と高さを統一する。
### 2. メイン関数
- <span style="color:blue">[MOD]</span> [F002] `refreshMobileNavigation()`
### 3. 引数
該当なし。
### 4. 戻り値
- [KEEP] [O002] `returnValue`: undefined。既存どおり値を返さない。
### 5. 外部変数
- [KEEP] [V001] `parent`: 親ウィンドウ。
- [KEEP] [V002] `document`: menu.html自身のDOM。
- <span style="color:green">[ADD]</span> [V003] `scrollingAttribute`: iframe属性名 `scrolling`。
- <span style="color:green">[ADD]</span> [V004] `scrollingValue`: 属性値 `auto`。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L301] `refreshMobileNavigation()` 初期化時に `menuIframe.setAttribute(scrollingAttribute, scrollingValue)` を実行する (S003)
- <span style="color:blue">[MOD]</span> [L302] モバイルの `iframe#menu` を縦スクロール可能とし、`overscroll-behavior:contain` とタッチ慣性スクロールを設定する (S003)
- <span style="color:blue">[MOD]</span> [L303] `menu.html` 内の `html/body/#sub-wrapper` を白背景・幅100%・最小高100%に統一し、背景画像による色ずれをスマホ時に無効化する (S003)
### 7. 特記事項
親bodyはメニュー開状態で固定し、ドロワー内だけをスクロールさせる。PC表示には適用しない。

## S004 PC・既存ナビゲーション維持
### 1. 処理概要
[KEEP] [S004] PC左メニュー、既存開閉処理、カテゴリ表示、高さ調整、既存URLを維持する。
### 2. メイン関数
- [KEEP] [F001] `Init()`
- [KEEP] [F003] `updateMobileMenuState()`
- [KEEP] [F004] `disp()`
- [KEEP] [F005] `set_height()`
### 3. 引数
- [KEEP] [I001] `parentDocument`
- [KEEP] [I002] `menuButton`
- [KEEP] [I003] `isOpen`
### 4. 戻り値
- [KEEP] [O001] `Init()` returnValue: undefined
- [KEEP] [O003] `updateMobileMenuState()` returnValue: undefined
- [KEEP] [O004] `disp()` returnValue: undefined
- [KEEP] [O005] `set_height()` returnValue: undefined
### 5. 外部変数
- [KEEP] [V001] `parent`
- [KEEP] [V002] `document`
### 6. 処理フロー
- [KEEP] [L401] 768px以上ではスマホ用ボタン/オーバーレイを非表示とする (S004)
- [KEEP] [L402] `updateMobileMenuState()` のbodyクラス・ARIA同期を変更しない (S004)
- [KEEP] [L403] `disp()` のカテゴリ表示ロジックを変更しない (S004)
- [KEEP] [L404] `set_height()` のPC用iframe高さ調整ロジックを変更しない (S004)
### 7. 特記事項
既存ナビゲーション機能は変更対象外。スマホ改善に必要なF002とCSS/HTMLのみ変更する。

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|[ADD]|5|L201,L203,V003,V004,L301|
|[MOD]|9|S001,L101,L102,S002,L202,S003,F002,L302,L303|
|[KEEP]|20|L103,S004,V001,V002,O002,F001,F003,F004,F005,I001-I003,O001,O003-O005,L401-L404|
|[DEL]|0|なし|
