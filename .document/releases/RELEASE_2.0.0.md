# Release 2.0.0 — 2026-09-20

## Summary

流体ブログの全面リニューアル版。レスポンシブ化、ナビゲーション再構成、数式のMathJax化、文字コード統一、数式レイアウト監査、本番デプロイ方式の整理を完了した。

## Major changes

- PC / smartphone responsive layout
- desktop content width: 1080px max
- desktop mega menu / mobile navigation
- font-size selector: 普通 / 大 / 特大
- homepage renewal notice and updated revision history
- MPS navigation publication
- UTF-8 normalization
- MathJax source-faithful formula rendering
  - source-exact / recovered: 633
  - user-approved inferred reconstruction: 1
  - operational canonical formula slots: 634
  - unresolved HOLD: 0
- formula outer spacing: 18pt
- multi-line top-level formula row spacing: 6pt
- automatic MathJax line breaking disabled
- operator alignment audit: PASS
- source-fidelity certification: PASS
- full browser QA: PASS

## Production deployment

- production deploy run: `35494354501`
- text/web assets uploaded and verified: 316 / 316
- production HTTP smoke: PASS
- production desktop/mobile browser smoke: PASS
- generated images: 0
- normal production deploy image upload: 0
- remote delete during normal production deploy: 0

## Legacy site

The previous `release_1.0.0` site is available under `/old/`.

- only legacy HTML / HTM / CSS / JS / XML / TXT are stored under `/old/`
- images are shared from the current `/img/`
- PDFs are shared from the current `/pdf/`
- duplicated `/old/img/` was removed
- legacy file encodings are preserved
- one missing legacy MPS formula image is not regenerated; that formula is rendered with MathJax
- final old-site deployment / verification run: `35496891008`
- HTTP verification: PASS
- desktop/mobile browser smoke: PASS

## Release branch

- previous release: `release_1.0.0`
- current release: `release_2.0.0`
- source branch: `develop`
