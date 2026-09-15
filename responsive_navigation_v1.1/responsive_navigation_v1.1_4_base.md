# responsive_navigation v1.1 基本設計書

## 仕様継承テーブル

|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|変更|767px以下のレスポンシブCSSを再設計|v1.1仕様 UI-RWD-002 / NFR-MOB-001|
|S002|新規|既存menu.htmlから親ページへスマホ用メニューボタンを初期化|v1.1仕様 UI-NAV-001|
|S003|新規|スマホ用メニューの開閉状態を制御|v1.1仕様 UI-NAV-002|
|S004|維持|既存menu.html内のリンク定義とtarget=_parent遷移を維持|release_1.0.0 menu.html|
|S005|維持|768px以上の左サイドメニュー表示を維持|release_1.0.0 css/lib.css / 各HTML|

## 1. 処理概要

既存`menu.html` iframeをナビゲーションの正本として維持し、767px以下でのみ同iframeをオフキャンバス型メニューとして利用する。`menu.html`は同一オリジンで親ページDOMへアクセスできるため、親ページのヘッダーへスマホ用ボタンとオーバーレイを生成する。JavaScript初期化に成功した場合だけ`mobile-nav-ready`クラスを親`body`へ付与し、CSSでiframeをドロワー表示へ切り替える。JavaScriptが失敗した場合は`mobile-nav-ready`が付与されず、CSSのみの1カラム＋既存メニュー縦配置をフォールバックとする。

## 2. 処理一覧

|処理ID|区分|処理|
|---|---|---|
|S001|<span style="color:blue">[MOD]</span>|767px以下のレイアウトを1カラム化し、グローバルなPC影響を除去する。|
|S002|<span style="color:green">[ADD]</span>|`menu.html`初期化時に親ページへハンバーガーボタンとオーバーレイを生成し、モバイルナビゲーション利用可能状態にする。|
|S003|<span style="color:green">[ADD]</span>|ボタン、オーバーレイ、Escape、リサイズに応じてメニュー開閉状態とARIA属性を更新する。|
|S004|[KEEP]|既存`menu.html`のリンク一覧、カテゴリ表示、`target="_parent"`による遷移を変更せず利用する。|
|S005|[KEEP]|768px以上では既存`#sub`と`iframe#menu`の左サイド表示を維持し、スマホ用ボタンを非表示にする。|

## 3. 入力

|入力|区分|型|説明|
|---|---|---|---|
|browserWidth|[KEEP]|number|CSSメディアクエリとリサイズ判定に使用する表示幅。|
|menuButtonAction|<span style="color:green">[ADD]</span>|click event|ハンバーガーボタンの押下。|
|closeAction|<span style="color:green">[ADD]</span>|click / keydown event|オーバーレイ押下またはEscapeキー。|

## 4. 出力

|出力|区分|型|説明|
|---|---|---|---|
|responsiveLayout|<span style="color:blue">[MOD]</span>|DOM/CSS state|767px以下は1カラム、768px以上は現行レイアウト。|
|mobileMenuState|<span style="color:green">[ADD]</span>|DOM class / aria state|`mobile-menu-open`と`aria-expanded`で開閉状態を表現。|
|existingNavigationTarget|[KEEP]|URL|既存`menu.html`のリンク先。|

## 5. 設定

|設定|区分|値|説明|
|---|---|---|---|
|mobileBreakpoint|<span style="color:blue">[MOD]</span>|767px|旧暫定768pxから、スマホのみを対象とする767px以下へ変更。|
|menuSource|[KEEP]|`menu.html`|メニュー項目の正本。複製しない。|
|mobileReadyClass|<span style="color:green">[ADD]</span>|`mobile-nav-ready`|JavaScript初期化成功時のみ親bodyへ付与。|

## 6. 特記事項

- `menu.html`の既存関数`Init()`, `disp()`, `set_height()`は現行コードを確認し、変更対象を詳細設計で個別判定する。
- 既存ページ192件へ新しいメニューHTMLを複製しない。
- 既に追加済みのviewport metaはv1.1のスマホ表示前提として維持する。
- `responsive.css`のルールは767px以下へ限定し、PC/タブレット表示への影響を最小化する。
- 親DOMへ生成する要素は静的なDOM APIで構築し、外部入力文字列を`innerHTML`へ挿入しない。
- 本番FTPへのデプロイは本設計・実装の対象外。

## コンパイル・ダイジェスト

|タグ|件数|内容（要約）|
|---|---:|---|
|[ADD]|6件|スマホ初期化、開閉制御、操作入力、状態出力、readyクラス|
|[MOD]|3件|スマホCSS、レスポンシブ出力、767pxブレークポイント|
|[DEL]|0件|削除なし|
|[KEEP]|5件|既存リンク、PC左メニュー、表示幅入力、既存URL、menu.html正本|
