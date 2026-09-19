# Formula Strict Re-audit Final Summary — 2026-09-19

## Overall status

**COMPLETE**

旧564式監査とは分離し、元画像 / 回収Word数式 / MathJax完成描画を用いた新厳密再監査として完了した。

## Formula totals

| 区分 | 数式数 | 備考 |
|---|---:|---|
| source-exact / source-recovered | **633** | 元画像または回収できた内部正本に基づく |
| inferred reconstruction | **1** | MPS `mps_6_2/image022`。ユーザー承認済み・明示ラベル付き |
| operational MathJax total | **634** | Browser QA対象として全件表示確認 |

### Category breakdown

| カテゴリ | 数式数 | 状態 |
|---|---:|---|
| FEM | 235 | COMPLETE |
| Heat | 94 | COMPLETE |
| Hydronamics | 131 | COMPLETE |
| Physics | 49 | COMPLETE |
| Appendix / Column / Mesh | 76 | COMPLETE |
| MPS | 49 | COMPLETE（48 source-exact + 1 inferred） |
| Counting | 0 | COMPLETE（フローチャート2枚保持） |

## Quality rules applied

- 元HP画像を最終正本とする。
- Word数式は高速な転記・比較元として利用する。
- 既存LaTeXは差分再利用する。
- 元画像 ↔ MathJax完成描画を直接比較する。
- `t/τ`, `i/j`, 大小文字、添字、上付き、`∂/d`, `+/-` を重点確認する。
- 理論的に不自然でも、正本で確認できる表記は推測修正しない。
- MPS image022のみ正本未回収のため、ユーザー承認済み推定復元として source-exact と区別する。

## Browser QA

- MathJax errors: 0（最終QA対象）
- unrendered formulas: 0
- uncontained formula overflow: 0
- page-wide horizontal overflow: 0
- Counting retained flowcharts: broken 0
- MPS residual formula images: 0

## MPS special note

MPS 49式のうち48式は回収Word Equation.3を内部正本として再監査済み。
`mps/mps_6_2.html -> image022.gif` のみ元GIF / Word Equation / Visioから正本を回収できなかった。

この1式は:
- source-exact: NO
- inferred reconstruction: YES
- user-approved: YES
- HTML metadata: `data-source-status="inferred-reconstruction"`
- Browser QA: PASS

## Final status

**新厳密再監査の実作業は完了。**
本番FTP/FTPS反映は本レポートの対象外。
