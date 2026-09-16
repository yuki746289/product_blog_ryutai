from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"replacement target not found: {label}")
    return text.replace(old, new, 1)


def update_menu() -> None:
    path = ROOT / "menu.html"
    text = path.read_bytes().decode("cp932")

    old_fixed_scroll = '''\t\t\tvar scrollingAttribute = "scrolling";\n\t\t\tvar scrollingValue = "auto";\n\t\t\tmenuIframe.setAttribute(scrollingAttribute, scrollingValue);'''
    new_fixed_scroll = '''\t\t\t// [L301] [MOD] viewport幅に応じたscrolling属性を同期\n\t\t\trefreshMenuScrollingMode(parentWindow, menuIframe);'''
    text = replace_once(text, old_fixed_scroll, new_fixed_scroll, "fixed menu scrolling")

    resize_old = '''\t\t\t\tparentWindow.addEventListener("resize", function(){\n\t\t\t\t\tvar desktopMinWidth = 768;'''
    resize_new = '''\t\t\t\tparentWindow.addEventListener("resize", function(){\n\t\t\t\t\t// [L402] [MOD] resize時もPC/スマホのscrolling属性を同期\n\t\t\t\t\trefreshMenuScrollingMode(parentWindow, menuIframe);\n\t\t\t\t\tvar desktopMinWidth = 768;'''
    text = replace_once(text, resize_old, resize_new, "resize scrolling sync")

    helper_marker = '''\n\t\t// [F003] [ADD] モバイルメニュー開閉状態更新'''
    helper = '''\n\t\t// [T001] [ADD] 表示幅に応じてmenu iframeのスクロール方式を更新\n\t\tfunction refreshMenuScrollingMode(parentWindow, menuIframe){\n\n\t\t\t// [I004] [ADD] parentWindow: 親ページWindow\n\t\t\t// [I005] [ADD] menuIframe: 親ページのmenu iframe\n\t\t\t// [O006] [ADD] 属性更新のみ行い値は返さない\n\t\t\tif(!parentWindow || !menuIframe)return;\n\n\t\t\t// [L401] [ADD] 767px以下のみauto、768px以上はno\n\t\t\tvar mobileMaxWidth = 767;\n\t\t\tvar scrollingAttribute = "scrolling"; // [V003] [KEEP]\n\t\t\tvar mobileScrollingValue = "auto";\n\t\t\tvar desktopScrollingValue = "no";\n\t\t\tvar isMobile = parentWindow.innerWidth <= mobileMaxWidth;\n\t\t\tvar scrollingValue = isMobile ? mobileScrollingValue : desktopScrollingValue;\n\t\t\tmenuIframe.setAttribute(scrollingAttribute, scrollingValue);\n\t\t\treturn;\n\t\t}\n'''
    if "function refreshMenuScrollingMode(" not in text:
        text = replace_once(text, helper_marker, helper + helper_marker, "helper insertion")

    text = text.replace(
        " * - [MOD]: Init() からモバイルナビゲーション初期化を呼び出す\n * - [DEL]: なし",
        " * - [MOD]: Init() からモバイルナビゲーション初期化を呼び出す\n * - [MOD]: [L301][L402] PC/スマホ別にmenu iframeのscrolling属性を同期\n * - [ADD]: [T001][L401] refreshMenuScrollingMode()を追加\n * - [DEL]: [V004] 固定scrollingValue=autoを廃止",
        1,
    )

    path.write_bytes(text.encode("cp932"))


def update_lib_css() -> None:
    path = ROOT / "css/lib.css"
    data = path.read_bytes()
    old = b"div#sub{\n\t\twidth:175px;"
    new = b"div#sub{\n\t\twidth:180px;"
    if old not in data:
        raise RuntimeError("lib.css #sub width target not found")
    path.write_bytes(data.replace(old, new, 1))


def update_responsive_css() -> None:
    path = ROOT / "css/responsive.css"
    text = path.read_text(encoding="utf-8")

    old_menu_width = '''\tdiv#sub-wrapper,\n\tdiv#sub-menu {\n\t\twidth: 100%;\n\t\tmax-width: 100%;\n\t\tbox-sizing: border-box;\n\t}'''
    new_menu_width = '''\tdiv#sub-wrapper,\n\tdiv#sub-menu {\n\t\twidth: 100% !important;\n\t\tmax-width: 100%;\n\t\tbox-sizing: border-box;\n\t}'''
    text = replace_once(text, old_menu_width, new_menu_width, "mobile menu width")

    old_sub_text = '''\tdiv.sub-text {\n\t\twidth: auto;\n\t\tmargin: 20px 12px 0 12px;\n\t}'''
    new_sub_text = '''\t/* [L303] [MOD] セクション見出し（広告を含む）の幅・位置を統一 */\n\tdiv.sub-text {\n\t\twidth: calc(100% - 24px) !important;\n\t\tmax-width: calc(100% - 24px);\n\t\tmargin: 20px 12px 0 12px !important;\n\t\tbox-sizing: border-box;\n\t}\n\n\tdiv.sub-text dt {\n\t\twidth: 100%;\n\t\tbox-sizing: border-box;\n\t\ttext-align: center !important;\n\t}'''
    text = replace_once(text, old_sub_text, new_sub_text, "mobile sub-text alignment")

    path.write_text(text, encoding="utf-8")


def history_rows() -> str:
    rows = [
        ("R-UI-004", "表示改善", "左メニュー・広告見出し", "PC左メニューの右端文字切れを解消し、スマートフォンメニュー内の「広告」を他セクション見出しと同じ幅・中央揃えへ統一。", None),
        ("R-UI-005", "操作性改善", "メニューiframe", "PCでは不要なiframe縦スクロールを抑止し、スマートフォンのオフキャンバーメニューでは縦スクロールを維持。", None),
        ("R-UI-006", "表示改善", "修正履歴", "修正履歴を No. / 修正種類 / 対象 / 修正内容 の4列へ整理し、内部管理IDを利用者向け表示から除外。", None),
        ("R-UI-001", "表示改善", "数式表示", "FEM主要5ページの数式表示をMathJax 4へ更新し、横スクロールを廃止。画面幅に合わせて数式を自動改行する表示へ変更。", None),
        ("R-UI-002", "操作性改善", "スマートフォンメニュー", "ハンバーガーメニュー内をマウスホイール・タッチで縦スクロールできるよう修正。背景色の境界ずれとモバイル用文字サイズ・レイアウトも補正。", None),
        ("R-UI-003", "表示改善", "修正履歴・お知らせ", "トップページの「お知らせ等」に今回の更新内容を追加。修正履歴への導線をフッターから左メニューの「お気に入りに追加」直下へ移動。", None),
        ("R-FEM2D-MASS-001", "数式修正", "2D質量収支式", "2D三角形要素の重み付き残差の積分領域を V,dV から S,dS へ修正。", "./fem/fem_7_1_1.html#fix-r-fem2d-mass-001"),
        ("R-FEM2D-MASS-002", "誤記修正", "2D質量収支式", "「体積積分の公式」を「三角形要素の面積積分の公式」へ修正。", "./fem/fem_7_1_1.html#fix-r-fem2d-mass-002"),
        ("R-FEM2D-MASS-003", "補足追加", "2D質量収支式", "積分外へ出せる対象が速度・圧力場そのものではなく節点自由度であることを明記。", "./fem/fem_7_1_1.html#fix-r-fem2d-mass-003"),
        ("R-FEM2D-MASS-004", "誤記修正", "2D質量収支式", "本文の「離散化式は、次式とります。」を「離散化式は、次式となります。」へ修正。", "./fem/fem_7_1_1.html#formula-fem-7-1-1-004"),
        ("R-FEM2D-MOM-001", "数式修正", "2D運動量収支式", "2D三角形要素の重み付き残差の積分領域を V,dV から S,dS へ修正。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-001"),
        ("R-FEM2D-MOM-002", "数式修正", "2D運動量収支式", "速度内挿式末尾の不要な =0 を削除し、Vx,Vy,P の内挿表記を統一。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-002"),
        ("R-FEM2D-MOM-003 / 005", "数式修正", "2D運動量収支式", "一次線要素の積分公式を (p+q+1)! に修正し、∫Li dL=L/2 とした。面積積分途中式の V も A に修正。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-003"),
        ("R-FEM2D-MOM-004", "数式修正", "2D運動量収支式", "線積分公式の修正に合わせ、表面張力項の係数を 2K*/We から K*/We へ修正し、後続式へ反映。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-004"),
        ("R-FEM2D-MOM-006", "数式修正", "2D運動量収支式", "2D方向添字を i=1,2 に修正。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-006"),
        ("R-FEM2D-MOM-007", "補足追加", "2D境界辺ベクトル", "境界辺2節点ベクトルから三角形3節点へのアセンブリ写像を補足。", "./fem/fem_7_1_2.html#fix-r-fem2d-mom-007"),
        ("R-FEM3D-MOM-001", "補足追加", "3D境界面ベクトル", "境界面3節点ベクトルから四面体4節点へのアセンブリ写像を補足し、要素方程式では4成分ベクトルとして式中に明示。", "./fem/fem_7_2_2.html#fix-r-fem3d-mom-001"),
        ("R-FEM3D-MASS-001", "補足追加", "3D質量収支式", "対流項の係数側速度を既知係数として扱う線形化と、節点自由度を積分外へ出す理由を明記。", "./fem/fem_7_2_1.html#fix-r-fem3d-mass-001"),
        ("R-TET-N-001", "補足追加", "四面体要素体積", "V を正の要素体積として扱う符号規約と節点向きの前提を補足。", "./fem/fem_6_2_1.html#fix-r-tet-n-001"),
    ]
    out = ['\t\t<table class="correction-history">', '\t\t<tr><th>No.</th><th>修正種類</th><th>対象</th><th>修正内容</th></tr>']
    for no, (revision_id, revision_type, target, description, href) in enumerate(rows, start=1):
        target_html = f'<a href="{href}">{target}</a>' if href else target
        out.append(f'\t\t<tr data-revision-id="{revision_id}"><td>{no}</td><td>{revision_type}</td><td>{target_html}</td><td>{description}</td></tr>')
    out.append('\t\t</table>')
    return "\n".join(out)


def update_revision_history() -> None:
    path = ROOT / "revision_history.html"
    text = path.read_text(encoding="utf-8")
    table_pattern = re.compile(r'\t\t<table class="correction-history">.*?\t\t</table>', re.S)
    if not table_pattern.search(text):
        raise RuntimeError("revision history table not found")
    text = table_pattern.sub(history_rows(), text, count=1)
    path.write_text(text, encoding="utf-8")


def update_math_css() -> None:
    path = ROOT / "css/math.css"
    text = path.read_text(encoding="utf-8")
    if ".correction-history th:nth-child(1)" not in text:
        anchor = '''.correction-history th {\n\tbackground: #f0f0f0;\n}\n'''
        extra = '''.correction-history th {\n\tbackground: #f0f0f0;\n}\n\n/* [L501][L502] No.と修正種類を読み取りやすい幅へ固定 */\n.correction-history th:nth-child(1),\n.correction-history td:nth-child(1) {\n\twidth: 48px;\n\ttext-align: center;\n}\n\n.correction-history th:nth-child(2),\n.correction-history td:nth-child(2) {\n\twidth: 92px;\n\twhite-space: nowrap;\n}\n'''
        text = replace_once(text, anchor, extra, "revision history column styles")
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    menu = (ROOT / "menu.html").read_bytes().decode("cp932")
    assert "function refreshMenuScrollingMode(parentWindow, menuIframe)" in menu
    assert 'var scrollingValue = "auto";' not in menu
    assert menu.count("refreshMenuScrollingMode(parentWindow, menuIframe);") >= 2

    lib_data = (ROOT / "css/lib.css").read_bytes()
    assert b"div#sub{\n\t\twidth:180px;" in lib_data

    responsive = (ROOT / "css/responsive.css").read_text(encoding="utf-8")
    assert "width: 100% !important;" in responsive
    assert "text-align: center !important;" in responsive

    history = (ROOT / "revision_history.html").read_text(encoding="utf-8")
    assert "<th>No.</th><th>修正種類</th><th>対象</th><th>修正内容</th>" in history
    assert "<th>ID</th>" not in history
    assert history.count("data-revision-id=") == 19

    sample_dir = ROOT / "design_samples/v1.5"
    for name in ["index.html", "technical-clean.html", "academic-minimal.html", "modern-dashboard.html", "design-samples.css"]:
        if not (sample_dir / name).exists():
            raise RuntimeError(f"design sample missing: {name}")


if __name__ == "__main__":
    update_menu()
    update_lib_css()
    update_responsive_css()
    update_revision_history()
    update_math_css()
    validate()
    print("site_ui v1.5 transformation: OK")
