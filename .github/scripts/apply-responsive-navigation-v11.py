from pathlib import Path

MENU_PATH = Path("menu.html")
CSS_PATH = Path("css/responsive.css")


def patch_menu():
    data = MENU_PATH.read_bytes()
    text = data.decode("cp932")
    original = text

    display_start = original.index("\t\t//表示", original.index("function Init()"))
    height_start = original.index("\t\t//高さ調節", display_start)
    script_end = original.index("\t//-->", height_start)
    original_disp = original[display_start:height_start]
    original_set_height = original[height_start:script_end]

    header_marker = "更新日時: 2026/09/15"
    if header_marker not in text:
        doctype_end = text.index(">", text.index("<!DOCTYPE")) + 1
        header = """
<!--
 更新日時: 2026/09/15
 処理概要: [S001][S002][S003] スマートフォン用ハンバーガーメニュー初期化・開閉制御
 前回バージョンとの違い:
 - [ADD]: refreshMobileNavigation(), updateMobileMenuState() を追加
 - [MOD]: Init() からモバイルナビゲーション初期化を呼び出す
 - [DEL]: なし
-->"""
        text = text[:doctype_end] + header + text[doctype_end:]

    init_start = text.index("\t\tfunction Init()")
    display_start = text.index("\t\t//表示", init_start)
    replacement = r'''		// [F001] [MOD] ページ初期化
		function Init(){

			// [L001] [KEEP] 選択中カテゴリ表示
			disp();		//表示

			// [L002] [KEEP] 既存iframe高さ調整
			set_height();		//高さ調節

			// [L003] [ADD] スマートフォンナビゲーション初期化
			refreshMobileNavigation();

			// [O001] [KEEP] 値は返さない
		}

		// [F002] [ADD] スマートフォンナビゲーション初期化
		function refreshMobileNavigation(){

			// [O002] [ADD] DOM初期化のみ行い値は返さない
			// [L004] [ADD] iframe外でmenu.htmlを直接表示した場合は終了
			if(parent === self)return;

			// [V001] [KEEP] 既存のiframe親ウィンドウを参照
			var parentWindow = parent;
			// [V002] [KEEP] 親ページDOMを取得
			var parentDocument = parentWindow.document;
			var parentBody = parentDocument.body;
			var headerId = "header";
			var menuIframeId = "menu";
			var parentHeader = parentDocument.getElementById(headerId);
			var menuIframe = parentDocument.getElementById(menuIframeId);

			// [L005] [ADD] 必要DOMが無い場合は本文へ影響を与えず終了
			if(!parentBody || !parentHeader || !menuIframe)return;

			// [L006] [ADD] iframeへアクセシビリティ用titleを設定
			var menuTitle = "サイトメニュー";
			menuIframe.setAttribute("title", menuTitle);

			// [L007] [ADD] モバイルメニューボタンを一度だけ生成
			var menuButtonId = "mobile-menu-button";
			var menuButtonClassName = "mobile-menu-button";
			var menuButton = parentDocument.getElementById(menuButtonId);
			if(!menuButton){
				var buttonTagName = "button";
				var buttonType = "button";
				var controlsAttribute = "aria-controls";
				var expandedAttribute = "aria-expanded";
				var labelAttribute = "aria-label";
				var closedValue = "false";
				var closedLabel = "メニューを開く";
				menuButton = parentDocument.createElement(buttonTagName);
				menuButton.id = menuButtonId;
				menuButton.className = menuButtonClassName;
				menuButton.type = buttonType;
				menuButton.setAttribute(controlsAttribute, menuIframeId);
				menuButton.setAttribute(expandedAttribute, closedValue);
				menuButton.setAttribute(labelAttribute, closedLabel);

				// [L008] [ADD] DOM APIでハンバーガー3本線を生成
				var hamburgerLineCount = 3;
				var hamburgerLineClassName = "mobile-menu-button-line";
				var spanTagName = "span";
				var lineIndex;
				for(lineIndex = 0; lineIndex < hamburgerLineCount; lineIndex++){
					var hamburgerLine = parentDocument.createElement(spanTagName);
					hamburgerLine.className = hamburgerLineClassName;
					menuButton.appendChild(hamburgerLine);
				}
				parentHeader.appendChild(menuButton);
			}

			// [L009] [ADD] 背景オーバーレイを一度だけ生成
			var overlayId = "mobile-menu-overlay";
			var overlayClassName = "mobile-menu-overlay";
			var menuOverlay = parentDocument.getElementById(overlayId);
			if(!menuOverlay){
				var overlayTagName = "div";
				menuOverlay = parentDocument.createElement(overlayTagName);
				menuOverlay.id = overlayId;
				menuOverlay.className = overlayClassName;
				parentBody.appendChild(menuOverlay);
			}

			var boundAttribute = "data-mobile-nav-bound";
			var boundValue = "true";
			var menuOpenClassName = "mobile-menu-open";
			if(menuButton.getAttribute(boundAttribute) !== boundValue){
				// [L011] [ADD] ボタン押下で現在の開閉状態を反転
				menuButton.addEventListener("click", function(){
					var currentIsOpen = parentBody.classList.contains(menuOpenClassName);
					var requestedIsOpen = !currentIsOpen;
					updateMobileMenuState(parentDocument, menuButton, requestedIsOpen);
				});

				// [L012] [ADD] オーバーレイ押下で閉じる
				menuOverlay.addEventListener("click", function(){
					var requestedIsOpen = false;
					updateMobileMenuState(parentDocument, menuButton, requestedIsOpen);
				});

				// [L013] [ADD] Escapeキーで閉じる
				parentWindow.addEventListener("keydown", function(event){
					var escapeKey = "Escape";
					if(event.key === escapeKey){
						var requestedIsOpen = false;
						updateMobileMenuState(parentDocument, menuButton, requestedIsOpen);
					}
				});

				// [L014] [ADD] 768px以上へ戻った場合は閉じる
				parentWindow.addEventListener("resize", function(){
					var desktopMinWidth = 768;
					if(parentWindow.innerWidth >= desktopMinWidth){
						var requestedIsOpen = false;
						updateMobileMenuState(parentDocument, menuButton, requestedIsOpen);
					}
				});

				menuButton.setAttribute(boundAttribute, boundValue);
			}

			// [L010] [ADD] 初期化成功後にreadyクラスを付与
			var mobileReadyClassName = "mobile-nav-ready";
			parentBody.classList.add(mobileReadyClassName);

			// [L015] [ADD] 初期状態を閉状態へ同期
			var initialIsOpen = false;
			updateMobileMenuState(parentDocument, menuButton, initialIsOpen);
		}

		// [F003] [ADD] モバイルメニュー開閉状態更新
		function updateMobileMenuState(parentDocument, menuButton, isOpen){

			// [I001] [ADD] parentDocument: 親ページDOM
			// [I002] [ADD] menuButton: ARIA状態を更新するボタン
			// [I003] [ADD] isOpen: true=開、false=閉
			// [O003] [ADD] 状態更新のみ行い値は返さない
			if(!parentDocument || !menuButton)return;

			var parentBody = parentDocument.body;
			if(!parentBody)return;

			// [L016] [ADD] bodyクラスを開閉状態と同期
			var menuOpenClassName = "mobile-menu-open";
			if(isOpen){
				parentBody.classList.add(menuOpenClassName);
			}else{
				parentBody.classList.remove(menuOpenClassName);
			}

			// [L017] [ADD] aria-expandedを同期
			var expandedAttribute = "aria-expanded";
			var expandedValue = isOpen ? "true" : "false";
			menuButton.setAttribute(expandedAttribute, expandedValue);

			// [L018] [ADD] aria-labelを同期
			var labelAttribute = "aria-label";
			var menuLabel = isOpen ? "メニューを閉じる" : "メニューを開く";
			menuButton.setAttribute(labelAttribute, menuLabel);
		}

'''
    text = text[:init_start] + replacement + text[display_start:]

    new_display_start = text.index("\t\t//表示", text.index("function updateMobileMenuState"))
    new_height_start = text.index("\t\t//高さ調節", new_display_start)
    new_script_end = text.index("\t//-->", new_height_start)
    assert text[new_display_start:new_height_start] == original_disp, "disp() changed unexpectedly"
    assert text[new_height_start:new_script_end] == original_set_height, "set_height() changed unexpectedly"

    encoded = text.encode("cp932")
    assert encoded.decode("cp932") == text
    MENU_PATH.write_bytes(encoded)


RESPONSIVE_CSS = r'''/**
 * 更新日時: 2026/09/15
 * 処理概要: [S001][STYLE001] スマートフォン幅767px以下のレスポンシブ表示とオフキャンバスメニュー
 * 前回バージョンとの違い:
 * - [ADD]: mobile-nav-ready / mobile-menu-open によるスマホメニュー表示を追加
 * - [MOD]: レスポンシブ指定を767px以下へ限定し、PC/タブレットへの影響を除去
 * - [DEL]: なし
 */

@media screen and (max-width: 767px) {
	html,
	body {
		width: 100%;
		min-width: 0;
	}

	body {
		font-size: 16px;
		line-height: 1.6em;
		letter-spacing: 0.04em;
		overflow-x: hidden;
	}

	img {
		max-width: 100%;
		height: auto;
	}

	iframe {
		max-width: 100%;
	}

	pre {
		max-width: 100%;
		overflow-x: auto;
		-webkit-overflow-scrolling: touch;
	}

	div#wrapper,
	div#header,
	div#main,
	div#content,
	div#footer {
		width: 100%;
		max-width: 100%;
		box-sizing: border-box;
	}

	div#wrapper,
	div#sub-wrapper {
		background-image: none;
	}

	div#main,
	div#image,
	div#content,
	div#content-text,
	div#content-main,
	div#content-attend,
	div#sub {
		float: none;
	}

	div#main,
	div#image,
	div#content {
		width: 100%;
	}

	div#content {
		margin-top: 0;
	}

	div#content-text {
		width: auto;
		margin: 20px 12px 10px 12px;
	}

	div#content-main {
		width: auto;
		margin: 0 12px;
	}

	div#content-attend {
		width: auto;
		margin: 20px 12px 0 12px;
	}

	div#header {
		position: relative;
	}

	div#header h1 {
		float: none;
		padding: 16px 68px 8px 12px;
	}

	div#header h1 a {
		font-size: 1.35em;
		overflow-wrap: anywhere;
	}

	div#header ul {
		margin-left: 12px !important;
		margin-right: 12px;
	}

	div#image {
		height: auto;
		min-height: 0;
		padding-bottom: 12px;
		background-size: cover;
		background-position: center top;
	}

	div#image p {
		font-size: 1.4em;
		padding: 14px 12px 0 12px;
		text-indent: 0;
	}

	div#content-text h2,
	div#content-main h2,
	div#content-attend h2 {
		margin-left: 0;
		margin-right: 0;
		padding-left: 12px;
	}

	p {
		padding-left: 0.75em;
		padding-right: 0.75em;
		overflow-wrap: anywhere;
	}

	table {
		display: block;
		max-width: 100%;
		overflow-x: auto;
		-webkit-overflow-scrolling: touch;
	}

	input,
	textarea,
	select {
		max-width: 100%;
		box-sizing: border-box;
	}

	div#sub {
		width: 100%;
		max-width: 100%;
		overflow: visible;
		margin-top: 24px;
	}

	div#sub iframe#menu {
		display: block;
		width: 100% !important;
		max-width: 100%;
	}

	div#sub-wrapper,
	div#sub-menu {
		width: 100%;
		max-width: 100%;
		box-sizing: border-box;
	}

	div#sub-menu {
		padding-top: 10px;
	}

	div.sub-text {
		width: auto;
		margin: 20px 12px 0 12px;
	}

	div#sub-menu li {
		padding-left: 12px;
		padding-right: 12px;
	}

	div#footer {
		margin-top: 24px;
	}

	body.mobile-nav-ready div#sub {
		width: 0;
		height: 0;
		margin: 0;
		padding: 0;
		overflow: visible;
	}

	body.mobile-nav-ready div#sub > *:not(iframe#menu) {
		display: none !important;
	}

	body.mobile-nav-ready div#sub iframe#menu {
		position: fixed;
		top: 0;
		left: 0;
		width: 86vw !important;
		max-width: 320px;
		height: 100vh !important;
		height: 100dvh !important;
		margin: 0;
		background: #ffffff;
		border: 0;
		border-right: 1px solid #b9b9b9;
		box-shadow: 3px 0 10px rgba(0, 0, 0, 0.2);
		transform: translateX(-105%);
		transition: transform 0.2s ease;
		z-index: 1002;
	}

	body.mobile-nav-ready.mobile-menu-open div#sub iframe#menu {
		transform: translateX(0);
	}

	.mobile-menu-button {
		position: fixed;
		top: 10px;
		right: 10px;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 5px;
		width: 46px;
		height: 46px;
		margin: 0;
		padding: 0;
		border: 1px solid #777777;
		border-radius: 4px;
		background: #ffffff;
		cursor: pointer;
		z-index: 1003;
	}

	.mobile-menu-button-line {
		display: block;
		width: 24px;
		height: 2px;
		margin: 0;
		padding: 0;
		background: #333333;
	}

	.mobile-menu-overlay {
		position: fixed;
		inset: 0;
		margin: 0;
		background: rgba(0, 0, 0, 0.35);
		opacity: 0;
		visibility: hidden;
		pointer-events: none;
		transition: opacity 0.2s ease, visibility 0.2s ease;
		z-index: 1001;
	}

	body.mobile-menu-open .mobile-menu-overlay {
		opacity: 1;
		visibility: visible;
		pointer-events: auto;
	}

	body.mobile-menu-open {
		overflow: hidden;
	}
}

@media screen and (min-width: 768px) {
	.mobile-menu-button,
	.mobile-menu-overlay {
		display: none !important;
	}
}
'''


def write_css():
    CSS_PATH.write_text(RESPONSIVE_CSS, encoding="utf-8")


def validate():
    menu_bytes = MENU_PATH.read_bytes()
    menu = menu_bytes.decode("cp932")
    assert menu.encode("cp932") == menu_bytes

    required_menu_tokens = [
        "// [F001] [MOD]",
        "function refreshMobileNavigation()",
        "// [F002] [ADD]",
        "function updateMobileMenuState(parentDocument, menuButton, isOpen)",
        "// [F003] [ADD]",
        "// [L003] [ADD]",
        "// [L018] [ADD]",
        "mobile-nav-ready",
        "mobile-menu-open",
        "aria-expanded",
        "aria-label",
    ]
    for token in required_menu_tokens:
        assert token in menu, token

    assert menu.count("function disp()") == 1
    assert menu.count("function set_height()") == 1
    new_code_start = menu.index("function refreshMobileNavigation()")
    old_code_start = menu.index("\t\t//表示", menu.index("function updateMobileMenuState"))
    assert "innerHTML" not in menu[new_code_start:old_code_start]

    css = CSS_PATH.read_text(encoding="utf-8")
    assert "@media screen and (max-width: 767px)" in css
    assert "@media screen and (max-width: 768px)" not in css
    assert "body.mobile-nav-ready div#sub iframe#menu" in css
    assert "body.mobile-nav-ready.mobile-menu-open div#sub iframe#menu" in css
    assert ".mobile-menu-button" in css
    assert ".mobile-menu-overlay" in css

    lib = Path("css/lib.css").read_bytes().decode("cp932")
    assert '@import url("responsive.css");' in lib


if __name__ == "__main__":
    patch_menu()
    write_css()
    validate()
    print("Implementation patch and validation: OK")
