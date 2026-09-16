from pathlib import Path
import re

PATH = Path('fem/fem_7_2_2.html')
text = PATH.read_bytes().decode('cp932')

formulas = {
1: r'''\[
\phi_x=\frac{\partial V_x}{\partial\tau}
+V_x\frac{\partial V_x}{\partial X}+V_y\frac{\partial V_x}{\partial Y}+V_z\frac{\partial V_x}{\partial Z}
-\frac{\partial\sigma^*_{xx}}{\partial X}-\frac{\partial\sigma^*_{yx}}{\partial Y}-\frac{\partial\sigma^*_{zx}}{\partial Z}-g_x^*=0
\]''',
2: r'''\[
\phi_y=\frac{\partial V_y}{\partial\tau}
+V_x\frac{\partial V_y}{\partial X}+V_y\frac{\partial V_y}{\partial Y}+V_z\frac{\partial V_y}{\partial Z}
-\frac{\partial\sigma^*_{xy}}{\partial X}-\frac{\partial\sigma^*_{yy}}{\partial Y}-\frac{\partial\sigma^*_{zy}}{\partial Z}-g_y^*=0
\]''',
3: r'''\[
\phi_z=\frac{\partial V_z}{\partial\tau}
+V_x\frac{\partial V_z}{\partial X}+V_y\frac{\partial V_z}{\partial Y}+V_z\frac{\partial V_z}{\partial Z}
-\frac{\partial\sigma^*_{xz}}{\partial X}-\frac{\partial\sigma^*_{yz}}{\partial Y}-\frac{\partial\sigma^*_{zz}}{\partial Z}-g_z^*=0
\]''',
4: r'''\[
\int_V[N]^T\phi_i\,dV
=\int_V\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}\phi_i\,dV
=\begin{bmatrix}0\\0\\0\\0\end{bmatrix},\qquad i=1,2,3
\]''',
5: r'''\[
\begin{aligned}
V_x&=[N]\{V_x\},\qquad V_y=[N]\{V_y\},\\
V_z&=[N]\{V_z\},\qquad P=[N]\{P\},\\
[N]&=\begin{bmatrix}N_1&N_2&N_3&N_4\end{bmatrix}.
\end{aligned}
\]''',
6: r'''\[
\int_V[N]^T\phi_i\,dV
=\int_V[N]^T\left(
\frac{\partial V_i}{\partial\tau}
+\sum_{a=x,y,z}V_a\frac{\partial V_i}{\partial a}
-\sum_{a=x,y,z}\frac{\partial\sigma^*_{ai}}{\partial a}
-g_i^*\right)dV,\qquad i=1,2,3
\]''',
7: r'''\[
\begin{aligned}
\int_V[N]^T\phi_i\,dV={}&
\int_V[N]^T\frac{\partial V_i}{\partial\tau}dV
+V_x\int_V[N]^T\frac{\partial V_i}{\partial X}dV
+V_y\int_V[N]^T\frac{\partial V_i}{\partial Y}dV
+V_z\int_V[N]^T\frac{\partial V_i}{\partial Z}dV\\
&-\int_V[N]^T\frac{\partial\sigma^*_{xi}}{\partial X}dV
-\int_V[N]^T\frac{\partial\sigma^*_{yi}}{\partial Y}dV
-\int_V[N]^T\frac{\partial\sigma^*_{zi}}{\partial Z}dV
-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
8: r'''\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}\\
&-\sum_{a=x,y,z}\int_V[N]^T\frac{\partial\sigma^*_{ai}}{\partial a}dV
-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
9: r'''\[
\begin{aligned}
={}&\int_V[N]^T[N]dV\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}\\
&+\sum_{a=x,y,z}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\sigma^*_{ai}dV
-\int_S[N]^T\left(\sigma^*_{xi}n_x+\sigma^*_{yi}n_y+\sigma^*_{zi}n_z\right)dS
-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
10: r'''\[
\sigma^*_{xi}n_x+\sigma^*_{yi}n_y+\sigma^*_{zi}n_z=-\frac{2K^*}{We}n_i,
\]
\[
-\int_S[N]^T(\boldsymbol\sigma_i^*\cdot\mathbf n)dS
=+\frac{2K^*}{We}n_i\int_S[N]^TdS.
\]''',
11: r'''\[
\sigma^*_{ai}=-\delta_{ai}P+\frac1{Re}\left(\frac{\partial V_i}{\partial a}+\frac{\partial V_a}{\partial x_i}\right),
\qquad a=x,y,z.
\]
\[
\begin{aligned}
\sum_{a=x,y,z}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\sigma^*_{ai}dV
={}&\sum_{a=x,y,z}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T
\left[-\delta_{ai}P+\frac1{Re}\left(\frac{\partial V_i}{\partial a}+\frac{\partial V_a}{\partial x_i}\right)\right]dV.
\end{aligned}
\]''',
12: r'''\[
\begin{aligned}
0={}&\int_V[N]^T[N]dV\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}\\
&+\sum_{a=x,y,z}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T
\left[-\delta_{ai}P+\frac1{Re}\left(\frac{\partial V_i}{\partial a}+\frac{\partial V_a}{\partial x_i}\right)\right]dV\\
&+\frac{2K^*}{We}n_i\int_S[N]^TdS-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
13: r'''\[
\begin{aligned}
0={}&\text{蓄積項}+\text{対流項}
+\sum_{a=x,y,z}\left[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial V_i}{\partial a}dV
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial V_a}{\partial x_i}dV
-\delta_{ai}\int_V\left(\frac{\partial[N]}{\partial a}\right)^TPdV\right]\\
&+\frac{2K^*}{We}n_i\int_S[N]^TdS-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
14: r'''\[
\begin{aligned}
0={}&\int_V[N]^T[N]dV\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}\\
&+\sum_{a=x,y,z}\left[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial[N]}{\partial x_i}dV\,\{V_a\}
-\delta_{ai}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T[N]dV\,\{P\}\right]\\
&+\frac{2K^*}{We}n_i\int_S[N]^TdS-\int_V[N]^Tg_i^*dV.
\end{aligned}
\]''',
15: r'''\[
\begin{aligned}
0={}&\int_V[N]^T[N]dV\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}\\
&+\sum_{a=x,y,z}\left[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T\frac{\partial[N]}{\partial x_i}dV\,\{V_a\}
-\delta_{ai}\int_V\left(\frac{\partial[N]}{\partial a}\right)^T[N]dV\,\{P\}\right]\\
&+\frac{2K^*}{We}n_i\int_S[N]^TdS-g_i^*\int_V[N]^TdV,
\qquad i=1,2,3.
\end{aligned}
\]''',
16: r'''\[
\int_V[N]^T[N]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
\]''',
17: r'''\[
\sum_{a=x,y,z}V_a\int_V[N]^T\frac{\partial[N]}{\partial a}dV\,\{V_i\}
\]''',
18: r'''\[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial X}dV\,\{V_i\}
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial X}\right)^T\frac{\partial[N]}{\partial x_i}dV\,\{V_x\}
-\delta_{xi}\int_V\left(\frac{\partial[N]}{\partial X}\right)^T[N]dV\,\{P\}
\]''',
19: r'''\[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial Y}dV\,\{V_i\}
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial Y}\right)^T\frac{\partial[N]}{\partial x_i}dV\,\{V_y\}
-\delta_{yi}\int_V\left(\frac{\partial[N]}{\partial Y}\right)^T[N]dV\,\{P\}
\]''',
20: r'''\[
\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial Z}\right)^T\frac{\partial[N]}{\partial Z}dV\,\{V_i\}
+\frac1{Re}\int_V\left(\frac{\partial[N]}{\partial Z}\right)^T\frac{\partial[N]}{\partial x_i}dV\,\{V_z\}
-\delta_{zi}\int_V\left(\frac{\partial[N]}{\partial Z}\right)^T[N]dV\,\{P\}
\]''',
21: r'''\[
+\frac{2K^*}{We}n_i\int_S\begin{bmatrix}N_1\\N_2\\N_3\end{bmatrix}dS
\]''',
22: r'''\[
-g_i^*\int_V\begin{bmatrix}N_1\\N_2\\N_3\\N_4\end{bmatrix}dV,
\qquad i=1,2,3
\]''',
23: r'''\[
\int_V[L]^T[L]dV\,
\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau},
\qquad [L]=\begin{bmatrix}L_1&L_2&L_3&L_4\end{bmatrix}
\]''',
24: r'''\[
\sum_{a=x,y,z}V_a\int_V\frac1{6V}[L]^T\mathbf c_a^T dV\,\{V_i\},
\qquad
\mathbf c_a=\begin{bmatrix}c_{1a}\\c_{2a}\\c_{3a}\\c_{4a}\end{bmatrix}
\]''',
25: r'''\[
\frac1{Re}\int_V\frac1{36V^2}\mathbf c_x\mathbf c_x^T dV\,\{V_i\}
+\frac1{Re}\int_V\frac1{36V^2}\mathbf c_x\mathbf c_i^T dV\,\{V_x\}
-\delta_{xi}\int_V\frac1{6V}\mathbf c_x[L]dV\,\{P\}
\]''',
26: r'''\[
\frac1{Re}\int_V\frac1{36V^2}\mathbf c_y\mathbf c_y^T dV\,\{V_i\}
+\frac1{Re}\int_V\frac1{36V^2}\mathbf c_y\mathbf c_i^T dV\,\{V_y\}
-\delta_{yi}\int_V\frac1{6V}\mathbf c_y[L]dV\,\{P\}
\]''',
27: r'''\[
\frac1{Re}\int_V\frac1{36V^2}\mathbf c_z\mathbf c_z^T dV\,\{V_i\}
+\frac1{Re}\int_V\frac1{36V^2}\mathbf c_z\mathbf c_i^T dV\,\{V_z\}
-\delta_{zi}\int_V\frac1{6V}\mathbf c_z[L]dV\,\{P\}
\]''',
28: r'''\[
+\frac{2K^*}{We}n_i\int_S\begin{bmatrix}L_1\\L_2\\L_3\end{bmatrix}dS
\]''',
29: r'''\[
-g_i^*\int_V\begin{bmatrix}L_1\\L_2\\L_3\\L_4\end{bmatrix}dV,
\qquad i=1,2,3
\]''',
30: r'''\[
\int_VL_1^pL_2^qL_3^rL_4^s\,dV
=\frac{p!q!r!s!}{(p+q+r+s+3)!}\,6V,
\]
\[
\int_VL_iL_j\,dV=\begin{cases}V/20,&i\ne j,\\V/10,&i=j,\end{cases}
\qquad \int_VL_i\,dV=V/4,
\]
\[
\int_SL_1^pL_2^qL_3^r\,dS
=\frac{p!q!r!}{(p+q+r+2)!}\,2S,
\qquad \int_SL_i\,dS=S/3.
\]''',
31: r'''\[
[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau},
\qquad
[C]=\frac{V}{20}
\begin{bmatrix}2&1&1&1\\1&2&1&1\\1&1&2&1\\1&1&1&2\end{bmatrix}
\]''',
32: r'''\[
\sum_{a=x,y,z}V_a\frac1{6V}\frac{V}{4}\,\mathbf 1_4\mathbf c_a^T\{V_i\},
\qquad \mathbf 1_4=\begin{bmatrix}1\\1\\1\\1\end{bmatrix}
\]''',
33: r'''\[
\frac1{Re}\frac{V}{36V^2}\mathbf c_x\mathbf c_x^T\{V_i\}
+\frac1{Re}\frac{V}{36V^2}\mathbf c_x\mathbf c_i^T\{V_x\}
-\delta_{xi}\frac{V}{24V}\mathbf c_x\mathbf 1_4^T\{P\}
\]''',
34: r'''\[
\frac1{Re}\frac{V}{36V^2}\mathbf c_y\mathbf c_y^T\{V_i\}
+\frac1{Re}\frac{V}{36V^2}\mathbf c_y\mathbf c_i^T\{V_y\}
-\delta_{yi}\frac{V}{24V}\mathbf c_y\mathbf 1_4^T\{P\}
\]''',
35: r'''\[
\frac1{Re}\frac{V}{36V^2}\mathbf c_z\mathbf c_z^T\{V_i\}
+\frac1{Re}\frac{V}{36V^2}\mathbf c_z\mathbf c_i^T\{V_z\}
-\delta_{zi}\frac{V}{24V}\mathbf c_z\mathbf 1_4^T\{P\}
\]''',
36: r'''\[
\mathbf f_S=\frac{2K^*}{We}n_i\frac{S}{3}
\begin{bmatrix}1\\1\\1\end{bmatrix}
\]''',
37: r'''\[
-g_i^*\frac{V}{4}\begin{bmatrix}1\\1\\1\\1\end{bmatrix},
\qquad i=1,2,3
\]''',
38: r'''\[
\sum_{a=x,y,z}V_a[C_a]\{V_i\},
\qquad [C_a]=\frac1{24}\mathbf 1_4\mathbf c_a^T
\]''',
39: r'''\[
\frac1{Re}[S_{xx}]\{V_i\}+\frac1{Re}[S_{xi}]\{V_x\}-\delta_{xi}[H_x]\{P\},
\quad [S_{ab}]=\frac1{36V}\mathbf c_a\mathbf c_b^T,
\quad [H_a]=\frac1{24}\mathbf c_a\mathbf 1_4^T
\]''',
40: r'''\[
\frac1{Re}[S_{yy}]\{V_i\}+\frac1{Re}[S_{yi}]\{V_y\}-\delta_{yi}[H_y]\{P\}
\]''',
41: r'''\[
\frac1{Re}[S_{zz}]\{V_i\}+\frac1{Re}[S_{zi}]\{V_z\}-\delta_{zi}[H_z]\{P\}
\]''',
42: r'''\[
\mathbf b_S=A_S^T\begin{bmatrix}1\\1\\1\end{bmatrix}\in\mathbb R^4,
\qquad
\mathbf f_e^{(S)}=\frac{2K^*}{3We}n_iS\,\mathbf b_S.
\]''',
43: r'''\[
\begin{aligned}
0={}&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}\\
&+\frac1{Re}\bigl([S_{xx}]+[S_{yy}]+[S_{zz}]\bigr)\{V_i\}
+\frac1{Re}\bigl([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\}+[S_{zi}]\{V_z\}\bigr)\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}
+\frac{2K^*}{3We}n_iS\,\mathbf b_S
-g_i^*\frac{V}{4}\mathbf 1_4,
\qquad i=1,2,3.
\end{aligned}
\]''',
44: r'''\[
\begin{aligned}
&[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}
+\frac1{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}\\
&\quad+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\}+[S_{zi}]\{V_z\})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}\\
&\quad+\frac{2K^*}{3We}n_iS\,\mathbf b_S
-g_i^*\frac{V}{4}\mathbf 1_4
=\mathbf 0_4,
\qquad i=1,2,3.
\end{aligned}
\]''',
45: r'''\[
\begin{aligned}
[C]\frac{\{V_i\}^{\tau+\Delta\tau}-\{V_i\}^{\tau}}{\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}
+\frac1{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}\\
&+\frac1{Re}([S_{xi}]\{V_x\}+[S_{yi}]\{V_y\}+[S_{zi}]\{V_z\})
-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}\\
&+\frac{2K^*}{3We}n_iS\,\mathbf b_S-g_i^*\frac{V}{4}\mathbf 1_4=\mathbf 0_4.
\end{aligned}
\]''',
46: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_i\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_i\}^{\tau+\Delta\tau}
+\frac1{Re}([S_{xx}]+[S_{yy}]+[S_{zz}])\{V_i\}^{\tau+\Delta\tau}\\
&+\frac1{Re}([S_{xi}]\{V_x\}^{\tau+\Delta\tau}+[S_{yi}]\{V_y\}^{\tau+\Delta\tau}+[S_{zi}]\{V_z\}^{\tau+\Delta\tau})\\
&-(\delta_{xi}[H_x]+\delta_{yi}[H_y]+\delta_{zi}[H_z])\{P\}^{\tau+\Delta\tau}\\
&=\frac{[C]}{\Delta\tau}\{V_i\}^{\tau}
-\frac{2K^*}{3We}n_iS\,\mathbf b_S+g_i^*\frac{V}{4}\mathbf 1_4,
\qquad i=1,2,3.
\end{aligned}
\]''',
47: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_x\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_x\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left((2[S_{xx}]+[S_{yy}]+[S_{zz}])\{V_x\}^{\tau+\Delta\tau}
+[S_{yx}]\{V_y\}^{\tau+\Delta\tau}+[S_{zx}]\{V_z\}^{\tau+\Delta\tau}-[H_x]\{P\}^{\tau+\Delta\tau}\right)\\
&=\frac{[C]}{\Delta\tau}\{V_x\}^{\tau}-\frac{2K^*}{3We}n_xS\,\mathbf b_S+g_x^*\frac{V}{4}\mathbf 1_4.
\end{aligned}
\]''',
48: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_y\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_y\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left([S_{xy}]\{V_x\}^{\tau+\Delta\tau}
+([S_{xx}]+2[S_{yy}]+[S_{zz}])\{V_y\}^{\tau+\Delta\tau}
+[S_{zy}]\{V_z\}^{\tau+\Delta\tau}-[H_y]\{P\}^{\tau+\Delta\tau}\right)\\
&=\frac{[C]}{\Delta\tau}\{V_y\}^{\tau}-\frac{2K^*}{3We}n_yS\,\mathbf b_S+g_y^*\frac{V}{4}\mathbf 1_4.
\end{aligned}
\]''',
49: r'''\[
\begin{aligned}
\frac{[C]}{\Delta\tau}\{V_z\}^{\tau+\Delta\tau}
&+(V_x[C_x]+V_y[C_y]+V_z[C_z])\{V_z\}^{\tau+\Delta\tau}\\
&+\frac1{Re}\left([S_{xz}]\{V_x\}^{\tau+\Delta\tau}+[S_{yz}]\{V_y\}^{\tau+\Delta\tau}
+([S_{xx}]+[S_{yy}]+2[S_{zz}])\{V_z\}^{\tau+\Delta\tau}-[H_z]\{P\}^{\tau+\Delta\tau}\right)\\
&=\frac{[C]}{\Delta\tau}\{V_z\}^{\tau}-\frac{2K^*}{3We}n_zS\,\mathbf b_S+g_z^*\frac{V}{4}\mathbf 1_4.
\end{aligned}
\]''',
}

for num, latex in formulas.items():
    src = f'./../img/fem_d_momentum_tet.files/image{num:03d}.png'
    pattern = re.compile(r'<p class="im"[^>]*>\s*<img src="' + re.escape(src) + r'">\s*</p>', re.I)
    matches = list(pattern.finditer(text))
    if not matches:
        raise RuntimeError(f'no image tag found: {src}')
    count_ref = {'n': 0}
    def repl(_m):
        count_ref['n'] += 1
        suffix = '' if count_ref['n'] == 1 else f'-repeat-{count_ref["n"]}'
        ident = f'formula-fem-7-2-2-{num:03d}{suffix}'
        return f'<div class="math-block" id="{ident}" data-source-image="{src}">\n{latex}\n</div>'
    text, count = pattern.subn(repl, text)
    if count != len(matches):
        raise RuntimeError(f'replacement count mismatch {src}: {count}/{len(matches)}')

# Update the explanatory note: the subsequent equations now explicitly use the mapped four-node vector b_S.
old_note = ('境界三角形で得られる3節点の表面力ベクトルは、要素方程式へ加算するときに境界面の節点番号から四面体4節点へ写像します。'
            '以下の式ではこのアセンブリ写像を省略しています。面局所ベクトルを \\(\\mathbf f_S\\) とすると、要素ベクトルは \\(\\mathbf f_e=A_S^T\\mathbf f_S\\) です。'
            '例えば境界面が要素節点1-2-3なら、第4成分を0として加算します。')
new_note = ('境界三角形で得られる3節点の表面力ベクトルは、要素方程式へ加算するときに境界面の節点番号から四面体4節点へ写像します。'
            '面局所ベクトルを \\(\\mathbf f_S\\) とすると、要素ベクトルは \\(\\mathbf f_e=A_S^T\\mathbf f_S\\) です。'
            '以下では \\(\\mathbf b_S=A_S^T[1\\;1\\;1]^T\\) を用いてこの写像を式中に明示します。例えば境界面が要素節点1-2-3なら \\(\\mathbf b_S=[1\\;1\\;1\\;0]^T\\) です。')
if old_note in text:
    text = text.replace(old_note, new_note, 1)
elif '以下では \\(\\mathbf b_S=' not in text:
    raise RuntimeError('3D surface assembly note not found')

heading = '<h2>・運動量収支式の離散化</h2>'
if 'formula-conversion-note' not in text:
    text = text.replace(
        heading,
        heading + '\n\t\t\t<p id="formula-conversion-note">数式はMathJaxで表示しています。変換前の数式画像は照合用としてリポジトリ内に保持しています。</p>',
        1,
    )

for num in range(1, 50):
    src = f'./../img/fem_d_momentum_tet.files/image{num:03d}.png'
    if re.search(r'<img\b[^>]*\bsrc=["\']' + re.escape(src) + r'["\']', text, re.I):
        raise RuntimeError(f'source image tag remains: {src}')
    if f'formula-fem-7-2-2-{num:03d}' not in text:
        raise RuntimeError(f'missing formula ID: image{num:03d}')

PATH.write_bytes(text.encode('cp932'))
print('Converted fem_7_2_2.html: all 49 source equations are MathJax/traceable.')
