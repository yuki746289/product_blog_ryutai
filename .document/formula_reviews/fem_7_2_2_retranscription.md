# 元画像忠実転記ドラフト: fem/fem_7_2_2.html

作成日: 2026-09-17
更新日: 2026-09-17

## 位置づけ

`fem/fem_7_2_2.html`（4面体1次要素・運動量収支式）の49数式画像を、**原画像と同一表記**でLaTeXへ再転記するための作業記録。

- 通常ページへは未反映。
- 数学的な一般化・簡略化・写像追加は原文式では行わない。
- 原画像の省略・誤記候補もそのまま保持する。
- 補足・修正版は原文式の外へ分離する。
- 履歴から不一致が確定しても、直接画像照合が終わるまでは正式Pass 1合格には数えない。

## 根拠資料

- 元画像版: `release_1.0.0/fem/fem_7_2_2.html`
- 現監査候補: `fem/fem_7_2_2_mathjax_audit.html`
- 初回MathJax変換: `9a02677ad86ce8d4670233999e943b1d20b5d8f8`
- 課題台帳: `.document/formula_reviews/ISSUES.md`

## 境界面写像の履歴確認

MathJax変換前の本文には、境界三角形で得られる3節点表面力ベクトルを四面体4節点へアセンブルする写像について、**後続式ではその写像を省略している**旨の補足が存在した。

初回MathJax変換 `9a02677...` では、その補足を変更し、

`b_S = A_S^T [1 1 1]^T`

を定義して後続式の式本体へ組み込んだ。

これは数値実装上は説明改善だが、原画像忠実転記では原画像にない写像を式本体へ追加したことになる。

## 現候補NGが履歴から確定している式

| 元画像 | 現監査候補 | 不一致理由 | Pass 1 |
|---|---|---|---|
| `image042` | NG確定 | 原画像の面局所3節点表面張力項を `b_S` を用いる4節点要素ベクトルへ変更 | **再転記Pass 1 OK** |
| `image043` | NG確定 | 原画像で省略されていた面→要素写像を `b_S` として式本体へ追加 | **再転記Pass 1 OK** |
| `image044` | NG確定 | 同上 | **再転記Pass 1 OK** |
| `image045` | NG確定 | 同上 | **再転記Pass 1 OK** |
| `image046` | NG確定 | 同上 | **再転記Pass 1 OK** |
| `image047` | NG確定 | x成分最終式へ `b_S` を組み込み、原画像の局所境界面項から変更 | **再転記Pass 1 OK** |
| `image048` | NG確定 | y成分最終式へ `b_S` を組み込み、原画像の局所境界面項から変更 | **再転記Pass 1 OK** |
| `image049` | NG確定 | z成分最終式へ `b_S` を組み込み、原画像の局所境界面項から変更 | **再転記Pass 1 OK** |

**履歴証拠による現候補NG確定: 8/49 (`042`～`049`)。**

原文復元時は、原画像の3節点局所ベクトルをそのまま転記し、`f_e=A_S^T f_S` 等の写像は補足ブロックにのみ記載する。

## `image042` 直接目視再転記（2026-09-17）

元画像 `img/fem_d_momentum_tet.files/image042.png` を直接表示して照合した。

原画像は、先頭に `+` を持つ表面張力項で、係数は `2K^*/(3We)`、続いて `n_i S`、最後に3成分列ベクトル `[1,1,1]^T` が配置されている。

元画像忠実転記:

```latex
\[
+\frac{2K^*}{3We}n_iS
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}
\]
```

照合項目:

- 先頭 `+`: OK
- 分子 `2K^*`: OK
- 分母 `3We`: OK
- `n_i`: OK
- `S`: OK
- ベクトル成分数: 3
- 成分: `1,1,1`
- `b_S`, `A_S`, 4成分化: **元画像には存在しない**

したがって現監査候補 `formula-fem-7-2-2-042` はNG、上記再転記は**Pass 1 = OK**とする。

## `image043`～`image049` 直接目視再転記（2026-09-17）

GIF/PNG元画像を直接表示して、項順、添字、時刻上付き、符号、係数、列ベクトル成分数を照合した。

### `image043`

原画像は先頭が `=` で始まる。x/y/z各項を個別に並べ、表面張力は3成分、重力は4成分の列ベクトルである。

```latex
\[
\begin{aligned}
={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{V_i\}+V_y[C_y]\{V_i\}+V_z[C_z]\{V_i\}\\
&+\frac{1}{Re}[S_{xx}]\{V_i\}+\frac{1}{Re}[S_{xi}]\{V_x\}-\delta_{xi}[H_x]\{P\}\\
&+\frac{1}{Re}[S_{yy}]\{V_i\}+\frac{1}{Re}[S_{yi}]\{V_y\}-\delta_{yi}[H_y]\{P\}\\
&+\frac{1}{Re}[S_{zz}]\{V_i\}+\frac{1}{Re}[S_{zi}]\{V_z\}-\delta_{zi}[H_z]\{P\}\\
&+\frac{2K^*}{3We}n_iS
\begin{bmatrix}1\\1\\1\end{bmatrix}
-g_i^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix},
\qquad (i=1,2,3)
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image044`

原画像は係数行列ごとにまとめた式で、先頭が `=`。末尾は4成分零ベクトルへ等置される。

```latex
\[
\begin{aligned}
={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}\\
&+\frac{1}{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}\\
&+\frac{1}{Re}\left([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\}+[S_{zi}]\{V_z\}\right)\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}\\
&+\frac{2K^*}{3We}n_iS
\begin{bmatrix}1\\1\\1\end{bmatrix}
-g_i^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
\qquad (i=1,2,3)\\
={}&\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image045`

原画像は `image044` の式を先頭の継続等号なしで記載し、4成分零ベクトルへ等置している。

```latex
\[
\begin{aligned}
&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}\\
&+\frac{1}{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}\\
&+\frac{1}{Re}\left([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\}+[S_{zi}]\{V_z\}\right)\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}\\
&+\frac{2K^*}{3We}n_iS
\begin{bmatrix}1\\1\\1\end{bmatrix}
-g_i^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix},
\qquad (i=1,2,3)
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image046`

既知項を右辺へ移項した式。未知速度・圧力には `\tau+\Delta\tau`、右辺の既知速度には `\tau` が付く。表面張力は右辺で負、重力は正。

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_i\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}^{\tau+\Delta\tau}\\
&+\frac{1}{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}^{\tau+\Delta\tau}\\
&+\frac{1}{Re}\left([S_{xi}]\{V_x\}^{\tau+\Delta\tau}
+[S_{yi}]\{V_y\}^{\tau+\Delta\tau}
+[S_{zi}]\{V_z\}^{\tau+\Delta\tau}\right)\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_i\}^{\tau}
-\frac{2K^*}{3We}n_iS
\begin{bmatrix}1\\1\\1\end{bmatrix}
+g_i^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix},
\qquad (i=1,2,3)
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image047`

x方向成分。粘性項の交差成分は `[S_{yx}]`, `[S_{zx}]`。圧力項 `-[H_x]\{P\}` は `1/Re` の括弧外にある。

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_x\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_x\}^{\tau+\Delta\tau}\\
&+\frac{1}{Re}\left\{
(2[S_{xx}]+[S_{yy}]+[S_{zz}])\{V_x\}^{\tau+\Delta\tau}
+[S_{yx}]\{V_y\}^{\tau+\Delta\tau}
+[S_{zx}]\{V_z\}^{\tau+\Delta\tau}
\right\}\\
&-[H_x]\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_x\}^{\tau}
-\frac{2K^*}{3We}n_xS
\begin{bmatrix}1\\1\\1\end{bmatrix}
+g_x^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image048`

y方向成分。粘性項の交差成分は `[S_{xy}]`, `[S_{zy}]`。圧力項は `1/Re` の括弧外。

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_y\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_y\}^{\tau+\Delta\tau}\\
&+\frac{1}{Re}\left\{
[S_{xy}]\{V_x\}^{\tau+\Delta\tau}
+([S_{xx}]+2[S_{yy}]+[S_{zz}])\{V_y\}^{\tau+\Delta\tau}
+[S_{zy}]\{V_z\}^{\tau+\Delta\tau}
\right\}\\
&-[H_y]\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_y\}^{\tau}
-\frac{2K^*}{3We}n_yS
\begin{bmatrix}1\\1\\1\end{bmatrix}
+g_y^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image049`

z方向成分。粘性項の交差成分は `[S_{xz}]`, `[S_{yz}]`。圧力項は `1/Re` の括弧外。

```latex
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_z\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_z\}^{\tau+\Delta\tau}\\
&+\frac{1}{Re}\left\{
[S_{xz}]\{V_x\}^{\tau+\Delta\tau}
+[S_{yz}]\{V_y\}^{\tau+\Delta\tau}
+([S_{xx}]+[S_{yy}]+2[S_{zz}])\{V_z\}^{\tau+\Delta\tau}
\right\}\\
&-[H_z]\{P\}^{\tau+\Delta\tau}\\
={}&\frac{[C]}{\Delta\tau}\{V_z\}^{\tau}
-\frac{2K^*}{3We}n_zS
\begin{bmatrix}1\\1\\1\end{bmatrix}
+g_z^*\frac{V}{4}
\begin{bmatrix}1\\1\\1\\1\end{bmatrix},
\qquad (i=1,2,3)
\end{aligned}
\]
```

**Pass 1 = OK**。

### 直接照合で追加確認した現候補の不一致

`b_S` の混入だけでなく、`image047`～`image049` の現候補は圧力項を `1/Re` の括弧内へ入れていた。原画像では圧力項は粘性項の `1/Re` とは別項である。

したがって `image042`～`image049` は、原画像直接照合後の忠実再転記として **8/8 Pass 1 OK** とする。

## 一般化記法の優先監査対象

現監査候補では以下の画像対応式に `\sum_{a=x,y,z}` 等の一般化が導入されている。

- `image006`
- `image008`
- `image009`
- `image011`
- `image012`
- `image013`
- `image014`
- `image015`
- `image017`
- `image024`
- `image032`
- `image038`

これらは原画像に同じ総和記号があるか未確認なので、現時点ではNG確定とはしない。ただし、x/y/zを個別展開している原画像を総和記号へ一般化した可能性があるため優先してPass 1を実施する。

## 再転記ルール

1. x/y/zの個別式を原画像にない総和記号で一般化しない。
2. 行列・ベクトルの成分数、転置、項順を変えない。
3. 境界三角形の3成分局所ベクトルを4成分へ自動拡張しない。
4. `b_S`, `A_S`, `f_e` 等の写像記号は原画像に存在しない限り原文式へ入れない。
5. `image031`, `image037` の再利用箇所は元画像と同一LaTeXを使う。
6. 数学的説明は原文転記とは別ブロックで扱う。

## 現在の状態

- 元画像との対応付け: **49/49**
- 履歴から現候補NG確定: **8/49 (`image042～049`)**
- 一般化記法の優先監査対象: **12/12監査完了**
- 元画像直接Pass 1合格: **49/49**
- Pass 2: **0/49**

`image001`～`image049` のPass 1は全式完了。`007,010～041` の忠実転記は `fem_7_2_2_pass1_batch_a.md` / `batch_b.md` / `batch_c.md` に記録した。次工程は再監査HTMLへの反映後、Pass 2を49式すべてで実施する。
