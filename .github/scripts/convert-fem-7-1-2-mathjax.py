from pathlib import Path
import re

PATH = Path('fem/fem_7_1_2.html')
text = PATH.read_bytes().decode('cp932')

# Compact notation used only where it is mathematically identical to the expanded 3x3 matrices.
formulas = {
1: r'''\[
\phi_x=
\frac{\partial V_x}{\partial\tau}
+V_x\frac{\partial V_x}{\partial X}
+V_y\frac{\partial V_x}{\partial Y}
-\frac{\partial\sigma^*_{xx}}{\partial X}
-\frac{\partial\sigma^*_{yx}}{\partial Y}
-g_x^*=0
\]''',
2: r'''\[
\phi_y=
\frac{\partial V_y}{\partial\tau}
+V_x\frac{\partial V_y}{\partial X}
+V_y\frac{\partial V_y}{\partial Y}
-\frac{\partial\sigma^*_{xy}}{\partial X}
-\frac{\partial\sigma^*_{yy}}{\partial Y}
-g_y^*=0
\]''',
5: r'''\[
\int_S[N]^T\phi_i\,dS
=\int_S[N]^T\left(
\frac{\partial V_i}{\partial\tau}
+V_x\frac{\partial V_i}{\partial X}
+V_y\frac{\partial V_i}{\partial Y}
-\frac{\partial\sigma^*_{xi}}{\partial X}
-\frac{\partial\sigma^*_{yi}}{\partial Y}
-g_i^*\right)dS,
\qquad i=1,2.
\]''',
6: r'''\[
\begin{aligned}
\int_S[N]^T\phi_i\,dS={}&
\int_S[N]^T\frac{\partial V_i}{\partial\tau}dS
+V_x\int_S[N]^T\frac{\partial V_i}{\partial X}dS
+V_y\int_S[N]^T\frac{\partial V_i}{\partial Y}dS\\
&-\int_S[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dS
-\int_S[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dS
-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
7: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}\\
&+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}
-\int_S[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dS
-\int_S[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dS
-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
8: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\sigma^*_{xi}dS
+\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\sigma^*_{yi}dS\\
&-\int_L[N]^T\left(\sigma^*_{xi}n_x+\sigma^*_{yi}n_y\right)dL
-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
9: r'''\[
\sigma^*_{xi}n_x+\sigma^*_{yi}n_y
=-\frac{2K^*}{We}n_i,
\]
\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\sigma^*_{xi}dS
+\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\sigma^*_{yi}dS\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL
-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
10: r'''\[
\sigma^*_{xi}=-\delta_{xi}P+\frac1{Re}\left(
\frac{\partial V_i}{\partial X}+\frac{\partial V_x}{\partial x_i}\right),
\qquad
\sigma^*_{yi}=-\delta_{yi}P+\frac1{Re}\left(
\frac{\partial V_i}{\partial Y}+\frac{\partial V_y}{\partial x_i}\right).
\]
\[
-\int_L[N]^T\left(-\frac{2K^*}{We}n_i\right)dL
=+\frac{2K^*}{We}n_i\int_L[N]^TdL.
\]''',
11: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\int_S\left(\frac{\partial[N]}{\partial X}\right)^T
\left[-\delta_{xi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial X}+\frac{\partial V_x}{\partial x_i}\right)\right]dS\\
&+\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T
\left[-\delta_{yi}P+\frac1{Re}\left(\frac{\partial V_i}{\partial Y}+\frac{\partial V_y}{\partial x_i}\right)\right]dS\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL
-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
12: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial V_i}{\partial X}dS
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial V_x}{\partial x_i}dS
-\delta_{xi}\int_S\left(\frac{\partial[N]}{\partial X}\right)^TPdS\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial V_i}{\partial Y}dS
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial V_y}{\partial x_i}dS
-\delta_{yi}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^TPdS\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
13: r'''\[
\begin{aligned}
={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_x\}\\
&-\delta_{xi}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T[N]dS\,\{P\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_y\}
-\delta_{yi}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T[N]dS\,\{P\}\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL-\int_S[N]^Tg_i^*dS.
\end{aligned}
\]''',
14: r'''\[
\begin{aligned}
0={}&\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_x\}
-\delta_{xi}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T[N]dS\,\{P\}\\
&+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_y\}
-\delta_{yi}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T[N]dS\,\{P\}\\
&+\frac{2K^*}{We}n_i\int_L[N]^TdL-\int_S[N]^Tg_i^*dS,
\qquad i=1,2.
\end{aligned}
\]''',
15: r'''\[
\int_S[N]^T[N]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]''',
16: r'''\[
V_x\int_S[N]^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+V_y\int_S[N]^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}
\]''',
17: r'''\[
\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial X}dS\,\{V_i\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_x\}
-\delta_{xi}\int_S\left(\frac{\partial[N]}{\partial X}\right)^T[N]dS\,\{P\}
\]''',
18: r'''\[
\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial Y}dS\,\{V_i\}
+\frac1{Re}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial x_i}dS\,\{V_y\}
-\delta_{yi}\int_S\left(\frac{\partial[N]}{\partial Y}\right)^T[N]dS\,\{P\}
\]''',
19: r'''\[
+\frac{2K^*}{We}n_i\int_L[N]^TdL
\]''',
20: r'''\[
-g_i^*\int_S[N]^TdS,\qquad i=1,2
\]''',
21: r'''\[
\int_S[L]^T[L]dS\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau},
\qquad [L]=\begin{bmatrix}L_1&L_2&L_3\end{bmatrix}
\]''',
22: r'''\[
V_x\int_S\frac1{2A}[L]^T\mathbf c_x^T dS\,\{V_i\}
+V_y\int_S\frac1{2A}[L]^T\mathbf c_y^T dS\,\{V_i\},
\]
\[
\mathbf c_x=\begin{bmatrix}c_{1x}\\c_{2x}\\c_{3x}\end{bmatrix},\qquad
\mathbf c_y=\begin{bmatrix}c_{1y}\\c_{2y}\\c_{3y}\end{bmatrix}.
\]''',
23: r'''\[
\frac1{Re}\int_S\frac{1}{4A^2}\mathbf c_x\mathbf c_x^T dS\,\{V_i\}
+\frac1{Re}\int_S\frac{1}{4A^2}\mathbf c_x\mathbf c_i^T dS\,\{V_x\}
-\delta_{xi}\int_S\frac1{2A}\mathbf c_x[L]dS\,\{P\}
\]''',
24: r'''\[
\frac1{Re}\int_S\frac{1}{4A^2}\mathbf c_y\mathbf c_y^T dS\,\{V_i\}
+\frac1{Re}\int_S\frac{1}{4A^2}\mathbf c_y\mathbf c_i^T dS\,\{V_y\}
-\delta_{yi}\int_S\frac1{2A}\mathbf c_y[L]dS\,\{P\}
\]''',
25: r'''\[
+\frac{2K^*}{We}n_i\int_L
\begin{bmatrix}L_1\\L_2\end{bmatrix}dL
\]''',
26: r'''\[
-g_i^*\int_S
\begin{bmatrix}L_1\\L_2\\L_3\end{bmatrix}dS,
\qquad i=1,2
\]''',
28: r'''\[
[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau},
\qquad
[C]=\frac{A}{12}
\begin{bmatrix}2&1&1\\1&2&1\\1&1&2\end{bmatrix}
\]''',
29: r'''\[
V_x\frac1{2A}\frac{A}{3}\,\mathbf 1\mathbf c_x^T\{V_i\}
+V_y\frac1{2A}\frac{A}{3}\,\mathbf 1\mathbf c_y^T\{V_i\},
\qquad
\mathbf 1=\begin{bmatrix}1\\1\\1\end{bmatrix}
\]''',
30: r'''\[
\frac1{Re}\frac{A}{4A^2}\mathbf c_x\mathbf c_x^T\{V_i\}
+\frac1{Re}\frac{A}{4A^2}\mathbf c_x\mathbf c_i^T\{V_x\}
-\delta_{xi}\frac{A}{6A}\mathbf c_x\mathbf 1^T\{P\}
\]''',
31: r'''\[
\frac1{Re}\frac{A}{4A^2}\mathbf c_y\mathbf c_y^T\{V_i\}
+\frac1{Re}\frac{A}{4A^2}\mathbf c_y\mathbf c_i^T\{V_y\}
-\delta_{yi}\frac{A}{6A}\mathbf c_y\mathbf 1^T\{P\}
\]''',
33: r'''\[
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},
\qquad i=1,2
\]''',
34: r'''\[
V_x\frac16\,\mathbf 1\mathbf c_x^T\{V_i\}
+V_y\frac16\,\mathbf 1\mathbf c_y^T\{V_i\}
\]''',
35: r'''\[
\frac1{4ARe}\mathbf c_x\mathbf c_x^T\{V_i\}
+\frac1{4ARe}\mathbf c_x\mathbf c_i^T\{V_x\}
-\frac{\delta_{xi}}6\mathbf c_x\mathbf 1^T\{P\}
\]''',
36: r'''\[
\frac1{4ARe}\mathbf c_y\mathbf c_y^T\{V_i\}
+\frac1{4ARe}\mathbf c_y\mathbf c_i^T\{V_y\}
-\frac{\delta_{yi}}6\mathbf c_y\mathbf 1^T\{P\}
\]''',
}

# Traceability for already-corrected MathJax blocks.
def attach_existing(block_id, source_num, formula_id):
    global text
    old = f'<div class="math-block" id="{block_id}">'
    if old in text:
        new = (f'<div class="math-block" id="{block_id}" '
               f'data-source-image="./../img/fem_d_momentum_tri.files/image{source_num:03d}.png">\n'
               f'<span id="{formula_id}"></span>')
        text = text.replace(old, new, 1)
    elif f'data-source-image="./../img/fem_d_momentum_tri.files/image{source_num:03d}.png"' not in text:
        raise RuntimeError(f'existing block not found: {block_id}')

attach_existing('fix-r-fem2d-mom-001', 3, 'formula-fem-7-1-2-003')
attach_existing('fix-r-fem2d-mom-002', 4, 'formula-fem-7-1-2-004')
attach_existing('fix-r-fem2d-mom-003', 27, 'formula-fem-7-1-2-027')
attach_existing('fix-r-fem2d-mom-004', 32, 'formula-fem-7-1-2-032')
attach_existing('fix-r-fem2d-mom-006', 38, 'formula-fem-7-1-2-038')

# Replace still-image-based equations. Repeated source images get a repeat suffix after the first instance.
for num, latex in formulas.items():
    src = f'./../img/fem_d_momentum_tri.files/image{num:03d}.png'
    pattern = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    matches = list(pattern.finditer(text))
    if not matches:
        raise RuntimeError(f'no image tag found for {src}')
    count_total = len(matches)
    counter = {'n': 0}
    def repl(_m):
        counter['n'] += 1
        suffix = '' if counter['n'] == 1 else f'-repeat-{counter["n"]}'
        ident = f'formula-fem-7-1-2-{num:03d}{suffix}'
        return (f'<div class="math-block" id="{ident}" data-source-image="{src}">\n{latex}\n</div>')
    text, count = pattern.subn(repl, text)
    if count != count_total:
        raise RuntimeError(f'replacement count mismatch {src}: {count}/{count_total}')

# Add source tracking/IDs to image037 and images039-042, which were corrected earlier and no longer have img tags.
def attach_by_token(token, source_num, formula_id):
    global text
    pos = text.find(token)
    if pos < 0:
        raise RuntimeError(f'unique token not found for image{source_num:03d}: {token[:30]}')
    start = text.rfind('<div class="math-block">', 0, pos)
    if start < 0:
        # May already have attributes.
        if f'id="{formula_id}"' in text:
            return
        raise RuntimeError(f'math block start not found for image{source_num:03d}')
    opening = '<div class="math-block">'
    new_opening = (f'<div class="math-block" id="{formula_id}" '
                   f'data-source-image="./../img/fem_d_momentum_tri.files/image{source_num:03d}.png">')
    text = text[:start] + text[start:].replace(opening, new_opening, 1)

attach_by_token('0={}&[C]\\frac{\\{V_i\\}^{\\tau+\\Delta\\tau}-\\{V_i\\}^{\\tau}}', 37, 'formula-fem-7-1-2-037')
attach_by_token('[C]\\frac{\\{V_i\\}^{\\tau+\\Delta\\tau}-\\{V_i\\}^{\\tau}}{\\Delta\\tau}\n&+(V_x[C_x]+V_y[C_y])', 39, 'formula-fem-7-1-2-039')
attach_by_token('\\frac{[C]}{\\Delta\\tau}\\{V_i\\}^{\\tau+\\Delta\\tau}', 40, 'formula-fem-7-1-2-040')
attach_by_token('\\frac{[C]}{\\Delta\\tau}\\{V_x\\}^{\\tau+\\Delta\\tau}', 41, 'formula-fem-7-1-2-041')
attach_by_token('\\frac{[C]}{\\Delta\\tau}\\{V_y\\}^{\\tau+\\Delta\\tau}', 42, 'formula-fem-7-1-2-042')

# The second already-corrected image032 occurrence: add traceability without duplicating the primary formula ID.
needle = '<div class="math-block">\n\\[\n+\\frac{K^*}{We}\\,n_iL\n\\begin{bmatrix}1\\\\1\\end{bmatrix}'
if needle in text:
    text = text.replace(
        '<div class="math-block">',
        '<div class="math-block" id="formula-fem-7-1-2-032-repeat-2" data-source-image="./../img/fem_d_momentum_tri.files/image032.png">',
        1 if text.find('<div class="math-block">') == text.find(needle) else 0
    )
# More robustly locate the un-attributed surface-tension block if still present.
if 'formula-fem-7-1-2-032-repeat-2' not in text:
    pos = text.find('\\frac{K^*}{We}\\,n_iL', text.find('fix-r-fem2d-mom-004') + 1)
    if pos >= 0:
        start = text.rfind('<div class="math-block">', 0, pos)
        if start >= 0:
            text = text[:start] + text[start:].replace(
                '<div class="math-block">',
                '<div class="math-block" id="formula-fem-7-1-2-032-repeat-2" data-source-image="./../img/fem_d_momentum_tri.files/image032.png">',
                1,
            )

heading = '<h2>・運動量収支式の離散化</h2>'
if 'formula-conversion-note' not in text:
    text = text.replace(
        heading,
        heading + '\n\t\t\t<p id="formula-conversion-note">数式はMathJaxで表示しています。変換前の数式画像は照合用としてリポジトリ内に保持しています。</p>',
        1,
    )

# All 42 original formula image files must now have no IMG tag in this page.
for num in range(1, 43):
    src = f'./../img/fem_d_momentum_tri.files/image{num:03d}.png'
    if re.search(r'<img\b[^>]*\bsrc=["\']' + re.escape(src) + r'["\']', text, re.I):
        raise RuntimeError(f'source image tag remains: {src}')

# Each unique source image must have a traceable formula anchor.
for num in range(1, 43):
    if f'formula-fem-7-1-2-{num:03d}' not in text:
        raise RuntimeError(f'missing formula ID for image{num:03d}')

PATH.write_bytes(text.encode('cp932'))
print('Converted fem_7_1_2.html: all 42 source equations are MathJax/traceable.')
