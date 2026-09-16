# site_navigation v1.6 詳細設計書

更新日: 2026-09-16

## 実装対象

|対象|変更区分|実装内容|
|---|---|---|
|`js/site_navigation_v1_6.js`|[ADD]|本体ナビゲーション生成・開閉・フォールバック制御|
|`css/site_v1_6.css`|[ADD]|D Monochrome＋PCメガメニュー＋モバイルドロワー|
|`footer.html`|[MOD]|既存Initは維持し、新JSの`script`読込だけ追加|
|`menu.html`|[KEEP]|既存リンクDOMを読み取り専用データ源として使用|
|各記事HTML|[KEEP]|本文・数式・URLを変更しない|

---

## [S001] [MOD] 共通ナビ初期化

### 1. 処理概要
`footer.html`から読み込まれた新規JSが、同一オリジンの親ページと既存`menu.html` iframeを取得し、新UIを初期化する。既存footerの高さ調整`Init()`は変更しない。

### 2. メイン関数
- [F001][ADD] `refreshSiteNavigationV16()`

### 3. 引数
該当なし。実行中のfooter iframe、`parent`、`document`から必要情報を取得する。

### 4. 戻り値
- [O001][ADD] `isInitialized:boolean`。初期化済みまたは正常初期化時`true`、親DOM不足時`false`。

### 5. 外部変数
- [V001][ADD] `mapSiteNavigationV16Config`：CSS URL、モバイル境界幅、カテゴリ設定、DOM ID。

### 6. 処理フロー
- [L001][ADD] `parent === self`の場合は処理せず`false`を返す。
- [L002][ADD] 親bodyに`rv-nav-ready`が既にある場合は二重生成せず`true`を返す。
- [L003][ADD] `selectLegacyMenuDocument()`で`#menu` iframeと`#sub-menu`を取得する。
- [L004][ADD] menu iframe未読込なら`load`へ1回だけ再実行を登録し、この時点では`false`を返す。
- [L005][ADD] `registSiteStylesheet()`、`selectNavigationModel()`、PC/モバイルDOM生成、イベント登録を順に行う。
- [L006][ADD] 必須DOM生成に成功した最後の時点でのみ親bodyへ`rv-nav-ready`を付与する。
- [L007][ADD] 例外時は`rv-nav-ready`を付与せず、既存本文・旧メニューを残す。

### 7. 特記事項
旧UIの非表示は`rv-nav-ready`に依存させる。新JS失敗時に旧メニューを消してはいけない。

---

## [S002] [ADD] PCメガメニュー

### 1. 処理概要
既存`menu.html`のカテゴリ・下位リンクをモデル化し、PC/タブレット用の8カテゴリ＋1枚式メガパネルを親ページへ生成する。

### 2. メイン関数
- [F002][ADD] `registDesktopNavigation(parentDocument, mapNavigationModel)`

### 3. 引数
- [I001][ADD] `parentDocument:Document`
- [I002][ADD] `mapNavigationModel:Object`

### 4. 戻り値
- [O002][ADD] `desktopNavigation:HTMLElement|null`

### 5. 外部変数
- [V001][KEEP] `mapSiteNavigationV16Config`

### 6. 処理フロー
- [L101][ADD] ヘッダー直後へ`nav#rv-site-navigation-v16`を生成する。
- [L102][ADD] 8カテゴリ分のbuttonを生成し`aria-expanded=false`、`aria-controls`を設定する。
- [L103][ADD] 各カテゴリのメガパネルを事前生成し、トップリンクと階層グループを配置する。
- [L104][ADD] 下位項目は階層ツリーの親子関係を`ul/li`で保持し、横方向フライアウトは生成しない。
- [L105][ADD] カテゴリ切替は`updateDesktopMenuState()`へ委譲する。

### 7. 特記事項
リンクhrefは元anchorの`anchor.href`（解決済み絶対URL）を使用し、親ページ階層へ相対URL文字列をコピーしない。

---

## [S003] [ADD] スマホドロワー

### 1. 処理概要
767px以下でハンバーガーから右ドロワーを開き、PCと同じナビゲーションモデルを`details`ベースの多層アコーディオンとして表示する。

### 2. メイン関数
- [F003][ADD] `registMobileNavigation(parentDocument, mapNavigationModel)`

### 3. 引数
- [I003][ADD] `parentDocument:Document`
- [I004][ADD] `mapNavigationModel:Object`

### 4. 戻り値
- [O003][ADD] `mapMobileElements:Object|null`（trigger、drawer、overlay、closeButton）

### 5. 外部変数
- [V001][KEEP] `mapSiteNavigationV16Config`

### 6. 処理フロー
- [L201][ADD] ヘッダーへハンバーガーボタンを生成する。
- [L202][ADD] body末尾へoverlayとdrawerを生成する。
- [L203][ADD] カテゴリを`details.rv-mobile-category`、子を再帰的`details`またはlinkで生成する。
- [L204][ADD] 初期状態はdrawerへ`aria-hidden=true`と`inert`を設定する。
- [L205][ADD] 開閉状態は`updateMobileMenuStateV16()`へ委譲する。

### 7. 特記事項
閉状態の画面外リンクへTabフォーカスを移動させない。ドロワー内は縦スクロール可能とする。

---

## [S004] [ADD] 補助リンク

### 1. 処理概要
`menu.html`の「メインコンテンツ」見出しより前にある既存ユーティリティリンクを取得し、新ヘッダーとモバイルドロワーへ複製する。

### 2. メイン関数
- [F004][ADD] `registUtilityNavigation(parentDocument, listUtilityLinks, mapMobileElements)`

### 3. 引数
- [I005][ADD] `parentDocument:Document`
- [I006][ADD] `listUtilityLinks:Array`
- [I007][ADD] `mapMobileElements:Object|null`

### 4. 戻り値
- [O004][ADD] `utilityNavigation:HTMLElement|null`

### 5. 外部変数
該当なし。

### 6. 処理フロー
- [L301][ADD] PCヘッダー内に補助リンク領域を生成する。
- [L302][ADD] 既存リンク順を維持して複製する。
- [L303][ADD] JavaScript擬似URL（お気に入り登録）は新UIへ複製せず、通常HTTP(S)/相対解決可能リンクだけを対象とする。
- [L304][ADD] モバイルdrawer上部へ同じ補助リンクを配置する。

### 7. 特記事項
既存`menu.html`自体は変更しないため、旧UIフォールバック時の導線はそのまま残る。

---

## [S005] [ADD] D Monochrome本文スタイル

### 1. 処理概要
新CSSを親ページへ追加し、`rv-nav-ready`時のみ旧920px＋左180px構成を解除して、白地・グレー罫線中心の単一カラム技術文書レイアウトへ切り替える。

### 2. メイン関数
- [F005][ADD] `registSiteStylesheet(parentDocument)`

### 3. 引数
- [I008][ADD] `parentDocument:Document`

### 4. 戻り値
- [O005][ADD] `stylesheetLink:HTMLLinkElement|null`

### 5. 外部変数
- [V001][KEEP] `mapSiteNavigationV16Config`

### 6. 処理フロー
- [L401][ADD] 親headに同一IDのlinkがあれば再利用する。
- [L402][ADD] JS自身のURLから解決した絶対CSS URLを`href`へ設定する。
- [L403][ADD] CSSは`body.rv-nav-ready`配下で`#sub`をレイアウトから除外する。
- [L404][ADD] `#wrapper/#header/#main/#content/#content-text/#content-main/#content-attend/#footer`をレスポンシブな中央配置へ上書きする。
- [L405][ADD] `#image`の旧300pxヒーロー背景は新UI時だけ非表示にする。
- [L406][ADD] 画像・表・iframeをコンテナ幅内へ収める。MathJaxの式内容には触れない。

### 7. 特記事項
既存`lib.css`・`responsive.css`は削除しない。新CSSが後から読み込まれ、`rv-nav-ready`時だけ上書きする。

---

## [S006] [KEEP] フォールバック

### 1. 処理概要
新ナビ初期化不能時に、既存本文・`menu.html` iframe・footerを維持する。

### 2. メイン関数
- [F006][ADD] `registNavigationEvents(parentWindow, parentDocument, desktopNavigation, mapMobileElements)`

### 3. 引数
- [I009][ADD] `parentWindow:Window`
- [I010][ADD] `parentDocument:Document`
- [I011][ADD] `desktopNavigation:HTMLElement`
- [I012][ADD] `mapMobileElements:Object`

### 4. 戻り値
- [O006][ADD] `isBound:boolean`

### 5. 外部変数
- [V001][KEEP] `mapSiteNavigationV16Config`

### 6. 処理フロー
- [L501][ADD] PCカテゴリbutton clickで`updateDesktopMenuState()`を呼ぶ。
- [L502][ADD] panel内clickは外側click判定へ伝播させない。
- [L503][ADD] 親document外側clickでPCメガメニューを閉じる。
- [L504][ADD] EscapeでPCメニューとモバイルdrawerを閉じる。
- [L505][ADD] モバイルtrigger/close/overlay/link clickを`updateMobileMenuStateV16()`へ接続する。
- [L506][ADD] resizeで768px以上ならmobileを閉じ、767px以下ならdesktopを閉じる。
- [L507][KEEP] イベント登録前に必要DOMが不足する場合は新UIを成立扱いにしない。

### 7. 特記事項
イベント登録自体で記事本文を削除・移動しない。

---

# 補助関数

## [T001][ADD] `selectLegacyMenuDocument(parentDocument)`
- 入力: [I013] `parentDocument`
- 出力: [O007] `legacyMenuDocument:Document|null`
- [L601] `#menu` iframe取得。
- [L602] `contentDocument`と`#sub-menu`の存在を確認。

## [T002][ADD] `selectNavigationModel(legacyMenuDocument)`
- 入力: [I014] `legacyMenuDocument`
- 出力: [O008] `mapNavigationModel:Object`
- [L611] knownカテゴリ`id_2/id_3/id_4/id_5/id_6/id_9/id_10`を取得。
- [L612] 既知カテゴリ以外のメイン/サブコンテンツrootを「その他」へ集約。
- [L613] `selectLinkTree()`で各submenuを階層化。
- [L614] `selectUtilityLinks()`で補助リンクを抽出。

## [T003][ADD] `selectLinkTree(containerElement)`
- 入力: [I015] `containerElement`
- 出力: [O009] `listTreeNodes:Array`
- [L621] anchor表示文字先頭の全角空白/空白からdepthを判定。
- [L622] 表示文字から先頭空白だけを除去し本文文字は変更しない。
- [L623] stackで親子関係を構築。
- [L624] hrefは`anchor.href`を保持。

## [T004][ADD] `selectUtilityLinks(legacyMenuDocument)`
- 入力: [I016] `legacyMenuDocument`
- 出力: [O010] `listUtilityLinks:Array`
- [L631] `#sub-menu`直下を先頭から走査し、最初の`div.sub-text`までのanchorを取得。
- [L632] `javascript:` hrefは除外。

## [T005][ADD] `registTreeList(parentDocument, listTreeNodes, isMobile)`
- 入力: [I017] `parentDocument`, [I018] `listTreeNodes`, [I019] `isMobile`
- 出力: [O011] `treeElement:HTMLElement`
- [L641] PCは`ul/li`、モバイルで子を持つnodeは`details/summary`として再帰生成。

## [T006][ADD] `updateDesktopMenuState(parentDocument, categoryKey, isOpen)`
- 入力: [I020] `parentDocument`, [I021] `categoryKey`, [I022] `isOpen`
- 出力: [O012] `isOpenResult:boolean`
- [L651] 全button/panelを一旦閉じ、要求カテゴリだけを開く。
- [L652] `aria-expanded`と`is-open`を同期。

## [T007][ADD] `updateMobileMenuStateV16(parentDocument, mapMobileElements, isOpen)`
- 入力: [I023] `parentDocument`, [I024] `mapMobileElements`, [I025] `isOpen`
- 出力: [O013] `isOpenResult:boolean`
- [L661] body class、overlay、drawer class、`aria-expanded`、`aria-hidden`、`inert`を同期。
- [L662] 閉じる時drawer内にfocusがあればtriggerへ戻す。

---

# 実装関数対応表

|ID|区分|ファイル|関数/箇所|変更内容|
|---|---|---|---|---|
|F001|ADD|`js/site_navigation_v1_6.js`|`refreshSiteNavigationV16`|初期化入口|
|F002|ADD|同上|`registDesktopNavigation`|PCナビ生成|
|F003|ADD|同上|`registMobileNavigation`|mobile生成|
|F004|ADD|同上|`registUtilityNavigation`|補助リンク生成|
|F005|ADD|同上|`registSiteStylesheet`|CSS注入|
|F006|ADD|同上|`registNavigationEvents`|イベント登録|
|T001-T007|ADD|同上|各補助関数|DOM抽出・階層化・状態更新|
|footer script読込|MOD|`footer.html`|`<head>`|外部JS読込追加。既存`Init()`はKEEP|
|D Monochrome CSS|ADD|`css/site_v1_6.css`|CSS全体|新UI時だけlegacy layoutを上書き|

# 不変条件

- `menu.html`既存リンク・`disp()`・`set_height()`を変更しない。
- 各記事HTML、数式画像src、TeX、本文文字列を変更しない。
- `release_1.0.0`を変更しない。
- 本番FTPへ反映しない。
- `*_mathjax_audit.html`を通常ナビへ掲載しない。

# コンパイル・ダイジェスト

|タグ|件数|内容（要約）|
|---|---:|---|
|[ADD]|13関数|F001-F006、T001-T007|
|[MOD]|1ファイル箇所|`footer.html` script読込追加|
|[DEL]|0|なし|
|[KEEP]|主要5領域|menu既存処理、記事本文、数式、URL、本番|
