# deploy_local v1.3 コード確認レポート

対象:
- `deploy_local_v1.3/deploy_local_v1.3_7_detail.json`
- `deploy_local_v1.3/deploy_local_v1.3.sh`
- 運用入口 `deploy_local.sh`
- 自動検証: GitHub Actions run `35062679397`

## 1. トレーサビリティ
- [x] ADD/MOD対象の L21 / F4 / T1 / I1 / O4 / V8 をコード内コメントで照合。
- [x] `writeLog` はT001のみ、4主関数はF001〜F004のみを割当。
- [x] rootラッパーにはnamed functionがなく、v1.3実装本体を `bash` で起動する運用入口のみ。
- [x] 設計外の本番FTP処理、Apache設定変更処理は存在しない。
- [x] KEEP対象の既存サイトコードは本実装で変更していない。

### F/T割当確認レポート
|検証項目|件数|判定|備考|
|---|---:|:---:|---|
|named function 総数|5|OK|`writeLog`, `checkEnvironment`, `updateLocalSite`, `updateApacheState`, `refreshLocalPreview`|
|F割当|4|OK|F001〜F004|
|T割当|1|OK|T001|
|F/T両方併記|0|OK|なし|
|F/T未割当|0|OK|なし|
|ID重複|0|OK|なし|

## 2. 品質・仕様
- [x] JSONカバレッジ100%。
- [x] 入力: develop作業ツリー、Apache既定 `/c/server/Apache24`。
- [x] 出力: `htdocs/ryutai`、標準ログ、HTTP確認URL。
- [x] 変数・関数はcamelCase。
- [x] `updateLocalSite`, `updateApacheState`, `refreshLocalPreview` は命名規則に沿う。
- [x] shell scriptはUTF-8テキストで、日本語を外部ファイルへ自動追記しない。
- [x] tarコピーは元ファイルを変換せず、CP932等をそのまま保持する。
- [x] 削除安全ガードにより `/`, apacheRoot, `apacheRoot/htdocs` をtargetDirとして削除しない。

## 3. 動作検証
GitHub Actions run `35062679397`: **SUCCESS**

- [x] `bash -n` によるrootラッパー/実装本体の構文確認。
- [x] 統合JSONの全ADD/MOD IDがコードに存在。
- [x] 疑似Apacheで設定テスト・起動・HTTP疎通を実行。
- [x] `index.html` を公開先へコピー。
- [x] `.git/.github/.document/.rules/deploy_local_v1.3/deploy_local.sh` を公開先から除外。
- [x] `index.html` と `fem/fem_7_2_2.html` を `cmp` し、バイト同一性を確認。
- [x] 同じスクリプトを2回連続実行し、再実行性を確認。
- [x] 2回目は既存HTTP応答を検出して重複Apache起動を回避。

### Windows実機固有確認
GitHub ActionsはユーザPCではないため、次は自動検証対象外。
- `C:\server\Apache24` 実体での `httpd.exe -t`
- Windows Git Bashからの `cmd.exe start` による既定ブラウザ表示
- `http://localhost/ryutai/` の実PC表示

これらはユーザPCで `bash deploy_local.sh` 実行時に最終確認する。

## 最終判定レポート
|検証項目|判定|備考|
|---|:---:|---|
|設計IDの一致|OK|43管理項目を照合|
|JSON仕様の網羅|OK|100%|
|不変領域の維持|OK|サイト本文・本番FTP未変更|
|自動動作確認|OK|run 35062679397 success|
|Windows実機確認|PENDING|ユーザPCで実行が必要|

**総合判定: 実装・自動検証は合格 / Windows実機受入のみ未完了**
