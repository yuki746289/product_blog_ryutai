# Final Retained Image Status — 2026-09-19

## 結論

最終残存画像状態を以下で固定する。

- 残存inline-image配置: **161**
- 非MPS残存配置: **112**
- MPS欠損参照: **49**
- 未確認数式画像: **0**
- 非MPS残存112配置: **全件確認済み保持図 / 混在図 / グラフ / フローチャート**
- MPS 49参照: **SOURCE BLOCKED / HOLD**

## 基準

基礎インベントリ:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.md`

最新全サイトBrowser QA:
- `.document/formula_reviews/FINAL_SITE_BROWSER_QA_20260919.md`

Browser QAでは、非MPS欠損画像 **0**、MPS欠損は既知49参照と完全一致した。

## カテゴリ別最終状態

| セクション | 残存配置 | 最終分類 |
|---|---:|---|
| FEM | 33 | 全件確認済み保持図・混在図 |
| Mesh | 23 | 全件確認済み保持図・グラフ・結果画像 |
| Hydronamics | 21 | 全件確認済み保持図 |
| Physics | 16 | 全件確認済み保持図・説明図・混在図 |
| Appendix | 9 | 全件確認済み保持図・混在図 |
| Heat | 8 | 全件確認済み保持図・模式図 |
| Counting | 2 | フローチャート |
| **非MPS合計** | **112** | **未確認数式画像 0** |
| MPS | 49 | **欠損参照 / SOURCE BLOCKED / HOLD** |
| **全体** | **161** |  |

## 非MPS 112配置

既知数式画像のMathJax化完了後に残った非MPS画像は、カテゴリ別最終監査で全件確認済み。

- FEM: 33/33
- Mesh: 23/23
- Hydronamics: 21/21
- Physics: 16/16
- Appendix: 9/9
- Heat: 8/8
- Counting: 2/2

これらは数式単体画像として変換すべき対象ではなく、図・模式図・グラフ・結果画像・説明図・混在図・フローチャートとして画像維持する。

## MPS 49参照

| ページ | 欠損数 |
|---|---:|
| `mps/mps_1.html` | 1 |
| `mps/mps_2.html` | 1 |
| `mps/mps_3.html` | 12 |
| `mps/mps_4.html` | 9 |
| `mps/mps_5.html` | 2 |
| `mps/mps_6_1.html` | 2 |
| `mps/mps_6_2.html` | 22 |
| **合計** | **49** |

GitHub / 本番FTPS / HTTP / Wayback等から正本を回収できていないため、引き続き **SOURCE BLOCKED / HOLD**。

元画像またはWord原稿を正本として取得できるまで、推測による式復元・MathJax化は行わない。

## 最終判定

- 非MPS残存112配置: **FIXED / RETAIN**
- MPS 49参照: **FIXED / SOURCE BLOCKED / HOLD**
- 未確認数式画像: **0**
- 追加の画像分類作業: **不要**
