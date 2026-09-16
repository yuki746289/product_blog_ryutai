# deploy_local v1.3 要件定義書

## 1. 目的・背景
Git Bashで更新した `develop` のサイトをローカルApacheへ反映し、`http://localhost/ryutai/` で確認できるようにする。

## 2. 対象範囲
- [ADD] Git Bash用ローカル配備スクリプト。
- [ADD] `C:\server\Apache24\htdocs\ryutai` への静的ファイルコピー。
- [ADD] Apache設定確認、必要時起動、HTTP疎通、既定ブラウザ起動。

## 3. 対象外
- [KEEP] 本番FTPは変更しない。
- [KEEP] サイト本文・数式・CSS等は変更しない。
- [KEEP] Apache設定ファイルは自動変更しない。

## 4. 入力要件
- 事前にGit Bashで `develop` を `git pull --ff-only origin develop` 済みであること。
- 実行位置に依存せず、スクリプト位置からrepoRootを解決すること。
- `index.html` が存在すること。

## 5. 出力要件
- `C:\server\Apache24\htdocs\ryutai` に公開ファイルを配置する。
- 開発管理ファイルを公開先へコピーしない。
- ログは標準出力/標準エラーへ出す。

## 6. 実行要件
- 手動実行: `bash deploy_local.sh`
- 再実行可能。
- 必須条件エラー時は非0終了。
- 作業ツリーdirtyは警告のみ。

## 7. 制約条件
- Windows + Git Bash。
- Apache root既定値 `/c/server/Apache24`。
- URL既定値 `http://localhost/ryutai/`。
- コピーで文字コードを変換しない。

## 8. 受入条件
- [ ] rootの `deploy_local.sh` を `bash deploy_local.sh` で実行できる。
- [ ] `htdocs/ryutai/index.html` が生成される。
- [ ] `.git/.github/.document/.rules` が公開先に無い。
- [ ] Apache config test成功。
- [ ] local URLがHTTP成功。
- [ ] ブラウザ起動を試行する。
- [ ] 本番FTP操作なし。

## 9. 未決事項
なし。
