# 数式元画像完全一致 再監査台帳

作成日: 2026-09-16
更新日: 2026-09-18

## 目的

2026-09-16から、数式画像→LaTeX/MathJax変換の判定基準を「数学的に同値」から**「元画像の式と忠実に一致」**へ変更した。
この台帳は、既存変換済みページを含め、すべての式を新基準で再確認するために使用する。

## 最優先ルール

- 既存レビューの `OK` は数学・物理的整合性の事前レビューを含むが、**元画像完全一致の認証ではない**。
- 数学的に同値でも、表記が元画像と異なれば不一致とする。
- 誤記候補があっても原文式は元画像どおり残し、補足・修正版は別表示とする。
- Pass 1 = 元画像とLaTeXソースの1文字・1記号単位照合。
- Pass 2 = 元画像とブラウザ上のMathJax描画結果の目視照合。
- Pass 1 / Pass 2が全式で完了し、要修正が0件になるまで通常ページへMathJax版を反映しない。

## 安全措置

旧基準でMathJax化済みだった主要5ページについて、再監査中に誤った式を通常ページへ残さないため、通常ページは元画像表示を優先する。

- 旧監査候補: `fem/*_mathjax_audit.html`
- 再転記候補はページごとに `*_reaudit.html` を作成する。
- 監査候補は通常ページからリンクせず、本番FTP公開対象外とする。
- 通常ページに未監査MathJax式が残っていた場合は、記事HTMLの文字コードを不用意に変更せず、`js/site_formula_guard_v1_6.js` で元画像表示へ戻す。

## 主要5ページ 再監査状況

| No. | 通常ページ | 元画像数 | 通常ページ状態 | 有効監査候補 | 対応付け | Pass 1 | Pass 2 | 判定 |
|---:|---|---:|---|---|---:|---:|---:|---|
| 1 | `fem/fem_6_2_6.html` | 12 | 元画像表示 | `fem/fem_6_2_6_mathjax_audit.html` | **12/12** | **12/12** | **12/12** | **Pass 1 / Pass 2 完了** |
| 2 | `fem/fem_7_1_1.html` | 20 | 認証済みLaTeX反映前 | `fem/fem_7_1_1_reaudit.html` | **20/20** | **20/20** | **20/20** | **Pass 1 / Pass 2 完了** |
| 3 | `fem/fem_7_1_2.html` | 42 | 認証済みLaTeX反映前 | `fem/fem_7_1_2_reaudit.html` | **42/42** | **42/42** | **42/42** | **Pass 1 / Pass 2 完了** |
| 4 | `fem/fem_7_2_1.html` | 20 | 元画像表示 | `fem/fem_7_2_1_reaudit.html` | **20/20** | **20/20** | **20/20** | **Pass 1 / Pass 2 完了** |
| 5 | `fem/fem_7_2_2.html` | 49 | 元画像表示 | `fem/fem_7_2_2_reaudit.html` | **49/49** | **49/49** | **49/49** | **Pass 1 / Pass 2 完了** |
|  | **合計** | **143** |  |  | **143/143** | **143/143** | **143/143** | **主要5ページ厳密監査完了** |
`fem/fem_6_2_1.html` は数式画像表示を維持している。体積の符号に関する補足文が追加されているため、数式本体とは別に説明文レビュー対象とする。

## 2026-09-17 監査進捗

### `fem/fem_6_2_6.html`

通常ページ上の `image021.png` ～ `image032.png` と、監査候補上の12個の式ID / `data-source-image` の1対1対応を確認した。
元画像を1式ずつ開き、変数・添字・微分方向・分母 `6V`・右辺6項・符号・項順・括弧・等号を照合した。

結果: **Pass 1 = 12/12 OK、要修正0件。**

実行環境内のMathJaxレンダラーによる補助描画比較も12/12で構造一致。ただし実ブラウザ上のCHTML描画ではないためPass 2には数えない。

### `fem/fem_7_1_1.html`

対象画像は `image001`～`image018`, `image020`, `image021` の20式。`image019` はこのページの数式対象外。

旧監査候補 `fem_7_1_1_mathjax_audit.html` は、元画像との目視監査で20/20式すべて不一致だった。
主な問題は、大小文字・積分領域・転置記号・時刻添字順の変更と、途中計算の一般化・省略だった。

そのため元画像忠実転記をやり直し、以下を作成した。

- `.document/formula_reviews/fem_7_1_1_retranscription.md`
- `.document/formula_reviews/fem_7_1_1_image011_retranscription.md`
- `fem/fem_7_1_1_reaudit.html`

再転記候補を元画像と再照合した結果: **Pass 1 = 20/20 OK。**

2026-09-18にChromium上のMathJax実描画を元画像と20式すべて目視比較し、**Pass 2 = 20/20 OK**。

### `fem/fem_7_1_2.html`

通常ページに残っていた11個の未監査MathJaxブロックを `image003 / 004 / 027 / 032 / 032 / 037 / 038 / 039 / 040 / 041 / 042` へ対応付け、安全ガードで元画像表示へ戻した。

監査候補全体も確認し、`image001`～`image042` の**対応付け = 42/42 OK**。`image028 / 032 / 033` の再利用も repeat ID で追跡可能。

さらにGit履歴を追跡し、以下を確認した。

- `b2686b91...` で `image003`, `image004`, `image027`, `image032` 等が元画像表示から理論修正版MathJaxへ置換された。
- `e5122081...` で残りの数式画像がMathJax化された。
- `6b25a2c1...` と `8376b22f...` はこのページの数式本文を変更していない。
- `image038` は課題台帳に原文 `i=1,2,3` → 修正版 `i=1,2` の変更対象として記録されている。

したがって、**現監査候補NG確定 = 5/42 (`003`, `004`, `027`, `032`, `038`)**。
ただし履歴証拠は元画像Pass 1の代替ではないため、Pass 1合格数は0/42のままとする。

再転記準備として `.document/formula_reviews/fem_7_1_2_retranscription.md` を作成した。

元画像42式をActions前処理3バッチ＋直接目視で再監査し、**Pass 1 = 42/42** を完了した。忠実LaTeXは3つのbatch記録へ分離。既知の誤記候補は原文のまま保持し、修正版は補足扱いとする。

### `fem/fem_7_2_1.html`

通常ページは `image001.png`～`image020.png` を画像表示。
監査候補 `formula-fem-7-2-1-001`～`020` も同番号の元画像を参照しており、**対応付け = 20/20 OK**。

元画像を順次目視比較した結果:

- 現候補の厳密比較: **20/20**
- 現候補の厳密一致: **0/20**
- 元画像忠実再転記: **20/20**
- Pass 1: **20/20**
- HOLD: **0/20**
- `image011`, `image012`, `image015` は元画像を白背景化・8倍拡大して再確認し、HOLDを解消した。

`image009` では、理論上不自然でも元画像に実際に `{V_x}`, `{V_y}`, `{V_z}` が記載されているため、原文転記ではそのまま保持する。

このページは既存候補の微修正ではなく、20式すべてを元画像忠実転記で再作成する。
詳細は `.document/formula_reviews/fem_7_2_1_review.md` と `fem_7_2_1_retranscription.md` に記録している。

### `fem/fem_7_2_2.html`

通常ページは主要数式を元画像表示。
監査候補 `formula-fem-7-2-2-001`～`049` と `image001.png`～`image049.png` の**対応付け = 49/49 OK**。`image031 / 037` の再利用も repeat ID で追跡可能。

Git履歴から、MathJax変換時に境界三角形の3節点表面力ベクトルを四面体4節点へ写像する `b_S` が式本体へ追加されていることを確認した。変換前本文ではこの写像を後続式で省略する旨の補足だったため、**現監査候補 `image042`～`image049` 対応式は8/8 NG確定**。

さらに `image042.png` を直接表示し、原画像が

`+(2K^*/(3We)) n_i S [1,1,1]^T`

の3成分局所ベクトルであることを目視確認した。現候補の `b_S` 4成分写像は原画像に存在しない。

`image042` の元画像忠実LaTeXを `.document/formula_reviews/fem_7_2_2_retranscription.md` に固定した。その後 `image001～041`, `043～049` も直接目視監査し、**Pass 1 = 49/49** を完了した。詳細は `fem_7_2_2_review.md` と3つのPass 1 batch記録に分離している。

現候補で `\sum_{a=x,y,z}` 等を用いていた12式 (`006`, `008`, `009`, `011`～`015`, `017`, `024`, `032`, `038`) も全式を直接照合し、元画像どおりの個別展開へ再転記した。

## 2026-09-18 Pass 2 実ブラウザ監査

GitHub Actions run `35283846226` でChromium + MathJaxの実描画を5ページ並列取得した。各式について元画像とブラウザ描画を並べた比較画像を作成し、143式すべてを式単位で目視確認した。

- `fem_6_2_6`: **12/12 OK**
- `fem_7_1_1`: **20/20 OK**
- `fem_7_1_2`: **42/42 OK**
- `fem_7_2_1`: **20/20 OK**
- `fem_7_2_2`: **49/49 OK**
- 合計: **143/143 OK**
- 横方向オーバーフロー: **0/143**

詳細な監査方法と結果は `.document/formula_reviews/PASS2_BROWSER_AUDIT_20260918.md` を正本とする。
## 2026-09-18 Appendix 監査・通常ページ反映

Appendixの数式画像について、元画像を正本として分類・再転記・Pass 1 / Pass 2・通常ページ反映・PC/スマホQAを実施した。

- `appendix_1.html`: **14式 完了**
- `appendix_2.html`: **11式 完了**
  - `image001.png` は数式単体ではなく球の幾何図＋式の混在画像のため画像維持。
  - Pass 2 workflow run: **35288931238**
  - 通常ページQA workflow run: **35290873659**
  - desktop: 11/11 blocks, formula images 0, MathJax errors 0, page overflowなし
  - mobile: 11/11 blocks, formula images 0, MathJax errors 0, local-scroll 7, uncontained 0, page overflowなし
- `appendix_3_1.html`: **8式 完了**
- `appendix_3_2.html`: **8式 完了**
- Appendix数式合計: **41式 完了**
- 図・混在画像は数式化せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/APPENDIX_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/APPENDIX_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/APPENDIX_2_NORMAL_BROWSER_QA_20260918.md`
- `.document/formula_reviews/APPENDIX_COORDINATE_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/APPENDIX_COORDINATE_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 Heat 7 監査・通常ページ反映

熱伝導の離散化ページ `heat_7_1.html` / `heat_7_2.html` について、元画像を正本として分類・再転記・Pass 1 / Pass 2・通常ページ反映・PC/スマホQAを実施した。

- `heat_7_1.html`: **33式 完了**
  - Pass 2 final run: **35292202973**
  - desktop: 33/33 blocks, formula images 0, MathJax errors 0, page overflowなし
  - mobile: 33/33 blocks, formula images 0, MathJax errors 0, local-scroll 7, uncontained 0, page overflowなし
- `heat_7_2.html`: **32式 完了**
  - Pass 2 final run: **35293474594**
  - normal QA run: **35294686097**
  - desktop: 32/32 blocks, formula images 0, MathJax errors 0, page overflowなし
  - mobile: 32/32 blocks, formula images 0, MathJax errors 0, local-scroll 12, uncontained 0, page overflowなし
  - `image014` のY方向行列内にある source-visible な `N_4 ∂N_2/∂Z` は、理論上の修正を行わず元画像どおり保持した。
- Heat 7 数式合計: **65式 完了**
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HEAT_7_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HEAT_7_1_NORMAL_BROWSER_QA_20260918.md`
- `.document/formula_reviews/HEAT_7_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HEAT_7_2_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 Heat 6 監査・通常ページ反映

`heat/heat_6.html` の無次元化関連13画像を元画像正本で監査した。

- 画像分類: **13件すべて数式系**
  - 表示数式: **11**
  - インライン数式記号: **2**
- Pass 1: **13/13**
- Pass 2: **13/13**
- Pass 2 workflow run: **35295172775**
- 通常ページへMathJax反映済み
- Normal browser QA run: **35295410479**
- desktop: display 11/11, inline 2/2, formula images 0, MathJax errors 0, page overflowなし
- mobile: display 11/11, inline 2/2, formula images 0, MathJax errors 0, page overflowなし
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HEAT_6_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HEAT_6_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HEAT_6_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 Remaining Heat 監査・通常ページ反映

Heat 6 / Heat 7以外に残っていた24画像を分類し、数式16件を厳密監査・通常ページ化した。

- 分類対象: **24画像**
  - 数式: **16**
  - 図・模式図: **8**（画像維持）
- Pass 1: **16/16**
- Pass 2: **16/16**
- Pass 2 workflow run: **35296027681**
- 通常ページ反映: **16/16**
- Normal browser QA run: **35310076540**
- desktop: 全8ページ PASS、MathJax errors 0、page overflowなし
- mobile: 全8ページ PASS、MathJax errors 0、uncontained 0、page overflowなし
- mobile local-scroll: heat_5_2=1, heat_5_3=1, heat_5_4=3
- 図8件は変更せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/REMAINING_HEAT_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/REMAINING_HEAT_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/REMAINING_HEAT_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 FEM Batch 1 監査・通常ページ反映

残存FEMの高密度4ページ34画像を分類した。

- `fem/fem_11_1.html`: 11数式 / 0図 → **11式完了**
- `fem/fem_13.html`: 0数式 / 8図 → 全件画像維持
- `fem/fem_2_1.html`: 6数式 / 2図 → **6式完了**
- `fem/fem_10.html`: 6数式 / 1図 → **6式完了**
- Batch formula total: **23式**
- Pass 1: **23/23**
- Pass 2 final run: **35311609362**
- Pass 2: **23/23**
- Normal browser QA run: **35311908407**
- desktop: 全3対象ページ PASS、MathJax errors 0、page overflowなし
- mobile: 全3対象ページ PASS、uncontained 0、page overflowなし
- `fem_10` mobile local-scroll: 3
- retained diagrams: fem_2_1=image001/image008, fem_10=image005, fem_13=8画像
- 本番FTP反映は未実施。

Pass 2目視で `fem_10/image002`, `image003` の非対角添字差異を検出し、元画像どおり `S_yx / S_zx / S_zy` へ修正して再監査した。

詳細:
- `.document/formula_reviews/FEM_BATCH_1_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/FEM_BATCH_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/FEM_BATCH_1_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 FEM Batch 2 監査・通常ページ反映

残存FEM第2バッチ28画像を分類し、即時変換対象16式を厳密監査・通常ページ化した。

- 分類対象: **28画像**
  - 数式・数式テキスト: **23**
  - 図・混在図: **5**
- 即時変換:
  - `fem_2_3.html`: 5式完了、図2件維持
  - `fem_6_2_1.html`: 6式完了、図1件維持
  - `fem_8_2_1.html`: 5式完了、図2件維持
- `fem_5.html`: 数式系7件は別処理（うち1件は日本語説明＋数式の混在テキスト）
- Pass 1: **16/16**
- Pass 2 run: **35314818685**
- Pass 2: **16/16**
- Normal browser QA run: **35315150868**
- desktop/mobile: MathJax errors 0、uncontained 0、page overflowなし
- mobile local-scroll: `fem_2_3` 1、`fem_6_2_1` 5、`fem_8_2_1` 2
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/FEM_BATCH_2_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/FEM_BATCH_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/FEM_BATCH_2_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 FEM Batch 3 監査・通常ページ反映

残存FEM第3バッチ24画像を分類し、16式を厳密監査・通常ページ化した。

- 分類対象: **24画像**
  - 数式: **16**
  - 図: **8**（画像維持）
- `fem_1.html`: 全6件が図のため画像維持
- `fem_2_2.html`: 5式完了、図1件維持
- `fem_6_1_1.html`: 5式完了、図1件維持
- `fem_6_1_5.html`: 6式完了
- Pass 1: **16/16**
- Pass 2 run: **35315585242**
- Pass 2: **16/16**
- Normal browser QA: **PASS**
- desktop/mobile: MathJax errors 0、uncontained 0、page overflowなし
- mobile local-scroll: `fem_2_2` 1式
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/FEM_BATCH_3_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/FEM_BATCH_3_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/FEM_BATCH_3_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 FEM 5 行列式ページ再構成

`fem/fem_5.html` の7画像を、元画像正本でHTML本文＋MathJaxへ再構成した。

- 対象: **7画像**
- 純MathJaxブロック: **6**
- 日本語説明＋MathJax混在ブロック: **1**
- Pass 1: **7/7**
- Pass 2 run: **35317241741**
- Pass 2: **7/7**
- Normal browser QA run: **35317676898**
- desktop: 7/7、MathJax errors 0、page overflowなし
- mobile: 7/7、MathJax errors 0、local-scroll 4、uncontained 0、page overflowなし
- image002の日本語説明、image003のsource-visibleな`a_{43}`、24項の順序・符号を維持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/FEM_5_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/FEM_5_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 FEM Batch 4 監査・通常ページ反映

残存FEM第4バッチ27画像を分類し、純数式19件を厳密監査・通常ページ化した。

- 分類対象: **27画像**
  - 純数式: **19**
  - 日本語説明＋数式の混在テキスト: **1**
  - 図・模式図: **7**
- `fem_4.html`: 4式完了、`image002` は混在テキストとして別処理
- `fem_9.html`: 3式完了、図2件維持
- `fem_6_2_2.html`～`fem_6_2_5.html`: 各3式、計12式完了
- `fem_12.html`: 5件すべて図として画像維持
- Pass 1: **19/19**
- Pass 2 run: **35317362082**
- Pass 2: **19/19**
- Normal browser QA run: **35317792518**
- desktop/mobile: MathJax errors 0、uncontained 0、page overflowなし
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/FEM_BATCH_4_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/FEM_BATCH_4_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/FEM_BATCH_4_NORMAL_BROWSER_QA_20260918.md`

## 2026-09-18 Remaining FEM 監査・通常ページ反映

FEM batches 1–3 / FEM 5後に残っていた未分類20画像を分類し、数学コンテンツ11件を厳密監査・通常ページ化した。

- 分類対象: **20画像**
  - 純数式: **10**
  - 日本語本文＋数式: **1**
  - 図・模式図・混在図: **9**（画像維持）
- 対象ページ:
  - `fem_3.html`: 2式
  - `fem_6_1_2.html`: 2式
  - `fem_6_1_3.html`: 2式
  - `fem_6_1_4.html`: 2式
  - `fem_8.html`: 2式
  - `fem_4.html`: HTML本文＋MathJax 1件
- Pass 1: **11/11**
- Pass 2 run: **35318416381**
- Pass 2: **11/11**
- Normal browser QA run: **35318974319**
- desktop/mobile: MathJax errors 0、uncontained 0、page overflowなし
- mobile local-scroll: fem_6_1_2=2, fem_6_1_3=2, fem_6_1_4=2
- source-visibleな中間式の `∂/∂x` 表記（fem_6_1_3/image010, fem_6_1_4/image012）は修正せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/REMAINING_FEM_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/REMAINING_FEM_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/REMAINING_FEM_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics Batch 1 監査・通常ページ反映

流体力学の高密度4ページ46画像を分類し、43式を厳密監査・通常ページ化した。

- 対象ページ: `hydronamics_14.html`, `hydronamics_8.html`, `hydronamics_12_1.html`, `hydronamics_4.html`
- 数式: **43**
- 図: **3**（画像維持）
- Word原稿OMMLを転記補助として利用し、元HP画像を正本として照合
- Pass 1: **43/43**
- Pass 2: **43/43**
- Pass 2 latest run: **35333776697**
- 通常ページ反映: **43/43**
- Normal browser QA run: **35336038209**
- desktop/mobile: MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: hydronamics_14=2, hydronamics_12_1=1, hydronamics_4=3
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_BATCH_1_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_BATCH_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_BATCH_1_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 9_2 監査・通常ページ反映

`hydronamics/hydronamics_9_2.html` の応力垂直成分ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **10画像**
  - 数式: **9**
  - 図: **1**（image001を維持）
- Pass 1: **9/9**
- Pass 2 run: **35336615932**
- Pass 2: **9/9**
- 通常ページ反映: **9/9**
- Apply final run: **35337018271**
- Normal browser QA run: **35337064399**
- desktop/mobile: 9/9 blocks、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_9_2_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_2_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 9_4 監査・通常ページ反映

`hydronamics/hydronamics_9_4.html` の剪断成分対称性ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **9画像**
  - 数式: **8**
  - 図: **1**（image001を維持）
- Pass 1: **8/8**
- Pass 2 run: **35337301521**
- Pass 2: **8/8**
- 通常ページ反映: **8/8**
- Apply run: **35337439565**
- Normal browser QA run: **35337486018**
- desktop/mobile: 8/8 blocks、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **2**
- source-visibleな慣性モーメント途中式は理論修正せず元画像どおり保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_9_4_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_4_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_4_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 10_1 監査・通常ページ反映

`hydronamics/hydronamics_10_1.html` の表面張力ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **8画像**
  - 数式: **5**
  - 図: **3**（image001 / image003 / image004 を維持）
- Pass 1: **5/5**
- Pass 2 run: **35338265893**
- Pass 2: **5/5**
- 通常ページ反映: **5/5**
- Apply run: **35338506941**
- Normal browser QA run: **35338543897**
- desktop/mobile: 5/5 blocks、3/3 retained diagrams、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- `image007` のsource-visibleな中間式の `r_2` 重複は理論修正せず保持。
- `image005` の近似記号は元画像に合わせ `\cong`（≅）を使用。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_10_1_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_10_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_10_1_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 12_2 監査・通常ページ反映

`hydronamics/hydronamics_12_2.html` の運動量収支式無次元化ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **8画像**
  - 表示数式: **6**
  - インライン数式: **2**
  - 図: **0**
- Pass 1: **8/8**
- Pass 2 run: **35339104446**
- Pass 2: **8/8**
- 通常ページ反映: **8/8**
- Apply success run: **35339449654**
- Normal browser QA success run: **35339518795**
- desktop: display 6/6, inline 2/2, formula images 0, MathJax errors 0, page overflowなし
- mobile: display 6/6, inline 2/2, formula images 0, MathJax errors 0, local-scroll 1, uncontained 0, page overflowなし
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_12_2_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_12_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_12_2_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 6_1 監査・通常ページ反映

`hydronamics/hydronamics_6_1.html` の慣性力ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **8画像**
  - 数式 / 日本語混在数式: **7**
  - 図: **1**（image001を維持）
- Pass 1: **7/7**
- Pass 2 run: **35339973936**
- Pass 2: **7/7**
- 通常ページ反映: **7/7**
- Apply run: **35340417996**
- Normal browser QA run: **35340448466**
- desktop/mobile: 7/7 blocks、1/1 retained diagram、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **4**
- `image002` 内の日本語説明（「ここで、m=...」「ここで、v_x=...」）も保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_6_1_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_1_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 6_2 監査・通常ページ反映

`hydronamics/hydronamics_6_2.html` の粘性力ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **7画像**
  - 数式: **6**
  - 図: **1**（image001を維持）
- Pass 1: **6/6**
- Pass 2 run: **35341075511**
- Pass 2: **6/6**
- 通常ページ反映: **6/6**
- Apply run: **35341250756**
- Normal browser QA run: **35341284413**
- desktop/mobile: 6/6 blocks、1/1 retained diagram、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **3**
- `image002`–`image007` の中央積は元画像に見える `ΔzxΔz` を理論修正せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_6_2_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_2_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_2_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 6_3 監査・通常ページ反映

`hydronamics/hydronamics_6_3.html` の圧力ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **7画像**
  - 数式: **6**
  - 図: **1**（image001を維持）
- Pass 1: **6/6**
- Pass 2 run: **35341863331**
- Pass 2: **6/6**
- 通常ページ反映: **6/6**
- Apply run: **35342011613**
- Normal browser QA run: **35342057169**
- desktop/mobile: 6/6 blocks、1/1 retained diagram、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_6_3_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_3_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_3_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 6_4 監査・通常ページ反映

`hydronamics/hydronamics_6_4.html` の重力ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **7画像**
  - 表示数式: **5**
  - インライン数式: **1**
  - 図: **1**（image001を維持）
- Pass 1: **6/6**
- Pass 2 run: **35342276962**
- Pass 2: **6/6**
- 通常ページ反映: **6/6**
- Apply final run: **35342502115**
- Normal browser QA run: **35342557215**
- desktop/mobile: display 5/5、inline 1/1、1/1 retained diagram、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- `image003` の source-visible な重複 `+ +` は理論修正せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_6_4_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_4_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_6_4_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 9_1 監査・通常ページ反映

`hydronamics/hydronamics_9_1.html` の剪断速度ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **6画像**
  - 数式: **4**
  - 図: **2**（image001 / image004 を維持）
- Pass 1: **4/4**
- Pass 2 run: **35342850776**
- Pass 2: **4/4**
- 通常ページ反映: **4/4**
- Apply final run: **35343067610**
- Normal browser QA run: **35343116289**
- desktop/mobile: 4/4 blocks、2/2 retained diagrams、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- 元HTMLの `image002` ラッパーが `<p>...<p>` と壊れていたため、反映workflowでその既存構造も安全に置換。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_9_1_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_1_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_1_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 9_5 監査・通常ページ反映

`hydronamics/hydronamics_9_5.html` の剪断成分の値ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **6画像**
  - 数式: **5**
  - 図: **1**（image001を維持）
- Pass 1: **5/5**
- Pass 2 run: **35346984090**
- Pass 2: **5/5**
- 通常ページ反映: **5/5**
- Apply run: **35347166296**
- Normal browser QA final run: **35347202731**
- desktop/mobile: 5/5 blocks、1/1 retained diagram、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- `image005` の `γ_y / γ_z` 同一式、`image006` の source-visible な応力添字は理論修正せず保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_9_5_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_5_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_5_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 9_6 監査・通常ページ反映

`hydronamics/hydronamics_9_6.html` の応力のまとめページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **5画像**
  - 数式: **5**
  - 図: **0**
- Pass 1: **5/5**
- Pass 2 run: **35347501891**
- Pass 2: **5/5**
- 通常ページ反映: **5/5**
- Apply run: **35347676111**
- Normal browser QA run: **35347716629**
- desktop/mobile: 5/5 blocks、残存画像0、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **0**
- `image005` のWord変換で欠落した2行目先頭の `=` は元画像から復元。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_9_6_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_6_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_9_6_NORMAL_BROWSER_QA_20260918.md`


## 2026-09-18 Hydronamics 11 監査・通常ページ反映

`hydronamics/hydronamics_11.html` の無次元数ページを、Word原稿を転記補助に使い、元HP画像を正本として処理した。

- 分類対象: **4画像**
  - 数式 / 日本語ラベル＋単位展開: **4**
  - 図: **0**
- Pass 1: **4/4**
- Pass 2 run: **35348035917**
- Pass 2: **4/4**
- 通常ページ反映: **4/4**
- Apply run: **35348221198**
- Normal browser QA run: **35348266451**
- desktop/mobile: 4/4 blocks、残存画像0、MathJax errors 0、unrendered 0、uncontained 0、page overflowなし
- mobile local-scroll: **1**
- 「慣性力」「粘性力」「表面張力/2」「重力」の日本語ラベルと単位展開を保持。
- 本番FTP反映は未実施。

詳細:
- `.document/formula_reviews/HYDRONAMICS_11_IMAGE_CLASSIFICATION_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_11_FORMULA_AUDIT_20260918.md`
- `.document/formula_reviews/HYDRONAMICS_11_NORMAL_BROWSER_QA_20260918.md`

## 次の優先順

1. サイト全体の残存画像を「数式 / 図 / 混在画像」に分類する。
2. 数式画像だけを、元画像正本のPass 1 → ブラウザPass 2 → 通常ページ反映 → PC/スマホQAの順で処理する。
3. 次の高密度候補として heat 系、残存FEM、fluid、physics を順次処理する。
4. MPSの欠損GIF参照は、数式変換と切り分けて元ファイルの所在・復元可否を調査する。
5. 全体QA完了後にのみ本番FTP反映を検討する。

## ページ監査手順

1. 元画像の出現順を確認する。
2. 監査候補のMathJax式IDと `data-source-image` を確認する。
3. 元画像とMathJax式を1対1で対応付ける。
4. 画像ごとにPass 1を実施する。
5. ブラウザ描画後にPass 2を実施する。
6. 完全一致しない式は監査候補を元画像どおりに修正する。
7. 誤記・補足・理論上の疑義は原文式の外へ分離する。
8. 全式完了後にPC/スマホ表示を確認する。
9. 要修正0件を確認後、通常ページへMathJax版を反映する。

## サイト全体の未変換ページ

主要5ページの再監査後、`release_1.0.0` を基準にサイト全HTMLを走査し、数式画像を使用するページをすべて一覧化する。

完了条件:

- [ ] 数式画像を持つ全ページを列挙した。
- [ ] 全数式画像に変換/画像維持の判定を付けた。
- [ ] MathJax化した全式で元画像とのPass 1/Pass 2が完了した。
- [ ] 未確認0件。
- [ ] 誤記・補足は原文式と分離されている。
- [ ] PC/スマホ表示確認済み。

## 現在の判定

**サイト全体: 未完了 / 数式画像のサイト全体展開中**

- 主要FEM 5ページ: **143/143 Pass 1・Pass 2完了、通常ページ反映・PC/スマホQA完了**
- Appendix: **41式完了、通常ページ反映・PC/スマホQA完了**
- Heat 7: **65式完了、通常ページ反映・PC/スマホQA完了**
- Heat 6: **13式完了、通常ページ反映・PC/スマホQA完了**
- Remaining Heat: **16式完了、図8件は画像維持、PC/スマホQA完了**
- **Heatカテゴリの既知数式画像は変換完了**
- FEM Batch 1: **23式完了、対象3ページPC/スマホQA完了**
- FEM Batch 2 immediate: **16式完了、図5件は画像維持、PC/スマホQA完了**
- FEM Batch 3: **16式完了、図8件は画像維持、PC/スマホQA完了**
- FEM 5: **7件完了（純MathJax 6 + HTML本文＋MathJax 1）、PC/スマホQA完了**
- Remaining FEM: **11件完了（純MathJax 10 + HTML本文＋MathJax 1）、PC/スマホQA完了**
- **FEMカテゴリの既知数式画像は変換完了**
- 厳密監査・通常ページ化まで完了した数式・数式テキスト: **467件**
- 残存画像は数式とは限らないため、今後はページ単位で分類してから数式のみ変換する。
- MPS欠損GIF参照は別タスクとして扱う。
- 本番FTP反映は未実施。
