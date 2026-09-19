# 数式再監査進捗（Word基準 + 既存LaTeX差分）

開始日: 2026-09-19

## 正本・優先順位

1. ユーザー提示の元画像 / 現在の正本画像
2. Word数式（元画像から貼り付けたもの）
3. 現在のLaTeX
4. 旧監査記録

旧監査の Pass 1 = OK は今回の再監査では未確認扱いとする。

## 再監査ルール

- Word数式を基本転記元とし、既存LaTeXは差分比較して再利用する。
- 元画像とWordの対応は 1:1 に限定しない。1:N / N:1 の分割・結合を許容する。
- 元画像は、式範囲・改行・分割/結合・貼り付け違いの確認に用いる。
- `t / τ`, `i / j`, `x / y / z`, 大小文字、添字、上付き、`∂ / d`, `+ / -` は重点確認する。
- 全体類似度が高くても上記の1文字差を自動合格にしない。
- 変換済みDOCX/LibreOfficeレンダリングで旧Equation Editor式が崩れる箇所があるため、変換結果だけを正本にしない。
- 判断不能は HOLD とし、推測修正しない。

## fem_7_2_2

| image | Word/元画像確認 | 既存LaTeX | 新再監査 | 備考 |
|---|---|---|---|---|
| 001 | Wordと元画像の構造一致 | 一致 | DONE | 時間記号は τ |
| 002 | Wordと元画像の構造一致 | 一致 | DONE | 時間記号は τ |
| 003 | Wordと元画像の構造一致 | 一致 | DONE | 時間記号は τ |
| 004 | 元画像と式内容一致 | 一致 | DONE | 4成分ベクトル + φ_i |
| 005 | Wordと元画像を再照合 | 一致 | DONE | 圧力節点添字は z |
| 006 | 元HP画像 + Wordを再照合 | 修正済み | DONE | 時間記号は τ。残差積分から各積分項まで同一画像内に含む |
| 007 | 元HP画像 + Wordを再照合 | 修正済み | DONE | 006と同じ式内容だが改行構成が異なる。画像007の改行に合わせて復元 |
| 008 | 元HP画像 + Wordを再照合 | 一致 | DONE | [N]^T表記、τ、対流3項・応力3項・重力項の行構成一致 |
| 009 | 元HP画像 + Wordを再照合 | 一致 | DONE | 時間差分 + Green-Gauss後のx/y/z各項を個別確認 |
| 010 | 元HP画像 + Wordを再照合 | 改行修正 | DONE | 表面応力積分と重力積分を元画像どおり別行に分離 |

進捗: 10 / 49（新再監査）

## image006 確定内容

元HP画像（image006.gif）とWordレンダリングを並べて再確認し、両者が一致することを確認した。
時間微分の分母は **τ**。画像006は残差積分から個別積分への展開までを含む。

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
\frac{\partial V_i}{\partial Y}dV
+V_z\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial V_i}{\partial Z}dV\\
&-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{xi}}{\partial X}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{yi}}{\partial Y}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\frac{\partial\sigma^*_{zi}}{\partial Z}dV
-\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
g_i^*dV
\end{aligned}
\]
```

## 次回再開位置

`fem_7_2_2 / image011` から。
