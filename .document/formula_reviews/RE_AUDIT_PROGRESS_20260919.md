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
| 006 | ユーザー提示元画像で再確認 | 不一致→修正 | DONE | 左辺 ∫[N]^T φ_i dV を含む。時間微分は t。次画像の展開を混在させない |
| 007 | 対応付け再確認中 | 候補あり | TODO | 006との式境界を独立確認 |
| 008 | 対応付け再確認中 | 候補あり | TODO | Word式との対応確認 |
| 009 | 対応付け再確認中 | 候補あり | TODO | Word式との対応確認 |
| 010 | 対応付け再確認中 | 候補あり | TODO | Word式との対応確認 |

進捗: 6 / 49（新再監査）

## image006 確定内容

```latex
\[
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\phi_i\,dV
=
\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\left(
\frac{\partial V_i}{\partial t}
+V_x\frac{\partial V_i}{\partial X}
+V_y\frac{\partial V_i}{\partial Y}
+V_z\frac{\partial V_i}{\partial Z}
-\frac{\partial\sigma^*_{xi}}{\partial X}
-\frac{\partial\sigma^*_{yi}}{\partial Y}
-\frac{\partial\sigma^*_{zi}}{\partial Z}
-g_i^*
\right)dV
\]
```

## 次回再開位置

`fem_7_2_2 / image007` から。
