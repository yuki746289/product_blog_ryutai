# site_navigation v1.6 基本設計書

## 仕様継承
|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|MOD|footer iframeから新共通ナビ初期化を起動|v1.5 `footer.html`|
|S002|ADD|PC上部8カテゴリ＋メガメニュー|v1.6 UI-NAV-005|
|S003|ADD|スマホ右ドロワー＋多層アコーディオン|v1.6 UI-NAV-005|
|S004|ADD|補助リンクを親ページへ生成|v1.6 UI-HISTORY-001|
|S005|ADD|D Monochrome共通本文スタイル|v1.6 UI-DESIGN-002|
|S006|KEEP|初期化失敗時は既存本文・menu情報を維持|v1.5 ERR-NAV-001|

## 1. 処理概要
`footer.html` を全ページ共通の新ナビ起動入口とし、親ページに存在する `#menu` iframeの `menu.html` DOMを読み取り専用データとして利用する。親ページのHTML本文や数式を直接書換えず、親ページへ新ナビDOMと新スタイルシートを追加する。

## 2. 処理一覧

### [S001][MOD] 共通ナビ初期化
- `footer.html` に `js/site_navigation_v1_6.js` を追加する。
- 既存footer高さ調整は維持する。
- footer `Init()` から `refreshSiteNavigationV16()` を呼ぶ。
- 親ページの `#menu` iframeが読込済みなら即時初期化する。
- menu iframe未読込の場合は `load` イベント後に再初期化する。
- 新JSが読めない場合はfooter既存処理だけを行う。

### [S002][ADD] PCメガメニュー生成
- menu iframe内の既存submenu `id_2, id_3, id_4, id_5, id_6, id_9, id_10` を読み取る。
- その他カテゴリはAppendix、コラム、ライブラリ、書籍、PDF等をまとめる。
- anchorテキスト先頭の全角空白数から階層深度を判定する。
- カテゴリ内の最小深度を0として正規化し、0階層リンクと後続下位リンクをブロック化する。
- 最大4列のメガパネルへ順序を維持して配置する。

### [S003][ADD] スマホドロワー生成
- S002と同じカテゴリモデルを利用する。
- カテゴリは `<details>`、下位ブロックは必要に応じて入れ子 `<details>` で表示する。
- `inert` / ARIA / bodyスクロール状態を開閉に同期する。

### [S004][ADD] 補助リンク生成
- menu iframe内 `#sub-menu` 冒頭の既存ユーティリティリンクを取得する。
- PCヘッダー補助領域とスマホドロワー上部へ複製する。
- hrefはmenu iframeで解決済みの `anchor.href` を使用する。

### [S005][ADD] D Monochrome本文スタイル
- 新規 `css/site_v1_6.css` を親ページhead末尾へJavaScriptで追加する。
- `rv-nav-ready` 時のみ旧左メニューを本文レイアウトから外す。
- legacy `#image` の大きな背景ヒーローは新UIでは非表示とし、ファイルは削除しない。
- `#main/#content/#content-text/#content-main` を中央単一カラム中心へ変更する。

### [S006][KEEP] フォールバック
- 親DOM取得失敗、footer不在、新JS読込失敗、menu iframe取得失敗時は新UI用bodyクラスを付けない。
- legacy menu iframe、既存モバイル処理、本文はDOM上に残す。

## 3. 入力
|名称|型|説明|
|---|---|---|
|parentWindow|Window|footer iframeの親ページWindow|
|parentDocument|Document|親ページDOM|
|menuIframe|HTMLIFrameElement|親ページ `#menu` iframe|
|legacyMenuDocument|Document|`menu.html` の既存リンクDOM|
|menuId|string|null|親ページの `menu_id` 値|
|menuId2|string|null|親ページの `menu_id_2` 値|
|viewportWidth|number|親ページ表示幅|

## 4. 出力
|名称|型|説明|
|---|---|---|
|desktopNavigation|HTMLElement|PC上部カテゴリ＋メガパネル|
|mobileNavigation|HTMLElement|スマホドロワー|
|utilityNavigation|HTMLElement|補助リンク領域|
|bodyState|string|`rv-nav-ready`, `rv-mobile-open` 等|

## 5. 設定
|名称|値|説明|
|---|---|---|
|mobileMaxWidth|767|スマホ上限px|
|categoryIds|2,3,4,5,6,9,10|既存カテゴリsubmenu ID|
|categoryCount|8|その他を含む上部カテゴリ数|
|stylesheetPath|`css/site_v1_6.css`|親ページへ追加するスタイル|
|navigationScriptPath|`js/site_navigation_v1_6.js`|footerが読み込む共通JS|

## 6. 特記事項
- relative href文字列を親ページへコピーするとnestedページで壊れるため、必ずmenu iframe内で解決済みの `anchor.href` を使用する。
- `menu.html` は変更せず既存階層をデータ源として利用する。
- 数式DOM・数式画像・記事本文は処理対象外。
- 新ナビDOM生成完了後だけ `rv-nav-ready` を付ける。
- 外部リンクは既存hrefを維持する。
- `footer.html` がない特殊ページは従来デザインを維持し、v1.6適用対象ページ一覧確認で扱う。

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|ADD|4|PCメガメニュー、スマホドロワー、補助リンク、Monochrome CSS|
|MOD|1|footerから新ナビ初期化を起動|
|DEL|0|なし|
|KEEP|1|menu/本文フォールバック維持|
