# 元画像忠実転記ドラフト: fem/fem_7_2_1.html

作成日: 2026-09-17
更新日: 2026-09-17

## 位置づけ

`fem/fem_7_2_1.html` の元数式画像を、**数学的な訂正・一般化・簡略化を行わず**LaTeXへ再転記する作業ドラフト。

- 通常ページへは未反映。
- 元画像を直接目視できた式だけ転記する。
- 原画像側に不自然な表記があっても原文転記では修正しない。
- 全20式の転記後にPass 1を再実施し、その後実ブラウザPass 2を行う。

## image001

```latex
\[
\phi=
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+V_z\frac{\partial P}{\partial z}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
+\frac{\partial V_z}{\partial Z}
\right)=0
\]
```

## image002

```latex
\[
\int_V[N]^T\phi\,dV
=\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}\phi\,dV
=\int_V
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}dV
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]
```

## image003

```latex
\[
\begin{aligned}
V_x
&=N_1V_{x1}+N_2V_{x2}+N_3V_{x3}+N_4V_{x4}\\
&=\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{Bmatrix}V_{x1}&V_{x2}&V_{x3}&V_{x4}\end{Bmatrix}\\
&=[N]^T\{V_x\},\\
V_y&=[N]^T\{V_y\},\\
V_z&=[N]^T\{V_z\},\\
P&=[N]^T\{P\}.
\end{aligned}
\]
```

## image004

```latex
\[
\int_V[N]^T\phi\,dV
=\int_V[N]^T\left\{
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+V_z\frac{\partial P}{\partial z}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
+\frac{\partial V_z}{\partial Z}
\right)
\right\}dV
\]
```

## image005

```latex
\[
\begin{aligned}
={}&\int_V[N]^T\frac{\partial P}{\partial\tau}\,dV
+\int_V[N]^TV_x\frac{\partial P}{\partial X}\,dV
+\int_V[N]^TV_y\frac{\partial P}{\partial Y}\,dV
+\int_V[N]^TV_z\frac{\partial P}{\partial Z}\,dV\\
&+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial V_x}{\partial X}\,dV
+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial V_y}{\partial Y}\,dV
+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial V_z}{\partial Z}\,dV
\end{aligned}
\]
```

## image006

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial Y}dV\\
&+V_z\int_V[N]^T\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial Z}dV\\
&+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_x\}^{\Delta\tau+\tau}}{\partial X}dV
+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_y\}^{\Delta\tau+\tau}}{\partial Y}dV\\
&+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_z\}^{\Delta\tau+\tau}}{\partial Z}dV
\end{aligned}
\]
```

## image007

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{P\}^{\Delta\tau+\tau}
+V_y\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_z\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{V_x\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image008

元画像は行列積を省略せず、7項を明示している。

```latex
\[
\begin{aligned}
={}&\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix}dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial X}&
\dfrac{\partial N_2}{\partial X}&
\dfrac{\partial N_3}{\partial X}&
\dfrac{\partial N_4}{\partial X}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_y\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Y}&
\dfrac{\partial N_2}{\partial Y}&
\dfrac{\partial N_3}{\partial Y}&
\dfrac{\partial N_4}{\partial Y}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_z\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Z}&
\dfrac{\partial N_2}{\partial Z}&
\dfrac{\partial N_3}{\partial Z}&
\dfrac{\partial N_4}{\partial Z}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial X}&
\dfrac{\partial N_2}{\partial X}&
\dfrac{\partial N_3}{\partial X}&
\dfrac{\partial N_4}{\partial X}
\end{bmatrix}dV\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Y}&
\dfrac{\partial N_2}{\partial Y}&
\dfrac{\partial N_3}{\partial Y}&
\dfrac{\partial N_4}{\partial Y}
\end{bmatrix}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Z}&
\dfrac{\partial N_2}{\partial Z}&
\dfrac{\partial N_3}{\partial Z}&
\dfrac{\partial N_4}{\partial Z}
\end{bmatrix}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image009

元画像は外積を4×4行列へ展開している。なお、対流3項の末尾は原画像上で `{P}` ではなく `{V_x}`, `{V_y}`, `{V_z}` と記載されているため、そのまま保持する。

```latex
\[
\begin{aligned}
={}&\int_V
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3&N_1N_4\\
N_2N_1&N_2N_2&N_2N_3&N_2N_4\\
N_3N_1&N_3N_2&N_3N_3&N_3N_4\\
N_4N_1&N_4N_2&N_4N_3&N_4N_4
\end{bmatrix}dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial X}&N_1\dfrac{\partial N_2}{\partial X}&N_1\dfrac{\partial N_3}{\partial X}&N_1\dfrac{\partial N_4}{\partial X}\\
N_2\dfrac{\partial N_1}{\partial X}&N_2\dfrac{\partial N_2}{\partial X}&N_2\dfrac{\partial N_3}{\partial X}&N_2\dfrac{\partial N_4}{\partial X}\\
N_3\dfrac{\partial N_1}{\partial X}&N_3\dfrac{\partial N_2}{\partial X}&N_3\dfrac{\partial N_3}{\partial X}&N_3\dfrac{\partial N_4}{\partial X}\\
N_4\dfrac{\partial N_1}{\partial X}&N_4\dfrac{\partial N_2}{\partial X}&N_4\dfrac{\partial N_3}{\partial X}&N_4\dfrac{\partial N_4}{\partial X}
\end{bmatrix}dV\,\{V_x\}^{\Delta\tau+\tau}\\
&+V_y\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Y}&N_1\dfrac{\partial N_2}{\partial Y}&N_1\dfrac{\partial N_3}{\partial Y}&N_1\dfrac{\partial N_4}{\partial Y}\\
N_2\dfrac{\partial N_1}{\partial Y}&N_2\dfrac{\partial N_2}{\partial Y}&N_2\dfrac{\partial N_3}{\partial Y}&N_2\dfrac{\partial N_4}{\partial Y}\\
N_3\dfrac{\partial N_1}{\partial Y}&N_3\dfrac{\partial N_2}{\partial Y}&N_3\dfrac{\partial N_3}{\partial Y}&N_3\dfrac{\partial N_4}{\partial Y}\\
N_4\dfrac{\partial N_1}{\partial Y}&N_4\dfrac{\partial N_2}{\partial Y}&N_4\dfrac{\partial N_3}{\partial Y}&N_4\dfrac{\partial N_4}{\partial Y}
\end{bmatrix}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+V_z\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Z}&N_1\dfrac{\partial N_2}{\partial Z}&N_1\dfrac{\partial N_3}{\partial Z}&N_1\dfrac{\partial N_4}{\partial Z}\\
N_2\dfrac{\partial N_1}{\partial Z}&N_2\dfrac{\partial N_2}{\partial Z}&N_2\dfrac{\partial N_3}{\partial Z}&N_2\dfrac{\partial N_4}{\partial Z}\\
N_3\dfrac{\partial N_1}{\partial Z}&N_3\dfrac{\partial N_2}{\partial Z}&N_3\dfrac{\partial N_3}{\partial Z}&N_3\dfrac{\partial N_4}{\partial Z}\\
N_4\dfrac{\partial N_1}{\partial Z}&N_4\dfrac{\partial N_2}{\partial Z}&N_4\dfrac{\partial N_3}{\partial Z}&N_4\dfrac{\partial N_4}{\partial Z}
\end{bmatrix}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image010

```latex
\[
\begin{aligned}
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial X}&N_1\dfrac{\partial N_2}{\partial X}&N_1\dfrac{\partial N_3}{\partial X}&N_1\dfrac{\partial N_4}{\partial X}\\
N_2\dfrac{\partial N_1}{\partial X}&N_2\dfrac{\partial N_2}{\partial X}&N_2\dfrac{\partial N_3}{\partial X}&N_2\dfrac{\partial N_4}{\partial X}\\
N_3\dfrac{\partial N_1}{\partial X}&N_3\dfrac{\partial N_2}{\partial X}&N_3\dfrac{\partial N_3}{\partial X}&N_3\dfrac{\partial N_4}{\partial X}\\
N_4\dfrac{\partial N_1}{\partial X}&N_4\dfrac{\partial N_2}{\partial X}&N_4\dfrac{\partial N_3}{\partial X}&N_4\dfrac{\partial N_4}{\partial X}
\end{bmatrix}dV\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Y}&N_1\dfrac{\partial N_2}{\partial Y}&N_1\dfrac{\partial N_3}{\partial Y}&N_1\dfrac{\partial N_4}{\partial Y}\\
N_2\dfrac{\partial N_1}{\partial Y}&N_2\dfrac{\partial N_2}{\partial Y}&N_2\dfrac{\partial N_3}{\partial Y}&N_2\dfrac{\partial N_4}{\partial Y}\\
N_3\dfrac{\partial N_1}{\partial Y}&N_3\dfrac{\partial N_2}{\partial Y}&N_3\dfrac{\partial N_3}{\partial Y}&N_3\dfrac{\partial N_4}{\partial Y}\\
N_4\dfrac{\partial N_1}{\partial Y}&N_4\dfrac{\partial N_2}{\partial Y}&N_4\dfrac{\partial N_3}{\partial Y}&N_4\dfrac{\partial N_4}{\partial Y}
\end{bmatrix}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Z}&N_1\dfrac{\partial N_2}{\partial Z}&N_1\dfrac{\partial N_3}{\partial Z}&N_1\dfrac{\partial N_4}{\partial Z}\\
N_2\dfrac{\partial N_1}{\partial Z}&N_2\dfrac{\partial N_2}{\partial Z}&N_2\dfrac{\partial N_3}{\partial Z}&N_2\dfrac{\partial N_4}{\partial Z}\\
N_3\dfrac{\partial N_1}{\partial Z}&N_3\dfrac{\partial N_2}{\partial Z}&N_3\dfrac{\partial N_3}{\partial Z}&N_3\dfrac{\partial N_4}{\partial Z}\\
N_4\dfrac{\partial N_1}{\partial Z}&N_4\dfrac{\partial N_2}{\partial Z}&N_4\dfrac{\partial N_3}{\partial Z}&N_4\dfrac{\partial N_4}{\partial Z}
\end{bmatrix}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image011～image012

**HOLD** — GitHub上の原画像は存在するが、この実行環境でバイナリを安定して直接表示できていないため転記しない。推測による補完は禁止する。

## image013

元画像では最終結果だけでなく階乗計算の途中式も表示されている。

```latex
\[
\int_VL_1^pL_2^qL_3^rL_4^s\,dV
=\frac{p!q!r!s!}{(p+q+r+s+3)!}\,6V
\]
\[
\int_VL_iL_j\,dV=
\begin{cases}
\dfrac{1!1!}{(1+1+3)!}\,6V
=\dfrac{6}{5!}V
=\dfrac{1}{20}V,& i\ne j,\\[6pt]
\dfrac{2!}{(1+1+3)!}\,6V
=\dfrac{12}{5!}V
=\dfrac{1}{10}V,& i=j,
\end{cases}
\]
\[
\int_VL_i\,dV
=\frac{1!}{(1+3)!}\,6V
=\frac{6}{4!}V
=\frac14V
\]
```

## image014

```latex
\[
\begin{aligned}
={}&\frac{V}{20}
\begin{bmatrix}
2&1&1&1\\
1&2&1&1\\
1&1&2&1\\
1&1&1&2
\end{bmatrix}
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{6V}\frac{V}{4}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image015

**HOLD** — 元GIF/PNGにパレット・透過情報の崩れがあり、先頭の質量行列項など一部は読めるが、式全体を1文字単位で保証できない。既存候補が元画像を大幅に要約しているため不一致判定は可能だが、忠実転記は画像復元後に行う。

## image016

```latex
\[
\begin{aligned}
={}&[C]\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}
+V_z[C_z]\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image017

```latex
\[
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]
```

## image018

```latex
\[
\begin{aligned}
[C]\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}
&+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}
+V_z[C_z]\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\Delta\tau+\tau}=0
\end{aligned}
\]
```

## image019

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{P\}^{\Delta\tau+\tau}
&+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}
+V_z[C_z]\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\Delta\tau+\tau}
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}
\end{aligned}
\]
```

## image020

```latex
\[
\begin{aligned}
\left(
\frac{[C]}{\Delta\tau}
+V_x[C_x]+V_y[C_y]+V_z[C_z]
\right)\{P\}^{\Delta\tau+\tau}
&+\frac1{Ma^2}\left(
[C_x]\{V_x\}^{\Delta\tau+\tau}
+[C_y]\{V_y\}^{\Delta\tau+\tau}
+[C_z]\{V_z\}^{\Delta\tau+\tau}
\right)\\
&=\frac{[C]}{\Delta\tau}\{P\}^{\tau}
\end{aligned}
\]
```

## 現在の状態

- 元画像との対応付け: **20/20**
- 現監査候補のPass 1比較: **18/20**
- 現監査候補の合格: **0/20**
- 現監査候補の要修正: **18/20**
- 元画像忠実再転記ドラフト: **17/20**
- 未転記/HOLD: **3/20** (`image011`, `image012`, `image015`)
- 再転記版の再Pass 1: 未実施
- Pass 2: **0/20**
