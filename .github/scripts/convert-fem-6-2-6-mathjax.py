from pathlib import Path
import re

PATH = Path('fem/fem_6_2_6.html')
raw = PATH.read_bytes()
text = raw.decode('cp932')

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
21: r'''\[
\frac{\partial N_1}{\partial x}
=\frac{\partial L_1}{\partial x}
=\frac{c_{1x}}{6V}
=\frac{1}{6V}\left(-y_3z_4+z_3y_4+y_2z_4-y_2z_3-z_2y_4+z_2y_3\right)
\]''',
22: r'''\[
\frac{\partial N_1}{\partial y}
=\frac{\partial L_1}{\partial y}
=\frac{c_{1y}}{6V}
=\frac{1}{6V}\left(x_3z_4-z_3x_4-x_2z_4+x_2z_3+z_2x_4-z_2x_3\right)
\]''',
23: r'''\[
\frac{\partial N_1}{\partial z}
=\frac{\partial L_1}{\partial z}
=\frac{c_{1z}}{6V}
=\frac{1}{6V}\left(-x_3y_4+y_3x_4+x_2y_4-x_2y_3-y_2x_4+y_2x_3\right)
\]''',
24: r'''\[
\frac{\partial N_2}{\partial x}
=\frac{\partial L_2}{\partial x}
=\frac{c_{2x}}{6V}
=\frac{1}{6V}\left(y_3z_4-z_3y_4-y_1z_4+y_1z_3+z_1y_4-z_1y_3\right)
\]''',
25: r'''\[
\frac{\partial N_2}{\partial y}
=\frac{\partial L_2}{\partial y}
=\frac{c_{2y}}{6V}
=\frac{1}{6V}\left(-x_3z_4+z_3x_4+x_1z_4-x_1z_3-z_1x_4+z_1x_3\right)
\]''',
26: r'''\[
\frac{\partial N_2}{\partial z}
=\frac{\partial L_2}{\partial z}
=\frac{c_{2z}}{6V}
=\frac{1}{6V}\left(x_3y_4-y_3x_4-x_1y_4+x_1y_3+y_1x_4-y_1x_3\right)
\]''',
27: r'''\[
\frac{\partial N_3}{\partial x}
=\frac{\partial L_3}{\partial x}
=\frac{c_{3x}}{6V}
=\frac{1}{6V}\left(-y_2z_4+z_2y_4+y_1z_4-y_1z_2-z_1y_4+z_1y_2\right)
\]''',
28: r'''\[
\frac{\partial N_3}{\partial y}
=\frac{\partial L_3}{\partial y}
=\frac{c_{3y}}{6V}
=\frac{1}{6V}\left(x_2z_4-z_2x_4-x_1z_4+x_1z_2+z_1x_4-z_1x_2\right)
\]''',
29: r'''\[
\frac{\partial N_3}{\partial z}
=\frac{\partial L_3}{\partial z}
=\frac{c_{3z}}{6V}
=\frac{1}{6V}\left(-x_2y_4+y_2x_4+x_1y_4-x_1y_2-y_1x_4+y_1x_2\right)
\]''',
30: r'''\[
\frac{\partial N_4}{\partial x}
=\frac{\partial L_4}{\partial x}
=\frac{c_{4x}}{6V}
=\frac{1}{6V}\left(y_2z_3-z_2y_3-y_1z_3+y_1z_2+z_1y_3-z_1y_2\right)
\]''',
31: r'''\[
\frac{\partial N_4}{\partial y}
=\frac{\partial L_4}{\partial y}
=\frac{c_{4y}}{6V}
=\frac{1}{6V}\left(-x_2z_3+z_2x_3+x_1z_3-x_1z_2-z_1x_3+z_1x_2\right)
\]''',
32: r'''\[
\frac{\partial N_4}{\partial z}
=\frac{\partial L_4}{\partial z}
=\frac{c_{4z}}{6V}
=\frac{1}{6V}\left(x_2y_3-y_2x_3-x_1y_3+x_1y_2+y_1x_3-y_1x_2\right)
\]''',
}

for num, latex in formulas.items():
    src = f'./../img/fem_n_tet.files/image{num:03d}.png'
    pattern = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    replacement = (
        f'<div class="math-block" id="formula-fem-6-2-6-{num:03d}" '
        f'data-source-image="{src}">\n{latex}\n</div>'
    )
    text, count = pattern.subn(lambda _m, r=replacement: r, text, count=1)
    if count != 1:
        raise RuntimeError(f'failed to replace {src}: count={count}')

# Traceability note; source images remain in the repository for comparison/history.
marker = '<h2>・内挿関数<span class="ft"><i>N</i></span>の微分まとめ</h2>'
if 'formula-conversion-note' not in text:
    note = marker + '\n\t\t\t<p id="formula-conversion-note">数式はMathJaxで表示しています。変換前の数式画像は照合用としてリポジトリ内に保持しています。</p>'
    text = text.replace(marker, note, 1)

# All 12 source IMG tags must have been removed from the HTML body.
for num in formulas:
    src = f'./../img/fem_n_tet.files/image{num:03d}.png'
    if re.search(r'<img\b[^>]*\bsrc=["\']' + re.escape(src) + r'["\']', text, re.I):
        raise RuntimeError(f'source image tag remains in HTML: {src}')

PATH.write_bytes(text.encode('cp932'))
print('Converted fem_6_2_6.html: 12 formulas -> MathJax, CP932 preserved.')
