from pathlib import Path
import re

PATH = Path('fem/fem_7_1_1.html')
text = PATH.read_bytes().decode('cp932')

formulas = {
1: r'''\[
\phi=
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial x}
+\frac{\partial V_y}{\partial y}
\right)=0
\]''',
3: r'''\[
\begin{aligned}
V_x&=N_1V_{x1}+N_2V_{x2}+N_3V_{x3}=[N]\{V_x\},\\
V_y&=N_1V_{y1}+N_2V_{y2}+N_3V_{y3}=[N]\{V_y\},\\
P&=N_1P_1+N_2P_2+N_3P_3=[N]\{P\}.
\end{aligned}
\]''',
4: r'''\[
\int_S[N]^T\phi\,dS
=
\int_S[N]^T\left[
\frac{\partial P}{\partial\tau}
+V_x\frac{\partial P}{\partial x}
+V_y\frac{\partial P}{\partial y}
+\frac{1}{Ma^2}\left(
\frac{\partial V_x}{\partial x}
+\frac{\partial V_y}{\partial y}
\right)
\right]dS
\]''',
5: r'''\[
\begin{aligned}
\int_S[N]^T\phi\,dS={}&
\int_S[N]^T\frac{\partial P}{\partial\tau}\,dS
+\int_S[N]^TV_x\frac{\partial P}{\partial x}\,dS
+\int_S[N]^TV_y\frac{\partial P}{\partial y}\,dS\\
&+\frac1{Ma^2}\int_S[N]^T\frac{\partial V_x}{\partial x}\,dS
+\frac1{Ma^2}\int_S[N]^T\frac{\partial V_y}{\partial y}\,dS.
\end{aligned}
\]''',
6: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S[N]^T\frac{\partial[N]\{P\}^{\tau+\Delta\tau}}{\partial x}dS
+V_y\int_S[N]^T\frac{\partial[N]\{P\}^{\tau+\Delta\tau}}{\partial y}dS\\
&+\frac1{Ma^2}\int_S[N]^T\frac{\partial[N]\{V_x\}^{\tau+\Delta\tau}}{\partial x}dS
+\frac1{Ma^2}\int_S[N]^T\frac{\partial[N]\{V_y\}^{\tau+\Delta\tau}}{\partial y}dS.
\end{aligned}
\]''',
7: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}\\
&+V_x\int_S[N]^T\frac{\partial[N]}{\partial x}dS\,\{P\}^{\tau+\Delta\tau}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial y}dS\,\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}\int_S[N]^T\frac{\partial[N]}{\partial x}dS\,\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}\int_S[N]^T\frac{\partial[N]}{\partial y}dS\,\{V_y\}^{\tau+\Delta\tau}.
\end{aligned}
\]''',
8: r'''\[
[N]^T[N]
=\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}N_1&N_2&N_3\end{bmatrix},
\]
\[
[N]^T\frac{\partial[N]}{\partial x}
=\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}
\begin{bmatrix}
\dfrac{\partial N_1}{\partial x}&
\dfrac{\partial N_2}{\partial x}&
\dfrac{\partial N_3}{\partial x}
\end{bmatrix},
\]
\[
[N]^T\frac{\partial[N]}{\partial y}\quad\text{も同様。}
\]''',
9: r'''\[
[N]^T[N]=
\begin{bmatrix}
N_1N_1&N_1N_2&N_1N_3\\
N_2N_1&N_2N_2&N_2N_3\\
N_3N_1&N_3N_2&N_3N_3
\end{bmatrix},
\]
\[
[N]^T\frac{\partial[N]}{\partial x}=
\begin{bmatrix}
N_1N_{1,x}&N_1N_{2,x}&N_1N_{3,x}\\
N_2N_{1,x}&N_2N_{2,x}&N_2N_{3,x}\\
N_3N_{1,x}&N_3N_{2,x}&N_3N_{3,x}
\end{bmatrix},
\qquad
N_{j,x}\equiv\frac{\partial N_j}{\partial x}.
\]''',
10: r'''\[
\frac1{Ma^2}\left(
\int_S[N]^T\frac{\partial[N]}{\partial x}dS\,\{V_x\}^{\tau+\Delta\tau}
+\int_S[N]^T\frac{\partial[N]}{\partial y}dS\,\{V_y\}^{\tau+\Delta\tau}
\right),
\]
\[
[N]^T\frac{\partial[N]}{\partial y}
=\begin{bmatrix}N_iN_{j,y}\end{bmatrix}_{i,j=1}^{3},
\qquad N_{j,y}\equiv\frac{\partial N_j}{\partial y}.
\]''',
11: r'''\[
N_i=L_i\qquad(i=1,2,3),
\qquad
[L]=\begin{bmatrix}L_1&L_2&L_3\end{bmatrix},
\]
\[
[N]^T[N]\rightarrow[L]^T[L],\qquad
[N]^T\frac{\partial[N]}{\partial x}\rightarrow[L]^T\frac{\partial[L]}{\partial x},\qquad
[N]^T\frac{\partial[N]}{\partial y}\rightarrow[L]^T\frac{\partial[L]}{\partial y}.
\]''',
12: r'''\[
\frac{\partial L_j}{\partial x}=\frac{c_{jx}}{2A},\qquad
\frac{\partial L_j}{\partial y}=\frac{c_{jy}}{2A},
\]
\[
[L]^T\frac{\partial[L]}{\partial x}
=\frac1{2A}
\begin{bmatrix}
L_1c_{1x}&L_1c_{2x}&L_1c_{3x}\\
L_2c_{1x}&L_2c_{2x}&L_2c_{3x}\\
L_3c_{1x}&L_3c_{2x}&L_3c_{3x}
\end{bmatrix},
\]
\[
y\text{方向は }c_{jy}\text{ を用いて同様。}
\]''',
13: r'''\[
\int_SL_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2A,
\]
\[
\int_SL_iL_j\,dS=
\begin{cases}
\dfrac{A}{12},&i\ne j,\\[4pt]
\dfrac{A}{6},&i=j,
\end{cases}
\qquad
\int_SL_i\,dS=\frac{A}{3}.
\]''',
14: r'''\[
\int_S[L]^T[L]dS
=\frac{A}{12}
\begin{bmatrix}
2&1&1\\1&2&1\\1&1&2
\end{bmatrix},
\]
\[
\int_S[L]^T\frac{\partial[L]}{\partial x}dS
=\frac{1}{2A}\frac{A}{3}
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix},
\qquad y\text{方向も同様。}
\]''',
15: r'''\[
[C]=\frac{A}{12}
\begin{bmatrix}
2&1&1\\1&2&1\\1&1&2
\end{bmatrix},
\]
\[
[C_x]=\frac16
\begin{bmatrix}
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}\\
c_{1x}&c_{2x}&c_{3x}
\end{bmatrix},
\qquad
[C_y]=\frac16
\begin{bmatrix}
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}\\
c_{1y}&c_{2y}&c_{3y}
\end{bmatrix}.
\]''',
16: r'''\[
\begin{aligned}
={}&[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}.
\end{aligned}
\]''',
17: r'''\[
\begin{bmatrix}0\\0\\0\end{bmatrix}
\]''',
18: r'''\[
[C]\frac{\{P\}^{\tau+\Delta\tau}-\{P\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}=\begin{bmatrix}0\\0\\0\end{bmatrix}.
\]''',
20: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{P\}^{\tau+\Delta\tau}
&+V_x[C_x]\{P\}^{\tau+\Delta\tau}
+V_y[C_y]\{P\}^{\tau+\Delta\tau}\\
&+\frac1{Ma^2}[C_x]\{V_x\}^{\tau+\Delta\tau}
+\frac1{Ma^2}[C_y]\{V_y\}^{\tau+\Delta\tau}
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\end{aligned}
\]''',
21: r'''\[
\left(
\frac{[C]}{\Delta\tau}+V_x[C_x]+V_y[C_y]
\right)\{P\}^{\tau+\Delta\tau}
+\frac1{Ma^2}\left(
[C_x]\{V_x\}^{\tau+\Delta\tau}
+[C_y]\{V_y\}^{\tau+\Delta\tau}
\right)
=\frac{[C]}{\Delta\tau}\{P\}^{\tau}.
\]''',
}

# Existing corrected image002 block: retain correction anchor and add conversion traceability.
old = '<div class="math-block" id="fix-r-fem2d-mass-001">'
new = '<div class="math-block" id="fix-r-fem2d-mass-001" data-source-image="./../img/fem_d_mass_tri.files/image002.png">\n<span id="formula-fem-7-1-1-002"></span>'
if old in text:
    text = text.replace(old, new, 1)
elif 'data-source-image="./../img/fem_d_mass_tri.files/image002.png"' not in text:
    raise RuntimeError('existing corrected image002 block not found')

for num, latex in formulas.items():
    src = f'./../img/fem_d_mass_tri.files/image{num:03d}.png'
    pattern = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    replacement = (
        f'<div class="math-block" id="formula-fem-7-1-1-{num:03d}" '
        f'data-source-image="{src}">\n{latex}\n</div>'
    )
    text, count = pattern.subn(lambda _m, r=replacement: r, text, count=1)
    if count != 1:
        raise RuntimeError(f'failed to replace {src}: count={count}')

heading = '<h2>・質量収支式の離散化</h2>'
if 'formula-conversion-note' not in text:
    text = text.replace(
        heading,
        heading + '\n\t\t\t<p id="formula-conversion-note">数式はMathJaxで表示しています。変換前の数式画像は照合用としてリポジトリ内に保持しています。</p>',
        1,
    )

# Clear text typo found during conversion.
text = text.replace('離散化式は、次式とります。', '離散化式は、次式となります。', 1)

# No formula image IMG tags should remain for this page.
for num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21]:
    src = f'./../img/fem_d_mass_tri.files/image{num:03d}.png'
    if re.search(r'<img\b[^>]*\bsrc=["\']' + re.escape(src) + r'["\']', text, re.I):
        raise RuntimeError(f'source image tag remains: {src}')

PATH.write_bytes(text.encode('cp932'))

# Add the newly corrected prose typo to revision history.
history_path = Path('revision_history.html')
history = history_path.read_bytes().decode('cp932')
if 'R-FEM2D-MASS-004' not in history:
    target = '<tr><td>R-FEM2D-MASS-003</td><td><a href="./fem/fem_7_1_1.html#fix-r-fem2d-mass-003">2D質量収支式</a></td><td>積分外へ出せる対象が速度・圧力場そのものではなく節点自由度であることを明記。</td></tr>'
    row = target + '\n\t\t<tr><td>R-FEM2D-MASS-004</td><td><a href="./fem/fem_7_1_1.html#formula-fem-7-1-1-004">2D質量収支式</a></td><td>本文の「離散化式は、次式とります。」を「離散化式は、次式となります。」へ修正。</td></tr>'
    if target not in history:
        raise RuntimeError('revision history insertion target not found')
    history = history.replace(target, row, 1)
    history_path.write_bytes(history.encode('cp932'))

print('Converted fem_7_1_1.html and updated revision history.')
