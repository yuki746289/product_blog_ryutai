# 数式レビュー: fem/fem_7_2_2.html

更新日: 2026-09-17

## 対象

- ページ: `fem/fem_7_2_2.html`
- タイトル: 運動量収支式の離散化（4面体1次要素）
- 数式画像: `img/fem_d_momentum_tet.files/image001.png` ～ `image049.png`
- 対象数: 49式
- 状態: **元画像完全一致の再監査対象 / 対応付け49/49確認済み / Pass 1 = 11/49**

## 2026-09-16 方針変更

旧レビューでは、数学的整合性を優先して「面→要素写像を補足、または4成分要素ベクトルへ書き換える」等の方針を許容していた。
この方針は廃止する。

今後は次の順序で扱う。

1. `image001.png`～`image049.png` の**原画像の式をそのままMathJaxへ再現**する。
2. 一般化、総和記号化、行列化、成分統合、写像の追加等によって原画像と異なる式へ置き換えない。
3. 原画像に理論上の省略・誤記候補がある場合も原文式は維持する。
4. 面→要素写像等の補足は原文式の下へ別記する。
5. `.document/CHECKLIST_FORMULA_CONVERSION.md` のPass 1 / Pass 2を全49画像で実施する。

## 対応付け確認（2026-09-17）

通常ページでは `image001.png`～`image049.png` が元画像として保持されていることを確認した。
監査候補 `fem_7_2_2_mathjax_audit.html` では、`formula-fem-7-2-2-001`～`formula-fem-7-2-2-049` が同番号の `data-source-image` を参照しており、**49/49の対応を確認**した。

再利用箇所も追跡可能である。

- `image031.png` は後半の「係数をまとめて」で `formula-fem-7-2-2-031-repeat-2` として再利用。
- `image037.png` は後半の重力項で `formula-fem-7-2-2-037-repeat-2` として再利用。

これらの再利用ブロックは式数49の追加式とは数えず、元画像との同一性を確認する補助対象とする。

なお、監査候補には `\sum`、`\mathbf b_S` 等を用いた一般化・補足済み表現が含まれる箇所がある。これらが元画像と一致するかは**対応付け確認だけでは判定せず、Pass 1で必ず原画像と照合する**。

## 2026-09-17 履歴監査

Git履歴を確認すると、MathJax変換前の本文には境界三角形で得られる3節点表面力ベクトルを四面体4節点へアセンブルする写像について、後続式では写像を省略している旨の補足があった。

初回MathJax変換 `9a02677ad86ce8d4670233999e943b1d20b5d8f8` では、この省略をやめて `\mathbf b_S=A_S^T[1\;1\;1]^T` を導入し、`image042`～`image049` に対応する式本体へ組み込んでいる。

したがって、現監査候補の `image042`～`image049` 対応式は原画像忠実基準では**8/8 NG確定**とする。理論的に有用な写像説明は原文式とは別の補足へ分離する。

## `image006` / `image008` / `image009` 直接目視結果

元PNG/GIFを直接表示し、現監査候補と比較した。3式とも現監査候補では原画像にない総和記号化・成分統合・式変形が行われていたため、候補式はNGとした。以下の忠実再転記を **Pass 1 OK** とする。

### `image006`

原画像は、重み関数を4成分列ベクトルのまま明示し、x/y/z各方向の対流項・応力項を個別に記載している。現候補の `\sum_{a=x,y,z}` は原画像に存在しない。

```latex
\[
\begin{aligned}
&\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\left(
\frac{\partial V_i}{\partial\tau}
+V_x\frac{\partial V_i}{\partial X}
+V_y\frac{\partial V_i}{\partial Y}
+V_z\frac{\partial V_i}{\partial Z}
-\frac{\partial\sigma^*_{xi}}{\partial X}
-\frac{\partial\sigma^*_{yi}}{\partial Y}
-\frac{\partial\sigma^*_{zi}}{\partial Z}
-g_i^*
\right)dV\\
={}&\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial\tau}dV
+V_x\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial X}dV
+V_y\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial Y}dV\\
&+V_z\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial Z}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{xi}}{\partial X}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{yi}}{\partial Y}dV\\
&-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{zi}}{\partial Z}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
g_i^*dV
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image008`

原画像は時間微分をまだ差分化しておらず、x/y/z各方向の対流項・応力項を個別に記載している。現候補にある時間差分式と `\sum` は原画像にない。

```latex
\[
\begin{aligned}
={}&\int_V[N]^T\frac{\partial V_i}{\partial\tau}dV\\
&+V_x\int_V[N]^T\frac{\partial V_i}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial V_i}{\partial Y}dV
+V_z\int_V[N]^T\frac{\partial V_i}{\partial Z}dV\\
&-\int_V[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dV
-\int_V[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dV
-\int_V[N]^T\frac{\partial\sigma^*_{zi}}{\partial Z}dV\\
&-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

**Pass 1 = OK**。

### `image009`

原画像は時間項を節点速度の差分で表し、Green-Gauss適用後の表面積分・体積積分を x/y/z ごとに個別記載している。現候補の総和記号化および3方向の表面項統合は原画像にない。

```latex
\[
\begin{aligned}
={}&\int_V[N]^T
\frac{[N](\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau})}{\Delta\tau}dV\\
&+V_x\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial Y}dV
+V_z\int_V[N]^T\frac{\partial[N]\{V_i\}}{\partial Z}dV\\
&-\int_S[N]^T\sigma^*_{xi}n_xdS
+\int_V\left[\frac{\partial N}{\partial X}\right]^T\sigma^*_{xi}dV\\
&-\int_S[N]^T\sigma^*_{yi}n_ydS
+\int_V\left[\frac{\partial N}{\partial Y}\right]^T\sigma^*_{yi}dV\\
&-\int_S[N]^T\sigma^*_{zi}n_zdS
+\int_V\left[\frac{\partial N}{\partial Z}\right]^T\sigma^*_{zi}dV\\
&-\int_V[N]^Tg_i^*dV
\end{aligned}
\]
```

**Pass 1 = OK**。

## `image042` 直接目視結果

元画像 `image042.png` を直接表示し、現監査候補と比較した。

原画像:

```latex
\[
+\frac{2K^*}{3We}n_iS
\begin{bmatrix}1\\1\\1\end{bmatrix}
\]
```

確認結果:

- 原画像は**3成分** `[1,1,1]^T`。
- 係数は `2K^*/(3We)`。
- `n_iS` が続く。
- `\mathbf b_S`、`A_S`、4成分要素ベクトル化は原画像にない。
- 現監査候補 `formula-fem-7-2-2-042` は不一致。
- 元画像忠実再転記は**Pass 1 OK**。

詳細は `.document/formula_reviews/fem_7_2_2_retranscription.md` に記録した。

## `image043`～`image049` 直接目視結果

元GIF/PNGを直接表示し、既存候補および再転記LaTeXと照合した。

結果: **7/7 Pass 1 OK（再転記後）**。

主な確認点:

- `image043`: 原画像は先頭 `=`。x/y/z各方向を個別記載。表面張力は3成分、重力は4成分。
- `image044`: 先頭 `=`、末尾は4成分零ベクトル。面→要素写像は式本体に存在しない。
- `image045`: 4成分零ベクトルへ等置。表面張力は3成分のまま。
- `image046`: `\tau+\Delta\tau` の未知項を左辺、`\tau` の既知速度と表面張力・重力を右辺へ移項。表面張力は負、重力は正。
- `image047`: x成分の交差項は `[S_{yx}]`, `[S_{zx}]`。圧力項 `-[H_x]\{P\}` は `1/Re` の外。
- `image048`: y成分の交差項は `[S_{xy}]`, `[S_{zy}]`。圧力項 `-[H_y]\{P\}` は `1/Re` の外。
- `image049`: z成分の交差項は `[S_{xz}]`, `[S_{yz}]`。圧力項 `-[H_z]\{P\}` は `1/Re` の外。

### 現監査候補で新たに確定した不一致

`image047`～`image049` の現監査候補では、粘性項と圧力項を同じ `1/Re` 括弧内へまとめていた。
原画像では `1/Re` は粘性項のみに掛かり、圧力項はその外にある。

したがって `image042`～`image049` は、単に `b_S` を除去するだけでは不十分であり、原画像に従った再転記が必要である。

忠実LaTeX全文は `.document/formula_reviews/fem_7_2_2_retranscription.md` に保存した。

## 旧レビューの位置づけ

以下の数学的検証結果は参考資料として維持するが、**元画像一致の認証を意味しない**。

| 対象 | 数学的検証の旧判定 | 新基準での扱い |
|---|---|---|
| `image001`～`image003` | x/y/z方向運動量式として追跡可能 | 元画像と1文字ずつ再照合 |
| `image004` | 重み付き残差式として追跡可能 | 元画像どおり転記 |
| `image005` | 速度・圧力内挿式として追跡可能 | 元画像どおり転記 |
| `image006`～`image015` | 一般式展開・Green-Gauss・応力展開を追跡可能 | 項順・記号・添字を原画像どおり再照合 |
| `image016`～`image029` | 各行列項を追跡可能 | 行列全成分を位置単位で再照合 |
| `image030` | 四面体体積・境界三角形面積の積分公式として数学的に整合 | 原画像の表記をそのまま転記 |
| `image031` | 四面体一貫質量行列として数学的に整合 | 行列全成分を再照合 |
| `image032`～`image042` | 係数整理を追跡可能 | 原画像どおり再照合 |
| `image043`～`image046` | 面局所3ベクトル→要素4ベクトル写像省略あり | **原画像式を維持し、写像は補足のみ** |
| `image047`～`image049` | x/y/z最終成分式として追跡可能 | **原画像どおり再転記済み / Pass 1 OK** |

## R-FEM3D-MOM-001: 境界面ベクトルと四面体要素ベクトル

境界面は三角形なので、面局所表面張力ベクトルは3成分となる。
数値実装ではこれを四面体要素の対応節点へアセンブルする。

この写像は理論説明として有用だが、**元画像の式そのものへ追加してはならない**。

表示方針:

- 原文: 元画像の3成分式を忠実に表示。
- 補足: `f_e=A_f^T f_f` 等の写像説明を別ブロックで記載可能。
- 修正版・拡張式を表示する場合は、原文式とは別に `参考` と明示する。

## R-FEM3D-MOM-002: 積分公式

旧レビューでは `image030` の体積積分・面積積分公式は標準的な一次四面体要素の公式と整合すると判定した。
これは数学的評価であり、転記時の式変更理由にはしない。

## R-FEM3D-MOM-003: 「速度、圧力は定数」の説明

旧レビューでは、節点自由度が積分変数へ依存しないという意味として解釈した。
説明文は補足可能だが、原画像の数式は変更しない。

## 再監査チェック

- [x] `release_1.0.0` / 通常ページの画像出現順を確認。
- [x] 監査候補の全49式と元画像を1対1対応。
- [x] `image001`～`image049` で欠番・重複・再利用を確認。
- [x] `image006`, `image008`, `image009` を元画像直接照合し、忠実再転記Pass 1完了。
- [x] `image042`～`image049` を元画像直接照合し、忠実再転記Pass 1完了。
- [ ] 全画像でPass 1を完了。
- [ ] 全画像でPass 2を完了。
- [ ] x/y/z個別式を勝手に一般化していない。
- [ ] 総和記号等、原画像にない記法を導入していない。
- [ ] 行列の全成分が一致している。
- [x] `image042`～`image049` の表面張力面局所式を原画像どおり確認。
- [ ] 補足は原文式と分離されている監査候補へ修正済み。
- [ ] PC/スマホ表示確認済み。

## 現在の判定

**未完了 / 対応付け49/49、現候補NG確定11/49、忠実再転記Pass 1 = 11/49 (`image006`, `image008`, `image009`, `image042～049`)、Pass 2 = 0/49。**

次は `image011`～`image015`, `image017`, `image024`, `image032`, `image038` の一般化記法9式を優先して直接照合し、その後 `image001`～`image005`, `image007`, `image010` 等を番号順に埋める。
