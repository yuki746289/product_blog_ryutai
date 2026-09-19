# Production Deployment Readiness — 2026-09-19

## Status

**READY FOR EXPLICIT PRODUCTION APPROVAL**

本番サイトへの書込みはまだ行っていない。
ユーザー指定どおり、デプロイ手前で停止する。

## 完了済み

### Formula conversion / audit

- 従来のsource-exact監査: **564**
- MPS source-exact / recovered: **48**
- source-exact / recovered subtotal: **612**
- MPS user-approved inferred reconstruction: **1**
- reflected formula/formula-text total: **613**
- MPS MathJax: **49/49**
- MPS residual formula images: **0**
- MPS HOLD: **0**

image022は正本未回収のため、
`data-source-status="inferred-reconstruction"` として他の48式と区別している。

### Residual images

- residual inline-image placements: **112**
- all 112 are confirmed retained non-formula images
- MPS residual images: **0**
- missing referenced assets: **0**
- unreviewed formula images: **0**

### Browser QA

Baseline full-site:
- HTML: **205 pages**
- desktop: **205/205**
- mobile: **205/205**
- checks: **410**
- hard failures: **0**

Final MPS delta QA:
- run: `35411325166`
- job: `105835730146`
- artifact: `10576893632`
- checks: **102**
- failures: **0**
- final `mps_6_2.html` desktop/mobile: **PASS**
- MathJax errors: **0**
- unrendered: **0**
- missing images: **0**
- page overflow: **0**

### FTPS capability

- FTPS接続: 過去に確認済み
- 一時ファイルupload/delete: 過去に確認済み
- 本番書込み: **未実施**

## 本番反映時の安全条件

1. source branchは `develop`
2. `.document` / `.github` / `design_samples` は公開しない
3. audit / re-audit用HTMLは公開しない
4. Remote側の削除は行わない
5. HTML / CSS / JS / img等の公開資産のみ上書き
6. image022は現在のユーザー承認済み推定復元MathJaxを使用
7. deploy後に公開URLでsmoke test
8. PC/mobileでMathJax・overflow・missing imageを再確認

## Deploy前チェック

- [x] develop反映
- [x] MPS 49式反映
- [x] MPS欠損画像0
- [x] 最終Browser QA PASS
- [x] 残存画像インベントリ更新
- [x] 監査台帳更新
- [x] デプロイ対象外パス確認方針
- [ ] **ユーザーの本番デプロイ明示承認**
- [ ] FTPS本番upload
- [ ] 公開サイトsmoke test

## 現在位置

**デプロイ直前。**

次の操作は本番FTPS書込みになるため、ここでは実施しない。
