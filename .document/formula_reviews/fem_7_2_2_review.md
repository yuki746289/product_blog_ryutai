# 数式レビュー: fem/fem_7_2_2.html

更新日: 2026-09-17

## 対象

- ページ: `fem/fem_7_2_2.html`
- タイトル: 運動量収支式の離散化（4面体1次要素）
- 元画像: `img/fem_d_momentum_tet.files/image001.png` ～ `image049.png`
- 対象数: 49式
- 対応付け: 49/49確認済み
- **Pass 1: 49/49**
- **Pass 2: 0/49**
- 通常ページへの反映: 未実施

## 厳密監査ルール

1. 元画像を原典とする。
2. 数学的に同値でも、総和記号化・行列化・成分統合・写像追加・項順変更は行わない。
3. 元画像に誤記・省略の疑いがあっても原文式はそのまま保持する。
4. 理論上の補足・修正式は原文式から分離する。
5. 読み切れない箇所は推測せず `HOLD` とする。
6. Pass 1完了後、独立してPass 2を全49式に実施する。

## 現在のPass 1一覧

| 画像 | 現候補 | Pass 1 | 備考 |
|---|---|---|---|
| `image001` | OK | **OK** | 元画像と一致 |
| `image002` | OK | **OK** | 元画像と一致 |
| `image003` | OK | **OK** | 元画像と一致 |
| `image004` | NG | **再転記OK** | `[N]^T` 短縮と `i=1,2,3` が原画像にない。零ベクトル積分を復元 |
| `image005` | NG | **再転記OK** | 節点値の明示展開を省略していた。原画像の `P_{x,1}`～`P_{x,4}` を維持 |
| `image006` | NG | **再転記OK** | 原画像にない `\sum` を除去しx/y/zを明示展開 |
| `image007` | NG | **再転記OK** | 元画像の継続等号・4成分重み関数を復元 |
| `image008` | NG | **再転記OK** | 原画像は時間微分のまま。現候補の時間差分化・`\sum` は不一致 |
| `image009` | NG | **再転記OK** | Green-Gauss後のx/y/z表面・体積積分を原画像どおり個別記載 |
| `image010` | NG | **再転記OK** | 元画像の展開式を復元 |
| `image011`～`image027` | NG | **再転記OK** | 成分展開・符号・注記を元画像どおり復元 |
| `image028` | OK | **OK** | 元画像と一致 |
| `image029`～`image041` | NG | **再転記OK** | 転置・中間等式・成分行列を元画像どおり復元 |
| `image042` | NG | **再転記OK** | 3成分表面張力ベクトルを復元 |
| `image043`～`image046` | NG | **再転記OK** | 面→要素写像を原文式から除去 |
| `image047`～`image049` | NG | **再転記OK** | `b_S` 除去に加え、圧力項を `1/Re` の外へ復元 |

Pass 1済み: `image001～image049` = **49/49式**。

現監査候補の厳密一致は `image001`, `image002`, `image003`, `image028` の4式。残る **45/49式は忠実再転記または注記復元が必要**。

## `image001`～`image003` 直接目視結果

元GIFを直接表示して、各記号・添字・符号・項順を照合した。現監査候補と一致する。

### `image001`

```latex
\[
\phi_x=\frac{\partial V_x}{\partial\tau}
+V_x\frac{\partial V_x}{\partial X}
+V_y\frac{\partial V_x}{\partial Y}
+V_z\frac{\partial V_x}{\partial Z}
-\frac{\partial\sigma^*_{xx}}{\partial X}
-\frac{\partial\sigma^*_{yx}}{\partial Y}
-\frac{\partial\sigma^*_{zx}}{\partial Z}
-g_x^*=0
\]
```

### `image002`

```latex
\[
\phi_y=\frac{\partial V_y}{\partial\tau}
+V_x\frac{\partial V_y}{\partial X}
+V_y\frac{\partial V_y}{\partial Y}
+V_z\frac{\partial V_y}{\partial Z}
-\frac{\partial\sigma^*_{xy}}{\partial X}
-\frac{\partial\sigma^*_{yy}}{\partial Y}
-\frac{\partial\sigma^*_{zy}}{\partial Z}
-g_y^*=0
\]
```

### `image003`

```latex
\[
\phi_z=\frac{\partial V_z}{\partial\tau}
+V_x\frac{\partial V_z}{\partial X}
+V_y\frac{\partial V_z}{\partial Y}
+V_z\frac{\partial V_z}{\partial Z}
-\frac{\partial\sigma^*_{xz}}{\partial X}
-\frac{\partial\sigma^*_{yz}}{\partial Y}
-\frac{\partial\sigma^*_{zz}}{\partial Z}
-g_z^*=0
\]
```

**`image001`～`image003`: Pass 1 OK。**

## `image004` 直接目視再転記

原画像は4成分重み関数ベクトルに `\phi_i` を掛けた体積積分を、零ベクトルの体積積分、さらに4成分零ベクトルへ等置している。
現候補にある先頭の `[N]^T` 短縮表現と末尾の `i=1,2,3` は原画像にはない。

```latex
\[
\int_V
\begin{bmatrix}
N_1\\N_2\\N_3\\N_4
\end{bmatrix}
\phi_i\,dV
=
\int_V
\begin{bmatrix}
0\\0\\0\\0
\end{bmatrix}
dV
=
\begin{bmatrix}
0\\0\\0\\0
\end{bmatrix}
\]
```

**Pass 1 = OK（再転記）**。

## `image005` 直接目視再転記

原画像は速度・圧力を節点値で明示展開している。現候補は `[N]\{V\}` 形式へ短縮しているため忠実転記ではない。

また最下段の圧力式は、元画像では各節点値が **`P_{x,1}`, `P_{x,2}`, `P_{x,3}`, `P_{x,4}`** と記載されている。圧力がスカラーであることから誤記の可能性はあるが、原文式では修正しない。

```latex
\[
\begin{aligned}
V_x={}&N_1V_{x,1}+N_2V_{x,2}+N_3V_{x,3}+N_4V_{x,4}\\
={}&
\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix}
\begin{bmatrix}V_{x,1}\\V_{x,2}\\V_{x,3}\\V_{x,4}\end{bmatrix}
=[N]\{V_x\},\\[4pt]
V_y={}&N_1V_{y,1}+N_2V_{y,2}+N_3V_{y,3}+N_4V_{y,4},\\
V_z={}&N_1V_{z,1}+N_2V_{z,2}+N_3V_{z,3}+N_4V_{z,4},\\
P={}&N_1P_{x,1}+N_2P_{x,2}+N_3P_{x,3}+N_4P_{x,4}
\end{aligned}
\]
```

**Pass 1 = OK（再転記）**。

## `image006` / `image008` / `image009` 直接目視再転記

### `image006`

添付元画像を再確認。原画像は左辺に4成分重み関数ベクトルと `\phi_i` の体積積分を置き、右辺に運動量残差を代入した式である。時間微分の分母は **`t`** で、`\tau` ではない。また、原画像内では右辺を各積分項へ展開していない（展開は次の `image007`）。

```latex
\[
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\phi_i\,dV
=
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\left(
\frac{\partial V_i}{\partial t}
+V_x\frac{\partial V_i}{\partial X}
+V_y\frac{\partial V_i}{\partial Y}
+V_z\frac{\partial V_i}{\partial Z}
-\frac{\partial\sigma^*_{xi}}{\partial X}
-\frac{\partial\sigma^*_{yi}}{\partial Y}
-\frac{\partial\sigma^*_{zi}}{\partial Z}
-g_i^*
\right)dV
\]
```

**Pass 1 = OK（2026-09-19 再照合・再修正）**。

### `image008`

原画像は時間微分をまだ差分化しておらず、x/y/z各方向の対流項・応力項を個別記載している。

```latex
\[
\begin{aligned}
={}&\int_V[N]^T\frac{\partial V_i}{\partial\tau}dV\\
&+V_x\int_V[N]^T\frac{\partial V_i}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial V_i}{\partial Y}dV
+V_z\int_V[N]^T\frac{\partial V_i}{\partial Z}dV\\
&-\int_V[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dV
-\int_V[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dV
-\int_V[N]^T\frac{\partial\sigma^*_{zi}}{\partial Z}dV\\
&-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

### `image009`

原画像は時間項を節点速度の差分で表し、Green-Gauss適用後の表面積分・体積積分をx/y/zごとに個別記載している。

```latex
\[
\begin{aligned}
={}&\int_V[N]^T
\frac{[N](\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau})}{\Delta\tau}dV\\
&+V_x\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial Y}dV
+V_z\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial Z}dV\\
&-\int_S[N]^T\sigma^*_{xi}n_xdS
+\int_V\left[\frac{\partial N}{\partial X}\right]^T\sigma^*_{xi}dV\\
&-\int_S[N]^T\sigma^*_{yi}n_ydS
+\int_V\left[\frac{\partial N}{\partial Y}\right]^T\sigma^*_{yi}dV\\
&-\int_S[N]^T\sigma^*_{zi}n_zdS
+\int_V\left[\frac{\partial N}{\partial Z}\right]^T\sigma^*_{zi}dV\\
&-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

**`image006`, `image008`, `image009`: Pass 1 OK（再転記）**。

## `image042`～`image049`

元GIF/PNGを直接表示して照合済み。忠実LaTeX全文は `.document/formula_reviews/fem_7_2_2_retranscription.md` に記録している。

主な確認事項:

- `image042`: 表面張力項は3成分 `[1,1,1]^T`。`b_S` / `A_S` は原画像にない。
- `image043`～`image046`: 原画像では面→要素写像を式本体に書いていない。
- `image047`: 交差項 `[S_{yx}]`, `[S_{zx}]`。圧力項 `-[H_x]\{P\}` は `1/Re` の外。
- `image048`: 交差項 `[S_{xy}]`, `[S_{zy}]`。圧力項 `-[H_y]\{P\}` は `1/Re` の外。
- `image049`: 交差項 `[S_{xz}]`, `[S_{yz}]`。圧力項 `-[H_z]\{P\}` は `1/Re` の外。

**`image042`～`image049`: 8/8 Pass 1 OK（再転記）**。

## `image007` / `image010`～`image041` 直接目視監査（2026-09-17）

GitHub Actionsは元画像の白背景化・4倍拡大・候補LaTeX抽出だけを並列実行し、Pass/NG判定は元画像の直接目視で実施した。

- `.document/formula_reviews/fem_7_2_2_pass1_batch_a.md`: `007`, `010～017` = 9/9 Pass 1 OK
- `.document/formula_reviews/fem_7_2_2_pass1_batch_b.md`: `018～029` = 12/12 Pass 1 OK
- `.document/formula_reviews/fem_7_2_2_pass1_batch_c.md`: `030～041` = 12/12 Pass 1 OK
- 既存の `001～006`, `008`, `009`, `042～049` = 16/16 Pass 1 OK

**合計: Pass 1 = 49/49 完了。Pass 2 = 0/49。**

## 旧レビュー結果の扱い

過去の「数学的に整合」「一般式として追跡可能」といった判定は参考情報としてのみ扱う。原画像一致のPass判定には使用しない。

特に次は原画像直接照合が必要:

- `image011`～`image015`, `image017`, `image024`, `image032`, `image038`: 現候補に一般化記法が含まれる可能性が高い。
- `image016`～`image029`: 行列成分を位置単位で確認する。
- `image030`, `image031`: 積分公式・質量行列を原表記のまま確認する。
- `image033`～`image041`: 係数整理過程を項順まで確認する。

## 再監査チェック

- [x] 49画像と49候補の対応付け確認。
- [x] `image001`～`image006` のPass 1（6/6）。
- [ ] `image007` のPass 1。
- [x] `image008`, `image009` のPass 1。
- [ ] `image010`～`image041` の残りPass 1。
- [x] `image042`～`image049` のPass 1（8/8）。
- [ ] 全49画像のPass 1完了。
- [ ] 全49画像のPass 2完了。
- [ ] 確定した忠実LaTeXを監査候補HTMLへ反映。
- [ ] PC/スマホでMathJax表示・横オーバーフロー確認。
- [ ] 通常ページへ反映。

## 現在の判定

**未完了。Pass 1 = 16/49、Pass 2 = 0/49。**

主要5ページ集計では、前回の実効 `40/143` に今回追加した8式（`001～006`, `008`, `009`）を加え、**実効 Pass 1 = 48/143**。

次は `image007` と `image010` を埋めたうえで、一般化の疑いが強い `image011`～`image015`, `image017`, `image024`, `image032`, `image038` を優先する。
