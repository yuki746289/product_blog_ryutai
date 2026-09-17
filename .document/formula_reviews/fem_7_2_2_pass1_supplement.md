# fem_7_2_2 Pass 1 補足転記

更新日: 2026-09-18

`fem_7_2_2` は既に Pass 1 = 49/49 完了しているが、監査HTML再生成に必要な忠実LaTeX全文が作業記録上で省略されていた `image012`, `image020`, `image025`, `image026`, `image027` を補完する。

原典は `img/fem_d_momentum_tet.files/imageNNN.png`。`image020`, `025`, `026`, `027` は白背景・8倍拡大した元PNGを再目視した。理論上の簡略化・外積記法への置換は行わない。

## image012

`image011` と式本文が同一であることを元画像目視で確認済み。画像自体は別ファイルとして扱う。

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+V_y\int_V[N]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+V_z\int_V[N]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}\\
&+\int_V\left[\frac{\partial N}{\partial X}\right]^T
\left\{-\delta_{xi}P+\frac{1}{Re}\left(\frac{\partial V_i}{\partial X}+\frac{\partial V_x}{\partial X_i}\right)\right\}dV\\
&+\int_V\left[\frac{\partial N}{\partial Y}\right]^T
\left\{-\delta_{yi}P+\frac{1}{Re}\left(\frac{\partial V_i}{\partial Y}+\frac{\partial V_y}{\partial X_i}\right)\right\}dV\\
&+\int_V\left[\frac{\partial N}{\partial Z}\right]^T
\left\{-\delta_{zi}P+\frac{1}{Re}\left(\frac{\partial V_i}{\partial Z}+\frac{\partial V_z}{\partial X_i}\right)\right\}dV\\
&-\frac{2K^*}{We}n_i\int_S[N]^T dS
-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

## image020

元画像注記: `粘性項の z 成分`、`圧力項の z 成分`。

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_1}{\partial Z}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_2}{\partial Z}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_3}{\partial Z}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_4}{\partial Z}\\
\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_1}{\partial Z}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_2}{\partial Z}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_3}{\partial Z}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_4}{\partial Z}\\
\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_1}{\partial Z}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_2}{\partial Z}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_3}{\partial Z}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_4}{\partial Z}\\
\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_1}{\partial Z}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_2}{\partial Z}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_3}{\partial Z}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_4}{\partial Z}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_1}{\partial X_i}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_2}{\partial X_i}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_3}{\partial X_i}&\dfrac{\partial N_1}{\partial Z}\dfrac{\partial N_4}{\partial X_i}\\
\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_1}{\partial X_i}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_2}{\partial X_i}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_3}{\partial X_i}&\dfrac{\partial N_2}{\partial Z}\dfrac{\partial N_4}{\partial X_i}\\
\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_1}{\partial X_i}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_2}{\partial X_i}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_3}{\partial X_i}&\dfrac{\partial N_3}{\partial Z}\dfrac{\partial N_4}{\partial X_i}\\
\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_1}{\partial X_i}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_2}{\partial X_i}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_3}{\partial X_i}&\dfrac{\partial N_4}{\partial Z}\dfrac{\partial N_4}{\partial X_i}
\end{bmatrix}dV\{V_z\}\\
&-\delta_{zi}\int_V
\begin{bmatrix}
\dfrac{\partial N_1}{\partial Z}N_1&\dfrac{\partial N_1}{\partial Z}N_2&\dfrac{\partial N_1}{\partial Z}N_3&\dfrac{\partial N_1}{\partial Z}N_4\\
\dfrac{\partial N_2}{\partial Z}N_1&\dfrac{\partial N_2}{\partial Z}N_2&\dfrac{\partial N_2}{\partial Z}N_3&\dfrac{\partial N_2}{\partial Z}N_4\\
\dfrac{\partial N_3}{\partial Z}N_1&\dfrac{\partial N_3}{\partial Z}N_2&\dfrac{\partial N_3}{\partial Z}N_3&\dfrac{\partial N_3}{\partial Z}N_4\\
\dfrac{\partial N_4}{\partial Z}N_1&\dfrac{\partial N_4}{\partial Z}N_2&\dfrac{\partial N_4}{\partial Z}N_3&\dfrac{\partial N_4}{\partial Z}N_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

## image025

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}&c_{1x}c_{4x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}&c_{2x}c_{4x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}&c_{3x}c_{4x}\\
c_{4x}c_{1x}&c_{4x}c_{2x}&c_{4x}c_{3x}&c_{4x}c_{4x}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}&c_{1x}c_{4i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}&c_{2x}c_{4i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}&c_{3x}c_{4i}\\
c_{4x}c_{1i}&c_{4x}c_{2i}&c_{4x}c_{3i}&c_{4x}c_{4i}
\end{bmatrix}dV\{V_x\}\\
&-\delta_{xi}\int_V\frac1{6V}
\begin{bmatrix}
c_{1x}L_1&c_{1x}L_2&c_{1x}L_3&c_{1x}L_4\\
c_{2x}L_1&c_{2x}L_2&c_{2x}L_3&c_{2x}L_4\\
c_{3x}L_1&c_{3x}L_2&c_{3x}L_3&c_{3x}L_4\\
c_{4x}L_1&c_{4x}L_2&c_{4x}L_3&c_{4x}L_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

## image026

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}&c_{1y}c_{4y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}&c_{2y}c_{4y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}&c_{3y}c_{4y}\\
c_{4y}c_{1y}&c_{4y}c_{2y}&c_{4y}c_{3y}&c_{4y}c_{4y}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}&c_{1y}c_{4i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}&c_{2y}c_{4i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}&c_{3y}c_{4i}\\
c_{4y}c_{1i}&c_{4y}c_{2i}&c_{4y}c_{3i}&c_{4y}c_{4i}
\end{bmatrix}dV\{V_y\}\\
&-\delta_{yi}\int_V\frac1{6V}
\begin{bmatrix}
c_{1y}L_1&c_{1y}L_2&c_{1y}L_3&c_{1y}L_4\\
c_{2y}L_1&c_{2y}L_2&c_{2y}L_3&c_{2y}L_4\\
c_{3y}L_1&c_{3y}L_2&c_{3y}L_3&c_{3y}L_4\\
c_{4y}L_1&c_{4y}L_2&c_{4y}L_3&c_{4y}L_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

## image027

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1z}c_{1z}&c_{1z}c_{2z}&c_{1z}c_{3z}&c_{1z}c_{4z}\\
c_{2z}c_{1z}&c_{2z}c_{2z}&c_{2z}c_{3z}&c_{2z}c_{4z}\\
c_{3z}c_{1z}&c_{3z}c_{2z}&c_{3z}c_{3z}&c_{3z}c_{4z}\\
c_{4z}c_{1z}&c_{4z}c_{2z}&c_{4z}c_{3z}&c_{4z}c_{4z}
\end{bmatrix}dV\{V_i\}\\
&+\frac1{Re}\int_V\frac1{36V^2}
\begin{bmatrix}
c_{1z}c_{1i}&c_{1z}c_{2i}&c_{1z}c_{3i}&c_{1z}c_{4i}\\
c_{2z}c_{1i}&c_{2z}c_{2i}&c_{2z}c_{3i}&c_{2z}c_{4i}\\
c_{3z}c_{1i}&c_{3z}c_{2i}&c_{3z}c_{3i}&c_{3z}c_{4i}\\
c_{4z}c_{1i}&c_{4z}c_{2i}&c_{4z}c_{3i}&c_{4z}c_{4i}
\end{bmatrix}dV\{V_z\}\\
&-\delta_{zi}\int_V\frac1{6V}
\begin{bmatrix}
c_{1z}L_1&c_{1z}L_2&c_{1z}L_3&c_{1z}L_4\\
c_{2z}L_1&c_{2z}L_2&c_{2z}L_3&c_{2z}L_4\\
c_{3z}L_1&c_{3z}L_2&c_{3z}L_3&c_{3z}L_4\\
c_{4z}L_1&c_{4z}L_2&c_{4z}L_3&c_{4z}L_4
\end{bmatrix}dV\{P\}
\end{aligned}
\]
```

以上5式を再監査HTML生成用の忠実LaTeX正本として追記する。