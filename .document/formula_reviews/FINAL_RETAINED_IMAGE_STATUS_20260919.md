# Final Retained Image Status — 2026-09-19

## 結論

MPS source recovery後の最終残存画像状態を以下で固定する。

- 残存inline-image配置: **113**
- 非MPS残存配置: **112**
- MPS残存配置: **1**
- MPS欠損参照: **1**
- 未確認数式画像: **0**
- 非MPS残存112配置: **全件確認済み保持図 / 混在図 / グラフ / フローチャート**
- MPS `mps/mps_6_2.html -> image022.gif`: **SOURCE BLOCKED / HOLD**

## 基準

最新インベントリ:
- `.document/formula_reviews/SITE_INLINE_IMAGE_INVENTORY_20260918.md`

MPS正本回収・監査:
- `.document/formula_reviews/MPS_SOURCE_RECOVERY_AND_FORMULA_AUDIT_20260919.md`

MPS targeted Browser QA:
- `.document/formula_reviews/MPS_FINAL_BROWSER_QA_20260919.md`

## MPS更新

Libraryの `HP(1).7z` は、

**Library → Google Drive copy → raw-file download → libarchive extraction**

で回収・展開できた。

MPS 49参照のうち:
- **48式**: Word Equation.3 / Word-rendered sourceから回収しMathJax化
- **1式**: `mps_6_2/image022.gif` のみ正本未回収

元GIFバイナリ自体は7z内に存在しなかった。

Visio:
- `粒子法.vsd`
- `HP図.vsd`
- `公式.vsd`

も確認したが、image022と一対一対応を確定できる式は見つからなかった。

## 2026-09-19 追加厳密監査

回収したWord-rendered数式画像と現在のMathJax 48式を再照合した。

- source-recoverable formula: **48/48確認**
- 転記差検出: **1件**
  - `mps/mps_6_2.html`
  - `image020.gif`
  - 元Word: `\nabla^2 P_j^{k+1}`
  - 旧MathJax: `\nabla^2 P_i^{k+1}`
  - **元Wordどおり `P_j` に修正済み**
- 元資料に見える理論上不自然な添字・記法は、勝手に正規化せず保持する。

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
| MPS | **1** | **image022 / SOURCE BLOCKED / HOLD** |
| **全体** | **113** | |

## 最終判定

- 非MPS残存112配置: **FIXED / RETAIN**
- MPS回収可能48式: **RECOVERED / MATHJAX / SOURCE AUDITED**
- MPS image022: **SOURCE BLOCKED / HOLD**
- 実際の残存MPS `<img>`: **1**
- 追加の未確認数式画像: **0**

