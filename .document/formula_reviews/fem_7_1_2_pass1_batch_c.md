# fem_7_1_2 厳密Pass 1 — batch C (`image029`～`image042`)

更新日: 2026-09-17

## 結果

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| `image029` | NG | **再転記OK** | 外積記法へ短縮せず反復行列を保持 |
| `image030` | NG | **再転記OK** | x方向粘性・圧力行列を全成分で保持 |
| `image031` | NG | **再転記OK** | y方向粘性・圧力行列を全成分で保持 |
| `image032` | NG | **再転記OK** | 原画像係数 `2K^*/We` と2成分列ベクトルを保持 |
| `image033` | OK | **OK** | 元画像と一致 |
| `image034` | NG | **再転記OK** | 対流行列を反復行列のまま保持 |
| `image035` | NG | **再転記OK** | x方向行列を全成分で保持 |
| `image036` | NG | **再転記OK** | y方向行列を全成分で保持 |
| `image037` | NG | **再転記OK** | 先頭は継続等号。`b_L` を使わず `2K^*/We` の2成分項を保持 |
| `image038` | NG | **再転記OK** | 原文 `i=1,2,3` と3成分零ベクトルを保持 |
| `image039` | NG | **再転記OK** | `b_L` を除去し原画像の2成分表面張力項を保持 |
| `image040` | NG | **再転記OK** | 右辺表面張力係数を原画像どおり復元 |
| `image041` | NG | **再転記OK** | 圧力項を `1/Re` の外へ復元。`2K^*/We` を保持 |
| `image042` | NG | **再転記OK** | y成分も圧力項を `1/Re` の外へ復元 |

**batch C: 14/14 Pass 1 OK。**

## 元画像忠実LaTeX

### `image029`

```latex
\[
\begin{aligned}
&+V_x\frac1{2A}\frac{A}{3}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{V_i\}\\
&+V_y\frac1{2A}\frac{A}{3}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{V_i\}
\end{aligned}
\]
```

### `image030`

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{4A^2}A
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{4A^2}A
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}
\end{bmatrix}\{V_x\}\\
&-\delta_{xi}\frac1{2A}\frac{A}{3}
\begin{bmatrix}
c_{1x}&c_{1x}&c_{1x}\\
c_{2x}&c_{2x}&c_{2x}\\
c_{3x}&c_{3x}&c_{3x}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

### `image031`

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{4A^2}A
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{4A^2}A
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}
\end{bmatrix}\{V_y\}\\
&-\delta_{yi}\frac1{2A}\frac{A}{3}
\begin{bmatrix}
c_{1y}&c_{1y}&c_{1y}\\
c_{2y}&c_{2y}&c_{2y}\\
c_{3y}&c_{3y}&c_{3y}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

### `image032`

```latex
\[
+\frac{2K^*}{We}n_iL
\begin{bmatrix}1\\1\end{bmatrix}
\]
```

### `image033`

```latex
\[
-g_i^*\frac{A}{3}
\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad (i=1,2)
\]
```

### `image034`

```latex
\[
\begin{aligned}
&+V_x\frac16
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix}\{V_i\}\\
&+V_y\frac16
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}\{V_i\}
\end{aligned}
\]
```

### `image035`

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{4A}
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{4A}
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}
\end{bmatrix}\{V_x\}\\
&-\delta_{xi}\frac16
\begin{bmatrix}
c_{1x}&c_{1x}&c_{1x}\\
c_{2x}&c_{2x}&c_{2x}\\
c_{3x}&c_{3x}&c_{3x}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

### `image036`

```latex
\[
\begin{aligned}
&+\frac1{Re}\frac1{4A}
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}
\end{bmatrix}\{V_i\}\\
&+\frac1{Re}\frac1{4A}
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}
\end{bmatrix}\{V_y\}\\
&-\delta_{yi}\frac16
\begin{bmatrix}
c_{1y}&c_{1y}&c_{1y}\\
c_{2y}&c_{2y}&c_{2y}\\
c_{3y}&c_{3y}&c_{3y}
\end{bmatrix}\{P\}
\end{aligned}
\]
```

### `image037`

```latex
\[
\begin{aligned}
={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{V_i\}+V_y[C_y]\{V_i\}\\
&+\frac1{Re}[S_{xx}]\{V_i\}+\frac1{Re}[S_{xi}]\{V_x\}-\delta_{xi}[H_x]\{P\}\\
&+\frac1{Re}[S_{yy}]\{V_i\}+\frac1{Re}[S_{yi}]\{V_y\}-\delta_{yi}[H_y]\{P\}\\
&+\frac{2K^*}{We}Ln_i\begin{bmatrix}1\\1\end{bmatrix}
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad (i=1,2)
\end{aligned}
\]
```

### `image038`

```latex
\[
\begin{aligned}
={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y])\{V_i\}\\
&+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}
+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\})\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}
+\frac{2K^*}{We}Ln_i\begin{bmatrix}1\\1\end{bmatrix}\\
&-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad (i=1,2,3)\\
={}&\begin{bmatrix}0\\0\\0\end{bmatrix}
\end{aligned}
\]
```

### `image039`

```latex
\[
\begin{aligned}
[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_i\}
+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}\\
&+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}\\
&+\frac{2K^*}{We}Ln_i\begin{bmatrix}1\\1\end{bmatrix}
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}
=\begin{bmatrix}0\\0\\0\end{bmatrix},
\qquad (i=1,2)
\end{aligned}
\]
```

### `image040`

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_i\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_i\}^{\tau+\Delta\tau}
+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}^{\tau+\Delta\tau}\\
&+\frac1{Re}([S_{xi}]\{V_x\}^{\tau+\Delta\tau}+[S_{yi}]\{V_y\}^{\tau+\Delta\tau})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_i\}^{\tau}
-\frac{2K^*}{We}Ln_i\begin{bmatrix}1\\1\end{bmatrix}
+g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad (i=1,2)
\end{aligned}
\]
```

### `image041`

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_x\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_x\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left\{(2[S_{xx}]+[S_{yy}])\{V_x\}^{\tau+\Delta\tau}+[S_{yx}]\{V_y\}^{\tau+\Delta\tau}\right\}
-[H_x]\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_x\}^{\tau}
-\frac{2K^*}{We}Ln_x\begin{bmatrix}1\\1\end{bmatrix}
+g_x^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}
\end{aligned}
\]
```

### `image042`

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_y\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_y\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left\{[S_{xy}]\{V_x\}^{\tau+\Delta\tau}+([S_{xx}]+2[S_{yy}])\{V_y\}^{\tau+\Delta\tau}\right\}
-[H_y]\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_y\}^{\tau}
-\frac{2K^*}{We}Ln_y\begin{bmatrix}1\\1\end{bmatrix}
+g_y^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}
\end{aligned}
\]
```

## 重要な原文維持事項

- `image038`: 2次元式だが元画像の添字範囲は **`i=1,2,3`**。修正しない。
- `image032`, `037`～`042`: 元画像の表面張力係数は **`2K^*/We`**。`b_L` を原文式へ導入しない。
- `image041`, `image042`: 圧力項は `1/Re` の括弧外にある。
