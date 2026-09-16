# deploy_local v1.3 基本設計書

## 仕様継承テーブル
|仕様ID|状態|変更内容|ソース元|
|---|---|---|---|
|S001|新規|実行環境とGit状態を検証|BAT-LOCAL-EXEC-001/BAT-LOCAL-ERR-001|
|S002|新規|Apache公開先を再作成し公開ファイルをコピー|BAT-LOCAL-PROC-001|
|S003|新規|Apache設定テストと必要時起動|BAT-LOCAL-PROC-002|
|S004|新規|HTTP疎通確認とブラウザ起動|BAT-LOCAL-PROC-003|

## 1. 処理概要
<span style="color:green">[ADD]</span> Git Bashから静的サイトをApacheの `htdocs/ryutai` へローカル配備し、localhostで表示確認する。

## 2. 処理フロー
1. <span style="color:green">[ADD]</span> **S001**: repoRoot、developブランチ、必須ファイル、Apacheファイルを検証する。dirty時は警告のみ。
2. <span style="color:green">[ADD]</span> **S002**: `targetDir` を削除・再作成し、開発管理物を除外してtarストリームでコピーする。コピー後 `index.html` を検証する。
3. <span style="color:green">[ADD]</span> **S003**: `httpd.exe -t` を実行し、localhost未応答時だけApacheをバックグラウンド起動して応答を待つ。
4. <span style="color:green">[ADD]</span> **S004**: `localUrl` がHTTP成功することを確認し、Windows既定ブラウザを開く。ブラウザ起動失敗は警告とする。

## 3. 入力形式
|項目|タグ|内容|
|---|---|---|
|repoRoot|<span style="color:green">[ADD]</span>|スクリプト実体から導出するリポジトリルート|
|apacheRoot|<span style="color:green">[ADD]</span>|既定 `/c/server/Apache24`、環境変数でテスト時のみ上書き可|
|localUrl|<span style="color:green">[ADD]</span>|既定 `http://localhost/ryutai/`|

## 4. 出力形式
|項目|タグ|内容|
|---|---|---|
|targetDir|<span style="color:green">[ADD]</span>|`${apacheRoot}/htdocs/ryutai`|
|stdout/stderr|<span style="color:green">[ADD]</span>|処理ログ・エラーメッセージ|
|exitCode|<span style="color:green">[ADD]</span>|0成功、非0失敗|

## 5. 設定
|設定|タグ|既定値|
|---|---|---|
|APACHE_ROOT|<span style="color:green">[ADD]</span>|`/c/server/Apache24`|
|LOCAL_URL|<span style="color:green">[ADD]</span>|`http://localhost/ryutai/`|
|OPEN_BROWSER|<span style="color:green">[ADD]</span>|`1`|
|isOutputLog|<span style="color:green">[ADD]</span>|`1`|

## 6. 特記事項
- <span style="color:green">[ADD]</span> rootの `deploy_local.sh` は運用入口で、実装本体 `deploy_local_v1.3/deploy_local_v1.3.sh` を `exec` する。
- <span style="color:green">[ADD]</span> スクリプト内でgit pullは行わない。
- <span style="color:green">[ADD]</span> 本番FTP、Apache設定変更、サービスインストールは行わない。

## コンパイル・ダイジェスト
|タグ|件数|内容（要約）|
|---|---:|---|
|[ADD]|18|概要1、処理4、入力3、出力3、設定4、特記事項3|
|[MOD]|0|なし|
|[DEL]|0|なし|
|[KEEP]|0|初版のためなし|
