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

## image008～image012

**HOLD** — 元画像直接確認後に転記する。

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

## image014～image015

**HOLD** — 元画像直接確認後に転記する。

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
- 現監査候補のPass 1目視監査: **13/20**
- 現監査候補の合格: **0/20**
- 元画像忠実再転記ドラフト: **13/20**
- 未転記: **7/20** (`image008～012`, `image014～015`)
- 再転記版の再Pass 1: 未実施
- Pass 2: **0/20**
