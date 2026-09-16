# v1.3 仕様インデックス

対象: Git Bash / Apache ローカル確認用デプロイスクリプト
開発種別: batch
未決事項: なし

> v1.1 はレスポンシブ app 仕様であり、batch 用仕様体系ではないためコピー元にはしない。v1.3 はローカル配備 batch の初版仕様とする。v1.2 はデプロイ準備レポートであり正式な `.document/v1.2/` 仕様セットではない。

## 仕様書変更一覧
|仕様書|状態|変更概要|関連仕様ID|
|---|---|---|---|
|[01_差分仕様.md](./01_差分仕様.md)|ADD|ローカル配備機能を追加|BAT-LOCAL-EXEC-001〜BAT-LOCAL-ACC-001|
|[02_概要・対象範囲.md](./02_概要・対象範囲.md)|ADD|目的・範囲を定義|BAT-LOCAL-SCOPE-001|
|[03_実行仕様.md](./03_実行仕様.md)|ADD|Git Bash手動実行を定義|BAT-LOCAL-EXEC-001|
|[04_入出力仕様.md](./04_入出力仕様.md)|ADD|リポジトリ入力とApache出力を定義|BAT-LOCAL-IN-001,BAT-LOCAL-OUT-001|
|[05_処理・データ仕様.md](./05_処理・データ仕様.md)|ADD|コピー・Apache確認・HTTP確認を定義|BAT-LOCAL-PROC-001〜003|
|[06_外部連携・ファイル構成.md](./06_外部連携・ファイル構成.md)|ADD|Windows/Git Bash/Apache構成を定義|BAT-LOCAL-FILE-001|
|[07_セキュリティ・非機能.md](./07_セキュリティ・非機能.md)|ADD|本番非接触等を定義|BAT-LOCAL-SEC-001|
|[08_ログ・エラー・復旧.md](./08_ログ・エラー・復旧.md)|ADD|失敗時停止・復旧を定義|BAT-LOCAL-ERR-001|
|[09_図・受け入れ条件.md](./09_図・受け入れ条件.md)|ADD|処理図・受入条件を定義|BAT-LOCAL-ACC-001|
|[10_未決事項・変更履歴.md](./10_未決事項・変更履歴.md)|ADD|未決事項なし・履歴を記録|BAT-LOCAL-HIST-001|

## 仕様ID対応
|仕様ID|概要|記載先|
|---|---|---|
|BAT-LOCAL-SCOPE-001|ローカル確認環境のみ対象|02|
|BAT-LOCAL-EXEC-001|pull後にGit Bashで手動実行|03|
|BAT-LOCAL-IN-001|develop作業ツリーを入力|04|
|BAT-LOCAL-OUT-001|Apache `htdocs/ryutai`へ出力|04|
|BAT-LOCAL-PROC-001|既存配置を更新して公開ファイルをコピー|05|
|BAT-LOCAL-PROC-002|Apache設定確認・必要時起動|05|
|BAT-LOCAL-PROC-003|HTTP疎通・ブラウザ起動|05|
|BAT-LOCAL-FILE-001|開発管理ファイルを公開先から除外|06|
|BAT-LOCAL-SEC-001|FTP・秘密情報・本番を変更しない|07|
|BAT-LOCAL-ERR-001|必須条件失敗時は非0終了|08|
|BAT-LOCAL-ACC-001|`http://localhost/ryutai/`で表示可能|09|
|BAT-LOCAL-HIST-001|v1.3変更履歴|10|
