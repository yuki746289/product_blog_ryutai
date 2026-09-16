from pathlib import Path
import re

PATH = Path('fem/fem_7_2_1.html')
text = PATH.read_bytes().decode('cp932')

MATHJAX = r'''
	<script>
	window.MathJax = {
		tex: {inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']]},
		chtml: {displayAlign: 'left', displayIndent: '0'}
	};
	</script>
	<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
'''.strip('\n')

if 'tex-mml-chtml.js' not in text:
    text = text.replace('</head>', MATHJAX + '\n</head>', 1)

formulas = {
1: r'''\[
\phi=
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+V_z\frac{\partial P}{\partial z}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial x}
+\frac{\partial V_y}{\partial y}
+\frac{\partial V_z}{\partial z}
\right)=0
\]''',
2: r'''\[
\int_V[N]^T\phi\,dV
=\int_V
\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}\phi\,dV
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]''',
3: r'''\[
\begin{aligned}
V_x&=N_1V_{x1}+N_2V_{x2}+N_3V_{x3}+N_4V_{x4}=[N]\{V_x\},\\
V_y&=N_1V_{y1}+N_2V_{y2}+N_3V_{y3}+N_4V_{y4}=[N]\{V_y\},\\
V_z&=N_1V_{z1}+N_2V_{z2}+N_3V_{z3}+N_4V_{z4}=[N]\{V_z\},\\
P&=N_1P_1+N_2P_2+N_3P_3+N_4P_4=[N]\{P\}.
\end{aligned}
\]''',
4: r'''\[
\int_V[N]^T\phi\,dV
=
\int_V[N]^T\left[
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial X}
+V_y\frac{\partial P}{\partial Y}
+V_z\frac{\partial P}{\partial Z}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial X}
+\frac{\partial V_y}{\partial Y}
+\frac{\partial V_z}{\partial Z}
\right)
\right]dV
\]''',
5: r'''\[
\begin{aligned}
\int_V[N]^T\phi\,dV={}&
\int_V[N]^T\frac{\partial P}{\partial\tau}\,dV
+\int_V[N]^TV_x\frac{\partial P}{\partial X}\,dV
+\int_V[N]^TV_y\frac{\partial P}{\partial Y}\,dV\\
&+\int_V[N]^TV_z\frac{\partial P}{\partial Z}\,dV
+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_x}{\partial X}\,dV
+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_y}{\partial Y}\,dV\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial V_z}{\partial Z}\,dV.
\end{aligned}
\]''',
6: r'''\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\frac{\partial[N]\{P\}^{\tau+\Delta\tau}}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial[N]\{P\}^{\tau+\Delta\tau}}{\partial Y}dV\\
&+V_z\int_V[N]^T\frac{\partial[N]\{P\}^{\tau+\Delta\tau}}{\partial Z}dV\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_x\}^{\tau+\Delta\tau}}{\partial X}dV
+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_y\}^{\tau+\Delta\tau}}{\partial Y}dV\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]\{V_z\}^{\tau+\Delta\tau}}{\partial Z}dV.
\end{aligned}
\]''',
7: r'''\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\,
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{P\}^{\tau+\Delta\tau}
+V_y\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{P\}^{\tau+\Delta\tau}\\
&+V_z\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{V_y\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{V_z\}^{\tau+\Delta\tau}.
\end{aligned}
\]''',
8: r'''\[
[N]^T[N]
=\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix},
\]
\[
[N]^T\frac{\partial[N]}{\partial X}
=\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial X}&
\dfrac{\partial N_2}{\partial X}&
\dfrac{\partial N_3}{\partial X}&
\dfrac{\partial N_4}{\partial X}
\end{bmatrix}.
\]
\[
[N]^T\frac{\partial[N]}{\partial Y},\quad
[N]^T\frac{\partial[N]}{\partial Z}
\quad\text{も同様。}
\]''',
9: r'''\[
[N]^T[N]=
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3&N_1N_4\\
N_2N_1&N_2N_2&N_2N_3&N_2N_4\\
N_3N_1&N_3N_2&N_3N_3&N_3N_4\\
N_4N_1&N_4N_2&N_4N_3&N_4N_4
\end{bmatrix},
\]
\[
[N]^T\frac{\partial[N]}{\partial X}=
\begin{bmatrix}
N_1N_{1,X}&N_1N_{2,X}&N_1N_{3,X}&N_1N_{4,X}\\
N_2N_{1,X}&N_2N_{2,X}&N_2N_{3,X}&N_2N_{4,X}\\
N_3N_{1,X}&N_3N_{2,X}&N_3N_{3,X}&N_3N_{4,X}\\
N_4N_{1,X}&N_4N_{2,X}&N_4N_{3,X}&N_4N_{4,X}
\end{bmatrix}.
\]
\[
N_{j,X}\equiv\frac{\partial N_j}{\partial X},
\qquad Y,Z\text{方向も同様。}
\]''',
10: r'''\[
\frac1{Ma^2}
\left(
\int_V[N]^T\frac{\partial[N]}{\partial X}dV\,\{V_x\}^{\tau+\Delta\tau}
+\int_V[N]^T\frac{\partial[N]}{\partial Y}dV\,\{V_y\}^{\tau+\Delta\tau}
+\int_V[N]^T\frac{\partial[N]}{\partial Z}dV\,\{V_z\}^{\tau+\Delta\tau}
\right),
\]
\[
[N]^T\frac{\partial[N]}{\partial Y}
=\begin{bmatrix}N_iN_{j,Y}\end{bmatrix}_{i,j=1}^{4},
\qquad
[N]^T\frac{\partial[N]}{\partial Z}
=\begin{bmatrix}N_iN_{j,Z}\end{bmatrix}_{i,j=1}^{4}.
\]''',
11: r'''\[
N_i=L_i\qquad(i=1,2,3,4),
\]
\[
[L]=\begin{bmatrix}L_1&L_2&L_3&L_4\end{bmatrix},
\]
\[
[N]^T[N]\rightarrow[L]^T[L],\qquad
[N]^T\frac{\partial[N]}{\partial X}
\rightarrow[L]^T\frac{\partial[L]}{\partial X},
\]
\[
Y,Z\text{方向も同様に置き換える。}
\]''',
12: r'''\[
\frac{\partial L_j}{\partial X}=\frac{c_{jx}}{6V},\qquad
\frac{\partial L_j}{\partial Y}=\frac{c_{jy}}{6V},\qquad
\frac{\partial L_j}{\partial Z}=\frac{c_{jz}}{6V},
\]
\[
[L]^T\frac{\partial[L]}{\partial X}
=\frac1{6V}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}&L_1c_{4x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}&L_2c_{4x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}&L_3c_{4x}\\
L_4c_{1x}&L_4c_{2x}&L_4c_{3x}&L_4c_{4x}
\end{bmatrix},
\]
\[
Y,Z\text{方向は }c_{jy},c_{jz}\text{ を用いて同様。}
\]''',
13: r'''\[
\int_VL_1^pL_2^qL_3^rL_4^s\,dV
=\frac{p!q!r!s!}{(p+q+r+s+3)!}\,6V,
\]
\[
\int_VL_iL_j\,dV=
\begin{cases}
\dfrac{V}{20},&i\ne j,\\[4pt]
\dfrac{V}{10},&i=j,
\end{cases}
\qquad
\int_VL_i\,dV=\frac{V}{4}.
\]''',
14: r'''\[
\int_V[L]^T[L]dV
=\frac{V}{20}
\begin{bmatrix}
2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2
\end{bmatrix},
\]
\[
\int_V[L]^T\frac{\partial[L]}{\partial X}dV
=\frac{1}{6V}\frac{V}{4}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix},
\]
\[
Y,Z\text{方向も同様。}
\]''',
15: r'''\[
[C]=\frac{V}{20}
\begin{bmatrix}
2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2
\end{bmatrix},
\]
\[
[C_x]=\frac1{24}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}\\
c_{1x}&c_{2x}&c_{3x}&c_{4x}
\end{bmatrix},
\]
\[
[C_y]=\frac1{24}
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}\\
c_{1y}&c_{2y}&c_{3y}&c_{4y}
\end{bmatrix},
\qquad
[C_z]=\frac1{24}
\begin{bmatrix}
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}\\
c_{1z}&c_{2z}&c_{3z}&c_{4z}
\end{bmatrix}.
\]''',
16: r'''\[
\begin{aligned}
={}&[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}.
\end{aligned}
\]''',
17: r'''\[
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}
\]''',
18: r'''\[
\begin{aligned}
[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
&+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}=0.
\end{aligned}
\]''',
19: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{P\}^{\tau+\Delta\tau}
&+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+V_z[C_z]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_z]\{V_z\}^{\tau+\Delta\tau}
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\end{aligned}
\]''',
20: r'''\[
\begin{aligned}
\left(
\frac{[C]}{\Delta\tau}
+V_x[C_x]+V_y[C_y]+V_z[C_z]
\right)\{P\}^{\tau+\Delta\tau}
&+\frac1{Ma^2}\left(
[C_x]\{V_x\}^{\tau+\Delta\tau}
+[C_y]\{V_y\}^{\tau+\Delta\tau}
+[C_z]\{V_z\}^{\tau+\Delta\tau}
\right)\\
&=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\end{aligned}
\]''',
}

for num, latex in formulas.items():
    src = f'./../img/fem_d_mass_tet.files/image{num:03d}.png'
    pattern = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    replacement = (
        f'<div class="math-block" id="formula-fem-7-2-1-{num:03d}" '
        f'data-source-image="{src}">\n{latex}\n</div>'
    )
    text, count = pattern.subn(lambda _m, r=replacement: r, text, count=1)
    if count != 1:
        raise RuntimeError(f'failed to replace {src}: count={count}')

heading = '<h2>・質量収支式の離散化</h2>'
if 'formula-conversion-note' not in text:
    note = heading + '\n\t\t\t<p id="formula-conversion-note">数式はMathJaxで表示しています。変換前の数式画像は照合用としてリポジトリ内に保持しています。</p>'
    text = text.replace(heading, note, 1)

for num in formulas:
    src = f'./../img/fem_d_mass_tet.files/image{num:03d}.png'
    if re.search(r'<img\b[^>]*\bsrc=["\']' + re.escape(src) + r'["\']', text, re.I):
        raise RuntimeError(f'source image tag remains in HTML: {src}')

PATH.write_bytes(text.encode('cp932'))
print('Converted fem_7_2_1.html: 20 formulas -> MathJax, CP932 preserved.')
