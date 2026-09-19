# 数式再監査進捗（Word基準 + 既存LaTeX差分）

開始日: 2026-09-19
更新日: 2026-09-19

## 正本・優先順位

1. 元HP画像
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
- Wordレンダリング画像で端の記号が欠ける場合は、Wordの構造化抽出テキストと元画像を優先する。
- 判断不能は HOLD とし、推測修正しない。

## fem_7_2_2 現在の進捗

| 工程 | 進捗 | 状態 |
|---|---:|---|
| Word数式 ↔ 既存LaTeX差分監査 | **49/49** | 完了 |
| 元HP画像 ↔ Word直接照合 | **10/49** | pilot 001～010 完了、10/10で式内容一致 |
| 差分修正のHTML反映 | **完了** | develop反映済み |
| 静的LaTeX/HTML QA | **完了** | PASS |
| MathJaxブラウザ Pass 2 | 未実施 | 次工程 |
| 元画像↔Word追加スポット監査 | 10/49 | 011以降を継続 |

### Word基準監査 49/49 の結果

- `001～010`: 元HP画像とWordを直接並べて確認。Wordを基準に既存LaTeXを再監査。
- `011～049`: Word数式（レンダリング + 構造化抽出）と既存LaTeXを全件比較。
- 既存LaTeXが一致する箇所はそのまま再利用。
- 差異のある箇所だけ修正した。

### 今回見つかった主な修正

| image | 修正内容 |
|---|---|
| 005 | 元Wordにない行末カンマと余分な行間指定を除去 |
| 006 | 元HP画像 + Wordに合わせて、時間記号 `τ`、式範囲、展開範囲を復元 |
| 007 | 006と同内容だが、元画像007固有の改行構成を復元 |
| 010 | 表面応力積分と重力積分を元画像どおり別行化 |
| 011, 012 | 元式の `-(-2K^*/We)` を簡略化せず、二重負号をそのまま復元 |
| 015 | 元Wordにない `(i=1,2,3)` 前のカンマを除去 |
| 030 | 元Wordにない `(i\ne j)` 後のカンマを除去 |
| 043, 045, 046, 049 | 元Wordにない `(i=1,2,3)` 前のカンマを除去 |

### 重点確認済み事項

- `image005`: 圧力節点添字は **z**（`P_{z,1}～P_{z,4}`）。理論上の推測で変更しない。
- `image006`: 元HP画像とWordはいずれも時間微分が **τ**。
- `image011/012`: 表面張力項は **二重負号を保持**。
- 表面張力ベクトルは3成分、重力ベクトルは4成分。
- 最終式の交差項:
  - x: `[S_{yx}], [S_{zx}]`
  - y: `[S_{xy}], [S_{zy}]`
  - z: `[S_{xz}], [S_{yz}]`
- 最終式の圧力項は `1/Re` の外。

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

## 静的LaTeX/HTML QA 結果

2026-09-19 実施。

- math-block: **51個**
- ID重複: **0**
- 元画像参照: **image001～image049 = 49/49存在**
- 意図した再掲: image031 / image037
- `\\[` / `\\]` の表示数式区切り: **全ブロック整合**
- `aligned`, `bmatrix`, `cases` の begin/end: **全ブロック整合**
- image005 の `P_{z,*}`: 維持確認
- image006 の `τ`: 維持確認
- image011/012 の二重負号: 維持確認

**静的QA = PASS。**

## 次回再開位置

1. MathJaxブラウザ Pass 2。
2. 元HP画像↔Wordの追加スポット監査（011以降）。
3. Pass 2結果を本進捗ファイルへ追記。
