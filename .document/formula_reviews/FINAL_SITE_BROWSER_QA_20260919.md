# Final Site Browser QA — 2026-09-19

## 結論

**PASS WITH KNOWN MPS HOLD**

最新 `develop` を対象に、全HTML 205ページを Chromium / Playwright で desktop / mobile の2 viewportに分けて確認した。

- 対象HTML: **205ページ**
- desktop: **205/205**
- mobile: **205/205**
- 総チェック: **410**
- hard failure rows: **0**
- 本番FTP/FTPS反映: **未実施**

## 実行条件

- Browser: Chromium / Playwright
- desktop: 1440×1000
- mobile: 390×844
- Shard: 4分割
- GitHub Actions run: `35411325166`
- 修正版QAでは既存の個別Browser QAと同じoverflow判定を使用

### overflow判定

- ページ全体の横スクロール: 不可
- 長い数式の `.math-block` 内横スクロール: 許容
- `.math-block` が横幅超過していて、`overflow-x:auto/scroll` でない場合のみ uncontained と判定

## 全体結果

| 項目 | 結果 |
|---|---:|
| HTMLページ | 205 |
| QAチェック | 410 |
| Hard failure | **0** |
| MathJax errors | **0** |
| Unrendered | **0** |
| Page overflow | **0** |
| Uncontained overflow | **0** |
| Page errors | **0** |
| MathJax console errors | **0** |
| 非MPS欠損画像 | **0** |
| 許容された `.math-block` local scroll | 146 |

`local scroll` は長い数式を `.math-block` 内だけで横スクロール可能にする既定仕様であり、hard failureではない。

## MPS SOURCE BLOCKED / HOLD

MPSの欠損画像は既知HOLDとして扱い、最終QAの失敗には含めない。

| ページ | 既知欠損 | QA実測 |
|---|---:|---:|
| `mps/mps_1.html` | 1 | 1 |
| `mps/mps_2.html` | 1 | 1 |
| `mps/mps_3.html` | 12 | 12 |
| `mps/mps_4.html` | 9 | 9 |
| `mps/mps_5.html` | 2 | 2 |
| `mps/mps_6_1.html` | 2 | 2 |
| `mps/mps_6_2.html` | 22 | 22 |
| **合計** | **49** | **49** |

MPS 49参照は元画像正本が未回収のため、引き続き **SOURCE BLOCKED / HOLD** とする。推測によるMathJax化は行わない。

## 初回QAの誤検出

初回runではmobile側の多数のページで `uncontained` を誤検出した。

原因:
- 全DOM要素のbounding boxを対象にしていたため、レスポンシブレイアウト内部の要素まで異常として計上していた。

修正:
- 既存の認証済み個別Browser QAと同じ方式へ変更。
- `.math-block` の `scrollWidth > clientWidth` の場合だけ確認。
- `overflow-x:auto/scroll` ならlocal scrollとして許容。
- それ以外のみuncontainedとして失敗扱い。

修正版の4Shardはすべて **success**。

## 判定

- MPS既知HOLD以外のhard failure: **0**
- MathJax errors: **0**
- unrendered: **0**
- page overflow: **0**
- uncontained overflow: **0**
- PC/mobile表示QA: **PASS**
- 非MPS欠損画像: **0**

したがって、**全サイト最終Browser QAは完了**とする。
