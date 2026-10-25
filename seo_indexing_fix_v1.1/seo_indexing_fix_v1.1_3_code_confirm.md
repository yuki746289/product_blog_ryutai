# SEOインデックス停滞修正 v1.1 - コード確認

## 総合判定
**PASS（develop修正完了 / 本番FTP反映・公開後検証完了）**

## 確認対象
- `seo_indexing_fix_v1.1_1_request.md`
- `.github/workflows/production-ftps-deploy.yml`
- `.github/workflows/production-old-site-ftps-deploy.yml`
- `robots.txt`

## 要件一致
- sitemap掲載ページへのself canonical付与: PASS
- `/old/` HTMLへの `noindex,follow` 付与: PASS
- `/old/` をrobotsでブロックしない: PASS
- sitemap URLをrobots.txtに明示: PASS
- 本文・数式・URL・画面レイアウトを変更しない: PASS
- 本番デプロイトリガーを変更しない: PASS

## 正常系確認
- sitemap.xml: 181 URL
  - HTML URL: 180
  - トップURL: 1（`index.html`へ対応）
- sitemap 181 URLに対応するdevelop上の実ファイル: 181/181
- release_1.0.0の旧HTML: 295件
- 旧HTML295件の現行側対応パス: 295/295
- canonical/noindexの正規表現・挿入ロジック単体smoke: PASS

## 異常系・境界値
- sitemapに想定外scheme/hostがあればFTP前に停止する。
- sitemap掲載HTMLがcheckoutに存在しなければFTP前に停止する。
- sitemap掲載HTMLに`</head>`がなければFTP前に停止する。
- 既存canonicalが期待URLと競合する場合はFTP前に停止する。
- old HTMLに`</head>`がなければFTP前に停止する。
- old stagingのHTML件数とnoindex付与件数が一致しなければFTP前に停止する。
- old HTTP smokeのnoindex確認はHTML/HTMのみに限定し、CSS等を誤判定しない。

## デグレ確認
基準commit `9692e6207542b264a78f51efbb1e852d76b20c60` からの差分は以下のみ。
- production FTPS workflow
- production old-site FTPS workflow
- robots.txt
- quick-fix記録

通常HTML本文、数式、sitemap.xml、デプロイトリガーには変更なし。

## コーディング規約確認
参照:
- `.rules/dev/rules_dev_other.md`
- `.rules/dev/quick_fix/rules_quick_fix_2_code.md`
- `.rules/dev/quick_fix/rules_quick_fix_3_code_confirm.md`

判定:
- 参照URL/タグ整合: PASS
- 無関係な整形: なし
- 文字コード変更: なし
- HTML/CSS/JSのID/DOM/レイアウト変更: 対象外
- 追加コードのインデント: 既存YAML/Python形式に準拠、タブ追加なし

## 本番反映結果
ユーザーの明示承認後、2026-10-25に本番反映を実施した。

- 現行サイト Production FTPS Deploy: run `40192883478` / SUCCESS
  - SEO metadata preparation: PASS
  - FTPS upload: PASS
  - HTTP content smoke: PASS
  - PC/mobile browser smoke: PASS
- 旧サイト Production Old Site FTPS Deploy: run `40192886915` / SUCCESS
  - legacy publish staging + noindex: PASS
  - FTPS upload: PASS
  - HTTP verification: PASS
  - old-site browser smoke: PASS

本番確認済み:
- root `robots.txt` の sitemap 宣言
- 現行代表ページの self canonical
- `/old/` 代表HTMLの `noindex,follow`
