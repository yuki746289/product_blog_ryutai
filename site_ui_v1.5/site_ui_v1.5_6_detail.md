# site_ui v1.5 詳細設計

## 実装関数対応表
|ID|区分|対象ファイル|対象関数/対象|変更内容|
|---|---|---|---|---|
|F001|[KEEP]|`menu.html`|`Init()`|変更なし。|
|F002|<span style="color:blue">[MOD]</span>|`menu.html`|`refreshMobileNavigation()`|初期化時とresize時に表示幅別scrolling同期を呼ぶ。|
|F003|[KEEP]|`menu.html`|`updateMobileMenuState()`|変更なし。|
|F004|[KEEP]|`menu.html`|`disp()`|変更なし。|
|F005|[KEEP]|`menu.html`|`set_height()`|既存高さ調整を維持。|
|T001|<span style="color:green">[ADD]</span>|`menu.html`|`refreshMenuScrollingMode()`|767px以下=auto、768px以上=noへiframe属性を同期。|
|STATIC001|[KEEP]|`css/math.css` / FEM主要5ページ|MathJax表示|v1.4自動改行を維持。|
|STATIC002|[KEEP]|`index.html` / `menu.html` / `footer.html`|告知・履歴導線|v1.4配置を維持。|
|STYLE001|<span style="color:blue">[MOD]</span>|`css/lib.css` / `css/responsive.css`|メニュー表示|PC幅整合、モバイル広告見出し整列。|
|STATIC003|<span style="color:blue">[MOD]</span>|`revision_history.html`|修正履歴テーブル|4列化・内部ID非表示。|
|STATIC004|<span style="color:green">[ADD]</span>|`design_samples/v1.5/*`|比較サンプル|一覧＋3テーマ＋共通CSSを追加。|

## S001 数式表示改善
### 1. 処理概要
[KEEP] [S001] MathJax 4自動改行を維持する。
### 2. メイン関数
該当なし。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- [KEEP] [L101] `.math-block` に水平スクロールを発生させない。
- [KEEP] [L102] MathJax 4 `displayOverflow='linebreak'` と幅100%を維持する。
- [KEEP] [L103] 既存TeX式本文・係数・添字・式順序を変更しない。
### 7. 特記事項
今回の実装対象外。

## S002 告知・修正履歴導線
### 1. 処理概要
[KEEP] [S002] トップ告知とメニューの修正履歴リンク位置を維持する。
### 2. メイン関数
該当なし。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- [KEEP] [L201] `index.html` の2026-09-16更新告知を維持する。
- [KEEP] [L202] `footer.html` に修正履歴リンクを置かない。
- [KEEP] [L203] `menu.html` の「お気に入りに追加」直下の修正履歴リンクを維持する。
### 7. 特記事項
既存hrefは変更しない。

## S003 モバイルメニュー操作・見出し整列
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S003] 767px以下のオフキャンバーメニューだけを縦スクロール可能とし、「広告」見出しを他セクション見出しと同じ配置にする。
### 2. メイン関数
- <span style="color:blue">[MOD]</span> [F002] `refreshMobileNavigation()`
### 3. 引数
該当なし。
### 4. 戻り値
- [KEEP] [O002] `returnValue`: undefined。
### 5. 外部変数
- [KEEP] [V001] `parent`: 親ウィンドウ。
- [KEEP] [V002] `document`: menu.html自身のDOM。
- [KEEP] [V003] `scrollingAttribute`: 属性名 `scrolling`。
- <span style="color:red"><s>[DEL]</s></span> [V004] `scrollingValue`: 固定値 `auto`。表示幅別制御へ置換するため廃止。
### 6. 処理フロー
- <span style="color:blue">[MOD]</span> [L301] 初期化時に固定 `auto` を設定せず、T001へ `parentWindow` と `menuIframe` を渡して現在幅に応じたscrollingを設定する。
- [KEEP] [L302] モバイルの `iframe#menu` は縦スクロール・overscroll抑制・タッチ慣性スクロールを維持する。
- <span style="color:blue">[MOD]</span> [L303] モバイルの `div.sub-text` と `dt` の幅・左右余白・中央揃えを統一し、末尾の「広告」も同じレイアウトにする。
### 7. 特記事項
親bodyの開状態固定とオーバーレイ動作は変更しない。

## S004 PC左メニュー表示
### 1. 処理概要
<span style="color:blue">[MOD]</span> [S004] PC左メニューの幅とiframeスクロール属性を整合させ、文字切れと不要なiframeスクロールバーを解消する。
### 2. メイン関数
- <span style="color:green">[ADD]</span> [T001] `refreshMenuScrollingMode(parentWindow, menuIframe)`
- [KEEP] [F005] `set_height()`
### 3. 引数
- <span style="color:green">[ADD]</span> [I004] `parentWindow`: 親Window。
- <span style="color:green">[ADD]</span> [I005] `menuIframe`: 親ページのmenu iframe要素。
### 4. 戻り値
- <span style="color:green">[ADD]</span> [O006] `returnValue`: undefined。
### 5. 外部変数
該当なし。閾値・属性値はT001のローカル変数とする。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L401] T001で `mobileMaxWidth=767` を定義し、現在幅が767以下なら `auto`、768以上なら `no` を選択してiframeの`scrolling`へ設定する。
- <span style="color:blue">[MOD]</span> [L402] F002のresizeハンドラでT001を再実行した後、既存どおり768px以上ではモバイルメニューを閉じる。
- <span style="color:blue">[MOD]</span> [L403] `css/lib.css` のPC `#sub` 幅を180pxへ揃え、`#sub-menu` とiframeの180px幅をクリップしない。
- [KEEP] [L404] `set_height()` によるPC iframe高さ調整ロジックを維持する。
### 7. 特記事項
PC側の通常ページ縦スクロールはブラウザ本体に任せ、iframe内部スクロールは表示しない。

## S005 修正履歴4列化
### 1. 処理概要
<span style="color:green">[ADD]</span> [S005] 利用者向け修正履歴をNo.と修正種類中心の表へ再構成する。
### 2. メイン関数
該当なし（HTML/CSS）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L501] ヘッダー列を `No. / 修正種類 / 対象 / 修正内容` に変更する。
- <span style="color:green">[ADD]</span> [L502] 各履歴を「誤記修正」「数式修正」「補足追加」「表示改善」「操作性改善」の主分類へ割り当てる。
- <span style="color:green">[ADD]</span> [L503] 既存管理IDは各`tr`の `data-revision-id` へ移し、視覚列として表示しない。
- <span style="color:green">[ADD]</span> [L504] v1.5の左メニュー/スクロール/広告配置改善と履歴表改善を新しい履歴項目として追加する。
### 7. 特記事項
既存の修正箇所リンクは維持する。

## S006 デザイン比較サンプル
### 1. 処理概要
<span style="color:green">[ADD]</span> [S006] 同一の代表技術コンテンツを3つのデザイン方式で比較できる独立サンプルを作成する。
### 2. メイン関数
該当なし（静的HTML/CSS）。
### 3. 引数
該当なし。
### 4. 戻り値
該当なし。
### 5. 外部変数
該当なし。
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L601] `design_samples/v1.5/index.html` に3案の説明とリンクを配置する。
- <span style="color:green">[ADD]</span> [L602] `technical-clean.html` を白基調・濃紺アクセント・左ナビ型で作成する。
- <span style="color:green">[ADD]</span> [L603] `academic-minimal.html` を余白・タイポグラフィ重視の技術ノート型で作成する。
- <span style="color:green">[ADD]</span> [L604] `modern-dashboard.html` をダークサイドバー・カードUI型で作成する。
- <span style="color:green">[ADD]</span> [L605] `design-samples.css` で共通コンテンツと各テーマ、390pxレスポンシブ表示を定義する。
### 7. 特記事項
サンプルは本体CSSを読み込まず、既存ページへリンクを追加しない。採用決定前に本体へ適用しない。

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|[ADD]|17|T001,I004,I005,O006,L401,S005,L501-L504,S006,L601-L605,STATIC004相当|
|[MOD]|9|F002,S003,L301,L303,S004,L402,L403,STYLE001,STATIC003相当|
|[KEEP]|20|S001,L101-L103,S002,L201-L203,O002,V001-V003,L302,F005,L404,F001,F003,F004,STATIC001,STATIC002|
|[DEL]|1|V004|
