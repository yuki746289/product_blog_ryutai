# Production Deployment Readiness — 2026-09-19

## Status

**READY FOR EXPLICIT PRODUCTION APPROVAL**

本番サイトへの書込みはまだ行っていない。

## 完了済み

- 厳密監査・通常ページ化: **612件**
  - 従来: 564
  - MPS追加: 48
- 全サイト最終Browser QA: **PASS WITH MPS IMAGE022 HOLD**
  - 205 HTML pages
  - baseline desktop 205/205
  - baseline mobile 205/205
  - baseline 410 checks
  - hard failure 0
  - MathJax errors 0
  - unrendered 0
  - page overflow 0
  - uncontained overflow 0
  - non-MPS missing images 0
- MPS source recovery:
  - 元参照 49
  - Word正本回収 / MathJax化: **48**
  - source re-audit: **48/48**
  - 実残存欠損: **image022 1件のみ**
- 残存画像最終固定:
  - 非MPS 112配置 = 全件確認済み保持図
  - MPS 1配置 = image022 SOURCE BLOCKED / HOLD
  - 全残存inline-image配置 = **113**
  - 未確認数式画像 = 0
- FTPS能力:
  - 過去に接続確認済み
  - 一時ファイルupload/delete確認済み

## 本番反映時の安全条件

1. 作業元は `develop`
2. `.document` / `.github` / `design_samples` は公開しない
3. 監査用 `*_mathjax_audit.html` / `*_reaudit.html` は公開しない
4. 本番Remote側の削除は行わない
5. HTML/CSS/JS/img等の公開資産のみ上書き
6. `mps_6_2/image022.gif` は正本未回収のため推測生成しない
7. 配備後に公開URLでスモークテスト
8. PC/mobileでMathJax・横スクロール・欠損画像を再確認

## 現時点の保留理由

過去の運用ルールで、本番反映は明示承認後のみとされている。
そのため、この時点ではFTP/FTPSへの本番書込みは実施しない。

## 本番反映後の完了条件

- FTPS upload success
- 公開トップページ HTTP 200
- 主要カテゴリページ HTTP 200
- MathJax表示確認
- PC/mobile表示確認
- MPS既知 `image022.gif` 1件以外の欠損画像 0
- 公開サイトのpage overflow 0
