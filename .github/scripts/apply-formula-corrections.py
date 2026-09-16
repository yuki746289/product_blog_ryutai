from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('.')

MATHJAX = r'''
	<script>
	window.MathJax = {
		tex: {inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']]},
		chtml: {displayAlign: 'left', displayIndent: '0'}
	};
	</script>
	<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
'''.strip('\n')


def read_text(path: str):
    p = ROOT / path
    data = p.read_bytes()
    for enc in ('cp932', 'utf-8'):
        try:
            return data.decode(enc), enc
        except UnicodeDecodeError:
            pass
    raise RuntimeError(f'cannot decode {path}')


def write_text(path: str, text: str, enc: str):
    (ROOT / path).write_bytes(text.encode(enc))


def ensure_mathjax(text: str) -> str:
    if 'tex-mml-chtml.js' in text:
        return text
    return text.replace('</head>', MATHJAX + '\n</head>', 1)


def replace_img(text: str, src: str, replacement: str) -> str:
    pat = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    text2, n = pat.subn(replacement, text, count=1)
    if n != 1:
        raise RuntimeError(f'image reference not uniquely replaced: {src}, count={n}')
    return text2


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f'missing replacement target {label}')
    return text.replace(old, new, 1)


# Common stylesheet import.
lib, enc = read_text('css/lib.css')
if '@import url("math.css");' not in lib:
    lib = lib.replace('@import url("responsive.css");', '@import url("responsive.css");\n@import url("math.css");', 1)
write_text('css/lib.css', lib, enc)

# ---------------------------------------------------------------------------
# 2D mass conservation
# ---------------------------------------------------------------------------
path = 'fem/fem_7_1_1.html'
text, enc = read_text(path)
text = ensure_mathjax(text)
text = replace_img(text, './../img/fem_d_mass_tri.files/image002.png', r'''<div class="math-block" id="fix-r-fem2d-mass-001">
\[
\int_S [N]^T\phi\,dS
=\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\phi\,dS
=\int_S
\begin{bmatrix}0\\0\\0\end{bmatrix}dS
=\begin{bmatrix}0\\0\\0\end{bmatrix}.
\]
</div>''')
text = replace_once(text, '<p>速度、圧力は定数なので積分の外に出す</p>', '<p id="fix-r-fem2d-mass-003">形状関数内挿後の節点自由度は積分変数に依存しないため、積分の外に出します。</p>', '2d mass nodal-value explanation')
text = replace_once(text, '<p>ここで、体積積分の公式より</p>', '<p id="fix-r-fem2d-mass-002">ここで、三角形要素の面積積分の公式より</p>', '2d mass area integral wording')
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# 2D momentum conservation
# ---------------------------------------------------------------------------
path = 'fem/fem_7_1_2.html'
text, enc = read_text(path)
text = ensure_mathjax(text)
text = replace_img(text, './../img/fem_d_momentum_tri.files/image003.png', r'''<div class="math-block" id="fix-r-fem2d-mom-001">
\[
\int_S
\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}\phi_i\,dS
=\int_S
\begin{bmatrix}0\\0\\0\end{bmatrix}dS
=\begin{bmatrix}0\\0\\0\end{bmatrix}.
\]
</div>''')
text = replace_img(text, './../img/fem_d_momentum_tri.files/image004.png', r'''<div class="math-block" id="fix-r-fem2d-mom-002">
\[
\begin{aligned}
V_x &= N_1V_{x,1}+N_2V_{x,2}+N_3V_{x,3}=[N]\{V_x\},\\
V_y &= N_1V_{y,1}+N_2V_{y,2}+N_3V_{y,3}=[N]\{V_y\},\\
P   &= N_1P_1+N_2P_2+N_3P_3=[N]\{P\}.
\end{aligned}
\]
</div>''')
text = replace_once(text, '<p>速度、圧力は定数なので積分の外に出す</p>', '<p>形状関数内挿後の節点自由度は積分変数に依存しないため、積分の外に出します。</p>', '2d momentum nodal-value explanation')
text = replace_img(text, './../img/fem_d_momentum_tri.files/image027.png', r'''<div class="math-block" id="fix-r-fem2d-mom-003">
<span id="fix-r-fem2d-mom-005"></span>
\[
\int_S L_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2A,
\]
\[
\int_S L_iL_j\,dS=
\begin{cases}
\dfrac{A}{12}, & i\ne j,\\[4pt]
\dfrac{A}{6}, & i=j,
\end{cases}
\qquad
\int_S L_i\,dS=\frac{A}{3},
\]
\[
\int_L L_1^pL_2^q\,dL
=\frac{p!q!}{(p+q+1)!}\,L,
\qquad
\int_L L_i\,dL=\frac{L}{2}.
\]
</div>''')
text = replace_img(text, './../img/fem_d_momentum_tri.files/image032.png', r'''<div class="math-block" id="fix-r-fem2d-mom-004">
\[
+\frac{K^*}{We}\,n_iL
\begin{bmatrix}1\\1\end{bmatrix}
\]
</div>
<div class="correction-note" id="fix-r-fem2d-mom-007">
境界辺上の2節点ベクトルは、要素方程式へ加算するときに境界辺の節点番号から三角形要素の3節点へ写像します。以降では
\(\mathbf b_L=A_L^T[1\;1]^T\)
と表し、例えば境界辺が要素節点1–2なら \(\mathbf b_L=[1\;1\;0]^T\) となります。
</div>''')

formula037 = r'''<div class="math-block">
\[
\begin{aligned}
0={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+V_x[C_x]\{V_i\}+V_y[C_y]\{V_i\}\\
&+\frac1{Re}[S_{xx}]\{V_i\}+\frac1{Re}[S_{xi}]\{V_x\}-\delta_{xi}[H_x]\{P\}\\
&+\frac1{Re}[S_{yy}]\{V_i\}+\frac1{Re}[S_{yi}]\{V_y\}-\delta_{yi}[H_y]\{P\}\\
&+\frac{K^*}{We}Ln_i\,\mathbf b_L
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},\qquad i=1,2.
\end{aligned}
\]
</div>'''
formula038 = r'''<div class="math-block" id="fix-r-fem2d-mom-006">
\[
\begin{aligned}
0={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y])\{V_i\}\\
&+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}
+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\})\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}
+\frac{K^*}{We}Ln_i\,\mathbf b_L
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},\qquad i=1,2.
\end{aligned}
\]
</div>'''
formula039 = r'''<div class="math-block">
\[
\begin{aligned}
[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_i\}
+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}\\
&+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}\\
&+\frac{K^*}{We}Ln_i\,\mathbf b_L
-g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}
=\begin{bmatrix}0\\0\\0\end{bmatrix},\qquad i=1,2.
\end{aligned}
\]
</div>'''
formula040 = r'''<div class="math-block">
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_i\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_i\}^{\tau+\Delta\tau}
+\frac1{Re}([S_{xx}]+[S_{yy}])\{V_i\}^{\tau+\Delta\tau}\\
&+\frac1{Re}([S_{xi}]\{V_x\}^{\tau+\Delta\tau}+[S_{yi}]\{V_y\}^{\tau+\Delta\tau})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y])\{P\}^{\tau+\Delta\tau}\\
&=\frac{[C]}{\Delta\tau}\{V_i\}^{\tau}
-\frac{K^*}{We}Ln_i\,\mathbf b_L
+g_i^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix},\qquad i=1,2.
\end{aligned}
\]
</div>'''
formula041 = r'''<div class="math-block">
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_x\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_x\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left((2[S_{xx}]+[S_{yy}])\{V_x\}^{\tau+\Delta\tau}
+[S_{yx}]\{V_y\}^{\tau+\Delta\tau}-[H_x]\{P\}^{\tau+\Delta\tau}\right)\\
&=\frac{[C]}{\Delta\tau}\{V_x\}^{\tau}
-\frac{K^*}{We}Ln_x\,\mathbf b_L
+g_x^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}.
\end{aligned}
\]
</div>'''
formula042 = r'''<div class="math-block">
\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_y\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y])\{V_y\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left([S_{xy}]\{V_x\}^{\tau+\Delta\tau}
+([S_{xx}]+2[S_{yy}])\{V_y\}^{\tau+\Delta\tau}-[H_y]\{P\}^{\tau+\Delta\tau}\right)\\
&=\frac{[C]}{\Delta\tau}\{V_y\}^{\tau}
-\frac{K^*}{We}Ln_y\,\mathbf b_L
+g_y^*\frac{A}{3}\begin{bmatrix}1\\1\\1\end{bmatrix}.
\end{aligned}
\]
</div>'''
for num, formula in [(37,formula037),(38,formula038),(39,formula039),(40,formula040),(41,formula041),(42,formula042)]:
    text = replace_img(text, f'./../img/fem_d_momentum_tri.files/image{num:03d}.png', formula)
text = text.replace('既知の項を右辺に移項すします。', '既知の項を右辺に移項します。')
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# 3D mass conservation: explain linearization and nodal-value treatment.
# ---------------------------------------------------------------------------
path = 'fem/fem_7_2_1.html'
text, enc = read_text(path)
text = replace_once(text, '<p>速度、圧力は定数なので積分の外に出す</p>', '<p id="fix-r-fem3d-mass-001">形状関数内挿後の節点自由度は積分変数に依存しないため、積分の外に出します。この式変形では、対流項の係数側に現れる <span class="ft"><i>V</i><sub>x</sub>, <i>V</i><sub>y</sub>, <i>V</i><sub>z</sub></span> を既知係数として扱う線形化を前提としています。</p>', '3d mass linearization explanation')
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# 3D momentum: document boundary-face to tetrahedron-node assembly.
# ---------------------------------------------------------------------------
path = 'fem/fem_7_2_2.html'
text, enc = read_text(path)
text = ensure_mathjax(text)
text = replace_once(text, '<p>速度、圧力は定数なので積分の外に出す</p>', '<p>形状関数内挿後の節点自由度は積分変数に依存しないため、積分の外に出します。</p>', '3d momentum nodal-value explanation')
needle = '<p>重力項</p>\n\t\t\t<p class="im" style="text-align:left;"><img src="./../img/fem_d_momentum_tet.files/image037.png"></p><br>'
note = needle + r'''
			<div class="correction-note" id="fix-r-fem3d-mom-001">
				境界三角形で得られる3節点の表面力ベクトルは、要素方程式へ加算するときに境界面の節点番号から四面体4節点へ写像します。以下の式ではこのアセンブリ写像を省略しています。面局所ベクトルを \(\mathbf f_S\) とすると、要素ベクトルは \(\mathbf f_e=A_S^T\mathbf f_S\) です。例えば境界面が要素節点1–2–3なら、第4成分を0として加算します。
			</div>'''
text = replace_once(text, needle, note, '3d boundary assembly note')
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# Tetrahedron volume sign convention.
# ---------------------------------------------------------------------------
path = 'fem/fem_6_2_1.html'
text, enc = read_text(path)
old = '<p><span class="ft">4</span>面体要素の体積を示します。</p>'
new = old + '\n\t\t\t<p class="correction-note" id="fix-r-tet-n-001">以降の式で <span class="ft"><i>V</i></span> は正の要素体積を表します。節点順序によって体積行列式が負になる場合は、絶対値を用いるか、正の向きになるよう節点順序を統一します。</p>'
text = replace_once(text, old, new, 'tetrahedron volume sign convention')
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# Footer link to public correction history.
# ---------------------------------------------------------------------------
path = 'footer.html'
text, enc = read_text(path)
if 'revision_history.html' not in text:
    text = text.replace('<div id="copyright">', '<div style="margin-bottom:4px;"><a href="./revision_history.html" target="_parent">修正履歴</a></div>\n\t\t<div id="copyright">', 1)
write_text(path, text, enc)

# ---------------------------------------------------------------------------
# Public correction history page.
# ---------------------------------------------------------------------------
history = r'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ja">
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="content-type" content="text/html; charset=shift_jis">
	<meta http-equiv="content-style-type" content="text/css">
	<meta name="description" content="有限要素法・流体力学による数値計算サイトの数式・記述修正履歴。">
	<title>修正履歴 - 有限要素法・流体力学による数値計算</title>
	<link href="./css/lib.css" rel="stylesheet" type="text/css" media="all">
</head>
<body>
	<div id="wrapper">
	<div id="header">
		<h1><a href="./index.html">有限要素法・流体力学による数値計算</a></h1>
		<br style="clear:both;">
		<ul style="margin-left:30px;"><li><a href="./index.html">index</a>&gt;</li><li>修正履歴&gt;</li></ul>
		<hr>
	</div>
	<div id="main">
	<div id="image"><p>流体力学から数値計算まで</p><p><img src="./img/shiki1.gif"></p><p><img src="./img/shiki2.gif"></p></div>
	<div id="content"><div id="content-text">
		<h2>修正履歴</h2>
		<p>数式画像のテキスト化・検証時に確認した誤記、表記不整合、説明不足の修正記録です。リンクから修正箇所へ直接移動できます。</p>
		<h2>2026-09-16</h2>
		<table class="correction-history">
		<tr><th>ID</th><th>対象</th><th>修正内容</th></tr>
		<tr><td>R-FEM2D-MASS-001</td><td><a href="./fem/fem_7_1_1.html#fix-r-fem2d-mass-001">2D質量収支式</a></td><td>2D三角形要素の重み付き残差の積分領域を V,dV から S,dS へ修正。</td></tr>
		<tr><td>R-FEM2D-MASS-002</td><td><a href="./fem/fem_7_1_1.html#fix-r-fem2d-mass-002">2D質量収支式</a></td><td>「体積積分の公式」を「三角形要素の面積積分の公式」へ修正。</td></tr>
		<tr><td>R-FEM2D-MASS-003</td><td><a href="./fem/fem_7_1_1.html#fix-r-fem2d-mass-003">2D質量収支式</a></td><td>積分外へ出せる対象が速度・圧力場そのものではなく節点自由度であることを明記。</td></tr>
		<tr><td>R-FEM2D-MOM-001</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-001">2D運動量収支式</a></td><td>2D三角形要素の重み付き残差の積分領域を V,dV から S,dS へ修正。</td></tr>
		<tr><td>R-FEM2D-MOM-002</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-002">2D運動量収支式</a></td><td>速度内挿式末尾の不要な =0 を削除し、Vx,Vy,P の内挿表記を統一。</td></tr>
		<tr><td>R-FEM2D-MOM-003 / 005</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-003">2D運動量収支式</a></td><td>一次線要素の積分公式を (p+q+1)! に修正し、∫Li dL=L/2 とした。面積積分途中式の V も A に修正。</td></tr>
		<tr><td>R-FEM2D-MOM-004</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-004">2D運動量収支式</a></td><td>線積分公式の修正に合わせ、表面張力項の係数を 2K*/We から K*/We へ修正し、後続式へ反映。</td></tr>
		<tr><td>R-FEM2D-MOM-006</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-006">2D運動量収支式</a></td><td>2D方向添字を i=1,2 に修正。</td></tr>
		<tr><td>R-FEM2D-MOM-007</td><td><a href="./fem/fem_7_1_2.html#fix-r-fem2d-mom-007">2D境界辺ベクトル</a></td><td>境界辺2節点ベクトルから三角形3節点へのアセンブリ写像を補足。</td></tr>
		<tr><td>R-FEM3D-MOM-001</td><td><a href="./fem/fem_7_2_2.html#fix-r-fem3d-mom-001">3D境界面ベクトル</a></td><td>境界面3節点ベクトルから四面体4節点へのアセンブリ写像が式中で省略されていることを補足。</td></tr>
		<tr><td>R-FEM3D-MASS-001</td><td><a href="./fem/fem_7_2_1.html#fix-r-fem3d-mass-001">3D質量収支式</a></td><td>対流項の係数側速度を既知係数として扱う線形化と、節点自由度を積分外へ出す理由を明記。</td></tr>
		<tr><td>R-TET-N-001</td><td><a href="./fem/fem_6_2_1.html#fix-r-tet-n-001">四面体要素体積</a></td><td>V を正の要素体積として扱う符号規約と節点向きの前提を補足。</td></tr>
		</table>
	</div></div>
	</div>
	<div id="sub"><iframe src="./menu.html" id="menu" name="menu" width="180" scrolling="no" frameborder="0"></iframe></div>
	<div id="footer"><iframe id="ft" name="ft" src="./footer.html" width="100%" scrolling="no" frameborder="0"></iframe></div>
	</div>
</body>
</html>
'''
write_text('revision_history.html', history, 'cp932')

print('Formula corrections and revision history applied.')
