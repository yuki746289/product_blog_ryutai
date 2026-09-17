# fem_7_1_2 厳密Pass 1 — batch B (`image015`～`image028`)

更新日: 2026-09-17

## 結果

元画像を4倍拡大して直接目視し、行列全成分、係数、添字、転置、原画像上の誤記候補まで照合した。

| 画像 | 現候補 | Pass 1 | 主な差分 |
|---|---|---|---|
| `image015` | NG | **再転記OK** | `[N]^T[N]` へ短縮せず3×3成分を保持 |
| `image016` | NG | **再転記OK** | 対流項の3×3成分を保持 |
| `image017` | NG | **再転記OK** | x方向粘性・圧力項を成分展開。`δ_{xi}` を保持 |
| `image018` | NG | **再転記OK** | y方向圧力項の原画像には `δ_{yi}` が無い。補わない |
| `image019` | NG | **再転記OK** | 境界2節点ベクトル `[N_1,N_2]^T` を明示 |
| `image020` | NG | **再転記OK** | 3節点列ベクトルを明示 |
| `image021` | NG | **再転記OK** | `[L]^T[L]` へ短縮せず3×3成分を保持 |
| `image022` | NG | **再転記OK** | `c_x,c_y` 外積へ短縮せず全成分を保持 |
| `image023` | NG | **再転記OK** | x方向粘性・圧力行列の全成分を保持 |
| `image024` | NG | **再転記OK** | y方向粘性・圧力行列の全成分を保持 |
| `image025` | OK | **OK** | 元画像と一致 |
| `image026` | NG | **再転記OK** | 元画像の列ベクトル右上の `T` を保持 |
| `image027` | NG | **再転記OK** | 原文積分公式・原文 `V`・線積分分母 `(p+q)!` を保持 |
| `image028` | NG | **再転記OK** | 原画像は継続等号から直接 `A/12` 行列を記載 |

**batch B: 14/14 Pass 1 OK。**

## 元画像忠実LaTeX

### `image015`

```latex
\[
=\int_S
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3\\
N_2N_1&N_2N_2&N_2N_3\\
N_3N_1&N_3N_2&N_3N_3
\end{bmatrix}dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```

元画像注記: `蓄積量`。

### `image016`

```latex
\[
\begin{aligned}
&+V_x\int_S
\begin{bmatrix}
N_1\frac{\partial N_1}{\partial X}&N_1\frac{\partial N_2}{\partial X}&N_1\frac{\partial N_3}{\partial X}\\
N_2\frac{\partial N_1}{\partial X}&N_2\frac{\partial N_2}{\partial X}&N_2\frac{\partial N_3}{\partial X}\\
N_3\frac{\partial N_1}{\partial X}&N_3\frac{\partial N_2}{\partial X}&N_3\frac{\partial N_3}{\partial X}
\end{bmatrix}dS\{V_i\}\\
&+V_y\int_S
\begin{bmatrix}
N_1\frac{\partial N_1}{\partial Y}&N_1\frac{\partial N_2}{\partial Y}&N_1\frac{\partial N_3}{\partial Y}\\
N_2\frac{\partial N_1}{\partial Y}&N_2\frac{\partial N_2}{\partial Y}&N_2\frac{\partial N_3}{\partial Y}\\
N_3\frac{\partial N_1}{\partial Y}&N_3\frac{\partial N_2}{\partial Y}&N_3\frac{\partial N_3}{\partial Y}
\end{bmatrix}dS\{V_i\}
\end{aligned}
\]
```

元画像注記: `対流項`。

### `image017`

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_1}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_1}{\partial X}\frac{\partial N_3}{\partial X}\\
\frac{\partial N_2}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_2}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_2}{\partial X}\frac{\partial N_3}{\partial X}\\
\frac{\partial N_3}{\partial X}\frac{\partial N_1}{\partial X}&\frac{\partial N_3}{\partial X}\frac{\partial N_2}{\partial X}&\frac{\partial N_3}{\partial X}\frac{\partial N_3}{\partial X}
\end{bmatrix}dS\{V_i\}\\
&+\frac1{Re}\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_1}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_1}{\partial X}\frac{\partial N_3}{\partial X_i}\\
\frac{\partial N_2}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_2}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_2}{\partial X}\frac{\partial N_3}{\partial X_i}\\
\frac{\partial N_3}{\partial X}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_3}{\partial X}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_3}{\partial X}\frac{\partial N_3}{\partial X_i}
\end{bmatrix}dS\{V_x\}\\
&-\delta_{xi}\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial X}N_1&\frac{\partial N_1}{\partial X}N_2&\frac{\partial N_1}{\partial X}N_3\\
\frac{\partial N_2}{\partial X}N_1&\frac{\partial N_2}{\partial X}N_2&\frac{\partial N_2}{\partial X}N_3\\
\frac{\partial N_3}{\partial X}N_1&\frac{\partial N_3}{\partial X}N_2&\frac{\partial N_3}{\partial X}N_3
\end{bmatrix}dS\{P\}
\end{aligned}
\]
```

元画像注記: `粘性項の x 成分`, `圧力項の x 成分`。

### `image018`

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_1}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_1}{\partial Y}\frac{\partial N_3}{\partial Y}\\
\frac{\partial N_2}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_2}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_2}{\partial Y}\frac{\partial N_3}{\partial Y}\\
\frac{\partial N_3}{\partial Y}\frac{\partial N_1}{\partial Y}&\frac{\partial N_3}{\partial Y}\frac{\partial N_2}{\partial Y}&\frac{\partial N_3}{\partial Y}\frac{\partial N_3}{\partial Y}
\end{bmatrix}dS\{V_i\}\\
&+\frac1{Re}\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_1}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_1}{\partial Y}\frac{\partial N_3}{\partial X_i}\\
\frac{\partial N_2}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_2}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_2}{\partial Y}\frac{\partial N_3}{\partial X_i}\\
\frac{\partial N_3}{\partial Y}\frac{\partial N_1}{\partial X_i}&\frac{\partial N_3}{\partial Y}\frac{\partial N_2}{\partial X_i}&\frac{\partial N_3}{\partial Y}\frac{\partial N_3}{\partial X_i}
\end{bmatrix}dS\{V_y\}\\
&-\int_S
\begin{bmatrix}
\frac{\partial N_1}{\partial Y}N_1&\frac{\partial N_1}{\partial Y}N_2&\frac{\partial N_1}{\partial Y}N_3\\
\frac{\partial N_2}{\partial Y}N_1&\frac{\partial N_2}{\partial Y}N_2&\frac{\partial N_2}{\partial Y}N_3\\
\frac{\partial N_3}{\partial Y}N_1&\frac{\partial N_3}{\partial Y}N_2&\frac{\partial N_3}{\partial Y}N_3
\end{bmatrix}dS\{P\}
\end{aligned}
\]
```

**重要:** 原画像のy方向圧力項の先頭には `δ_{yi}` が見当たらない。理論的に補完せず、そのまま保持する。

### `image019`

```latex
\[
+\frac{2K^*}{We}n_i\int_L
\begin{bmatrix}N_1\\N_2\end{bmatrix}dL
\]
```

### `image020`

```latex
\[
-g_i^*\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}dS,
\qquad (i=1,2)
\]
```

### `image021`

```latex
\[
=\int_S
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3\\
L_2L_1&L_2L_2&L_2L_3\\
L_3L_1&L_3L_2&L_3L_3
\end{bmatrix}dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```

### `image022`

```latex
\[
\begin{aligned}
&+V_x\int_S\frac1{2A}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}
\end{bmatrix}dS\{V_i\}\\
&+V_y\int_S\frac1{2A}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}
\end{bmatrix}dS\{V_i\}
\end{aligned}
\]
```

### `image023`

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_S\frac1{4A^2}
\begin{bmatrix}
c_{1x}c_{1x}&c_{1x}c_{2x}&c_{1x}c_{3x}\\
c_{2x}c_{1x}&c_{2x}c_{2x}&c_{2x}c_{3x}\\
c_{3x}c_{1x}&c_{3x}c_{2x}&c_{3x}c_{3x}
\end{bmatrix}dS\{V_i\}\\
&+\frac1{Re}\int_S\frac1{4A^2}
\begin{bmatrix}
c_{1x}c_{1i}&c_{1x}c_{2i}&c_{1x}c_{3i}\\
c_{2x}c_{1i}&c_{2x}c_{2i}&c_{2x}c_{3i}\\
c_{3x}c_{1i}&c_{3x}c_{2i}&c_{3x}c_{3i}
\end{bmatrix}dS\{V_x\}\\
&-\delta_{xi}\int_S\frac1{2A}
\begin{bmatrix}
c_{1x}L_1&c_{1x}L_2&c_{1x}L_3\\
c_{2x}L_1&c_{2x}L_2&c_{2x}L_3\\
c_{3x}L_1&c_{3x}L_2&c_{3x}L_3
\end{bmatrix}dS\{P\}
\end{aligned}
\]
```

### `image024`

```latex
\[
\begin{aligned}
&+\frac1{Re}\int_S\frac1{4A^2}
\begin{bmatrix}
c_{1y}c_{1y}&c_{1y}c_{2y}&c_{1y}c_{3y}\\
c_{2y}c_{1y}&c_{2y}c_{2y}&c_{2y}c_{3y}\\
c_{3y}c_{1y}&c_{3y}c_{2y}&c_{3y}c_{3y}
\end{bmatrix}dS\{V_i\}\\
&+\frac1{Re}\int_S\frac1{4A^2}
\begin{bmatrix}
c_{1y}c_{1i}&c_{1y}c_{2i}&c_{1y}c_{3i}\\
c_{2y}c_{1i}&c_{2y}c_{2i}&c_{2y}c_{3i}\\
c_{3y}c_{1i}&c_{3y}c_{2i}&c_{3y}c_{3i}
\end{bmatrix}dS\{V_y\}\\
&-\delta_{yi}\int_S\frac1{2A}
\begin{bmatrix}
c_{1y}L_1&c_{1y}L_2&c_{1y}L_3\\
c_{2y}L_1&c_{2y}L_2&c_{2y}L_3\\
c_{3y}L_1&c_{3y}L_2&c_{3y}L_3
\end{bmatrix}dS\{P\}
\end{aligned}
\]
```

### `image025`

```latex
\[
+\frac{2K^*}{We}n_i\int_L
\begin{bmatrix}L_1\\L_2\end{bmatrix}dL
\]
```

### `image026`

```latex
\[
-g_i^*\int_S
\begin{bmatrix}L_1\\L_2\\L_3\end{bmatrix}^{T}dS,
\qquad (i=1,2)
\]
```

### `image027`

```latex
\[
\int_S L_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2A
\]

\[
\int_S L_iL_j\,dS=
\begin{cases}
\displaystyle \frac{1!1!}{(1+1+2)!}\,2A=\frac{2}{4!}A=\frac1{12}A,&(i\ne j),\\[6pt]
\displaystyle \frac{2!}{(1+1+2)!}\,2A=\frac{4}{4!}V=\frac1{6}A,&(i=j)
\end{cases}
\]

\[
\int_S L_i\,dS=\frac{1!}{(1+2)!}\,2A=\frac{2}{3!}A=\frac13A
\]

\[
\int_L L_1^pL_2^q\,dL=\frac{p!q!}{(p+q)!}L
\]

\[
\int_L L_i\,dL=\frac1{1!}L=L
\]
```

原画像の `V`、線積分の `(p+q)!`、`∫L_i dL=L` は誤記候補だが原文として保持する。

### `image028`

```latex
\[
=\frac1{12}A
\begin{bmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{bmatrix}
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]
```
