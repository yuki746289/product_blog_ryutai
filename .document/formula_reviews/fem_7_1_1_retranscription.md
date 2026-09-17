# 元画像忠実転記ドラフト: fem/fem_7_1_1.html

作成日: 2026-09-17

## 位置づけ

このファイルは `fem/fem_7_1_1.html` の元数式画像を、**数学的な訂正・一般化・簡略化を行わず**LaTeXへ再転記するための作業ドラフトである。

- 通常ページへは未反映。
- `image011` は元画像の直接目視が未完了のため保留。
- 以下の転記も、監査候補HTMLへ反映後に再度Pass 1を行う。
- 原画像側に誤記と思われる表記があっても、この原文転記では修正しない。

## image001

元画像上の対流項は小文字 `x/y`、発散項は大文字 `X/Y`。

```latex
\[
\phi=
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
\right)=0
\]
```

## image002

元画像は積分領域 `V,dV`。列ベクトル第2成分も原画像どおり `N_1` とする。

```latex
\[
\int_V[N]^T\phi\,dV
=
\int_V
\begin{bmatrix}
N_1\\
N_1\\
N_3
\end{bmatrix}
\phi\,dV
=
\int_V
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
dV
=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}
\]
```

## image003

```latex
\[
\begin{aligned}
V_x
&=N_1V_{x1}+N_2V_{x2}+N_3V_{x3}\\
&=
\begin{bmatrix}
N_1\\N_2\\N_3
\end{bmatrix}
\{V_{x1}\;V_{x2}\;V_{x3}\}\\
&=[N]^T\{V_x\},\\[4pt]
V_y&=[N]^T\{V_y\},\\
P&=[N]^T\{P\}.
\end{aligned}
\]
```

## image004

```latex
\[
\int_S[N]^T\phi\,dS
=
\int_S[N]^T\left\{
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
\right)
\right\}dS
\]
```

## image005

元画像では、この段階から空間微分が大文字 `X/Y` 表記になっている。

```latex
\[
\begin{aligned}
={}&
\int_S[N]^T\frac{\partial P}{\partial\tau}\,dS
+\int_S[N]^TV_x\frac{\partial P}{\partial X}\,dS
+\int_S[N]^TV_y\frac{\partial P}{\partial Y}\,dS\\
&+\frac{1}{Ma^2}\int_S[N]^T\frac{\partial V_x}{\partial X}\,dS
+\frac{1}{Ma^2}\int_S[N]^T\frac{\partial V_y}{\partial Y}\,dS
\end{aligned}
\]
```

## image006

時刻添字は原画像どおり `\Delta\tau+\tau` の順序を維持する。

```latex
\[
\begin{aligned}
={}&
\int_S[N]^T[N]dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S[N]^T
\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial X}dS
+V_y\int_S[N]^T
\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial Y}dS\\
&+\frac{1}{Ma^2}\int_S[N]^T
\frac{\partial[N]\{V_x\}^{\Delta\tau+\tau}}{\partial X}dS
+\frac{1}{Ma^2}\int_S[N]^T
\frac{\partial[N]\{V_y\}^{\Delta\tau+\tau}}{\partial Y}dS
\end{aligned}
\]
```

## image007

```latex
\[
\begin{aligned}
={}&
\int_S[N]^T[N]dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,
\{P\}^{\Delta\tau+\tau}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,
\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,
\{V_x\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,
\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image008

```latex
\[
\begin{aligned}
={}&
\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}N_1&N_2&N_3\end{bmatrix}
dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial X}&
\dfrac{\partial N_2}{\partial X}&
\dfrac{\partial N_3}{\partial X}
\end{bmatrix}
dS\,\{P\}^{\Delta\tau+\tau}\\
&+V_y\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Y}&
\dfrac{\partial N_2}{\partial Y}&
\dfrac{\partial N_3}{\partial Y}
\end{bmatrix}
dS\,\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial X}&
\dfrac{\partial N_2}{\partial X}&
\dfrac{\partial N_3}{\partial X}
\end{bmatrix}
dS\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Y}&
\dfrac{\partial N_2}{\partial Y}&
\dfrac{\partial N_3}{\partial Y}
\end{bmatrix}
dS\,\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image009

```latex
\[
\begin{aligned}
={}&
\int_S
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3\\
N_2N_1&N_2N_2&N_2N_3\\
N_3N_1&N_3N_2&N_3N_3
\end{bmatrix}
dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial X}&N_1\dfrac{\partial N_2}{\partial X}&N_1\dfrac{\partial N_3}{\partial X}\\
N_2\dfrac{\partial N_1}{\partial X}&N_2\dfrac{\partial N_2}{\partial X}&N_2\dfrac{\partial N_3}{\partial X}\\
N_3\dfrac{\partial N_1}{\partial X}&N_3\dfrac{\partial N_2}{\partial X}&N_3\dfrac{\partial N_3}{\partial X}
\end{bmatrix}
dS\,\{V_x\}^{\Delta\tau+\tau}\\
&+V_y\int_S
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Y}&N_1\dfrac{\partial N_2}{\partial Y}&N_1\dfrac{\partial N_3}{\partial Y}\\
N_2\dfrac{\partial N_1}{\partial Y}&N_2\dfrac{\partial N_2}{\partial Y}&N_2\dfrac{\partial N_3}{\partial Y}\\
N_3\dfrac{\partial N_1}{\partial Y}&N_3\dfrac{\partial N_2}{\partial Y}&N_3\dfrac{\partial N_3}{\partial Y}
\end{bmatrix}
dS\,\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

> 注: `image009` の元画像では対流項末尾が `{V_x}`, `{V_y}` と読める。理論上 `{P}` が自然に見えても原文転記では変更しない。再照合必須。

## image010

```latex
\[
\begin{aligned}
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial X}&N_1\dfrac{\partial N_2}{\partial X}&N_1\dfrac{\partial N_3}{\partial X}\\
N_2\dfrac{\partial N_1}{\partial X}&N_2\dfrac{\partial N_2}{\partial X}&N_2\dfrac{\partial N_3}{\partial X}\\
N_3\dfrac{\partial N_1}{\partial X}&N_3\dfrac{\partial N_2}{\partial X}&N_3\dfrac{\partial N_3}{\partial X}
\end{bmatrix}
dS\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}
N_1\dfrac{\partial N_1}{\partial Y}&N_1\dfrac{\partial N_2}{\partial Y}&N_1\dfrac{\partial N_3}{\partial Y}\\
N_2\dfrac{\partial N_1}{\partial Y}&N_2\dfrac{\partial N_2}{\partial Y}&N_2\dfrac{\partial N_3}{\partial Y}\\
N_3\dfrac{\partial N_1}{\partial Y}&N_3\dfrac{\partial N_2}{\partial Y}&N_3\dfrac{\partial N_3}{\partial Y}
\end{bmatrix}
dS\,\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image011

**HOLD** — 元画像を直接表示して再監査するまで転記しない。

## image012

元画像末尾に、`{V_x}^{Δτ+τ}` の直後へ単独の `3` が表示されている。誤記候補だが原文転記では残す。

```latex
\[
\begin{aligned}
={}&\int_S
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3\\
L_2L_1&L_2L_2&L_2L_3\\
L_3L_1&L_3L_2&L_3L_3
\end{bmatrix}dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S\frac{1}{2A}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}
\end{bmatrix}dS\,\{P\}^{\Delta\tau+\tau}\\
&+V_y\int_S\frac{1}{2A}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}
\end{bmatrix}dS\,\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\int_S\frac{1}{2A}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}
\end{bmatrix}dS\,\{V_x\}^{\Delta\tau+\tau}3\\
&+\frac{1}{Ma^2}\int_S\frac{1}{2A}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}
\end{bmatrix}dS\,\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image013

原画像の `i=j` 側途中式に `V` が含まれる。誤記候補でもそのまま保持する。

```latex
\[
\int_S L_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2A
\]

\[
\int_S L_iL_j\,dS=
\begin{cases}
\dfrac{1!1!}{(1+1+2)!}\,2A
=\dfrac{2}{4!}A
=\dfrac{1}{12}A &(i\ne j),\\[8pt]
\dfrac{2!}{(1+1+2)!}\,2A
=\dfrac{4}{4!}V
=\dfrac{1}{6}A &(i=j)
\end{cases}
\]

\[
\int_S L_i\,dS
=\frac{1!}{(1+2)!}\,2A
=\frac{2}{3!}A
=\frac{1}{3}A
\]
```

## image014

```latex
\[
\begin{aligned}
={}&\frac{A}{12}
\begin{bmatrix}
2&1&1\\1&2&1\\1&1&2
\end{bmatrix}
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\frac{1}{2A}\frac{A}{3}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+V_y\frac{1}{2A}\frac{A}{3}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\frac{1}{2A}\frac{A}{3}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{V_x\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\frac{1}{2A}\frac{A}{3}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image015

```latex
\[
\begin{aligned}
={}&\frac{A}{12}
\begin{bmatrix}
2&1&1\\1&2&1\\1&1&2
\end{bmatrix}
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\frac{1}{6}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+V_y\frac{1}{6}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\frac{1}{6}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{V_x\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}\frac{1}{6}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image016

```latex
\[
\begin{aligned}
={}&[C]
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}\\
&+\frac{1}{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## image017

```latex
\[
=\begin{bmatrix}0\\0\\0\end{bmatrix}
\]
```

## image018

元画像右辺は列ベクトルへの展開ではなく `[0]` 表記。

```latex
\[
[C]\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
=[0]
\]
```

## image020

```latex
\[
\frac{[C]}{\Delta\tau}\{P\}^{\Delta\tau+\tau}
+V_x[C_x]\{P\}^{\Delta\tau+\tau}
+V_y[C_y]\{P\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}[C_x]\{V_x\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}[C_y]\{V_y\}^{\Delta\tau+\tau}
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}
\]
```

## image021

```latex
\[
\left(
\frac{[C]}{\Delta\tau}
+V_x[C_x]
+V_y[C_y]
\right)\{P\}^{\Delta\tau+\tau}
+\frac{1}{Ma^2}\left(
[C_x]\{V_x\}^{\Delta\tau+\tau}
+[C_y]\{V_y\}^{\Delta\tau+\tau}
\right)
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}
\]
```

## 次工程

1. `image011` を元画像で直接確認して転記する。
2. 本ドラフト19式を元画像と再照合し、転記ミスを0件にする。
3. 監査候補HTMLへ反映する。
4. 修正後の監査候補についてPass 1を20/20再実施する。
5. Pass 1合格後のみPass 2へ進む。
