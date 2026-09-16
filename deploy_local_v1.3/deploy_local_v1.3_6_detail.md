# deploy_local v1.3 詳細設計書

全項目は初版のため <span style="color:green">[ADD]</span>。

## S001 実行環境検証
### 1. 処理概要
<span style="color:green">[ADD]</span> [S001] リポジトリ、ブランチ、必須ファイル、Apache実体を検証する。
### 2. メイン関数
<span style="color:green">[ADD]</span> [F001] `checkEnvironment`
### 3. 引数
該当なし。
### 4. 戻り値
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [O001]|status|integer|0成功、異常時は終了|
### 5. メイン変数
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [V001]|repoRoot|string|リポジトリルート|
|<span style="color:green">[ADD]</span> [V002]|apacheRoot|string|Apacheルート|
|<span style="color:green">[ADD]</span> [V005]|httpdExe|string|httpd.exe|
|<span style="color:green">[ADD]</span> [V006]|httpdConf|string|httpd.conf|
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L101] Git管理下か確認する (S001)
- <span style="color:green">[ADD]</span> [L102] 現在ブランチがdevelopか確認する (S001)
- <span style="color:green">[ADD]</span> [L103] dirtyなら警告する (S001)
- <span style="color:green">[ADD]</span> [L104] `index.html` を確認する (S001)
- <span style="color:green">[ADD]</span> [L105] Apache実体と設定ファイルを確認する (S001)
### 7. 特記事項
失敗時は即時非0終了。本番環境には接続しない。

## S002 公開ファイルコピー
### 1. 処理概要
<span style="color:green">[ADD]</span> [S002] `htdocs/ryutai` を再作成し公開ファイルのみコピーする。
### 2. メイン関数
<span style="color:green">[ADD]</span> [F002] `updateLocalSite`
### 3. 引数
該当なし。
### 4. 戻り値
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [O002]|status|integer|0成功、異常時は終了|
### 5. メイン変数
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [V003]|targetDir|string|Apache公開先|
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L201] 既存targetDirを削除する (S002)
- <span style="color:green">[ADD]</span> [L202] targetDirを再作成する (S002)
- <span style="color:green">[ADD]</span> [L203] 開発管理物を除外しtarストリームでコピーする (S002)
- <span style="color:green">[ADD]</span> [L204] コピー後index.htmlを検証する (S002)
- <span style="color:green">[ADD]</span> [L205] 配置先をログ表示する (S002)
### 7. 特記事項
コピーはバイト列として扱い文字コード変換しない。再実行可能。

## S003 Apache確認・起動
### 1. 処理概要
<span style="color:green">[ADD]</span> [S003] Apache設定を検証し、未起動時のみ起動する。
### 2. メイン関数
<span style="color:green">[ADD]</span> [F003] `updateApacheState`
### 3. 引数
該当なし。
### 4. 戻り値
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [O003]|status|integer|0成功、異常時は終了|
### 5. メイン変数
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [V004]|localUrl|string|確認URL|
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L301] `httpd.exe -t` を実行する (S003)
- <span style="color:green">[ADD]</span> [L302] localhost応答済みか確認する (S003)
- <span style="color:green">[ADD]</span> [L303] 未応答ならhttpd.exeをバックグラウンド起動する (S003)
- <span style="color:green">[ADD]</span> [L304] 最大10回、1秒間隔で応答待機する (S003)
- <span style="color:green">[ADD]</span> [L305] 起動失敗時はApacheログ位置を示して異常終了する (S003)
- <span style="color:green">[ADD]</span> [L306] 起動済みなら重複起動しない (S003)
### 7. 特記事項
Apache設定ファイルの自動編集やサービス登録は行わない。

## S004 HTTP確認・ブラウザ表示
### 1. 処理概要
<span style="color:green">[ADD]</span> [S004] ryutai URLを確認し、既定ブラウザで開く。
### 2. メイン関数
<span style="color:green">[ADD]</span> [F004] `refreshLocalPreview`
### 3. 引数
該当なし。
### 4. 戻り値
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [O004]|status|integer|HTTP成功時0|
### 5. メイン変数
|ID|名称|型|説明|
|---|---|---|---|
|<span style="color:green">[ADD]</span> [V007]|isOutputLog|integer|ログ出力制御|
|<span style="color:green">[ADD]</span> [V008]|openBrowser|integer|ブラウザ起動制御|
### 6. 処理フロー
- <span style="color:green">[ADD]</span> [L401] localUrlへcurlしHTTP成功を確認する (S004)
- <span style="color:green">[ADD]</span> [L402] 成功URLをログ表示する (S004)
- <span style="color:green">[ADD]</span> [L403] openBrowser=1ならWindows既定ブラウザ起動を試行する (S004)
- <span style="color:green">[ADD]</span> [L404] ブラウザ起動失敗は警告のみとする (S004)
### 7. 特記事項
HTTP成功を配備成功条件とし、ブラウザ起動は補助機能とする。

## 共通補助関数
<span style="color:green">[ADD]</span> [T001] `writeLog`: [V007] `isOutputLog` が1のときログを標準出力する。

## コンパイル・ダイジェスト
管理対象件数（本集計表自身を除く）:
|タグ|件数|内容|
|---|---:|---|
|[ADD]|38|S4,F4,T1,O4,V8,L20,各章の処理概要/定義を含む設計管理項目|
|[MOD]|0|なし|
|[DEL]|0|なし|
|[KEEP]|0|初版|
