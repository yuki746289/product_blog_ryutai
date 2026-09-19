# MPS Final Browser QA — 2026-09-19

- Overall: **PASS WITH IMAGE022 HOLD**
- Scope: MPS 7 pages only
- Formula replacements: **48**
- Known HOLD: **mps/mps_6_2.html image022.gif only**
- GitHub Actions run: `35411325166`
- Latest mps_6_2 shard: `qa-shard-1` job `105827914216`
- Latest shard artifact: `10576437193`
- Latest shard result: **102 checks / failures 0**

## Final MPS page result

| Page | Viewport | Formula | MathJax | Unrendered | Overflow | Uncontained | MPS img | Missing |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| mps/mps_1.html | desktop | 1/1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_2.html | desktop | 1/1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_3.html | desktop | 12/12 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_4.html | desktop | 9/9 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_5.html | desktop | 2/2 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_6_1.html | desktop | 2/2 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_6_2.html | desktop | 21/21 | 0 | 0 | 0 | 0 | 1 | 1 |
| mps/mps_1.html | mobile | 1/1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_2.html | mobile | 1/1 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_3.html | mobile | 12/12 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_4.html | mobile | 9/9 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_5.html | mobile | 2/2 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_6_1.html | mobile | 2/2 | 0 | 0 | 0 | 0 | 0 | 0 |
| mps/mps_6_2.html | mobile | 21/21 | 0 | 0 | 0 | 0 | 1 | 1 |

## Post-correction verification

`mps/mps_6_2.html` の `image020` 相当式を元Wordどおり
`\\nabla^2P_j^{k+1}` に修正後、同ページを含む最新 `qa-shard-1` を再実行した。

Desktop / mobile ともに:

- HTTP: **200**
- MathJax errors: **0**
- unrendered: **0**
- page overflow: **0**
- uncontained overflow: **0**
- page errors: **0**
- console errors: **0**
- missing image: **image022.gif 1件のみ**
- issues: **0**

**判定: MPS表示QA完了。**
