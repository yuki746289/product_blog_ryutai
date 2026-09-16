# site_ui v1.5 基本設計

## 仕様継承
|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|維持|MathJax 4自動改行表示を維持|v1.4 S001|
|S002|維持|トップ告知・修正履歴導線を維持|v1.4 S002|
|S003|変更|スマホのみiframeスクロール可、広告見出し整列|v1.4 S003|
|S004|変更|PC左メニュー幅・iframeスクロール状態を修正|v1.4 S004|
|S005|新規|修正履歴をNo./種類/対象/内容で表示|v1.5|
|S006|新規|独立したデザイン比較サンプル3案を追加|v1.5|

## 処理一覧
- [KEEP] [S001] MathJax 4による数式自動改行と既存数式内容を維持する。
- [KEEP] [S002] トップ更新告知と「お気に入りに追加」直下の修正履歴導線を維持する。
- <span style="color:blue">[MOD]</span> [S003] 767px以下ではmenu iframeの縦スクロールを許可し、「広告」見出しを他セクションと同じ配置にする。
- <span style="color:blue">[MOD]</span> [S004] 768px以上では左メニューの幅を180px基準で整合させ、menu iframeのscrollingをnoへ同期して文字切れ・不要スクロールを抑止する。
- <span style="color:green">[ADD]</span> [S005] `revision_history.html` を `No. / 修正種類 / 対象 / 修正内容` の4列表示へ変更する。
- <span style="color:green">[ADD]</span> [S006] `design_samples/v1.5/` にTechnical Clean / Academic Minimal / Modern Dashboardと比較一覧を作成する。

## 入力
|項目|内容|
|---|---|
|viewport|スマホ390px、PC1365pxを代表確認幅とする|
|メニュー操作|ページ初期化、resize、ハンバーガー、マウスホイール、タッチ|
|修正履歴|v1.4までの履歴＋v1.5表示/操作改善|
|デザインサンプル|同一の代表技術コンテンツ|

## 出力
|項目|内容|
|---|---|
|PC左メニュー|右端まで文字表示、iframe縦スクロールバーなし|
|スマホメニュー|縦スクロール可、見出し配置統一|
|修正履歴|No./修正種類/対象/修正内容|
|デザイン比較|3案＋一覧ページ|

## 設定
|項目|値|
|---|---|
|mobileMaxWidth|767px|
|desktopMinWidth|768px|
|desktopMenuWidth|180px|
|sampleDesktopWidth|1365px|
|sampleMobileWidth|390px|

## 特記事項
- サンプルは本体の正式デザインへ反映しない。
- 本番FTPは変更しない。
- 既存メニューhrefとカテゴリ展開ロジックは維持する。

## コンパイル・ダイジェスト
|タグ|件数|内容|
|---|---:|---|
|[ADD]|2|S005,S006|
|[MOD]|2|S003,S004|
|[KEEP]|2|S001,S002|
|[DEL]|0|なし|