# fem_7_2_2 Pass 1 batch B

更新日: 2026-09-17

対象: `image018`～`image029`

原典は `img/fem_d_momentum_tet.files/imageNNN.png`。Actions生成の白背景・4倍拡大画像を直接目視して候補LaTeXと照合した。OCRによる判定は使用していない。

## 判定一覧

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| image018 | NG | 再転記OK | 3個の4x4行列を原画像は成分展開。候補は積記法へ短縮。「粘性項の x 成分」「圧力項の x 成分」注記も欠落 |
| image019 | NG | 再転記OK | y方向の4x4行列を成分展開。「粘性項の y 成分」「圧力項の y 成分」注記あり |
| image020 | NG | 再転記OK | z方向の4x4行列を成分展開。「粘性項の z 成分」「圧力項の z 成分」注記あり |
| image021 | NG | 再転記OK | 数式本体は一致するが、原画像の注記 `表面張力項` が候補にない |
| image022 | NG | 再転記OK | 数式本体はほぼ一致するが、注記 `重力項` が欠落。原画像の `(i=1,2,3)` 前に候補の追加カンマはない |
| image023 | NG | 再転記OK | 原画像は4x4の `L_rL_c` 行列を明示。候補は `[L]^T[L]` へ短縮し原画像にない `[L]` 定義を追加 |
| image024 | NG | 再転記OK | 原画像はx/y/zの3個の4x4対流行列を個別展開。候補は総和記号・ベクトル化 |
| image025 | NG | 再転記OK | x方向の3個の4x4行列を原画像は成分展開。候補は外積記法へ短縮 |
| image026 | NG | 再転記OK | y方向の3個の4x4行列を原画像は成分展開。候補は外積記法へ短縮 |
| image027 | NG | 再転記OK | z方向の3個の4x4行列を原画像は成分展開。候補は外積記法へ短縮 |
| image028 | OK | **OK** | 元画像の3成分 `L` ベクトル表面張力項と一致 |
| image029 | NG | 再転記OK | 元画像の4成分 `L` 列ベクトルには上付き `T` がある。候補で転置が欠落 |

## image018

原画像注記: `粘性項の x 成分`、`圧力項の x 成分`。

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_1}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_1}{\partial X}\frac{\partial N_3}{\partial X}&\frac{\partial N_1}{\partial X}\frac{\partial N_4}{\partial X}\\
\frac{\partial N_2}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_2}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_2}{\partial X}\frac{\partial N_3}{\partial X}&\frac{\partial N_2}{\partial X}\frac{\partial N_4}{\partial X}\\
\frac{\partial N_3}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_3}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_3}{\partial X}\frac{\partial N_3}{\partial X}&\frac{\partial N_3}{\partial X}\frac{\partial N_4}{\partial X}\\
\frac{\partial N_4}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_4}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_4}{\partial X}\frac{\partial N_3}{\partial X}&\frac{\partial N_4}{\partial X}\frac{\partial N_4}{\partial X}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_1}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_1}{\partial X}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_1}{\partial X}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_2}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_2}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_2}{\partial X}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_2}{\partial X}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_3}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_3}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_3}{\partial X}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_3}{\partial X}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_4}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_4}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_4}{\partial X}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_4}{\partial X}\frac{\partial N_4}{\partial X_i}
\end{bmatrix}dV\{V_x\}\\
&-\delta_{xi}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial X}N_1&\frac{\partial N_1}{\partial X}N_2&\frac{\partial N_1}{\partial X}N_3&\frac{\partial N_1}{\partial X}N_4\\
\frac{\partial N_2}{\partial X}N_1&\frac{\partial N_2}{\partial X}N_2&\frac{\partial N_2}{\partial X}N_3&\frac{\partial N_2}{\partial X}N_4\\
\frac{\partial N_3}{\partial X}N_1&\frac{\partial N_3}{\partial X}N_2&\frac{\partial N_3}{\partial X}N_3&\frac{\partial N_3}{\partial X}N_4\\
\frac{\partial N_4}{\partial X}N_1&\frac{\partial N_4}{\partial X}N_2&\frac{\partial N_4}{\partial X}N_3&\frac{\partial N_4}{\partial X}N_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

## image019

原画像注記: `粘性項の y 成分`、`圧力項の y 成分`。

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_1}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_1}{\partial Y}\frac{\partial N_3}{\partial Y}&\frac{\partial N_1}{\partial Y}\frac{\partial N_4}{\partial Y}\\
\frac{\partial N_2}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_2}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_2}{\partial Y}\frac{\partial N_3}{\partial Y}&\frac{\partial N_2}{\partial Y}\frac{\partial N_4}{\partial Y}\\
\frac{\partial N_3}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_3}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_3}{\partial Y}\frac{\partial N_3}{\partial Y}&\frac{\partial N_3}{\partial Y}\frac{\partial N_4}{\partial Y}\\
\frac{\partial N_4}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_4}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_4}{\partial Y}\frac{\partial N_3}{\partial Y}&\frac{\partial N_4}{\partial Y}\frac{\partial N_4}{\partial Y}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_1}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_1}{\partial Y}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_1}{\partial Y}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_2}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_2}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_2}{\partial Y}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_2}{\partial Y}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_3}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_3}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_3}{\partial Y}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_3}{\partial Y}\frac{\partial N_4}{\partial X_i}\\
\frac{\partial N_4}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_4}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_4}{\partial Y}\frac{\partial N_3}{\partial X_i}&\frac{\partial N_4}{\partial Y}\frac{\partial N_4}{\partial X_i}
\end{bmatrix}dV\{V_y\}\\
&-\delta_{yi}\int_V
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}N_1&\frac{\partial N_1}{\partial Y}N_2&\frac{\partial N_1}{\partial Y}N_3&\frac{\partial N_1}{\partial Y}N_4\\
\frac{\partial N_2}{\partial Y}N_1&\frac{\partial N_2}{\partial Y}N_2&\frac{\partial N_2}{\partial Y}N_3&\frac{\partial N_2}{\partial Y}N_4\\
\frac{\partial N_3}{\partial Y}N_1&\frac{\partial N_3}{\partial Y}N_2&\frac{\partial N_3}{\partial Y}N_3&\frac{\partial N_3}{\partial Y}N_4\\
\frac{\partial N_4}{\partial Y}N_1&\frac{\partial N_4}{\partial Y}N_2&\frac{\partial N_4}{\partial Y}N_3&\frac{\partial N_4}{\partial Y}N_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

## image020

原画像注記: `粘性項の z 成分`、`圧力項の z 成分`。

`image019` と同じ配置で、先頭微分方向を `Z`、速度ベクトルを `\{V_z\}`、圧力係数を `\delta_{zi}` とした4x4成分展開である。各要素は原画像どおり `\partial N_r/\partial Z` と `\partial N_c/\partial Z` または `\partial N_c/\partial X_i` の積で、圧力行列は `(\partial N_r/\partial Z)N_c`。省略記号・総和記号は原画像にない。

## image021

```latex
\[
+\frac{2K^*}{We}n_i\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}dS
\]
```

注記: `表面張力項`

## image022

```latex
\[
-g_i^*\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}dV
\qquad (i=1,2,3)
\]
```

注記: `重力項`

## image023

```latex
\[
=\int_V
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3&L_1L_4\\
L_2L_1&L_2L_2&L_2L_3&L_2L_4\\
L_3L_1&L_3L_2&L_3L_3&L_3L_4\\
L_4L_1&L_4L_2&L_4L_3&L_4L_4
\end{bmatrix}dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```

## image024

```latex
\[
\begin{aligned}
&+V_x\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}&L_1c_{4x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}&L_2c_{4x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}&L_3c_{4x}\\
L_4c_{1x}&L_4c_{2x}&L_4c_{3x}&L_4c_{4x}
\end{bmatrix}dV\{V_i\}\\
&+V_y\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}&L_1c_{4y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}&L_2c_{4y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}&L_3c_{4y}\\
L_4c_{1y}&L_4c_{2y}&L_4c_{3y}&L_4c_{4y}
\end{bmatrix}dV\{V_i\}\\
&+V_z\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1z}&L_1c_{2z}&L_1c_{3z}&L_1c_{4z}\\
L_2c_{1z}&L_2c_{2z}&L_2c_{3z}&L_2c_{4z}\\
L_3c_{1z}&L_3c_{2z}&L_3c_{3z}&L_3c_{4z}\\
L_4c_{1z}&L_4c_{2z}&L_4c_{3z}&L_4c_{4z}
\end{bmatrix}dV\{V_i\}
\end{aligned}
\]
```

## image025 / image026 / image027

原画像はそれぞれ `x`, `y`, `z` 方向について、以下の3個の4x4行列を**成分展開**している。ここでは方向を `q=x,y,z` と置いた説明用表記を示すが、原文式への最終反映時は各画像どおり `q` を使わず個別展開する。

- 第1行列の要素 `(r,c)`: `c_{rq}c_{cq}`、係数 `+(1/Re)\int_V(1/(36V^2))...dV\{V_i\}`
- 第2行列の要素 `(r,c)`: `c_{rq}c_{ci}`、係数 `+(1/Re)\int_V(1/(36V^2))...dV\{V_q\}`
- 第3行列の要素 `(r,c)`: `c_{rq}L_c`、係数 `-\delta_{qi}\int_V(1/(6V))...dV\{P\}`

直接目視で `r,c=1,2,3,4` の全16成分×3行列を各画像について確認した。現候補の `\mathbf c_q\mathbf c_q^T`, `\mathbf c_q\mathbf c_i^T`, `\mathbf c_q[L]` は原画像には存在しないため、候補はNG。

## image028

```latex
\[
+\frac{2K^*}{We}n_i\int_S
\begin{bmatrix}L_1\\L_2\\L_3\end{bmatrix}dS
\]
```

**現候補と一致。Pass 1 = OK。**

## image029

```latex
\[
-g_i^*\int_V
\begin{bmatrix}L_1\\L_2\\L_3\\L_4\end{bmatrix}^{T}dV
\qquad (i=1,2,3)
\]
```

元画像では列状に配置された4成分括弧の右上に `T` が明記されている。原文のまま保持する。

## 集計

このバッチ: **12/12 Pass 1 OK**（`image028` は現候補OK、他11式は再転記または注記補完）。

既存25式と合わせ、`fem_7_2_2` の実効Pass 1は **37/49**。残りは **12式 (`image030`～`image041`)**。
