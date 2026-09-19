# MPS image022 Final Investigation — 2026-09-19

## 結論

`mps/mps_6_2.html -> img/mps_fluid_count.files/image022.gif` は、
内部正本を最終的に回収できなかったため **SOURCE BLOCKED / HOLD** とする。

推測・一般論・外部文献だけを根拠に通常HTMLへ数式を追加しない。

## 1. Archive full extraction

Libraryの `HP(1).7z` を以下の経路で取得した。

1. Library → Google Drive temporary copy
2. Google Drive raw-file download
3. system `libarchive.so` で展開

Archive:
- compressed size: **30,415,485 bytes**
- extracted files: **2,010**
- extracted byte volume: 約 **645 MB**

全展開後の `HP/source/img/` を確認したが、
以下MPS画像ディレクトリは存在しなかった。

- `mps_weight.files`
- `mps_num.files`
- `mps_nabra.files`
- `mps_dot.files`
- `mps_rap.files`
- `mps_fluid_eq.files`
- `mps_fluid_count.files`

従って、元GIFバイナリはarchiveに含まれていない。

## 2. Original HTML / BAK

`HP/source/mps/mps_6_2.html` と `.BAK` はともに、

> ここで、圧力の勾配モデルは数値安定性のため、次式を使用します。

の直後に

`img/mps_fluid_count.files/image022.gif`

を参照するだけで、式内容そのものはHTMLに残っていない。

width / height / alt / title等、式を復元できる追加属性もない。

## 3. Word source

対象:
- `HP/資料/粒子法_非圧縮性流れ_計算の流れ.doc`

Word本文には上記文言が残っているが、その直後に式オブジェクトはない。

確認:
- LibreOffice Word→HTML: 数式画像 **21**
- Word→ODT / MathML: recoverable equation **21**
- Word binary `EMBED Equation.3`: **21**
- Word XML/ODT上で当該文直後: image / OLE / Equation object **なし**

従って、22個目がLibreOfficeだけで欠落したとは判断しない。

## 4. Other Word / PDF search

7z全展開後、Word/PDF/HTML/BAKを対象に以下を横断検索した。

- 圧力の勾配モデル
- 数値安定性
- 最低圧力
- 最小圧力
- 排斥力
- 斥力
- 勾配モデル

問題の文言が確認できた内部原稿は、
`粒子法_非圧縮性流れ_計算の流れ.doc` とそのHTML/BAK系のみ。

別の内部Word/PDF正本は確認できなかった。

## 5. Visio investigation

確認したVisio:
- `HP/資料/粒子法.vsd`
- `HP/HP図.vsd`
- `HP/公式.vsd`
- `HP/HP図(物質移動工学).vsd`
- `HP/HP図(伝熱工学).vsd`

`粒子法.vsd`:
- 重み関数
- 粒子数密度
- 勾配モデル
- 発散モデル
等の数式を確認したが、image022相当はなし。

`HP図.vsd`:
- 全36ページを視覚確認。
- 29ページに粒子・圧力差・引力/斥力・勾配補正に関する図と式がある。
- ただし、これはimage022と1対1対応すると証明できない。
- 元HTML / WordにVisioへのリンクやオブジェクトIDが残っていないため採用しない。

`公式.vsd`:
- FEM / 面積座標・積分系でMPS image022とは無関係。

## 6. External corroboration — NOT authoritative source

外部のMPS文献では、ほぼ同じ文脈で
「数値安定性のため圧力勾配モデルを修正し、粒子iと近傍粒子の最低圧力を用いる」
標準MPS式が確認できる。

これはimage022の内容を推定する強い技術的手掛かりではあるが、
**元サイトの画像正本ではない**。

したがって:
- candidate / reference: 可
- strict source replacement: 不可
- normal HTML反映: **しない**

## 7. Final status

- MPS original references: **49**
- authoritative recovered source: **48**
- MathJax: **48**
- source re-audit: **48/48**
- actual residual MPS image: **1**
- `image022.gif`: **SOURCE BLOCKED / HOLD**
- inferential replacement: **not performed**

MPSカテゴリは、image022 1件を明示HOLDとした状態で監査完了とする。
