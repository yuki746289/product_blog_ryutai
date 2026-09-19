# Final Site Browser QA — 2026-09-19

## 結論

**PASS WITH KNOWN MPS IMAGE022 HOLD**

全サイト基準QAと、MPS source recovery後のMPS専用QAを組み合わせた最新判定。

- 対象HTML: **205ページ**
- baseline full-site desktop: **205/205**
- baseline full-site mobile: **205/205**
- baseline総チェック: **410**
- baseline hard failure rows: **0**
- MPS recovery後 targeted QA: **MPS 7ページ / desktop+mobile PASS**
- 本番FTP/FTPS反映: **未実施**

## 実行条件

- Browser: Chromium / Playwright
- desktop: 1440×1000
- mobile: 390×844
- GitHub Actions run: `35411325166`

MPS source recovery後は、MPS 7ページを別途確認している。
最新の `mps_6_2.html` 修正後確認:
- job: `105827914216`
- artifact: `10576437193`
- shard checks: **102**
- shard failures: **0**

## 全体結果

| 項目 | 結果 |
|---|---:|
| HTMLページ | 205 |
| baseline QAチェック | 410 |
| Hard failure | **0** |
| MathJax errors | **0** |
| Unrendered | **0** |
| Page overflow | **0** |
| Uncontained overflow | **0** |
| Page errors | **0** |
| MathJax console errors | **0** |
| 非MPS欠損画像 | **0** |

長い数式の `.math-block` 内横スクロールは許容し、ページ全体の横スクロールは不可とする。

## MPS最新状態

Libraryの `HP(1).7z` を回収・展開し、MPS 49参照を再監査した。

| 項目 | 件数 |
|---|---:|
| MPS元参照 | 49 |
| Word正本から回収 | **48** |
| MathJax反映 | **48** |
| source re-audit | **48/48** |
| 実際に残るMPS `<img>` | **1** |
| SOURCE BLOCKED / HOLD | **1** |

唯一のHOLD:
- `mps/mps_6_2.html`
- `img/mps_fluid_count.files/image022.gif`

`data-source-image` 属性に残る旧GIFパスは監査用メタデータであり、残存表示画像としては数えない。

## MPS postfix QA

`image020` の転記差を元Wordどおり修正後、`mps_6_2.html` を含む最新Shardを再実行した。

Desktop / mobile ともに:
- HTTP 200
- MathJax errors 0
- unrendered 0
- page overflow 0
- uncontained 0
- missing imageは `image022.gif` 1件のみ
- issues 0

詳細:
- `.document/formula_reviews/MPS_FINAL_BROWSER_QA_20260919.md`

## 判定

- MPS image022以外のhard failure: **0**
- MathJax errors: **0**
- unrendered: **0**
- page overflow: **0**
- uncontained overflow: **0**
- PC/mobile表示QA: **PASS**
- 非MPS欠損画像: **0**

**全サイト最終Browser QAは、MPS image022 1件HOLDを明示した上で完了。**
