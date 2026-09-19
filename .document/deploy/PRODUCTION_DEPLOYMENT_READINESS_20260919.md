# Production Deployment Readiness — 2026-09-19

## Status

**BLOCKED — SOURCE-FIDELITY REVALIDATION REQUIRED**

本番サイトへの書込みはまだ行っていない。
2026-09-20に数式の元画像忠実性（改行・配置）と文字コード整合性の仕様を修正したため、旧Browser QA PASSはデプロイ判定には使用しない。
再検証完了まで本番デプロイを禁止する。

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
- status: **REVALIDATION IN PROGRESS**

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
- 本番書込み: **未実施**

## Deploy前整合確認

- 引継ぎ時HEAD `c080be9f6e289ba92bf652e41781ee4828e336ca` 以降、今回のQA修正・再実行による変更は `.document` 内のみ。
- 公開対象（HTML / CSS / JS / img等）の追加変更: **0件**
- QAスクリプト・QAトリガー・QAレポート・本デプロイ準備台帳は公開対象外。
- 本番FTPS書込み: **未実施**

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
- [ ] 2026-09-20 source-fidelity再検証 PASS
- [x] 残存画像インベントリ更新
- [x] 監査台帳更新
- [x] デプロイ対象外パス確認方針
- [x] 最新FTPS read-only接続確認
- [ ] **ユーザーの本番デプロイ明示承認**
- [ ] FTPS本番upload
- [ ] 公開サイトsmoke test

## 現在位置

**再検証中。デプロイ不可。**

次の操作は再検証結果の確認・必要箇所の修正であり、本番FTPS書込みではない。
