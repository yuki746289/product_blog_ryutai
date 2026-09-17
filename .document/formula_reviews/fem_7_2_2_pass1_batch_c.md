# fem_7_2_2 Pass 1 batch C

更新日: 2026-09-17

対象: `image030`～`image041`

原典は `img/fem_d_momentum_tet.files/imageNNN.png`。GitHub Actions で生成した白背景・4倍拡大画像を直接目視し、候補LaTeXと照合した。OCRによる自動判定は使用していない。

## 判定一覧

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| image030 | NG | **再転記OK** | 候補が積分公式の中間等式を省略 |
| image031 | NG | **再転記OK** | 原画像にない `[C]` 定義・短縮記号を追加 |
| image032 | NG | **再転記OK** | 原画像はx/y/zの3個の4×4行列を個別展開。候補は総和・外積へ一般化 |
| image033 | NG | **再転記OK** | x方向の3個の4×4行列を原画像どおり展開。候補は外積へ短縮し係数も代数整理 |
| image034 | NG | **再転記OK** | y方向。同上 |
| image035 | NG | **再転記OK** | z方向。同上 |
| image036 | NG | **再転記OK** | 原画像にない `\mathbf f_S` を候補が追加 |
| image037 | NG | **再転記OK** | 候補に原画像にないカンマを追加 |
| image038 | NG | **再転記OK** | 原画像はx/y/zの3個の4×4行列を個別記載。候補は `\sum` と `[C_a]` へ一般化 |
| image039 | NG | **再転記OK** | x方向の3個の4×4行列を原画像は成分展開。候補は `[S]`,`[H]` へ短縮 |
| image040 | NG | **再転記OK** | y方向。同上 |
| image041 | NG | **再転記OK** | z方向。同上 |

## image030

```latex
\[
\int_V L_1^pL_2^qL_3^rL_4^s\,dV
=\frac{p!q!r!s!}{(p+q+r+s+3)!}\,6V
\]

\[
\int_VL_iL_j\,dV
=\begin{cases}
\displaystyle
\frac{1!1!}{(1+1+3)!}\,6V
=\frac{6}{5!}V
=\frac{1}{20}V & (i\ne j),\\[6pt]
\displaystyle
\frac{2!}{(1+1+3)!}\,6V
=\frac{12}{5!}V
=\frac{1}{10}V & (i=j)
\end{cases}
\]

\[
\int_VL_i\,dV
=\frac{1!}{(1+3)!}\,6V
=\frac{6}{4!}V
=\frac14V
\]

\[
\int_SL_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2S
\]

\[
\int_SL_i\,dS
=\frac{1!}{(1+2)!}\,2S
=\frac13S
\]
```

候補では中間の階乗計算を省略しているため、数学的には同値でも忠実転記としてはNG。

## image031

```latex
\[
=\frac1{20}V
\begin{bmatrix}
2&1&1&1\\
1&2&1&1\\
1&1&2&1\\
1&1&1&2
\end{bmatrix}
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```

原画像に `[C]` 記号・定義は存在しない。

## image032

```latex
\[
\begin{aligned}
&+V_x\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{V_i\}\\
&+V_y\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{V_i\}\\
&+V_z\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{V_i\}
\end{aligned}
\]
```

## image033

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}&c_{1x}c_{4x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}&c_{2x}c_{4x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}&c_{3x}c_{4x}\\
c_{4x}c_{1x}&c_{4x}c_{2x}&c_{4x}c_{3x}&c_{4x}c_{4x}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}&c_{1x}c_{4i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}&c_{2x}c_{4i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}&c_{3x}c_{4i}\\
c_{4x}c_{1i}&c_{4x}c_{2i}&c_{4x}c_{3i}&c_{4x}c_{4i}
\end{bmatrix}\{V_x\}\\
&-\delta_{xi}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{1x}&c_{1x}&c_{1x}\\
c_{2x}&c_{2x}&c_{2x}&c_{2x}\\
c_{3x}&c_{3x}&c_{3x}&c_{3x}\\
c_{4x}&c_{4x}&c_{4x}&c_{4x}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## image034

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}&c_{1y}c_{4y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}&c_{2y}c_{4y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}&c_{3y}c_{4y}\\
c_{4y}c_{1y}&c_{4y}c_{2y}&c_{4y}c_{3y}&c_{4y}c_{4y}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}&c_{1y}c_{4i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}&c_{2y}c_{4i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}&c_{3y}c_{4i}\\
c_{4y}c_{1i}&c_{4y}c_{2i}&c_{4y}c_{3i}&c_{4y}c_{4i}
\end{bmatrix}\{V_y\}\\
&-\delta_{yi}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1y}&c_{1y}&c_{1y}&c_{1y}\\
c_{2y}&c_{2y}&c_{2y}&c_{2y}\\
c_{3y}&c_{3y}&c_{3y}&c_{3y}\\
c_{4y}&c_{4y}&c_{4y}&c_{4y}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## image035

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1z}c_{1z}&c_{1z}c_{2z}&c_{1z}c_{3z}&c_{1z}c_{4z}\\
c_{2z}c_{1z}&c_{2z}c_{2z}&c_{2z}c_{3z}&c_{2z}c_{4z}\\
c_{3z}c_{1z}&c_{3z}c_{2z}&c_{3z}c_{3z}&c_{3z}c_{4z}\\
c_{4z}c_{1z}&c_{4z}c_{2z}&c_{4z}c_{3z}&c_{4z}c_{4z}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V^2}V
\begin{bmatrix}
c_{1z}c_{1i}&c_{1z}c_{2i}&c_{1z}c_{3i}&c_{1z}c_{4i}\\
c_{2z}c_{1i}&c_{2z}c_{2i}&c_{2z}c_{3i}&c_{2z}c_{4i}\\
c_{3z}c_{1i}&c_{3z}c_{2i}&c_{3z}c_{3i}&c_{3z}c_{4i}\\
c_{4z}c_{1i}&c_{4z}c_{2i}&c_{4z}c_{3i}&c_{4z}c_{4i}
\end{bmatrix}\{V_z\}\\
&-\delta_{zi}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1z}&c_{1z}&c_{1z}&c_{1z}\\
c_{2z}&c_{2z}&c_{2z}&c_{2z}\\
c_{3z}&c_{3z}&c_{3z}&c_{3z}\\
c_{4z}&c_{4z}&c_{4z}&c_{4z}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## image036

```latex
\[
+\frac{2K^*}{We}n_i\frac{S}{3}
\begin{bmatrix}1\\1\\1\end{bmatrix}
\]
```

原画像に `\mathbf f_S` は存在しない。

## image037

```latex
\[
-g_i^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
\qquad(i=1,2,3)
\]
```

原画像では列ベクトルの後にカンマはない。

## image038

```latex
\[
\begin{aligned}
&+V_x\frac1{24}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{V_i\}\\
&+V_y\frac1{24}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{V_i\}\\
&+V_z\frac1{24}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{V_i\}
\end{aligned}
\]
```

## image039

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}&c_{1x}c_{4x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}&c_{2x}c_{4x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}&c_{3x}c_{4x}\\
c_{4x}c_{1x}&c_{4x}c_{2x}&c_{4x}c_{3x}&c_{4x}c_{4x}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}&c_{1x}c_{4i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}&c_{2x}c_{4i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}&c_{3x}c_{4i}\\
c_{4x}c_{1i}&c_{4x}c_{2i}&c_{4x}c_{3i}&c_{4x}c_{4i}
\end{bmatrix}\{V_x\}\\
&-\delta_{xi}\frac1{24}
\begin{bmatrix}
c_{1x}&c_{1x}&c_{1x}&c_{1x}\\
c_{2x}&c_{2x}&c_{2x}&c_{2x}\\
c_{3x}&c_{3x}&c_{3x}&c_{3x}\\
c_{4x}&c_{4x}&c_{4x}&c_{4x}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## image040

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}&c_{1y}c_{4y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}&c_{2y}c_{4y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}&c_{3y}c_{4y}\\
c_{4y}c_{1y}&c_{4y}c_{2y}&c_{4y}c_{3y}&c_{4y}c_{4y}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}&c_{1y}c_{4i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}&c_{2y}c_{4i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}&c_{3y}c_{4i}\\
c_{4y}c_{1i}&c_{4y}c_{2i}&c_{4y}c_{3i}&c_{4y}c_{4i}
\end{bmatrix}\{V_y\}\\
&-\delta_{yi}\frac1{24}
\begin{bmatrix}
c_{1y}&c_{1y}&c_{1y}&c_{1y}\\
c_{2y}&c_{2y}&c_{2y}&c_{2y}\\
c_{3y}&c_{3y}&c_{3y}&c_{3y}\\
c_{4y}&c_{4y}&c_{4y}&c_{4y}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## image041

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1z}c_{1z}&c_{1z}c_{2z}&c_{1z}c_{3z}&c_{1z}c_{4z}\\
c_{2z}c_{1z}&c_{2z}c_{2z}&c_{2z}c_{3z}&c_{2z}c_{4z}\\
c_{3z}c_{1z}&c_{3z}c_{2z}&c_{3z}c_{3z}&c_{3z}c_{4z}\\
c_{4z}c_{1z}&c_{4z}c_{2z}&c_{4z}c_{3z}&c_{4z}c_{4z}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{36V}
\begin{bmatrix}
c_{1z}c_{1i}&c_{1z}c_{2i}&c_{1z}c_{3i}&c_{1z}c_{4i}\\
c_{2z}c_{1i}&c_{2z}c_{2i}&c_{2z}c_{3i}&c_{2z}c_{4i}\\
c_{3z}c_{1i}&c_{3z}c_{2i}&c_{3z}c_{3i}&c_{3z}c_{4i}\\
c_{4z}c_{1i}&c_{4z}c_{2i}&c_{4z}c_{3i}&c_{4z}c_{4i}
\end{bmatrix}\{V_z\}\\
&-\delta_{zi}\frac1{24}
\begin{bmatrix}
c_{1z}&c_{1z}&c_{1z}&c_{1z}\\
c_{2z}&c_{2z}&c_{2z}&c_{2z}\\
c_{3z}&c_{3z}&c_{3z}&c_{3z}\\
c_{4z}&c_{4z}&c_{4z}&c_{4z}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

## 集計

このバッチ: **12/12 Pass 1 OK（全て再転記）**。

これにより `fem/fem_7_2_2.html` の49数式画像は **Pass 1 = 49/49 完了**。Pass 2 は未実施（0/49）。
