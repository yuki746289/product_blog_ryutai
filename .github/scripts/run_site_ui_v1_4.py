from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import apply_site_ui_v1_4 as transform


def validate_math_block_rules() -> None:
    math_css = (transform.ROOT / "css/math.css").read_text(encoding="utf-8")
    math_block = math_css.split(".math-block {", 1)[1].split("}", 1)[0]
    math_container = math_css.split('.math-block mjx-container[display="true"] {', 1)[1].split("}", 1)[0]
    if "overflow-x: auto" in math_block:
        raise RuntimeError("math-block still contains horizontal scrolling")
    if "min-width: max-content" in math_container:
        raise RuntimeError("math container still forces max-content width")


def main() -> None:
    transform.update_math_css()
    transform.update_responsive_css()
    transform.update_math_pages()
    transform.update_menu()
    transform.update_index()
    transform.update_footer()

    validate_math_block_rules()

    responsive = (transform.ROOT / "css/responsive.css").read_text(encoding="utf-8")
    for token in ["overflow-y: auto", "overscroll-behavior: contain", "min-height: 100dvh"]:
        if token not in responsive:
            raise RuntimeError(f"responsive.css missing {token}")

    menu = transform.read_cp932(transform.ROOT / "menu.html")
    if 'menuIframe.setAttribute(scrollingAttribute, scrollingValue);' not in menu:
        raise RuntimeError("menu iframe scrolling update missing")
    if menu.count('href="./revision_history.html"') != 1:
        raise RuntimeError("menu revision-history link count invalid")

    index = transform.read_cp932(transform.ROOT / "index.html")
    if index.count("2026.9.16") < 2 or "修正履歴はこちら" not in index:
        raise RuntimeError("top-page announcement missing")

    footer = transform.read_cp932(transform.ROOT / "footer.html")
    if "revision_history.html" in footer:
        raise RuntimeError("footer still contains revision-history link")

    for path in transform.MATH_PAGES:
        text = transform.read_cp932(path)
        for token in ["mathjax@4/tex-mml-chtml.js", "displayOverflow: 'linebreak'", "width: '100%'"]:
            if token not in text:
                raise RuntimeError(f"{path}: missing {token}")
        if "mathjax@3" in text or "/es5/" in text:
            raise RuntimeError(f"{path}: old MathJax reference remains")

    print("site_ui v1.4 apply/static validation: OK")


if __name__ == "__main__":
    main()
