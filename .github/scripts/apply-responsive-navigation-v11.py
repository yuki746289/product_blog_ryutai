import re
from pathlib import Path

MENU_PATH = Path("menu.html")


def heading_positions(text, label):
    pattern = r"^\t\t//" + re.escape(label) + r"\r?$"
    return [match.start() for match in re.finditer(pattern, text, re.M)]


def repair_menu():
    data = MENU_PATH.read_bytes()
    text = data.decode("cp932")

    malformed_pattern = re.compile(
        r"^\t\t//表示\r?\n"
        r"\r?\n"
        r"\t\t\tset_height\(\);\t\t//高さ調節\r?\n"
        r"\r?\n"
        r"\t\t\}\r?\n"
        r"\r?\n"
        r"(?=^\t\t//表示\r?$)",
        re.M,
    )
    text, repair_count = malformed_pattern.subn("", text, count=1)
    assert repair_count == 1, f"expected one malformed Init fragment, found {repair_count}"

    assert len(heading_positions(text, "表示")) == 1
    assert len(heading_positions(text, "高さ調節")) == 1
    assert text.count("function Init()") == 1
    assert text.count("function refreshMobileNavigation()") == 1
    assert text.count("function updateMobileMenuState(parentDocument, menuButton, isOpen)") == 1
    assert text.count("function disp()") == 1
    assert text.count("function set_height()") == 1

    encoded = text.encode("cp932")
    assert encoded.decode("cp932") == text
    MENU_PATH.write_bytes(encoded)
    print("Removed duplicated legacy Init fragment: OK")
    print("CP932 round-trip: OK")


if __name__ == "__main__":
    repair_menu()
