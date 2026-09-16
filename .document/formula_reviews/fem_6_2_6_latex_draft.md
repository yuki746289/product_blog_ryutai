# LaTeX変換ドラフト: fem/fem_6_2_6.html

## 対象

- ページ: `fem/fem_6_2_6.html`
- 画像: `img/fem_n_tet.files/image021.png` ～ `image032.png`
- 状態: HTML置換前ドラフト
- 数学レビュー: `fem_6_2_6_review.md` で確認済み

## N1

### image021.png

```latex
\[
\frac{\partial N_1}{\partial x}
=\frac{\partial L_1}{\partial x}
=\frac{c_{1x}}{6V}
=\frac{1}{6V}
\left(
-y_3z_4+z_3y_4+y_2z_4-y_2z_3-z_2y_4+z_2y_3
\right)
\]
```

### image022.png

```latex
\[
\frac{\partial N_1}{\partial y}
=\frac{\partial L_1}{\partial y}
=\frac{c_{1y}}{6V}
=\frac{1}{6V}
\left(
x_3z_4-z_3x_4-x_2z_4+x_2z_3+z_2x_4-z_2x_3
\right)
\]
```

### image023.png

```latex
\[
\frac{\partial N_1}{\partial z}
=\frac{\partial L_1}{\partial z}
=\frac{c_{1z}}{6V}
=\frac{1}{6V}
\left(
-x_3y_4+y_3x_4+x_2y_4-x_2y_3-y_2x_4+y_2x_3
\right)
\]
```

## N2

### image024.png

```latex
\[
\frac{\partial N_2}{\partial x}
=\frac{\partial L_2}{\partial x}
=\frac{c_{2x}}{6V}
=\frac{1}{6V}
\left(
y_3z_4-z_3y_4-y_1z_4+y_1z_3+z_1y_4-z_1y_3
\right)
\]
```

### image025.png

```latex
\[
\frac{\partial N_2}{\partial y}
=\frac{\partial L_2}{\partial y}
=\frac{c_{2y}}{6V}
=\frac{1}{6V}
\left(
-x_3z_4+z_3x_4+x_1z_4-x_1z_3-z_1x_4+z_1x_3
\right)
\]
```

### image026.png

```latex
\[
\frac{\partial N_2}{\partial z}
=\frac{\partial L_2}{\partial z}
=\frac{c_{2z}}{6V}
=\frac{1}{6V}
\left(
x_3y_4-y_3x_4-x_1y_4+x_1y_3+y_1x_4-y_1x_3
\right)
\]
```

## N3

### image027.png

```latex
\[
\frac{\partial N_3}{\partial x}
=\frac{\partial L_3}{\partial x}
=\frac{c_{3x}}{6V}
=\frac{1}{6V}
\left(
-y_2z_4+z_2y_4+y_1z_4-y_1z_2-z_1y_4+z_1y_2
\right)
\]
```

### image028.png

```latex
\[
\frac{\partial N_3}{\partial y}
=\frac{\partial L_3}{\partial y}
=\frac{c_{3y}}{6V}
=\frac{1}{6V}
\left(
x_2z_4-z_2x_4-x_1z_4+x_1z_2+z_1x_4-z_1x_2
\right)
\]
```

### image029.png

```latex
\[
\frac{\partial N_3}{\partial z}
=\frac{\partial L_3}{\partial z}
=\frac{c_{3z}}{6V}
=\frac{1}{6V}
\left(
-x_2y_4+y_2x_4+x_1y_4-x_1y_2-y_1x_4+y_1x_2
\right)
\]
```

## N4

### image030.png

```latex
\[
\frac{\partial N_4}{\partial x}
=\frac{\partial L_4}{\partial x}
=\frac{c_{4x}}{6V}
=\frac{1}{6V}
\left(
y_2z_3-z_2y_3-y_1z_3+y_1z_2+z_1y_3-z_1y_2
\right)
\]
```

### image031.png

```latex
\[
\frac{\partial N_4}{\partial y}
=\frac{\partial L_4}{\partial y}
=\frac{c_{4y}}{6V}
=\frac{1}{6V}
\left(
-x_2z_3+z_2x_3+x_1z_3-x_1z_2-z_1x_3+z_1x_2
\right)
\]
```

### image032.png

```latex
\[
\frac{\partial N_4}{\partial z}
=\frac{\partial L_4}{\partial z}
=\frac{c_{4z}}{6V}
=\frac{1}{6V}
\left(
x_2y_3-y_2x_3-x_1y_3+x_1y_2+y_1x_3-y_1x_2
\right)
\]
```

## 独立整合性確認

四面体一次要素は

```latex
\[
N_1+N_2+N_3+N_4=1
\]
```

なので、各座標で微分すると

```latex
\[
\sum_{i=1}^{4}\frac{\partial N_i}{\partial x}=0,
\qquad
\sum_{i=1}^{4}\frac{\partial N_i}{\partial y}=0,
\qquad
\sum_{i=1}^{4}\frac{\partial N_i}{\partial z}=0.
\]
```

上記12式の分子を各方向について加算するとすべて0となり、この条件を満たすことを確認済み。

## HTML置換時の条件

- 元画像ファイルは初回パイロットでは削除しない。
- 各数式ブロックに元画像パスを追跡できるコメントまたは属性を残す。
- MathJax表示と元画像を並べて最終照合する。
- スマホではページ全体ではなく数式ブロック単位で横スクロール可能にする。
- HTML本体のCP932を維持する。
