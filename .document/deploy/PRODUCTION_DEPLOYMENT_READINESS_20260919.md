# Production Deployment Readiness — 2026-09-19

## Status

**PRODUCTION DEPLOYED — VERIFIED**

本番サイトへのFTPS反映を2026-09-20に実施し、公開後検証まで完了した。
2026-09-20に数式の元画像忠実性（改行・配置）と文字コード整合性の仕様を修正し、再検証を完了した。
最新Browser QA / source-fidelity / operator-alignment audit はすべてPASS。

## 完了済み

### Formula conversion / audit

- source-exact / source-recovered: **633**
- user-approved inferred reconstruction: **1**
- operational MathJax total: **634**
- formula pages: **95**
- unresolved HOLD: **0**
- MPS MathJax: **49/49**
  - source-exact / recovered: **48**
  - inferred reconstruction: **1**
- MPS residual formula images: **0**

MPS `mps/mps_6_2.html` の former `image022.gif` は正本未回収のため、
`data-source-status="inferred-reconstruction"` として他の48式と区別している。

旧「564式」は旧スコープの履歴値であり、現行634式とは単純比較しない。

### Residual images

- residual inline-image placements: **112**
- all 112 are confirmed retained non-formula images
- MPS residual images: **0**
- missing referenced assets: **0**
- unreviewed formula images: **0**

### Source-fidelity revalidation (2026-09-20)

- canonical spec: `.document/formula_reviews/SOURCE_FIDELITY_SPEC_20260920.md`
- required encoding: UTF-8 bytes + UTF-8 declarations
- automatic MathJax line breaking: prohibited for source-faithful formulas
- responsive rule: preserve source line structure; use local horizontal scroll when needed
- status: **PASS**
- source-fidelity certification: **PASS**
- operator alignment audit: **606 math blocks / 0 issues**
- shared desktop content width: **1080px max**
- latest full-site QA run: `35491138623`
- latest QA trigger head: `a6e4352f0fe65cf6345f742ba0de8c1ddb792cd3`
- normal HTML: **205 pages**
- desktop + mobile checks: **410**
- hard failures: **0**
- desktop formula-local scroll: **1 formula / 1 page** (`fem/fem_5.html`)
- mobile formula-local scroll: **240 formula instances / 47 pages**
- page-wide overflow: **0**
- MathJax errors / unrendered / page errors / charset / mojibake / missing images: **all 0**

### Previous Browser QA (historical; not sufficient for deployment)

Final full-site QA:
- run: `35446925022`
- source head at trigger: `04b3f060b585023987bdfdc657bf6bac30f44673`
- HTML: **205 pages**
- desktop: **205/205**
- mobile: **205/205**
- checks: **410**
- hard failures: **0**
- page errors: **0**
- MathJax errors: **0**
- unrendered formulas: **0**
- page-wide horizontal overflow: **0**
- uncontained formula overflow: **0**
- non-MPS missing images: **0**
- MPS known missing references: **0**
- allowed local math scroll: **148**
- overall: **PASS**

QAでは外部広告・外部トラッカーを遮断し、ローカル公開資産とMathJax CDNを対象に確認した。
`pageerror` もhard failure条件に含めて再実行済み。

補足:
- 直前のrun `35446528245` はhard failure 0だったが、外部スクリプト由来の一過性 `pageerror: int64` が2件あった。
- 最終runでは外部広告/トラッカーを遮断し、`pageerror=0` を確認した。
- さらにその前のrun `35445949212` の全ページ `navigation` FAILは、QA内JavaScript正規表現の不具合による誤判定で、HTTP応答自体は200だった。QAコード修正後に再検証済み。

Final MPS delta QA:
- run: `35411325166`
- job: `105835730146`
- artifact: `10576893632`
- checks: **102**
- failures: **0**
- final `mps_6_2.html` desktop/mobile: **PASS**

### FTPS capability

- 最新read-only接続確認: **接続成功**
  - run: `35408141850`
  - job: `105836951290`
  - checkout: latest `develop`
  - `FTP_TLS.connect` / login / `PROT P` / passive mode: 成功
  - remote `/img` read access: 到達
  - remote write/delete: **なし**
- job conclusion自体はfailureだが、原因は旧スクリプトの「MPS画像参照49件」assert。
  - 現在の実測: **0件**
  - 接続処理完了後に `Expected 49 MPS references but parsed 0` で終了したもの。
  - workflowの期待値は **0件** へ修正済み。
- 一時ファイルupload/delete能力: 過去に確認済み
- 本番書込み: **実施済み**

## Deploy前整合確認

- 2026-09-20に公開HTML/CSSへ、UTF-8統一、source-faithful line break/alignment、共通本文幅1080pxの修正を反映済み。
- 公開変更は最新の全サイトBrowser QA / source-fidelity / operator-alignment auditで再検証済み。
- QAスクリプト・QAトリガー・QAレポート・本デプロイ準備台帳は公開対象外。
- 本番FTPS書込み: **実施済み**

## 本番反映時の安全条件

1. source branchは `develop`
2. `.document` / `.github` / `design_samples` は公開しない
3. audit / re-audit用HTMLは公開しない
4. 通常デプロイではRemote側の削除は行わない
5. 通常デプロイはHTML / HTM / CSS / JS / XML / TXTのみ上書きし、既存画像は再転送しない
6. image022は現在のユーザー承認済み推定復元MathJaxを使用
7. deploy後に公開URLでsmoke test
8. PC/mobileでMathJax・overflow・missing imageを再確認

## Deploy前チェック

- [x] develop反映
- [x] MPS 49式反映
- [x] MPS欠損画像0
- [x] 2026-09-20 source-fidelity再検証 PASS
- [x] 残存画像インベントリ更新
- [x] 監査台帳更新
- [x] デプロイ対象外パス確認方針
- [x] 最新FTPS read-only接続確認
- [x] **ユーザーの本番デプロイ明示承認**
- [x] FTPS本番upload
- [x] 公開サイトsmoke test

## 現在位置

**本番デプロイ完了。**

- Production workflow run: `35494354501`
- text/web assets uploaded: **316 / 316**
- remote size verification: **316 / 316**
- image upload: **0**
- remote deletion: **0**
- HTTP content smoke: **PASS**
- production browser smoke: **PASS** (5 pages × desktop/mobile = 10 checks)

### 旧ページ `/old/` 最終構成

- source: `release_1.0.0`
- legacy text assets: HTML / HTM / CSS / JS / XML / TXTのみ `/old/` に配置
- images: `/old/img/` を保持せず、現行 `/img/` を共用
- PDFs: 現行 `/pdf/` を共用
- duplicated `/old/img/`: **削除済み**
- `mps/mps_1.html` の旧数式画像1件は正本画像がrepository/共通assetに無いため、**新規画像を作らずMathJax表示**
- final old-site workflow run: `35496891008`
- HTTP verification: **PASS**
- desktop/mobile browser smoke: **PASS**
