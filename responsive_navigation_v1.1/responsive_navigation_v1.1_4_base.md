# responsive_navigation v1.1 基本設計書

## 仕様継承テーブル

|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|変更|既存`Init()`からスマホ用ナビゲーション初期化を呼び出す|release_1.0.0 `menu.html` / UI-NAV-001|
|S002|新規|親ページへスマホ用メニューボタンとオーバーレイを初期化する|UI-NAV-001 / REQ-003〜REQ-005|
|S003|新規|スマホ用メニューの開閉状態とARIA属性を更新する|UI-NAV-002 / REQ-004〜REQ-007|
|S004|維持|既存`disp()`による選択中メニュー表示を維持する|release_1.0.0 `menu.html`|
|S005|維持|既存`set_height()`によるiframe高さ調整を維持する|release_1.0.0 `menu.html`|

## 1. 処理概要

既存`menu.html` iframeをナビゲーションの正本として維持し、767px以下でのみ同iframeをオフキャンバス型メニューとして利用する。`menu.html`は同一オリジンで親ページDOMへアクセスできるため、既存`Init()`から新規初期化関数を呼び出し、親ページのヘッダーへスマホ用ボタンと背景オーバーレイを生成する。JavaScript初期化に成功した場合だけ`mobile-nav-ready`クラスを親`body`へ付与し、CSSでiframeをドロワー表示へ切り替える。JavaScriptが失敗した場合は`mobile-nav-ready`が付与されず、CSSのみの1カラム＋既存メニュー縦配置をフォールバックとする。

## 2. 処理一覧

|処理ID|区分|処理|
|---|---|---|
|S001|<span style="color:blue">[MOD]</span>|既存`Init()`の`disp()`・`set_height()`を維持しつつ、スマホナビゲーション初期化処理を追加呼び出しする。|
|S002|<span style="color:green">[ADD]</span>|親ページDOMを確認し、ハンバーガーボタン、背景オーバーレイ、iframe属性、イベントハンドラを初期化する。|
|S003|<span style="color:green">[ADD]</span>|`mobile-menu-open`クラスと`aria-expanded`を同期し、開閉状態を更新する。|
|S004|[KEEP]|既存`disp()`で現在カテゴリの表示・強調を行う。コードは変更しない。|
|S005|[KEEP]|既存`set_height()`でPC表示時のmenu iframe高さを調整する。コードは変更しない。|

## 3. 入力

|入力|区分|型|説明|
|---|---|---|---|
|browserWidth|[KEEP]|number|CSSメディアクエリとリサイズ判定に使用する表示幅。|
|menuButtonAction|<span style="color:green">[ADD]</span>|click event|ハンバーガーボタンの押下。|
|closeAction|<span style="color:green">[ADD]</span>|click / keydown event|オーバーレイ押下またはEscapeキー。|

## 4. 出力

|出力|区分|型|説明|
|---|---|---|---|
|responsiveLayout|<span style="color:blue">[MOD]</span>|DOM/CSS state|767px以下は1カラム、768px以上は現行レイアウト。CSS側で制御する。|
|mobileMenuState|<span style="color:green">[ADD]</span>|DOM class / aria state|`mobile-menu-open`と`aria-expanded`で開閉状態を表現。|
|existingNavigationTarget|[KEEP]|URL|既存`menu.html`のリンク先。|

## 5. 設定

|設定|区分|値|説明|
|---|---|---|---|
|mobileBreakpoint|<span style="color:blue">[MOD]</span>|767px|旧暫定768pxから、スマホのみを対象とする767px以下へ変更。|
|menuSource|[KEEP]|`menu.html`|メニュー項目の正本。複製しない。|
|mobileReadyClass|<span style="color:green">[ADD]</span>|`mobile-nav-ready`|JavaScript初期化成功時のみ親bodyへ付与。|

## 6. 特記事項

- `menu.html`の既存関数`Init()`, `disp()`, `set_height()`を現行コードと照合済み。
- `Init()`のみ変更し、`disp()`と`set_height()`は変更しない。
- 新規関数は`refreshMobileNavigation()`と`updateMobileMenuState()`を予定する。
- CSSは`css/responsive.css`のみを変更し、767px以下へレスポンシブ影響を限定する。
- 既存ページ192件へ新しいメニューHTMLを複製しない。
- 既に追加済みのviewport metaはv1.1のスマホ表示前提として維持する。
- 親DOMへ生成する要素はDOM APIで構築し、外部入力文字列を`innerHTML`へ挿入しない。
- 本番FTPへのデプロイは本設計・実装の対象外。

## コンパイル・ダイジェスト

|タグ|件数|内容（要約）|
|---|---:|---|
|[ADD]|6件|スマホ初期化、開閉制御、操作入力、状態出力、readyクラス|
|[MOD]|3件|Init変更、レスポンシブ出力、767pxブレークポイント|
|[DEL]|0件|削除なし|
|[KEEP]|5件|disp、set_height、表示幅入力、既存URL、menu.html正本|
