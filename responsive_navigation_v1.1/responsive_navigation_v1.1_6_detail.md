# responsive_navigation v1.1 詳細設計書

## 実装関数対応表

|ID|区分|対象ファイル|対象関数/対象|変更内容|
|---|---|---|---|---|
|F001|<span style="color:blue">[MOD]</span>|`menu.html`|`Init()`|既存`disp()`・`set_height()`の後に`refreshMobileNavigation()`を呼び出す。|
|F002|<span style="color:green">[ADD]</span>|`menu.html`|`refreshMobileNavigation()`|親ページへボタン・オーバーレイを生成しイベントを登録する。|
|F003|<span style="color:green">[ADD]</span>|`menu.html`|`updateMobileMenuState()`|親bodyクラスとARIA属性を同期して開閉状態を更新する。|
|F004|[KEEP]|`menu.html`|`disp()`|変更なし。|
|F005|[KEEP]|`menu.html`|`set_height()`|変更なし。|
|STYLE001|<span style="color:blue">[MOD]</span>|`css/responsive.css`|767px以下のモバイルスタイル|PC影響を除去し、ready時だけiframeをオフキャンバス化する。|

---

## S001 <span style="color:blue">[MOD]</span> Init初期化拡張

### 1. 処理概要
既存`Init()`の処理順を維持し、最後にスマートフォンナビゲーション初期化を追加する。

### 2. メイン関数
- F001 <span style="color:blue">[MOD]</span> `Init()`
- 対象: `menu.html`

### 3. 引数
該当なし。

### 4. 戻り値
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|O001|[KEEP]|returnValue|undefined|値を返さない既存初期化関数。|

### 5. 外部変数
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|V001|[KEEP]|`parent`|Window|iframe親ウィンドウ。既存コードでも参照。|
|V002|[KEEP]|`document`|Document|menu.html自身のDOM。既存コードでも参照。|

### 6. 処理フロー
- L001 [KEEP] `disp()`を呼び出し、選択中カテゴリを表示する。
- L002 [KEEP] `set_height()`を呼び出し、PC用iframe高さを既存方式で調整する。
- L003 <span style="color:green">[ADD]</span> `refreshMobileNavigation()`を呼び出す。

### 7. 特記事項
`disp()`と`set_height()`のコード自体は変更しない。

---

## S002 <span style="color:green">[ADD]</span> スマートフォンナビゲーション初期化

### 1. 処理概要
`menu.html`がiframeとして読み込まれた場合に、親ページDOMへスマートフォン用操作要素を1回だけ生成する。初期化成功後にのみ親`body`へ`mobile-nav-ready`を付与する。

### 2. メイン関数
- F002 <span style="color:green">[ADD]</span> `refreshMobileNavigation()`
- 対象: `menu.html`

### 3. 引数
該当なし。

### 4. 戻り値
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|O002|<span style="color:green">[ADD]</span>|returnValue|undefined|DOM初期化のみ行い値は返さない。|

### 5. 外部変数
- V001 [KEEP] `parent`を参照する。
- V002 [KEEP] `document`を参照する。

### 6. 処理フロー
- L004 <span style="color:green">[ADD]</span> `parent === self`の場合は単体表示と判断して終了する。
- L005 <span style="color:green">[ADD]</span> 親`document`、`body`、`#header`、`#menu`を取得し、必要要素がない場合は本文へ影響を与えず終了する。
- L006 <span style="color:green">[ADD]</span> `#menu`へ`title="サイトメニュー"`を設定する。
- L007 <span style="color:green">[ADD]</span> 親ページに`#mobile-menu-button`がなければ`button`要素を生成し、`aria-controls="menu"`、`aria-expanded="false"`、操作ラベルを設定する。
- L008 <span style="color:green">[ADD]</span> ボタン内部の3本線は`span`要素をDOM APIで生成し、`innerHTML`を使用しない。
- L009 <span style="color:green">[ADD]</span> 親ページに`.mobile-menu-overlay`がなければ`div`要素を生成する。
- L010 <span style="color:green">[ADD]</span> 親`body`へ`mobile-nav-ready`クラスを付与する。
- L011 <span style="color:green">[ADD]</span> ボタン押下時は現在の`mobile-menu-open`有無を反転してF003を呼び出す。
- L012 <span style="color:green">[ADD]</span> オーバーレイ押下時は閉状態としてF003を呼び出す。
- L013 <span style="color:green">[ADD]</span> 親ウィンドウの`keydown`でEscapeを検出した場合は閉状態としてF003を呼び出す。
- L014 <span style="color:green">[ADD]</span> 親ウィンドウの`resize`で幅が768px以上になった場合は閉状態としてF003を呼び出す。
- L015 <span style="color:green">[ADD]</span> 初期状態を閉状態としてF003へ渡す。

### 7. 特記事項
- 親ページとmenu iframeは同一オリジンである現行構成を前提とする。
- 新規DOM要素の文字列は固定値のみを使用し、外部入力を挿入しない。
- 既存ページへ個別のメニューHTMLを複製しない。

---

## S003 <span style="color:green">[ADD]</span> メニュー開閉状態更新

### 1. 処理概要
スマートフォンメニューの開閉状態を親`body`クラスとボタンARIA属性へ反映する。

### 2. メイン関数
- F003 <span style="color:green">[ADD]</span> `updateMobileMenuState(parentDocument, menuButton, isOpen)`
- 対象: `menu.html`

### 3. 引数
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|I001|<span style="color:green">[ADD]</span>|parentDocument|Document|親ページDOM。|
|I002|<span style="color:green">[ADD]</span>|menuButton|HTMLButtonElement|開閉状態を反映するボタン。|
|I003|<span style="color:green">[ADD]</span>|isOpen|boolean|true=開、false=閉。|

### 4. 戻り値
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|O003|<span style="color:green">[ADD]</span>|returnValue|undefined|状態更新のみ行い値は返さない。|

### 5. 外部変数
該当なし。

### 6. 処理フロー
- L016 <span style="color:green">[ADD]</span> `isOpen=true`の場合は親`body`へ`mobile-menu-open`クラスを追加し、falseの場合は削除する。
- L017 <span style="color:green">[ADD]</span> `aria-expanded`を`true`/`false`へ更新する。
- L018 <span style="color:green">[ADD]</span> `aria-label`を開状態では「メニューを閉じる」、閉状態では「メニューを開く」に更新する。

### 7. 特記事項
クラス操作と属性更新のみを担当し、DOM生成は行わない。

---

## S004 [KEEP] 既存カテゴリ表示

### 1. 処理概要
現在ページに対応するカテゴリをmenu.html内で表示・強調する既存処理。

### 2. メイン関数
- F004 [KEEP] `disp()`

### 3. 引数
該当なし。

### 4. 戻り値
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|O004|[KEEP]|returnValue|undefined|既存どおり。|

### 5. 外部変数
- V001 [KEEP] `parent`
- V002 [KEEP] `document`

### 6. 処理フロー
- L019 [KEEP] 親`menu_id`を取得する。
- L020 [KEEP] 対応する`id_x`カテゴリを表示し太字化する。
- L021 [KEEP] `menu_id_2`がある場合は対応する下位カテゴリを表示する。

### 7. 特記事項
コード変更禁止。

---

## S005 [KEEP] 既存iframe高さ調整

### 1. 処理概要
menu iframeの高さを内容量に合わせる既存処理。

### 2. メイン関数
- F005 [KEEP] `set_height()`

### 3. 引数
該当なし。

### 4. 戻り値
|ID|区分|名称|型|説明|
|---|---|---|---|---|
|O005|[KEEP]|returnValue|undefined|既存どおり。|

### 5. 外部変数
- V001 [KEEP] `parent`
- V002 [KEEP] `document`

### 6. 処理フロー
- L022 [KEEP] 親iframe IDとして`menu`を使用する。
- L023 [KEEP] 親iframeが存在することを確認する。
- L024 [KEEP] ブラウザ条件に応じて`scrollHeight`または`offsetHeight`をiframe高さへ設定する。

### 7. 特記事項
コード変更禁止。スマホready時はCSSの`height:100vh !important`を優先し、PCでは既存高さ調整を利用する。

---

## CSS実装仕様

`css/responsive.css`は以下を変更する。

- 全レスポンシブ上書きを`@media screen and (max-width: 767px)`内へ限定する。
- 画像・iframe・preの幅調整もスマホ時のみとし、768px以上へ影響させない。
- JavaScript未初期化時は`#sub`を本文下に表示できるフォールバックを残す。
- `body.mobile-nav-ready`時は`#sub`内の`iframe#menu`以外をスマホ表示から外す。
- `iframe#menu`を固定配置、左からスライドするドロワーとして表示する。
- `body.mobile-menu-open`時のみドロワーを画面内へ移動する。
- `.mobile-menu-button`と`.mobile-menu-overlay`をスマホ時のみ有効化する。
- オーバーレイは閉状態でpointer-eventsを無効化し、開状態で有効化する。
- メニュー開状態では親bodyのスクロールを抑制する。

## コンパイル・ダイジェスト

管理対象IDを1件ずつ数えた変更区分は以下。

|タグ|件数|内容（要約）|
|---|---:|---|
|[ADD]|25件|S002/S003、F002/F003、I001〜I003、O002/O003、L003〜L018|
|[MOD]|3件|S001、F001、STYLE001|
|[DEL]|0件|削除なし|
|[KEEP]|17件|S004/S005、F004/F005、O001/O004/O005、V001/V002、L001/L002/L019〜L024|
