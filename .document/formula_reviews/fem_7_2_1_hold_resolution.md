# fem_7_2_1 HOLD解消記録 — image011 / image012 / image015

更新日: 2026-09-17

## 方針

GitHub ActionsでPNG/GIFを白背景化・8倍拡大し、元画像を直接目視した。理論的な修正・一般化・略記は行わない。

## image011

```latex
\[
\begin{aligned}
={}&\int_V
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3&L_1L_4\\
L_2L_1&L_2L_2&L_2L_3&L_2L_4\\
L_3L_1&L_3L_2&L_3L_3&L_3L_4\\
L_4L_1&L_4L_2&L_4L_3&L_4L_4
\end{bmatrix}dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial X}&L_1\dfrac{\partial L_2}{\partial X}&L_1\dfrac{\partial L_3}{\partial X}&L_1\dfrac{\partial L_4}{\partial X}\\
L_2\dfrac{\partial L_1}{\partial X}&L_2\dfrac{\partial L_2}{\partial X}&L_2\dfrac{\partial L_3}{\partial X}&L_2\dfrac{\partial L_4}{\partial X}\\
L_3\dfrac{\partial L_1}{\partial X}&L_3\dfrac{\partial L_2}{\partial X}&L_3\dfrac{\partial L_3}{\partial X}&L_3\dfrac{\partial L_4}{\partial X}\\
L_4\dfrac{\partial L_1}{\partial X}&L_4\dfrac{\partial L_2}{\partial X}&L_4\dfrac{\partial L_3}{\partial X}&L_4\dfrac{\partial L_4}{\partial X}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_y\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Y}&L_1\dfrac{\partial L_2}{\partial Y}&L_1\dfrac{\partial L_3}{\partial Y}&L_1\dfrac{\partial L_4}{\partial Y}\\
L_2\dfrac{\partial L_1}{\partial Y}&L_2\dfrac{\partial L_2}{\partial Y}&L_2\dfrac{\partial L_3}{\partial Y}&L_2\dfrac{\partial L_4}{\partial Y}\\
L_3\dfrac{\partial L_1}{\partial Y}&L_3\dfrac{\partial L_2}{\partial Y}&L_3\dfrac{\partial L_3}{\partial Y}&L_3\dfrac{\partial L_4}{\partial Y}\\
L_4\dfrac{\partial L_1}{\partial Y}&L_4\dfrac{\partial L_2}{\partial Y}&L_4\dfrac{\partial L_3}{\partial Y}&L_4\dfrac{\partial L_4}{\partial Y}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_z\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Z}&L_1\dfrac{\partial L_2}{\partial Z}&L_1\dfrac{\partial L_3}{\partial Z}&L_1\dfrac{\partial L_4}{\partial Z}\\
L_2\dfrac{\partial L_1}{\partial Z}&L_2\dfrac{\partial L_2}{\partial Z}&L_2\dfrac{\partial L_3}{\partial Z}&L_2\dfrac{\partial L_4}{\partial Z}\\
L_3\dfrac{\partial L_1}{\partial Z}&L_3\dfrac{\partial L_2}{\partial Z}&L_3\dfrac{\partial L_3}{\partial Z}&L_3\dfrac{\partial L_4}{\partial Z}\\
L_4\dfrac{\partial L_1}{\partial Z}&L_4\dfrac{\partial L_2}{\partial Z}&L_4\dfrac{\partial L_3}{\partial Z}&L_4\dfrac{\partial L_4}{\partial Z}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial X}&L_1\dfrac{\partial L_2}{\partial X}&L_1\dfrac{\partial L_3}{\partial X}&L_1\dfrac{\partial L_4}{\partial X}\\
L_2\dfrac{\partial L_1}{\partial X}&L_2\dfrac{\partial L_2}{\partial X}&L_2\dfrac{\partial L_3}{\partial X}&L_2\dfrac{\partial L_4}{\partial X}\\
L_3\dfrac{\partial L_1}{\partial X}&L_3\dfrac{\partial L_2}{\partial X}&L_3\dfrac{\partial L_3}{\partial X}&L_3\dfrac{\partial L_4}{\partial X}\\
L_4\dfrac{\partial L_1}{\partial X}&L_4\dfrac{\partial L_2}{\partial X}&L_4\dfrac{\partial L_3}{\partial X}&L_4\dfrac{\partial L_4}{\partial X}
\end{bmatrix}dV\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Y}&L_1\dfrac{\partial L_2}{\partial Y}&L_1\dfrac{\partial L_3}{\partial Y}&L_1\dfrac{\partial L_4}{\partial Y}\\
L_2\dfrac{\partial L_1}{\partial Y}&L_2\dfrac{\partial L_2}{\partial Y}&L_2\dfrac{\partial L_3}{\partial Y}&L_2\dfrac{\partial L_4}{\partial Y}\\
L_3\dfrac{\partial L_1}{\partial Y}&L_3\dfrac{\partial L_2}{\partial Y}&L_3\dfrac{\partial L_3}{\partial Y}&L_3\dfrac{\partial L_4}{\partial Y}\\
L_4\dfrac{\partial L_1}{\partial Y}&L_4\dfrac{\partial L_2}{\partial Y}&L_4\dfrac{\partial L_3}{\partial Y}&L_4\dfrac{\partial L_4}{\partial Y}
\end{bmatrix}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Z}&L_1\dfrac{\partial L_2}{\partial Z}&L_1\dfrac{\partial L_3}{\partial Z}&L_1\dfrac{\partial L_4}{\partial Z}\\
L_2\dfrac{\partial L_1}{\partial Z}&L_2\dfrac{\partial L_2}{\partial Z}&L_2\dfrac{\partial L_3}{\partial Z}&L_2\dfrac{\partial L_4}{\partial Z}\\
L_3\dfrac{\partial L_1}{\partial Z}&L_3\dfrac{\partial L_2}{\partial Z}&L_3\dfrac{\partial L_3}{\partial Z}&L_3\dfrac{\partial L_4}{\partial Z}\\
L_4\dfrac{\partial L_1}{\partial Z}&L_4\dfrac{\partial L_2}{\partial Z}&L_4\dfrac{\partial L_3}{\partial Z}&L_4\dfrac{\partial L_4}{\partial Z}
\end{bmatrix}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

**Pass 1 = OK（HOLD解消）**。

## image012

```latex
\[
\begin{aligned}
={}&\int_V
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3&L_1L_4\\
L_2L_1&L_2L_2&L_2L_3&L_2L_4\\
L_3L_1&L_3L_2&L_3L_3&L_3L_4\\
L_4L_1&L_4L_2&L_4L_3&L_4L_4
\end{bmatrix}dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}&L_1c_{4x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}&L_2c_{4x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}&L_3c_{4x}\\
L_4c_{1x}&L_4c_{2x}&L_4c_{3x}&L_4c_{4x}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_y\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}&L_1c_{4y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}&L_2c_{4y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}&L_3c_{4y}\\
L_4c_{1y}&L_4c_{2y}&L_4c_{3y}&L_4c_{4y}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+V_z\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1z}&L_1c_{2z}&L_1c_{3z}&L_1c_{4z}\\
L_2c_{1z}&L_2c_{2z}&L_2c_{3z}&L_2c_{4z}\\
L_3c_{1z}&L_3c_{2z}&L_3c_{3z}&L_3c_{4z}\\
L_4c_{1z}&L_4c_{2z}&L_4c_{3z}&L_4c_{4z}
\end{bmatrix}dV\,\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}&L_1c_{4x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}&L_2c_{4x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}&L_3c_{4x}\\
L_4c_{1x}&L_4c_{2x}&L_4c_{3x}&L_4c_{4x}
\end{bmatrix}dV\,\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1y}&L_1c_{2y}&L_1c_{3y}&L_1c_{4y}\\
L_2c_{1y}&L_2c_{2y}&L_2c_{3y}&L_2c_{4y}\\
L_3c_{1y}&L_3c_{2y}&L_3c_{3y}&L_3c_{4y}\\
L_4c_{1y}&L_4c_{2y}&L_4c_{3y}&L_4c_{4y}
\end{bmatrix}dV\,\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\int_V\frac1{6V}
\begin{bmatrix}
L_1c_{1z}&L_1c_{2z}&L_1c_{3z}&L_1c_{4z}\\
L_2c_{1z}&L_2c_{2z}&L_2c_{3z}&L_2c_{4z}\\
L_3c_{1z}&L_3c_{2z}&L_3c_{3z}&L_3c_{4z}\\
L_4c_{1z}&L_4c_{2z}&L_4c_{3z}&L_4c_{4z}
\end{bmatrix}dV\,\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

**Pass 1 = OK（HOLD解消）**。

## image015

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
&+\frac1{24}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{24}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{24}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{P\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{24}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix}\{V_x\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{24}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix}\{V_y\}^{\Delta\tau+\tau}\\
&+\frac1{Ma^2}\frac1{24}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}\{V_z\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

元画像上では、この段階の3つの圧力行列項の前に `V_x`, `V_y`, `V_z` は表示されていない。理論的な補完は行わない。

**Pass 1 = OK（HOLD解消）**。

## 結果

- `image011`: HOLD → **Pass 1 OK**
- `image012`: HOLD → **Pass 1 OK**
- `image015`: HOLD → **Pass 1 OK**
- これにより `fem_7_2_1` の元画像忠実再転記は **20/20** まで揃った。
