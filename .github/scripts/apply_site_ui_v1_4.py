from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

MATH_PAGES = [
    ROOT / "fem/fem_6_2_6.html",
    ROOT / "fem/fem_7_1_1.html",
    ROOT / "fem/fem_7_1_2.html",
    ROOT / "fem/fem_7_2_1.html",
    ROOT / "fem/fem_7_2_2.html",
]


def read_cp932(path: Path) -> str:
    return path.read_bytes().decode("cp932")


def write_cp932(path: Path, text: str) -> None:
    path.write_bytes(text.encode("cp932"))


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def update_math_css() -> None:
    path = ROOT / "css/math.css"
    text = path.read_text(encoding="utf-8")
    old = '''/* MathJax and correction-history styles */
.math-block {
\tmax-width: 100%;
\toverflow-x: auto;
\toverflow-y: hidden;
\t-webkit-overflow-scrolling: touch;
\tmargin: 12px 0 18px 0;
\tpadding: 4px 0;
}

.math-block mjx-container[display="true"] {
\ttext-align: left !important;
\tmargin: 0 !important;
\tmin-width: max-content;
}
'''
    new = '''/**
 * 更新日時: 2026/09/16
 * 処理概要: [S001] MathJax数式を横スクロールなしでコンテナ幅内に表示する。
 * 前回バージョンとの違い:
 * - [MOD]: [L101] 横スクロール指定とmin-width:max-contentを廃止。
 */
/* MathJax and correction-history styles */
.math-block {
\tmax-width: 100%;
\toverflow: visible;
\tmargin: 12px 0 18px 0;
\tpadding: 4px 0;
}

.math-block mjx-container[display="true"] {
\tmax-width: 100%;
\ttext-align: left !important;
\tmargin: 0 !important;
\tmin-width: 0;
}
'''
    text = replace_once(text, old, new, "math.css block")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_responsive_css() -> None:
    path = ROOT / "css/responsive.css"
    text = path.read_text(encoding="utf-8")
    text = text.replace(" * 更新日時: 2026/09/16\n", " * 更新日時: 2026/09/16\n", 1)
    old = '''\tbody.mobile-nav-ready div#sub iframe#menu {
\t\tposition: fixed;
\t\ttop: 0;
\t\tleft: 0;
\t\twidth: 86vw !important;
\t\tmax-width: 320px;
\t\theight: 100vh !important;
\t\theight: 100dvh !important;
\t\tmargin: 0;
\t\tbackground: #ffffff;
\t\tborder: 0;
\t\tborder-right: 1px solid #b9b9b9;
\t\tbox-shadow: 3px 0 10px rgba(0, 0, 0, 0.2);
\t\ttransform: translateX(-105%);
\t\ttransition: transform 0.2s ease;
\t\tz-index: 1002;
\t}
'''
    new = '''\tbody.mobile-nav-ready div#sub iframe#menu {
\t\tposition: fixed;
\t\ttop: 0;
\t\tleft: 0;
\t\twidth: 86vw !important;
\t\tmax-width: 320px;
\t\theight: 100vh !important;
\t\theight: 100dvh !important;
\t\tmargin: 0;
\t\tbackground: #ffffff;
\t\tborder: 0;
\t\tborder-right: 1px solid #b9b9b9;
\t\tbox-shadow: 3px 0 10px rgba(0, 0, 0, 0.2);
\t\toverflow-x: hidden;
\t\toverflow-y: auto;
\t\toverscroll-behavior: contain;
\t\t-webkit-overflow-scrolling: touch;
\t\ttransform: translateX(-105%);
\t\ttransition: transform 0.2s ease;
\t\tz-index: 1002;
\t}

\t/* [L303] menu.htmlをiframe表示した際の背景色・全高を統一する */
\thtml,
\tbody,
\tdiv#sub-wrapper,
\tdiv#sub-menu {
\t\tbackground-color: #ffffff;
\t}

\thtml,
\tbody {
\t\tmin-height: 100%;
\t}

\tbody > div#sub-wrapper {
\t\tmin-height: 100vh;
\t\tmin-height: 100dvh;
\t\tbackground-image: none;
\t}
'''
    text = replace_once(text, old, new, "responsive iframe block")
    path.write_text(text, encoding="utf-8", newline="\n")


def update_math_pages() -> None:
    config_pattern = re.compile(
        r'''\t<script>\r?\n\twindow\.MathJax = \{\r?\n'''
        r'''\t\ttex: \{inlineMath: \[\['\\\\\(', '\\\\\)'\]\], displayMath: \[\['\\\\\[', '\\\\\]'\]\]\},\r?\n'''
        r'''\t\tchtml: \{displayAlign: 'left', displayIndent: '0'\}\r?\n'''
        r'''\t\};\r?\n\t</script>\r?\n'''
        r'''\t<script async src="https://cdn\.jsdelivr\.net/npm/mathjax@3/es5/tex-mml-chtml\.js"></script>'''
    )
    new_config = '''\t<script>
\twindow.MathJax = {
\t\ttex: {inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']]},
\t\toutput: {
\t\t\tdisplayOverflow: 'linebreak',
\t\t\tlinebreaks: {inline: true, width: '100%', lineleading: 0.2}
\t\t},
\t\tchtml: {displayAlign: 'left', displayIndent: '0'}
\t};
\t</script>
\t<script defer src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>'''

    for path in MATH_PAGES:
        text = read_cp932(path)
        updated, count = config_pattern.subn(lambda _: new_config, text, count=1)
        if count != 1:
            raise RuntimeError(f"{path}: MathJax v3 config not found exactly once")
        write_cp932(path, updated)


def update_menu() -> None:
    path = ROOT / "menu.html"
    text = read_cp932(path)

    old_header = " 更新日時: 2026/09/15"
    if old_header in text:
        text = text.replace(old_header, " 更新日時: 2026/09/16", 1)

    old_required = '''\t\t\t// [L005] [ADD] 必要DOMが無い場合は本文へ影響を与えず終了
\t\t\tif(!parentBody || !parentHeader || !menuIframe)return;

\t\t\t// [L006] [ADD] iframeへアクセシビリティ用titleを設定'''
    new_required = '''\t\t\t// [L005] [ADD] 必要DOMが無い場合は本文へ影響を与えず終了
\t\t\tif(!parentBody || !parentHeader || !menuIframe)return;

\t\t\t// [V003][V004][L301] [ADD] モバイルiframeをマウス/タッチでスクロール可能にする
\t\t\tvar scrollingAttribute = "scrolling";
\t\t\tvar scrollingValue = "auto";
\t\t\tmenuIframe.setAttribute(scrollingAttribute, scrollingValue);

\t\t\t// [L006] [ADD] iframeへアクセシビリティ用titleを設定'''
    text = replace_once(text, old_required, new_required, "menu scrolling insertion")

    favorite = '''\t\t\t<li><a href="javascript:window.external.AddFavorite('http://ryutai.ninja-web.net/','流体力学・有限要素法による数値計算')">お気に入りに追加</a></li>'''
    history = favorite + '''\n\t\t\t<li><a href="./revision_history.html" target="_parent" title="修正履歴へ">修正履歴</a></li>'''
    text = replace_once(text, favorite, history, "menu revision link")
    write_cp932(path, text)


def update_index() -> None:
    path = ROOT / "index.html"
    text = read_cp932(path)
    marker = '''\t\t\t<p>2016.5.20 図式の解像度を向上。</p>'''
    notice = '''\t\t\t<p>2026.9.16 スマートフォン表示に対応し、メニューの操作性・レイアウトを改善しました。</p>
\t\t\t<p>2026.9.16 FEM主要ページの数式をMathJax表示へ変更し、確認で見つかった数式・表記を修正しました。<a href="./revision_history.html" target="_parent" title="修正履歴へ">修正履歴はこちら</a></p>
'''
    text = replace_once(text, marker, notice + marker, "index notice")
    write_cp932(path, text)


def update_footer() -> None:
    path = ROOT / "footer.html"
    text = read_cp932(path)
    history = '''\t\t<div style="margin-bottom:4px;"><a href="./revision_history.html" target="_parent">修正履歴</a></div>\n'''
    text = replace_once(text, history, "", "footer history link")
    write_cp932(path, text)


def validate() -> None:
    math_css = (ROOT / "css/math.css").read_text(encoding="utf-8")
    if "overflow-x: auto" in math_css or "min-width: max-content" in math_css:
        raise RuntimeError("math.css still contains horizontal-scroll rules")

    responsive = (ROOT / "css/responsive.css").read_text(encoding="utf-8")
    for token in ["overflow-y: auto", "overscroll-behavior: contain", "min-height: 100dvh"]:
        if token not in responsive:
            raise RuntimeError(f"responsive.css missing {token}")

    menu = read_cp932(ROOT / "menu.html")
    if 'menuIframe.setAttribute(scrollingAttribute, scrollingValue);' not in menu:
        raise RuntimeError("menu scrolling attribute update missing")
    if menu.count('href="./revision_history.html"') != 1:
        raise RuntimeError("menu revision history link count invalid")

    index = read_cp932(ROOT / "index.html")
    if "2026.9.16" not in index or 'href="./revision_history.html"' not in index:
        raise RuntimeError("index announcement missing")

    footer = read_cp932(ROOT / "footer.html")
    if "revision_history.html" in footer:
        raise RuntimeError("footer still contains revision history link")

    for path in MATH_PAGES:
        text = read_cp932(path)
        if "mathjax@3" in text or "/es5/" in text:
            raise RuntimeError(f"{path}: old MathJax reference remains")
        for token in ["mathjax@4/tex-mml-chtml.js", "displayOverflow: 'linebreak'", "width: '100%'"]:
            if token not in text:
                raise RuntimeError(f"{path}: missing {token}")


if __name__ == "__main__":
    update_math_css()
    update_responsive_css()
    update_math_pages()
    update_menu()
    update_index()
    update_footer()
    validate()
    print("site_ui v1.4 transformation: OK")
