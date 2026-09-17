# fem_7_1_1 image011 元画像忠実転記

作成日: 2026-09-17

`img/fem_d_mass_tri.files/image011.png` を直接目視して転記した作業ドラフト。
通常ページには未反映。監査候補へ反映後に再度Pass 1を実施する。

元画像は、質量行列1項と `X/Y` 方向の4項をすべて3×3行列で展開している。既存監査候補の `N_i=L_i` と行列置換だけの短い式は元画像と一致しない。

```latex
\[
\begin{aligned}
={}&
\int_S
\begin{bmatrix}
L_1L_1&L_1L_2&L_1L_3\\
L_2L_1&L_2L_2&L_2L_3\\
L_3L_1&L_3L_2&L_3L_3
\end{bmatrix}
dS\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\[4pt]
&+V_x\int_S
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial X}&L_1\dfrac{\partial L_2}{\partial X}&L_1\dfrac{\partial L_3}{\partial X}\\
L_2\dfrac{\partial L_1}{\partial X}&L_2\dfrac{\partial L_2}{\partial X}&L_2\dfrac{\partial L_3}{\partial X}\\
L_3\dfrac{\partial L_1}{\partial X}&L_3\dfrac{\partial L_2}{\partial X}&L_3\dfrac{\partial L_3}{\partial X}
\end{bmatrix}
dS\,\{P\}^{\Delta\tau+\tau}\\[4pt]
&+V_y\int_S
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Y}&L_1\dfrac{\partial L_2}{\partial Y}&L_1\dfrac{\partial L_3}{\partial Y}\\
L_2\dfrac{\partial L_1}{\partial Y}&L_2\dfrac{\partial L_2}{\partial Y}&L_2\dfrac{\partial L_3}{\partial Y}\\
L_3\dfrac{\partial L_1}{\partial Y}&L_3\dfrac{\partial L_2}{\partial Y}&L_3\dfrac{\partial L_3}{\partial Y}
\end{bmatrix}
dS\,\{P\}^{\Delta\tau+\tau}\\[4pt]
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial X}&L_1\dfrac{\partial L_2}{\partial X}&L_1\dfrac{\partial L_3}{\partial X}\\
L_2\dfrac{\partial L_1}{\partial X}&L_2\dfrac{\partial L_2}{\partial X}&L_2\dfrac{\partial L_3}{\partial X}\\
L_3\dfrac{\partial L_1}{\partial X}&L_3\dfrac{\partial L_2}{\partial X}&L_3\dfrac{\partial L_3}{\partial X}
\end{bmatrix}
dS\,\{V_x\}^{\Delta\tau+\tau}\\[4pt]
&+\frac{1}{Ma^2}\int_S
\begin{bmatrix}
L_1\dfrac{\partial L_1}{\partial Y}&L_1\dfrac{\partial L_2}{\partial Y}&L_1\dfrac{\partial L_3}{\partial Y}\\
L_2\dfrac{\partial L_1}{\partial Y}&L_2\dfrac{\partial L_2}{\partial Y}&L_2\dfrac{\partial L_3}{\partial Y}\\
L_3\dfrac{\partial L_1}{\partial Y}&L_3\dfrac{\partial L_2}{\partial Y}&L_3\dfrac{\partial L_3}{\partial Y}
\end{bmatrix}
dS\,\{V_y\}^{\Delta\tau+\tau}
\end{aligned}
\]
```

## 照合メモ

- 積分領域は `S`、微小量は `dS`。
- 時刻添字はすべて元画像どおり `Δτ+τ`。
- 微分方向は大文字 `X/Y`。
- 第2・第3項は `{P}^{Δτ+τ}`。
- 第4・第5項はそれぞれ `{V_x}^{Δτ+τ}`, `{V_y}^{Δτ+τ}`。
- 行列は各項3×3で全成分を省略しない。
