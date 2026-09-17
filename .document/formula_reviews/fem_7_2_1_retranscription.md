# 元画像忠実転記ドラフト: fem/fem_7_2_1.html

作成日: 2026-09-17

## 位置づけ

このファイルは `fem/fem_7_2_1.html` の元数式画像を、**数学的な訂正・一般化・簡略化を行わず**LaTeXへ再転記するための作業ドラフトである。

- 通常ページへは未反映。
- 2026-09-17時点では `image001`～`image006` を直接目視して転記済み。
- `image007`～`image020` は元画像を直接確認するまで転記しない。
- 原画像側に不自然な表記があっても、この原文転記では勝手に修正しない。
- 全20式の再転記後、元画像とのPass 1を再実施する。
- 実ブラウザ上のMathJax描画確認はPass 2として別判定する。

## image001

元画像は、圧力の対流項が小文字 `x/y/z`、速度の発散項が大文字 `X/Y/Z`。

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

元画像は零ベクトルを積分する途中段階も明示している。

```latex
\[
\int_V[N]^T\phi\,dV
=
\int_V
\begin{bmatrix}
N_1\\N_2\\N_3\\N_4
\end{bmatrix}
\phi\,dV
=
\int_V
\begin{bmatrix}
0\\0\\0\\0
\end{bmatrix}
dV
=
\begin{bmatrix}
0\\0\\0\\0
\end{bmatrix}
\]
```

## image003

元画像は `V_x` のみ節点値まで展開し、その後 `V_y`, `V_z`, `P` は `[N]^T` 表記としている。

```latex
\[
\begin{aligned}
V_x
&=N_1V_{x1}+N_2V_{x2}+N_3V_{x3}+N_4V_{x4}\\
&=
\begin{bmatrix}
N_1\\N_2\\N_3\\N_4
\end{bmatrix}
\begin{Bmatrix}
V_{x1}&V_{x2}&V_{x3}&V_{x4}
\end{Bmatrix}\\
&=[N]^T\{V_x\},\\
V_y&=[N]^T\{V_y\},\\
V_z&=[N]^T\{V_z\},\\
P&=[N]^T\{P\}.
\end{aligned}
\]
```

## image004

元画像は圧力対流項が小文字 `x/y/z`、速度発散項が大文字 `X/Y/Z`。式内部は波括弧で囲まれている。

```latex
\[
\int_V[N]^T\phi\,dV
=
\int_V[N]^T\left\{
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

元画像は前式からの継続として先頭が単独 `=`。この段階では空間微分は大文字 `X/Y/Z`。

```latex
\[
\begin{aligned}
={}&
\int_V[N]^T\frac{\partial P}{\partial\tau}\,dV
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

元画像の時刻添字は `\Delta\tau+\tau` の順序。先頭は前式から続く単独 `=`。

```latex
\[
\begin{aligned}
={}&
\int_V[N]^T[N]dV\,
\frac{\{P\}^{\Delta\tau+\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T
\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial X}dV
+V_y\int_V[N]^T
\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial Y}dV\\
&+V_z\int_V[N]^T
\frac{\partial[N]\{P\}^{\Delta\tau+\tau}}{\partial Z}dV\\
&+\frac{1}{Ma^2}\int_V[N]^T
\frac{\partial[N]\{V_x\}^{\Delta\tau+\tau}}{\partial X}dV
+\frac{1}{Ma^2}\int_V[N]^T
\frac{\partial[N]\{V_y\}^{\Delta\tau+\tau}}{\partial Y}dV\\
&+\frac{1}{Ma^2}\int_V[N]^T
\frac{\partial[N]\{V_z\}^{\Delta\tau+\tau}}{\partial Z}dV
\end{aligned}
\]
```

## image007～image020

**HOLD** — 元画像を直接表示して1式ずつ照合後に追記する。

## 現在の状態

- 元画像との対応付け: 20/20
- 現監査候補のPass 1目視監査: 6/20
- 現監査候補の合格: 0/20
- 元画像忠実再転記ドラフト: 6/20
- 再転記版の再Pass 1: 未実施
- Pass 2: 0/20
