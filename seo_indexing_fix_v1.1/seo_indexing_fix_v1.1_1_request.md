# SEOインデックス停滞修正 v1.1 - 修正内容の要件

## 修正概要
Search Consoleでsitemap掲載URLが約180件認識されている一方、インデックスが約40件で停滞している問題について、旧サイト `/old/` との重複競合とcanonical不足をSEOメタ情報で補正する。

## 修正対象
- `.github/workflows/production-ftps-deploy.yml`
- `.github/workflows/production-old-site-ftps-deploy.yml`
- `robots.txt`

## 現在の問題点
- 現行ページに明示的なself canonicalがない。
- `/old/` に旧版HTMLが公開され、Google検索結果にも旧URLが残っている。
- 旧ページに検索除外指定がなく、新旧URLの重複評価が発生している。
- rootに `robots.txt` がなく、sitemapの場所を明示していない。

## 修正方針
1. 現行サイトのデプロイ時に、sitemap.xml掲載HTMLへ絶対URLのself canonicalを付与する。
2. 旧 `/old/` サイトのデプロイ時に、全HTMLへ `<meta name="robots" content="noindex,follow">` を付与する。
3. `/old/` はrobots.txtでDisallowしない。Googlebotがnoindexを読める状態を維持する。
4. root `robots.txt` に全体Allowとsitemap URLを記載する。
5. 本文、数式、既存URL、画面レイアウトは変更しない。
6. 本番デプロイトリガーファイルは変更しない。

## 影響範囲
検索エンジン向けメタ情報のみ。ユーザー向け本文・表示・URL構造・数式には影響しない。

## 実装可能性
既存のFTPSデプロイワークフローには公開前処理用Pythonが存在するため、同じデプロイ工程内でメタタグを付加できる。旧releaseブランチ自体を変更する必要はない。

## 簡易開発として扱う理由
既存の公開仕様・URL・本文を変更せず、既存デプロイ処理へSEOメタ情報の補正を追加する小規模な不具合修正である。

## 動作確認方針
- sitemap掲載HTMLへのcanonical付与件数と欠落0件をデプロイ前処理で検証する。
- old公開対象HTMLへのnoindex付与件数と欠落0件をデプロイ前処理で検証する。
- 本番HTTP smokeでcanonical、robots.txt、old noindexを確認する。
- 本番FTP反映は別途ユーザーの明示承認後のみ行う。

## ユーザー承認
2026-10-25、修正方針提示後にユーザーから「承認」を受領済み。
