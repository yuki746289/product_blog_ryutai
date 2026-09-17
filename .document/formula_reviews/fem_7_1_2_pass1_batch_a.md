# fem_7_1_2 厳密Pass 1 — batch A (`image001`～`image014`)

更新日: 2026-09-17

## 判定基準

元画像 `img/fem_d_momentum_tri.files/image001.png`～`image014.png` を4倍拡大・白背景化して直接目視した。数学的同値性ではなく、元画像の表記・項順・積分領域・添字・係数を優先する。

## 結果

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| `image001` | OK | **OK** | 元画像と一致 |
| `image002` | OK | **OK** | 元画像と一致 |
| `image003` | NG | **再転記OK** | 原画像は `V,dV`。3成分ベクトルを明示 |
| `image004` | NG | **再転記OK** | `V_x`, `V_y` 末尾の `=0`、原画像の `P_{x,j}` を保持 |
| `image005` | NG | **再転記OK** | 左辺は `V,dV`、右辺は `S,dS`。重み関数3成分を明示 |
| `image006` | NG | **再転記OK** | 原画像は3成分重み関数を各項で明示 |
| `image007` | NG | **再転記OK** | 原画像ではまだ時間差分化していない |
| `image008` | NG | **再転記OK** | Green-Gauss後の境界・領域積分をx/y別に明示 |
| `image009` | NG | **再転記OK** | 境界応力をまとめる前の原式へ復元 |
| `image010` | NG | **再転記OK** | 応力展開後の全式。表面張力項は負 |
| `image011` | NG | **再転記OK** | `X_i` を保持。表面張力項は正 |
| `image012` | NG | **再転記OK** | `δ` を積分の外へ移さず原画像配置を保持 |
| `image013` | NG | **再転記OK** | 原画像にある `n_i L` の追加 `L` を保持 |
| `image014` | NG | **再転記OK** | 先頭は継続等号 `=`。原画像にない `0=` を入れない |

**batch A: 14/14 Pass 1 OK。**

## 元画像忠実LaTeX

### `image001`

```latex
\[
\phi_x=\frac{\partial V_x}{\partial\tau}
+V_x\frac{\partial V_x}{\partial X}
+V_y\frac{\partial V_x}{\partial Y}
-\frac{\partial\sigma^*_{xx}}{\partial X}
-\frac{\partial\sigma^*_{yx}}{\partial Y}
-g_x^*=0
\]
```

### `image002`

```latex
\[
\phi_y=\frac{\partial V_y}{\partial\tau}
+V_x\frac{\partial V_y}{\partial X}
+V_y\frac{\partial V_y}{\partial Y}
-\frac{\partial\sigma^*_{xy}}{\partial X}
-\frac{\partial\sigma^*_{yy}}{\partial Y}
-g_y^*=0
\]
```

### `image003`

```latex
\[
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\phi_i\,dV
=
\int_V
\begin{bmatrix}0\\0\\0\end{bmatrix}dV
=
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]
```

### `image004`

```latex
\[
\begin{aligned}
V_x&=N_1V_{x,1}+N_2V_{x,2}+N_3V_{x,3}
=\begin{bmatrix}N_1&N_2&N_3\end{bmatrix}
\begin{bmatrix}V_{x,1}\\V_{x,2}\\V_{x,3}\end{bmatrix}
=[N]\{V_x\}=0,\\
V_y&=N_1V_{y,1}+N_2V_{y,2}+N_3V_{y,3}=0,\\
P&=N_1P_{x,1}+N_2P_{x,2}+N_3P_{x,3}
\end{aligned}
\]
```

### `image005`

```latex
\[
\begin{aligned}
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\phi_i\,dV
={}&\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\left(
\frac{\partial V_i}{\partial\tau}
+V_x\frac{\partial V_i}{\partial X}
+V_y\frac{\partial V_i}{\partial Y}
-\frac{\partial\sigma^*_{xi}}{\partial X}
-\frac{\partial\sigma^*_{yi}}{\partial Y}
-g_i^*
\right)dS
\end{aligned}
\]
```

### `image006`

```latex
\[
\begin{aligned}
={}&\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\frac{\partial V_i}{\partial\tau}dS
+V_x\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\frac{\partial V_i}{\partial X}dS
+V_y\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\frac{\partial V_i}{\partial Y}dS\\
&-\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\frac{\partial\sigma^*_{xi}}{\partial X}dS
-\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\frac{\partial\sigma^*_{yi}}{\partial Y}dS
-\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}g_i^*dS
\end{aligned}
\]
```

### `image007`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T\frac{\partial V_i}{\partial\tau}dS
+V_x\int_S[N]^T\frac{\partial V_i}{\partial X}dS
+V_y\int_S[N]^T\frac{\partial V_i}{\partial Y}dS\\
&-\int_S[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dS
-\int_S[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dS
-\int_S[N]^Tg_i^*dS
\end{aligned}
\]
```

### `image008`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T\frac{[N](\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau})}{\Delta\tau}dS\\
&+V_x\int_S[N]^T\frac{\partial[N]\{V_i\}}{\partial X}dS
+V_y\int_S[N]^T\frac{\partial[N]\{V_i\}}{\partial Y}dS\\
&-\int_L[N]^T\sigma^*_{xi}n_xdL
+\int_S\left[\frac{\partial N}{\partial X}\right]^T\sigma^*_{xi}dS\\
&-\int_L[N]^T\sigma^*_{yi}n_ydL
+\int_S\left[\frac{\partial N}{\partial Y}\right]^T\sigma^*_{yi}dS
-\int_S[N]^Tg_i^*dS
\end{aligned}
\]
```

### `image009`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\int_S\left[\frac{\partial N}{\partial X}\right]^T\sigma^*_{xi}dS
+\int_S\left[\frac{\partial N}{\partial Y}\right]^T\sigma^*_{yi}dS\\
&-\int_L[N]^T(\sigma^*_{xi}n_x+\sigma^*_{yi}n_y)dL
-\int_S[N]^Tg_i^*dS
\end{aligned}
\]
```

### `image010`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\int_S\left[\frac{\partial N}{\partial X}\right]^T
\left\{-\delta_{xi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial X}+\frac{\partial V_x}{\partial X_i}\right)\right\}dS\\
&+\int_S\left[\frac{\partial N}{\partial Y}\right]^T
\left\{-\delta_{yi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial Y}+\frac{\partial V_y}{\partial X_i}\right)\right\}dS\\
&-\frac{2K^*}{We}n_i\int_L[N]^TdL
-\int_S[N]^Tg_i^*dS
\end{aligned}
\]
```

### `image011`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\int_S\left[\frac{\partial N}{\partial X}\right]^T
\left\{-\delta_{xi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial X}+\frac{\partial V_x}{\partial X_i}\right)\right\}dS\\
&+\int_S\left[\frac{\partial N}{\partial Y}\right]^T
\left\{-\delta_{yi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial Y}+\frac{\partial V_y}{\partial X_i}\right)\right\}dS\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL
-\int_S[N]^Tg_i^*dS
\end{aligned}
\]
```

### `image012`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial V_i}{\partial X}dS
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial V_x}{\partial X_i}dS
-\int_S\left[\frac{\partial N}{\partial X}\right]^T\delta_{xi}P\,dS\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial V_i}{\partial Y}dS
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial V_y}{\partial X_i}dS
-\int_S\left[\frac{\partial N}{\partial Y}\right]^T\delta_{yi}P\,dS\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL
-g_i^*\int_S[N]^TdS
\end{aligned}
\]
```

### `image013`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial[N]\{V_i\}}{\partial X}dS
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\frac{\partial[N]\{V_x\}}{\partial X_i}dS
-\delta_{xi}\int_S\left[\frac{\partial N}{\partial X}\right]^T[N]\{P\}dS\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial[N]\{V_i\}}{\partial Y}dS
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\frac{\partial[N]\{V_y\}}{\partial X_i}dS
-\delta_{yi}\int_S\left[\frac{\partial N}{\partial Y}\right]^T[N]\{P\}dS\\
&+\frac{2K^*}{We}n_iL\int_L[N]^TdL
-g_i^*\int_S[N]^TdS
\end{aligned}
\]
```

### `image014`

```latex
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+V_y\int_S[N]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\left[\frac{\partial N}{\partial X}\right]dS\{V_i\}
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial X}\right]^T\left[\frac{\partial N}{\partial X_i}\right]dS\{V_x\}
-\delta_{xi}\int_S\left[\frac{\partial N}{\partial X}\right]^T[N]dS\{P\}\\
&+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\left[\frac{\partial N}{\partial Y}\right]dS\{V_i\}
+\frac1{Re}\int_S\left[\frac{\partial N}{\partial Y}\right]^T\left[\frac{\partial N}{\partial X_i}\right]dS\{V_y\}
-\delta_{yi}\int_S\left[\frac{\partial N}{\partial Y}\right]^T[N]dS\{P\}\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL
-g_i^*\int_S[N]^TdS,
\qquad (i=1,2)
\end{aligned}
\]
```

## 注意

- `image013` の表面張力項には、元画像上で `n_i` と積分記号の間に明示的な `L` がある。理論上の整合性ではなく元画像表記を保持した。
- `image004` の `P_{x,j}`、`image005` の `V,dV`、`image010`～`image014` の `X_i` は、原画像の大文字小文字をそのまま維持する。
