# site_ui v1.4 基本設計

## 仕様継承
|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|変更|MathJax表示を横スクロールから自動改行へ|v1.2 MathJax化|
|S002|変更|トップ告知と修正履歴導線を更新|v1.2 修正履歴|
|S003|変更|モバイルメニューのスクロール/背景を改善|v1.1 responsive|
|S004|維持|PC左メニュー・既存URL|v1.1 responsive|

## 処理フロー
- <span style="color:blue">[MOD]</span> [S001] `css/math.css` の横スクロール指定を撤去し、MathJax 4の自動改行設定へ更新する。
- <span style="color:blue">[MOD]</span> [S002] `index.html` に更新告知を追加し、修正履歴リンクを `footer.html` から `menu.html` へ移す。
- <span style="color:blue">[MOD]</span> [S003] `refreshMobileNavigation()` でメニューiframeのscrollingをautoへ変更し、CSSでiframe内文書の縦スクロール・白背景・全高を保証する。
- [KEEP] [S004] 768px以上のPC/タブレット左メニュー、既存href、`disp()`、`set_height()`を維持する。

## 入力
|項目|内容|
|---|---|
|viewport|スマホ390px、PC1365pxを代表確認幅とする|
|操作|ハンバーガー、マウスホイール、タッチ、Escape、オーバーレイ|

## 出力
|項目|内容|
|---|---|
|数式|スクロールなし、自動改行|
|メニュー|縦スクロール可能、白背景|
|トップ|更新告知と修正履歴リンク|

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|[MOD]|3|S001〜S003|
|[KEEP]|1|S004|
|[ADD]|0|なし|
|[DEL]|0|なし|
