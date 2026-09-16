# LaTeX変換ドラフト: fem/fem_7_2_1.html

## 対象

- ページ: `fem/fem_7_2_1.html`
- 画像: `img/fem_d_mass_tet.files/image001.png` ～ `image020.png`
- 数学レビュー: `fem_7_2_1_review.md` で確認済み
- 方針: 原式と数学的に同値な範囲で、反復する巨大行列は記号定義を用いて可読化する。

## 共通記号

\[
[N]=\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix},\qquad
\{P\}=\begin{bmatrix}P_1&P_2&P_3&P_4\end{bmatrix}^T
\]

\[
\{V_x\}=\begin{bmatrix}V_{x1}&V_{x2}&V_{x3}&V_{x4}\end{bmatrix}^T
\]

`V_y`, `V_z` も同様。

## image001

\[
\phi=
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+V_z\frac{\partial P}{\partial z}
+\frac{1}{Ma^2}
\left(
\frac{\partial V_x}{\partial x}
+\frac{\partial V_y}{\partial y}
+\frac{\partial V_z}{\partial z}
\right)=0
\]

## image002

\[
\int_V[N]^T\phi\,dV
=\int_V\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}\phi\,dV
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]

## image003

\[
\begin{aligned}
V_x&=[N]\{V_x\},\\
V_y&=[N]\{V_y\},\\
V_z&=[N]\{V_z\},\\
P&=[N]\{P\}.
\end{aligned}
\]

## image004

\[
\int_V[N]^T\phi\,dV
=
\int_V[N]^T\left[
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial X}
+V_y\frac{\partial P}{\partial Y}
+V_z\frac{\partial P}{\partial Z}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
+\frac{\partial V_z}{\partial Z}
\right)
\right]dV
\]

## image005

各項へ分解する。

\[
\begin{aligned}
\int_V[N]^T\phi\,dV={}&
\int_V[N]^T\frac{\partial P}{\partial\tau}\,dV
+\int_V[N]^TV_x\frac{\partial P}{\partial X}\,dV
+\int_V[N]^TV_y\frac{\partial P}{\partial Y}\,dV\\
&+\int_V[N]^TV_z\frac{\partial P}{\partial Z}\,dV
+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_x}{\partial X}\,dV
+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_y}{\partial Y}\,dV\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_z}{\partial Z}\,dV.
\end{aligned}
\]

## image006

時間差分と形状関数内挿を代入する。

\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{P\}^{\tau+\Delta\tau}
+V_y\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{P\}^{\tau+\Delta\tau}\\
&+V_z\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{V_y\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{V_z\}^{\tau+\Delta\tau}.
\end{aligned}
\]

## image007

節点自由度は積分変数に依存しないので積分外へ出す。対流係数の `V_x,V_y,V_z` は既知値として扱う線形化を前提とする。

式は image006 と同値。

## image008

形状関数を列・行ベクトルで明示する。

\[
[N]^T[N]
=\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix}
\]

\[
[N]^T\frac{\partial[N]}{\partial X}
=\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\partial N_1/\partial X&\partial N_2/\partial X&\partial N_3/\partial X&\partial N_4/\partial X
\end{bmatrix}
\]

`Y`, `Z` も同様。

## image009 / image010

外積を4×4行列として展開する。

\[
[N]^T[N]=
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3&N_1N_4\\
N_2N_1&N_2N_2&N_2N_3&N_2N_4\\
N_3N_1&N_3N_2&N_3N_3&N_3N_4\\
N_4N_1&N_4N_2&N_4N_3&N_4N_4
\end{bmatrix}
\]

\[
[N]^T\frac{\partial[N]}{\partial X}=
\begin{bmatrix}
N_1N_{1,X}&N_1N_{2,X}&N_1N_{3,X}&N_1N_{4,X}\\
N_2N_{1,X}&N_2N_{2,X}&N_2N_{3,X}&N_2N_{4,X}\\
N_3N_{1,X}&N_3N_{2,X}&N_3N_{3,X}&N_3N_{4,X}\\
N_4N_{1,X}&N_4N_{2,X}&N_4N_{3,X}&N_4N_{4,X}
\end{bmatrix}
\]

`Y`, `Z` も同様。image009 は圧力時間項・対流項、image010 は速度発散項にこの行列を適用している。

## image011

四面体一次要素では `N_i=L_i` とする。

\[
[L]=\begin{bmatrix}L_1&L_2&L_3&L_4\end{bmatrix}
\]

従って image009 / image010 の `N_i` を `L_i` へ置換する。

## image012

形状関数微分は

\[
\frac{\partial L_j}{\partial X}=\frac{c_{jx}}{6V},\qquad
\frac{\partial L_j}{\partial Y}=\frac{c_{jy}}{6V},\qquad
\frac{\partial L_j}{\partial Z}=\frac{c_{jz}}{6V}.
\]

よって

\[
[L]^T\frac{\partial[L]}{\partial X}
=\frac1{6V}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}&L_1c_{4x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}&L_2c_{4x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}&L_3c_{4x}\\
L_4c_{1x}&L_4c_{2x}&L_4c_{3x}&L_4c_{4x}
\end{bmatrix}
\]

`Y`, `Z` も同様。

## image013

\[
\int_VL_1^pL_2^qL_3^rL_4^s\,dV
=\frac{p!q!r!s!}{(p+q+r+s+3)!}\,6V
\]

従って

\[
\int_VL_iL_j\,dV=
\begin{cases}
V/20,&i\ne j,\\
V/10,&i=j,
\end{cases}
\qquad
\int_VL_i\,dV=V/4.
\]

## image014

積分を適用する。質量項は

\[
\frac{V}{20}
\begin{bmatrix}
2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2
\end{bmatrix}
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}.
\]

また

\[
\int_V[L]^T\frac{\partial[L]}{\partial X}dV
=\frac{1}{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}.
\]

`Y`, `Z` も同様。

## image015

`(1/(6V))(V/4)=1/24` より、

\[
[C_x]=\frac1{24}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix},
\]

`[C_y]`, `[C_z]` も各 `c_{jy}`, `c_{jz}` を用いて同様に定義する。

## image016

\[
\begin{aligned}
={}&[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}.
\end{aligned}
\]

ここで

\[
[C]=\frac{V}{20}
\begin{bmatrix}
2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2
\end{bmatrix}.
\]

## image017

\[
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]

## image018

\[
\begin{aligned}
[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
&+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}=0.
\end{aligned}
\]

## image019

既知時刻 `τ` の圧力項を右辺へ移す。

\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{P\}^{\tau+\Delta\tau}
&+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\end{aligned}
\]

## image020

`{P}^{τ+Δτ}` をまとめる。

\[
\begin{aligned}
\left(
\frac{[C]}{\Delta\tau}
+V_x[C_x]+V_y[C_y]+V_z[C_z]
\right)\{P\}^{\tau+\Delta\tau}
&+\frac1{Ma^2}\left(
[C_x]\{V_x\}^{\tau+\Delta\tau}
+[C_y]\{V_y\}^{\tau+\Delta\tau}
+[C_z]\{V_z\}^{\tau+\Delta\tau}
\right)\\
&=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\end{aligned}
\]

## 整合性確認

- image001 → image005: PDEを重み付き残差へ代入して項分解しており整合。
- image006 → image007: 節点ベクトルを積分外へ出しただけで整合。対流係数速度は既知値として扱う前提を本文に追記済み。
- image008 → image012: 外積展開、`N_i=L_i`、`∂L_j/∂X=c_{jx}/(6V)` の順で整合。
- image013 → image015: 四面体一次要素の標準体積積分から `V/20`, `V/10`, `V/4`, `1/24` が導かれる。
- image016 → image020: 行列略記、残差=0、既知項移項、未知圧力ベクトルのくくり出しが整合。
- `1/Ma^2` は x/y/z の速度発散3項すべてに保持する。

## HTML置換条件

- HTMLはCP932維持。
- 元画像ファイルは削除しない。
- 各数式ブロックへ `data-source-image` を付与する。
- 長い式は `.math-block` 内だけ横スクロールさせる。
- PC/スマホでMathJax描画を確認する。
