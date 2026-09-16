# deploy_local v1.3 最終確認

確認日: 2026-09-16
対象ブランチ: `develop`
判定: **実装完了 / Windows実機受入待ち**

## 確認対象
- `.document/v1.3/00_index.md`〜`10_未決事項・変更履歴.md`
- `.document/v1.3/99_仕様確認.md`
- `deploy_local_v1.3_3_request.md`
- `deploy_local_v1.3_4_base.md`
- `deploy_local_v1.3_5_base_confirm.md`
- `deploy_local_v1.3_6_detail.md`
- `deploy_local_v1.3_6_detail.json`
- `deploy_local_v1.3_7_detail.json`
- `deploy_local_v1.3.sh`
- root運用入口 `deploy_local.sh`
- `deploy_local_v1.3_9_code_confirm.md`

## 最終確認項目
- [x] 全仕様IDが要件・設計へ反映されている。
- [x] v1.3仕様書11件と仕様確認結果を確認した。
- [x] ADD仕様が要件・設計・コードへ追跡可能。
- [x] サイト既存本文・数式・CSS等を本作業で変更していない。
- [x] 実行前の `git pull --ff-only origin develop` とスクリプト責務を分離した。
- [x] 配置先は `C:\server\Apache24\htdocs\ryutai` で、Apache root直下ではない。
- [x] 開発管理物のコピー除外を実装した。
- [x] Apache設定テスト、必要時起動、HTTP確認、ブラウザ起動試行を実装した。
- [x] 本番FTPへの接続・変更処理は存在しない。
- [x] 自動テスト run `35062679397` が成功した。
- [x] 疑似Apache環境で2回連続実行し、コピー・HTTP・冪等性を確認した。
- [ ] ユーザPCの `C:\server\Apache24` で実行し、`http://localhost/ryutai/` を実ブラウザ表示する。

## 仕様・実装整合
|項目|仕様|実装|判定|
|---|---|---|:---:|
|実行|Git Bash手動|`bash deploy_local.sh`|OK|
|入力|pull済みdevelop|branch検証・作業ツリー使用|OK|
|出力|`htdocs/ryutai`|targetDir既定値に実装|OK|
|除外|開発管理物を非公開|tar exclude|OK|
|Apache|設定確認・必要時起動|`httpd.exe -t` + 起動処理|OK|
|HTTP|localUrl確認|curl|OK|
|ブラウザ|既定ブラウザ起動試行|`cmd.exe //C start`|実機確認待ち|
|本番|FTP非接触|FTP処理なし|OK|

## 残作業
ユーザPCのGit Bashで以下を実行する。

```bash
cd /c/Users/yuki_/OneDrive/Documents/github/product_blog_ryutai
git checkout develop
git pull --ff-only origin develop
bash deploy_local.sh
```

成功時は `http://localhost/ryutai/` が自動で開く。自動起動しない場合もURLがログ表示されるので手動で開ける。

**最終状態: コード・自動検証は完了。Windows実機受入結果の確認後にv1.3を完全合格とする。**
