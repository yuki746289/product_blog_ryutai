# fem_7_2_2 Pass 1 batch A

更新日: 2026-09-17

対象: `image007`, `image010`～`image017`

原典は `img/fem_d_momentum_tet.files/imageNNN.png`。Actionsで生成した白背景・4倍拡大画像を直接目視し、候補LaTeXと照合した。OCRによる自動判定は使用していない。

## 判定一覧

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| image007 | NG | 再転記OK | 原画像は先頭が継続等号 `=`、重み関数は4成分列ベクトルを明示。候補はLHS追加と `[N]^T` 短縮 |
| image010 | NG | 再転記OK | 候補は別内容。原画像は時間差分・対流・体積応力・境界応力・重力を含む展開式 |
| image011 | NG | 再転記OK | 原画像はx/y/zを個別展開。表面張力項は負号 |
| image012 | NG | 再転記OK | 原画像はx/y/zを個別展開。表面張力項は負号 |
| image013 | NG | 再転記OK | 原画像は粘性・圧力をx/y/zごとに個別分解。表面張力項は正号 |
| image014 | NG | 再転記OK | 原画像は内挿関数を代入した各方向の個別式 |
| image015 | NG | 再転記OK | 原画像は各方向の行列積を個別記載。末尾 `(i=1,2,3)` あり |
| image016 | NG | 再転記OK | 原画像は4x4質量行列を成分展開し「蓄積量」注記あり |
| image017 | NG | 再転記OK | 原画像はx/y/z各4x4対流行列を成分展開し「対流項」注記あり |

## image007

```latex
\[
\begin{aligned}
={}&\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial\tau}\,dV\\
&+V_x\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial X}\,dV
+V_y\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial Y}\,dV\\
&+V_z\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial Z}\,dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{xi}}{\partial X}\,dV\\
&-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{yi}}{\partial Y}\,dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{zi}}{\partial Z}\,dV\\
&-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
g_i^*\,dV
\end{aligned}
\]
```

## image010

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+V_y\int_V[N]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+V_z\int_V[N]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}\\
&+\int_V\left[\frac{\partial N}{\partial X}\right]^T\sigma^*_{xi}dV
+\int_V\left[\frac{\partial N}{\partial Y}\right]^T\sigma^*_{yi}dV
+\int_V\left[\frac{\partial N}{\partial Z}\right]^T\sigma^*_{zi}dV\\
&-\int_S[N]^T\left(\sigma^*_{xi}n_x+\sigma^*_{yi}n_y+\sigma^*_{zi}n_z\right)dS
-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

## image011 / image012

両画像は直接目視上、式本文は同一。画像寸法・描画は完全同一ではないため、画像自体を同一物とは扱わない。

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

注意: `image011` / `image012` の表面張力項は原画像では `-2K^*/We`。後続 `image013`～`image015` は `+2K^*/We` だが、原画像忠実転記では符号を統一しない。

## image013

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+V_y\int_V[N]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+V_z\int_V[N]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial V_i}{\partial X}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial V_x}{\partial X_i}dV
-\int_V\left[\frac{\partial N}{\partial X}\right]^T\delta_{xi}P\,dV\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial V_i}{\partial Y}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial V_y}{\partial X_i}dV
-\int_V\left[\frac{\partial N}{\partial Y}\right]^T\delta_{yi}P\,dV\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T\frac{\partial V_i}{\partial Z}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T\frac{\partial V_z}{\partial X_i}dV
-\int_V\left[\frac{\partial N}{\partial Z}\right]^T\delta_{zi}P\,dV\\
&+\frac{2K^*}{We}n_i\int_S[N]^T dS
-g_i^*\int_V[N]^T dV
\end{aligned}
\]
```

## image014

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+V_y\int_V[N]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+V_z\int_V[N]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T
\frac{\partial[N]\{V_i\}}{\partial X}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T
\frac{\partial[N]\{V_x\}}{\partial X_i}dV
-\delta_{xi}\int_V\left[\frac{\partial N}{\partial X}\right]^T[N]\{P\}dV\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T
\frac{\partial[N]\{V_i\}}{\partial Y}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T
\frac{\partial[N]\{V_y\}}{\partial X_i}dV
-\delta_{yi}\int_V\left[\frac{\partial N}{\partial Y}\right]^T[N]\{P\}dV\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T
\frac{\partial[N]\{V_i\}}{\partial Z}dV
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T
\frac{\partial[N]\{V_z\}}{\partial X_i}dV
-\delta_{zi}\int_V\left[\frac{\partial N}{\partial Z}\right]^T[N]\{P\}dV\\
&+\frac{2K^*}{We}n_i\int_S[N]^T dS
-g_i^*\int_V[N]^T dV
\end{aligned}
\]
```

## image015

```latex
\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+V_y\int_V[N]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+V_z\int_V[N]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T\left[\frac{\partial N}{\partial X}\right]dV\{V_i\}
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial X}\right]^T\left[\frac{\partial N}{\partial X_i}\right]dV\{V_x\}
-\delta_{xi}\int_V\left[\frac{\partial N}{\partial X}\right]^T[N]dV\{P\}\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T\left[\frac{\partial N}{\partial Y}\right]dV\{V_i\}
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Y}\right]^T\left[\frac{\partial N}{\partial X_i}\right]dV\{V_y\}
-\delta_{yi}\int_V\left[\frac{\partial N}{\partial Y}\right]^T[N]dV\{P\}\\
&+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T\left[\frac{\partial N}{\partial Z}\right]dV\{V_i\}
+\frac1{Re}\int_V\left[\frac{\partial N}{\partial Z}\right]^T\left[\frac{\partial N}{\partial X_i}\right]dV\{V_z\}
-\delta_{zi}\int_V\left[\frac{\partial N}{\partial Z}\right]^T[N]dV\{P\}\\
&+\frac{2K^*}{We}n_i\int_S[N]^T dS
-g_i^*\int_V[N]^T dV,
\qquad (i=1,2,3)
\end{aligned}
\]
```

## image016

原画像には式の右上に `蓄積量` の注記枠がある。

```latex
\[
=\int_V
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3&N_1N_4\\
N_2N_1&N_2N_2&N_2N_3&N_2N_4\\
N_3N_1&N_3N_2&N_3N_3&N_3N_4\\
N_4N_1&N_4N_2&N_4N_3&N_4N_4
\end{bmatrix}
dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```

注記: `蓄積量`

## image017

原画像には式の右上に `対流項` の注記枠がある。

```latex
\[
\begin{aligned}
&+V_x\int_V
\begin{bmatrix}
N_1\frac{\partial N_1}{\partial X}&N_1\frac{\partial N_2}{\partial X}&N_1\frac{\partial N_3}{\partial X}&N_1\frac{\partial N_4}{\partial X}\\
N_2\frac{\partial N_1}{\partial X}&N_2\frac{\partial N_2}{\partial X}&N_2\frac{\partial N_3}{\partial X}&N_2\frac{\partial N_4}{\partial X}\\
N_3\frac{\partial N_1}{\partial X}&N_3\frac{\partial N_2}{\partial X}&N_3\frac{\partial N_3}{\partial X}&N_3\frac{\partial N_4}{\partial X}\\
N_4\frac{\partial N_1}{\partial X}&N_4\frac{\partial N_2}{\partial X}&N_4\frac{\partial N_3}{\partial X}&N_4\frac{\partial N_4}{\partial X}
\end{bmatrix}dV\{V_i\}\\
&+V_y\int_V
\begin{bmatrix}
N_1\frac{\partial N_1}{\partial Y}&N_1\frac{\partial N_2}{\partial Y}&N_1\frac{\partial N_3}{\partial Y}&N_1\frac{\partial N_4}{\partial Y}\\
N_2\frac{\partial N_1}{\partial Y}&N_2\frac{\partial N_2}{\partial Y}&N_2\frac{\partial N_3}{\partial Y}&N_2\frac{\partial N_4}{\partial Y}\\
N_3\frac{\partial N_1}{\partial Y}&N_3\frac{\partial N_2}{\partial Y}&N_3\frac{\partial N_3}{\partial Y}&N_3\frac{\partial N_4}{\partial Y}\\
N_4\frac{\partial N_1}{\partial Y}&N_4\frac{\partial N_2}{\partial Y}&N_4\frac{\partial N_3}{\partial Y}&N_4\frac{\partial N_4}{\partial Y}
\end{bmatrix}dV\{V_i\}\\
&+V_z\int_V
\begin{bmatrix}
N_1\frac{\partial N_1}{\partial Z}&N_1\frac{\partial N_2}{\partial Z}&N_1\frac{\partial N_3}{\partial Z}&N_1\frac{\partial N_4}{\partial Z}\\
N_2\frac{\partial N_1}{\partial Z}&N_2\frac{\partial N_2}{\partial Z}&N_2\frac{\partial N_3}{\partial Z}&N_2\frac{\partial N_4}{\partial Z}\\
N_3\frac{\partial N_1}{\partial Z}&N_3\frac{\partial N_2}{\partial Z}&N_3\frac{\partial N_3}{\partial Z}&N_3\frac{\partial N_4}{\partial Z}\\
N_4\frac{\partial N_1}{\partial Z}&N_4\frac{\partial N_2}{\partial Z}&N_4\frac{\partial N_3}{\partial Z}&N_4\frac{\partial N_4}{\partial Z}
\end{bmatrix}dV\{V_i\}
\end{aligned}
\]
```

注記: `対流項`

## 集計

このバッチ: **9/9 Pass 1 OK（全て再転記）**。

既存Pass 1 16式と合わせ、`fem_7_2_2` の実効Pass 1は **25/49**。残りは **24式** (`image018`～`image041` のうち未監査分)。
