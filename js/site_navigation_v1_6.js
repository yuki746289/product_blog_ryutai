/**
 * Updated: 2026/09/20
 * Summary: [S001]-[S006] Build the v1.6 shared navigation and D Monochrome bootstrap from the footer iframe.
 * Differences from previous version:
 * - [ADD]: PC 8-category mega menu, mobile drawer/accordion, utility links and safe fallback.
 * - [ADD]: Existing menu.html is read-only navigation data; resolved anchor.href values are reused.
 * - [MOD]: Start core navigation immediately from the footer iframe and do not wait for the duplicate stylesheet link before building the UI.
 * - [DEL]: None.
 */
"use strict";

// [V001] Shared configuration for v1.6 navigation.
var mapSiteNavigationV16Config = {
    styleElementId: "rv-site-v1-6-style",
    navigationId: "rv-site-navigation-v16",
    mobileTriggerId: "rv-mobile-trigger-v16",
    mobileDrawerId: "rv-mobile-drawer-v16",
    mobileOverlayId: "rv-mobile-overlay-v16",
    mobileMaxWidth: 767,
    styleUrl: new URL(
        "../css/site_v1_6.css",
        document.currentScript && document.currentScript.src ? document.currentScript.src : window.location.href
    ).href,
    listCategories: [
        {key: "physics", title: "物理", submenuId: "id_2"},
        {key: "fluid", title: "流体力学", submenuId: "id_3"},
        {key: "fem", title: "有限要素法", submenuId: "id_4"},
        {key: "mesh", title: "メッシュ", submenuId: "id_5"},
        {key: "simple", title: "SIMPLE法", submenuId: "id_6"},
        {key: "heat", title: "伝熱工学", submenuId: "id_9"},
        {key: "fortran", title: "Fortran", submenuId: "id_10"}
    ],
    otherCategoryKey: "other",
    otherCategoryTitle: "その他"
};

// [F001] Main initialization entry point.
// [O001] Return value: isInitialized.
function refreshSiteNavigationV16() {
    // [L001] Run only from the shared footer iframe.
    var isInitialized = false;
    if (parent === self) {
        return isInitialized;
    }

    var parentWindow = parent;
    var parentDocument = parentWindow.document;
    var parentBody = parentDocument.body;
    if (!parentBody) {
        return isInitialized;
    }

    // [L002] Prevent duplicate initialization.
    if (parentBody.classList.contains("rv-nav-ready")) {
        isInitialized = true;
        return isInitialized;
    }

    // [L003] Read the existing menu iframe without modifying it.
    var legacyMenuDocument = selectLegacyMenuDocument(parentDocument);

    // [L004] If menu.html is not ready yet, retry exactly from its load event.
    if (!legacyMenuDocument) {
        var menuIframe = parentDocument.getElementById("menu");
        if (menuIframe && menuIframe.getAttribute("data-rv-v16-load-bound") !== "true") {
            menuIframe.setAttribute("data-rv-v16-load-bound", "true");
            menuIframe.addEventListener("load", function() {
                refreshSiteNavigationV16();
            });
        }
        return isInitialized;
    }

    try {
        // [L005] Load CSS first, then build the shared model and both navigation surfaces.
        var stylesheetLink = registSiteStylesheet(parentDocument);
        if (!stylesheetLink) {
            return isInitialized;
        }

        var mapNavigationModel = selectNavigationModel(legacyMenuDocument);
        if (!mapNavigationModel || mapNavigationModel.listCategories.length !== 8) {
            return isInitialized;
        }

        var desktopNavigation = registDesktopNavigation(parentDocument, mapNavigationModel);
        var mapMobileElements = registMobileNavigation(parentDocument, mapNavigationModel);
        var utilityNavigation = registUtilityNavigation(
            parentDocument,
            mapNavigationModel.listUtilityLinks,
            mapMobileElements
        );

        if (!desktopNavigation || !mapMobileElements || !utilityNavigation) {
            return isInitialized;
        }

        var isBound = registNavigationEvents(
            parentWindow,
            parentDocument,
            desktopNavigation,
            mapMobileElements
        );
        if (!isBound) {
            return isInitialized;
        }

        parentBody.classList.remove("mobile-menu-open");

        // [L006] Hide the legacy left menu only after every required v1.6 component exists.
        parentBody.classList.add("rv-nav-ready");
        isInitialized = true;
    } catch (error) {
        // [L007] Keep the legacy UI visible when initialization fails.
        parentBody.classList.remove("rv-nav-ready");
        isInitialized = false;
    }

    return isInitialized;
}

// [F002] Build the desktop category bar and mega panels.
// [I001] parentDocument: parent page DOM.
// [I002] mapNavigationModel: resolved navigation model.
// [O002] Return value: desktopNavigation.
function registDesktopNavigation(parentDocument, mapNavigationModel) {
    var desktopNavigation = parentDocument.getElementById(mapSiteNavigationV16Config.navigationId);
    if (desktopNavigation) {
        return desktopNavigation;
    }

    var headerElement = parentDocument.getElementById("header");
    if (!headerElement || !headerElement.parentNode) {
        desktopNavigation = null;
        return desktopNavigation;
    }

    // [L101] Insert the new shared navigation immediately after the legacy header.
    desktopNavigation = parentDocument.createElement("nav");
    desktopNavigation.id = mapSiteNavigationV16Config.navigationId;
    desktopNavigation.className = "rv-site-navigation";
    desktopNavigation.setAttribute("aria-label", "主要カテゴリ");
    headerElement.parentNode.insertBefore(desktopNavigation, headerElement.nextSibling);

    var categoryBar = parentDocument.createElement("div");
    categoryBar.className = "rv-category-bar";
    desktopNavigation.appendChild(categoryBar);

    // [L102][L103] Create all eight buttons and their panels in advance.
    mapNavigationModel.listCategories.forEach(function(category) {
        var categoryButton = parentDocument.createElement("button");
        var panelId = "rv-mega-panel-" + category.key;
        categoryButton.type = "button";
        categoryButton.className = "rv-category-button";
        categoryButton.textContent = category.title;
        categoryButton.setAttribute("data-rv-category", category.key);
        categoryButton.setAttribute("aria-expanded", "false");
        categoryButton.setAttribute("aria-controls", panelId);
        categoryBar.appendChild(categoryButton);

        var megaPanel = parentDocument.createElement("section");
        megaPanel.id = panelId;
        megaPanel.className = "rv-mega-panel";
        megaPanel.setAttribute("data-rv-panel", category.key);

        var megaInner = parentDocument.createElement("div");
        megaInner.className = "rv-mega-inner";
        megaPanel.appendChild(megaInner);

        var megaHeading = parentDocument.createElement("div");
        megaHeading.className = "rv-mega-heading";
        var megaTitle = parentDocument.createElement("h2");
        megaTitle.textContent = category.title;
        megaHeading.appendChild(megaTitle);

        if (category.home) {
            var homeLink = parentDocument.createElement("a");
            homeLink.href = category.home.href;
            homeLink.textContent = category.title + "トップへ";
            if (category.home.target === "_blank") {
                homeLink.target = "_blank";
                homeLink.rel = "noopener";
            }
            megaHeading.appendChild(homeLink);
        }
        megaInner.appendChild(megaHeading);

        var megaGrid = parentDocument.createElement("div");
        megaGrid.className = "rv-mega-grid";

        // [L104] Render hierarchy inside one panel; never create horizontal fly-outs.
        if (category.sections && category.sections.length > 0) {
            category.sections.forEach(function(sectionModel) {
                var sectionElement = parentDocument.createElement("section");
                sectionElement.className = "rv-mega-group";

                var sectionHeading = parentDocument.createElement("h3");
                var sectionLink = parentDocument.createElement("a");
                sectionLink.href = sectionModel.href;
                sectionLink.textContent = sectionModel.text;
                if (sectionModel.target === "_blank") {
                    sectionLink.target = "_blank";
                    sectionLink.rel = "noopener";
                }
                sectionHeading.appendChild(sectionLink);
                sectionElement.appendChild(sectionHeading);

                if (sectionModel.children.length > 0) {
                    var sectionTree = registTreeList(parentDocument, sectionModel.children, false);
                    sectionElement.appendChild(sectionTree);
                }
                megaGrid.appendChild(sectionElement);
            });
        } else {
            category.tree.forEach(function(rootNode) {
                var groupElement = parentDocument.createElement("section");
                groupElement.className = "rv-mega-group";

                var groupHeading = parentDocument.createElement("h3");
                var groupLink = parentDocument.createElement("a");
                groupLink.href = rootNode.href;
                groupLink.textContent = rootNode.text;
                if (rootNode.target === "_blank") {
                    groupLink.target = "_blank";
                    groupLink.rel = "noopener";
                }
                groupHeading.appendChild(groupLink);
                groupElement.appendChild(groupHeading);

                if (rootNode.children.length > 0) {
                    var groupTree = registTreeList(parentDocument, rootNode.children, false);
                    groupElement.appendChild(groupTree);
                }
                megaGrid.appendChild(groupElement);
            });
        }

        megaInner.appendChild(megaGrid);
        desktopNavigation.appendChild(megaPanel);
    });

    // [L105] State changes are handled by updateDesktopMenuState().
    return desktopNavigation;
}

// [F003] Build the mobile trigger, overlay and nested drawer.
// [I003] parentDocument: parent page DOM.
// [I004] mapNavigationModel: resolved navigation model.
// [O003] Return value: mapMobileElements.
function registMobileNavigation(parentDocument, mapNavigationModel) {
    var existingDrawer = parentDocument.getElementById(mapSiteNavigationV16Config.mobileDrawerId);
    if (existingDrawer) {
        var existingElements = {
            trigger: parentDocument.getElementById(mapSiteNavigationV16Config.mobileTriggerId),
            drawer: existingDrawer,
            overlay: parentDocument.getElementById(mapSiteNavigationV16Config.mobileOverlayId),
            closeButton: existingDrawer.querySelector(".rv-mobile-close"),
            utilityContainer: existingDrawer.querySelector(".rv-mobile-utility")
        };
        return existingElements;
    }

    var headerElement = parentDocument.getElementById("header");
    if (!headerElement || !parentDocument.body) {
        var mapMobileElements = null;
        return mapMobileElements;
    }

    // [L201] Create the mobile hamburger trigger.
    var mobileTrigger = parentDocument.createElement("button");
    mobileTrigger.id = mapSiteNavigationV16Config.mobileTriggerId;
    mobileTrigger.className = "rv-mobile-trigger";
    mobileTrigger.type = "button";
    mobileTrigger.setAttribute("aria-controls", mapSiteNavigationV16Config.mobileDrawerId);
    mobileTrigger.setAttribute("aria-expanded", "false");
    mobileTrigger.setAttribute("aria-label", "メニューを開く");
    for (var lineIndex = 0; lineIndex < 3; lineIndex += 1) {
        var triggerLine = parentDocument.createElement("span");
        triggerLine.setAttribute("aria-hidden", "true");
        mobileTrigger.appendChild(triggerLine);
    }
    headerElement.appendChild(mobileTrigger);

    // [L202] Create the overlay and right-side drawer.
    var mobileOverlay = parentDocument.createElement("div");
    mobileOverlay.id = mapSiteNavigationV16Config.mobileOverlayId;
    mobileOverlay.className = "rv-mobile-overlay";
    parentDocument.body.appendChild(mobileOverlay);

    var mobileDrawer = parentDocument.createElement("aside");
    mobileDrawer.id = mapSiteNavigationV16Config.mobileDrawerId;
    mobileDrawer.className = "rv-mobile-drawer";
    mobileDrawer.setAttribute("aria-hidden", "true");
    mobileDrawer.setAttribute("inert", "");
    mobileDrawer.setAttribute("aria-label", "サイトメニュー");

    var drawerHeader = parentDocument.createElement("div");
    drawerHeader.className = "rv-mobile-drawer-header";
    var drawerTitle = parentDocument.createElement("strong");
    drawerTitle.textContent = "サイトメニュー";
    drawerHeader.appendChild(drawerTitle);

    var closeButton = parentDocument.createElement("button");
    closeButton.type = "button";
    closeButton.className = "rv-mobile-close";
    closeButton.setAttribute("aria-label", "メニューを閉じる");
    closeButton.textContent = "×";
    drawerHeader.appendChild(closeButton);
    mobileDrawer.appendChild(drawerHeader);

    var utilityContainer = parentDocument.createElement("div");
    utilityContainer.className = "rv-mobile-utility";
    mobileDrawer.appendChild(utilityContainer);

    var categoryContainer = parentDocument.createElement("div");
    categoryContainer.className = "rv-mobile-categories";

    // [L203] Render categories and child groups as nested details elements.
    mapNavigationModel.listCategories.forEach(function(category) {
        var categoryDetails = parentDocument.createElement("details");
        categoryDetails.className = "rv-mobile-category";

        var categorySummary = parentDocument.createElement("summary");
        categorySummary.textContent = category.title;
        categoryDetails.appendChild(categorySummary);

        var categoryBody = parentDocument.createElement("div");
        categoryBody.className = "rv-mobile-category-body";

        if (category.home) {
            var categoryHomeLink = parentDocument.createElement("a");
            categoryHomeLink.className = "rv-mobile-home-link";
            categoryHomeLink.href = category.home.href;
            categoryHomeLink.textContent = category.title + "トップ";
            categoryBody.appendChild(categoryHomeLink);
        }

        if (category.sections && category.sections.length > 0) {
            var listSectionNodes = category.sections.map(function(sectionModel) {
                return {
                    text: sectionModel.text,
                    href: sectionModel.href,
                    target: sectionModel.target,
                    children: sectionModel.children
                };
            });
            var sectionTree = registTreeList(parentDocument, listSectionNodes, true);
            categoryBody.appendChild(sectionTree);
        } else {
            var mobileTree = registTreeList(parentDocument, category.tree, true);
            categoryBody.appendChild(mobileTree);
        }

        categoryDetails.appendChild(categoryBody);
        categoryContainer.appendChild(categoryDetails);
    });

    mobileDrawer.appendChild(categoryContainer);
    parentDocument.body.appendChild(mobileDrawer);

    // [L204][L205] Initial closed state and later changes are synchronized by updateMobileMenuStateV16().
    var mapMobileElements = {
        trigger: mobileTrigger,
        drawer: mobileDrawer,
        overlay: mobileOverlay,
        closeButton: closeButton,
        utilityContainer: utilityContainer
    };
    return mapMobileElements;
}

// [F004] Copy utility links into the new PC and mobile navigation surfaces.
// [I005] parentDocument: parent page DOM.
// [I006] listUtilityLinks: resolved utility link models.
// [I007] mapMobileElements: mobile navigation elements.
// [O004] Return value: utilityNavigation.
function registUtilityNavigation(parentDocument, listUtilityLinks, mapMobileElements) {
    var headerElement = parentDocument.getElementById("header");
    if (!headerElement || !mapMobileElements || !mapMobileElements.utilityContainer) {
        var utilityNavigation = null;
        return utilityNavigation;
    }

    var utilityNavigation = headerElement.querySelector(".rv-utility-navigation");
    if (!utilityNavigation) {
        // [L301] Create a separate utility area in the header.
        utilityNavigation = parentDocument.createElement("nav");
        utilityNavigation.className = "rv-utility-navigation";
        utilityNavigation.setAttribute("aria-label", "補助メニュー");

        var breadcrumbList = headerElement.querySelector("ul");
        if (breadcrumbList) {
            headerElement.insertBefore(utilityNavigation, breadcrumbList);
        } else {
            headerElement.appendChild(utilityNavigation);
        }
    }

    utilityNavigation.textContent = "";
    mapMobileElements.utilityContainer.textContent = "";

    // [L302][L303][L304] Preserve order, omit javascript pseudo-links, and copy to both surfaces.
    listUtilityLinks.forEach(function(linkModel) {
        var utilityLink = parentDocument.createElement("a");
        utilityLink.href = linkModel.href;
        utilityLink.textContent = linkModel.text;
        if (linkModel.target === "_blank") {
            utilityLink.target = "_blank";
            utilityLink.rel = "noopener";
        }
        utilityNavigation.appendChild(utilityLink);

        var mobileUtilityLink = utilityLink.cloneNode(true);
        mapMobileElements.utilityContainer.appendChild(mobileUtilityLink);
    });

    return utilityNavigation;
}

// [F005] Register the v1.6 stylesheet in the parent page.
// [I008] parentDocument: parent page DOM.
// [O005] Return value: stylesheetLink.
function registSiteStylesheet(parentDocument) {
    // [L401] Reuse the same stylesheet element if initialization is retried.
    var stylesheetLink = parentDocument.getElementById(mapSiteNavigationV16Config.styleElementId);
    if (stylesheetLink) {
        return stylesheetLink;
    }

    // [L402] Use the absolute URL resolved from this JavaScript file, not from the parent page path.
    stylesheetLink = parentDocument.createElement("link");
    stylesheetLink.id = mapSiteNavigationV16Config.styleElementId;
    stylesheetLink.rel = "stylesheet";
    stylesheetLink.href = mapSiteNavigationV16Config.styleUrl;
    stylesheetLink.addEventListener("load", function() {
        stylesheetLink.setAttribute("data-rv-loaded", "true");
        refreshSiteNavigationV16();
    });
    stylesheetLink.addEventListener("error", function() {
        stylesheetLink.setAttribute("data-rv-load-error", "true");
    });
    parentDocument.head.appendChild(stylesheetLink);

    // [L403][L404][L405][L406] Layout changes are implemented only by CSS under body.rv-nav-ready.
    return stylesheetLink;
}

// [F006] Bind all desktop and mobile navigation events.
// [I009] parentWindow: parent page Window.
// [I010] parentDocument: parent page DOM.
// [I011] desktopNavigation: desktop navigation root.
// [I012] mapMobileElements: mobile elements.
// [O006] Return value: isBound.
function registNavigationEvents(parentWindow, parentDocument, desktopNavigation, mapMobileElements) {
    var isBound = false;

    // [L507] Do not mark the new UI ready when required DOM is missing.
    if (!parentWindow || !parentDocument || !desktopNavigation ||
        !mapMobileElements || !mapMobileElements.trigger ||
        !mapMobileElements.drawer || !mapMobileElements.overlay ||
        !mapMobileElements.closeButton) {
        return isBound;
    }

    if (desktopNavigation.getAttribute("data-rv-events-bound") === "true") {
        isBound = true;
        return isBound;
    }

    // [L501] Toggle the requested desktop category.
    var listButtons = Array.prototype.slice.call(
        desktopNavigation.querySelectorAll(".rv-category-button")
    );
    listButtons.forEach(function(categoryButton) {
        categoryButton.addEventListener("click", function(event) {
            event.stopPropagation();
            var categoryKey = categoryButton.getAttribute("data-rv-category");
            var isOpen = categoryButton.getAttribute("aria-expanded") !== "true";
            updateDesktopMenuState(parentDocument, categoryKey, isOpen);
        });
    });

    // [L502] Keep clicks inside a mega panel from being treated as outside clicks.
    var listPanels = Array.prototype.slice.call(
        desktopNavigation.querySelectorAll(".rv-mega-panel")
    );
    listPanels.forEach(function(megaPanel) {
        megaPanel.addEventListener("click", function(event) {
            event.stopPropagation();
        });
    });

    // [L503] Close desktop panels on outside click.
    parentDocument.addEventListener("click", function(event) {
        if (!desktopNavigation.contains(event.target)) {
            updateDesktopMenuState(parentDocument, null, false);
        }
    });

    // [L504] Escape closes both desktop and mobile navigation.
    parentWindow.addEventListener("keydown", function(event) {
        if (event.key === "Escape") {
            updateDesktopMenuState(parentDocument, null, false);
            updateMobileMenuStateV16(parentDocument, mapMobileElements, false);
        }
    });

    // [L505] Bind mobile open/close actions and close after navigation.
    mapMobileElements.trigger.addEventListener("click", function() {
        updateMobileMenuStateV16(parentDocument, mapMobileElements, true);
    });
    mapMobileElements.closeButton.addEventListener("click", function() {
        updateMobileMenuStateV16(parentDocument, mapMobileElements, false);
    });
    mapMobileElements.overlay.addEventListener("click", function() {
        updateMobileMenuStateV16(parentDocument, mapMobileElements, false);
    });

    var listMobileLinks = Array.prototype.slice.call(
        mapMobileElements.drawer.querySelectorAll("a")
    );
    listMobileLinks.forEach(function(mobileLink) {
        mobileLink.addEventListener("click", function() {
            updateMobileMenuStateV16(parentDocument, mapMobileElements, false);
        });
    });

    // [L506] Keep PC/mobile states mutually exclusive across the breakpoint.
    parentWindow.addEventListener("resize", function() {
        if (parentWindow.innerWidth > mapSiteNavigationV16Config.mobileMaxWidth) {
            updateMobileMenuStateV16(parentDocument, mapMobileElements, false);
        } else {
            updateDesktopMenuState(parentDocument, null, false);
        }
    });

    desktopNavigation.setAttribute("data-rv-events-bound", "true");
    isBound = true;
    return isBound;
}

// [T001] Select the existing menu iframe document.
// [I013] parentDocument: parent page DOM.
// [O007] Return value: legacyMenuDocument.
function selectLegacyMenuDocument(parentDocument) {
    // [L601] Select the existing iframe by the legacy stable ID.
    var menuIframe = parentDocument.getElementById("menu");
    var legacyMenuDocument = null;
    if (!menuIframe) {
        return legacyMenuDocument;
    }

    // [L602] Require both contentDocument and #sub-menu before using the menu as a data source.
    try {
        if (menuIframe.contentDocument &&
            menuIframe.contentDocument.getElementById("sub-menu")) {
            legacyMenuDocument = menuIframe.contentDocument;
        }
    } catch (error) {
        legacyMenuDocument = null;
    }
    return legacyMenuDocument;
}

// [T002] Convert legacy menu DOM into the eight-category shared model.
// [I014] legacyMenuDocument: menu.html DOM.
// [O008] Return value: mapNavigationModel.
function selectNavigationModel(legacyMenuDocument) {
    var subMenu = legacyMenuDocument.getElementById("sub-menu");
    var listCategories = [];
    var listDirectChildren = Array.prototype.slice.call(subMenu.children);
    var listRootModels = [];
    var passedMainContentMarker = false;

    listDirectChildren.forEach(function(childElement) {
        if (childElement.tagName === "DIV" &&
            childElement.classList.contains("sub-text") &&
            childElement.textContent.indexOf("メインコンテンツ") >= 0) {
            passedMainContentMarker = true;
            return;
        }

        if (!passedMainContentMarker ||
            childElement.tagName !== "UL" ||
            childElement.id) {
            return;
        }

        var rootAnchor = childElement.querySelector("li a");
        if (!rootAnchor) {
            return;
        }

        var rootText = rootAnchor.textContent.replace(/^\s+|\s+$/g, "");
        var nextElement = childElement.nextElementSibling;
        var submenuElement = nextElement &&
            nextElement.tagName === "UL" &&
            nextElement.id ? nextElement : null;

        listRootModels.push({
            text: rootText,
            href: rootAnchor.href,
            target: rootAnchor.target || "",
            submenuElement: submenuElement
        });
    });

    // [L611] Build the seven configured technical categories.
    mapSiteNavigationV16Config.listCategories.forEach(function(categoryConfig) {
        var rootModel = null;
        listRootModels.some(function(candidateModel) {
            if (candidateModel.text === categoryConfig.title) {
                rootModel = candidateModel;
                return true;
            }
            return false;
        });

        var submenuElement = legacyMenuDocument.getElementById(categoryConfig.submenuId);
        var listTreeNodes = submenuElement ? selectLinkTree(submenuElement) : [];

        listCategories.push({
            key: categoryConfig.key,
            title: categoryConfig.title,
            home: rootModel ? {
                text: rootModel.text,
                href: rootModel.href,
                target: rootModel.target
            } : null,
            tree: listTreeNodes,
            sections: []
        });
    });

    // [L612] Aggregate every non-configured root after "メインコンテンツ" into "その他".
    var listKnownTitles = mapSiteNavigationV16Config.listCategories.map(function(categoryConfig) {
        return categoryConfig.title;
    });
    var listOtherSections = [];
    listRootModels.forEach(function(rootModel) {
        if (listKnownTitles.indexOf(rootModel.text) >= 0) {
            return;
        }

        var listChildren = rootModel.submenuElement ?
            selectLinkTree(rootModel.submenuElement) : [];
        listOtherSections.push({
            text: rootModel.text,
            href: rootModel.href,
            target: rootModel.target,
            children: listChildren
        });
    });

    listCategories.push({
        key: mapSiteNavigationV16Config.otherCategoryKey,
        title: mapSiteNavigationV16Config.otherCategoryTitle,
        home: null,
        tree: [],
        sections: listOtherSections
    });

    // [L613][L614] Submenus are already tree-structured; utility links are stored separately.
    var listUtilityLinks = selectUtilityLinks(legacyMenuDocument);
    var mapNavigationModel = {
        listCategories: listCategories,
        listUtilityLinks: listUtilityLinks
    };
    return mapNavigationModel;
}

// [T003] Convert a legacy submenu into a parent/child link tree.
// [I015] containerElement: submenu UL.
// [O009] Return value: listTreeNodes.
function selectLinkTree(containerElement) {
    var listTreeNodes = [];
    var listStack = [];
    if (!containerElement) {
        return listTreeNodes;
    }

    var listAnchors = Array.prototype.slice.call(containerElement.querySelectorAll("a"));
    var listParsedLinks = [];
    var minimumDepth = null;

    listAnchors.forEach(function(anchorElement) {
        var rawText = anchorElement.textContent || "";
        var leadingMatch = rawText.match(/^[\u3000 ]+/);
        var leadingText = leadingMatch ? leadingMatch[0] : "";
        var rawDepth = 0;
        for (var charIndex = 0; charIndex < leadingText.length; charIndex += 1) {
            if (leadingText.charAt(charIndex) === "\u3000") {
                rawDepth += 1;
            }
        }
        if (rawDepth === 0 && leadingText.length > 0) {
            rawDepth = Math.floor(leadingText.length / 2);
        }

        var linkText = rawText.replace(/^[\u3000\s]+/, "").replace(/\s+$/, "");
        if (!linkText) {
            return;
        }

        if (minimumDepth === null || rawDepth < minimumDepth) {
            minimumDepth = rawDepth;
        }
        listParsedLinks.push({
            anchorElement: anchorElement,
            rawDepth: rawDepth,
            text: linkText
        });
    });

    listParsedLinks.forEach(function(parsedLink) {
        // [L621] Normalize the legacy indentation so the shallowest item becomes depth 0.
        var depth = parsedLink.rawDepth - (minimumDepth || 0);

        // [L622] Only leading/trailing whitespace was removed from the displayed label.
        var treeNode = {
            text: parsedLink.text,
            href: parsedLink.anchorElement.href,
            target: parsedLink.anchorElement.target || "",
            children: []
        };

        // [L623] Use the closest available ancestor when legacy depth jumps unexpectedly.
        if (depth > 0 && listStack.length > 0) {
            var parentIndex = Math.min(depth - 1, listStack.length - 1);
            var parentNode = listStack[parentIndex];
            if (parentNode) {
                parentNode.children.push(treeNode);
            } else {
                listTreeNodes.push(treeNode);
                depth = 0;
            }
        } else {
            listTreeNodes.push(treeNode);
            depth = 0;
        }

        listStack[depth] = treeNode;
        listStack.length = depth + 1;

        // [L624] anchorElement.href is already resolved against menu.html.
    });

    return listTreeNodes;
}

// [T004] Select utility links that appear before the main-content marker.
// [I016] legacyMenuDocument: menu.html DOM.
// [O010] Return value: listUtilityLinks.
function selectUtilityLinks(legacyMenuDocument) {
    var listUtilityLinks = [];
    var subMenu = legacyMenuDocument.getElementById("sub-menu");
    if (!subMenu) {
        return listUtilityLinks;
    }

    // [L631] Read direct children only until the first sub-text divider.
    var listDirectChildren = Array.prototype.slice.call(subMenu.children);
    for (var childIndex = 0; childIndex < listDirectChildren.length; childIndex += 1) {
        var childElement = listDirectChildren[childIndex];
        if (childElement.tagName === "DIV" && childElement.classList.contains("sub-text")) {
            break;
        }
        if (childElement.tagName !== "UL") {
            continue;
        }

        var listAnchors = Array.prototype.slice.call(childElement.querySelectorAll("a"));
        listAnchors.forEach(function(anchorElement) {
            // [L632] Exclude JavaScript pseudo-links from the new UI.
            var rawHref = anchorElement.getAttribute("href") || "";
            if (rawHref.toLowerCase().indexOf("javascript:") === 0) {
                return;
            }

            var linkText = (anchorElement.textContent || "").replace(/^\s+|\s+$/g, "");
            if (!linkText) {
                return;
            }

            listUtilityLinks.push({
                text: linkText,
                href: anchorElement.href,
                target: anchorElement.target || ""
            });
        });
    }

    return listUtilityLinks;
}

// [T005] Render a navigation tree as PC lists or mobile nested details.
// [I017] parentDocument: parent page DOM.
// [I018] listTreeNodes: hierarchy nodes.
// [I019] isMobile: mobile rendering flag.
// [O011] Return value: treeElement.
function registTreeList(parentDocument, listTreeNodes, isMobile) {
    var treeElement = parentDocument.createElement(isMobile ? "div" : "ul");
    treeElement.className = isMobile ? "rv-mobile-tree" : "rv-nav-list";

    // [L641] Recursively render the same hierarchy in the surface-specific markup.
    listTreeNodes.forEach(function(treeNode) {
        if (isMobile) {
            if (treeNode.children.length > 0) {
                var subgroup = parentDocument.createElement("details");
                subgroup.className = "rv-mobile-subgroup";

                var subgroupSummary = parentDocument.createElement("summary");
                subgroupSummary.textContent = treeNode.text;
                subgroup.appendChild(subgroupSummary);

                var subgroupBody = parentDocument.createElement("div");
                subgroupBody.className = "rv-mobile-subgroup-body";

                var parentLink = parentDocument.createElement("a");
                parentLink.href = treeNode.href;
                parentLink.textContent = treeNode.text + "を開く";
                if (treeNode.target === "_blank") {
                    parentLink.target = "_blank";
                    parentLink.rel = "noopener";
                }
                subgroupBody.appendChild(parentLink);

                var childMobileTree = registTreeList(parentDocument, treeNode.children, true);
                subgroupBody.appendChild(childMobileTree);
                subgroup.appendChild(subgroupBody);
                treeElement.appendChild(subgroup);
            } else {
                var mobileLink = parentDocument.createElement("a");
                mobileLink.className = "rv-mobile-link";
                mobileLink.href = treeNode.href;
                mobileLink.textContent = treeNode.text;
                if (treeNode.target === "_blank") {
                    mobileLink.target = "_blank";
                    mobileLink.rel = "noopener";
                }
                treeElement.appendChild(mobileLink);
            }
        } else {
            var listItem = parentDocument.createElement("li");
            var desktopLink = parentDocument.createElement("a");
            desktopLink.href = treeNode.href;
            desktopLink.textContent = treeNode.text;
            if (treeNode.target === "_blank") {
                desktopLink.target = "_blank";
                desktopLink.rel = "noopener";
            }
            listItem.appendChild(desktopLink);

            if (treeNode.children.length > 0) {
                desktopLink.className = "rv-parent-link";
                var childDesktopTree = registTreeList(parentDocument, treeNode.children, false);
                listItem.appendChild(childDesktopTree);
            }
            treeElement.appendChild(listItem);
        }
    });

    return treeElement;
}

// [T006] Synchronize desktop button/panel state.
// [I020] parentDocument: parent page DOM.
// [I021] categoryKey: category to open.
// [I022] isOpen: requested state.
// [O012] Return value: isOpenResult.
function updateDesktopMenuState(parentDocument, categoryKey, isOpen) {
    // [L651] Close every desktop category first.
    var listButtons = Array.prototype.slice.call(
        parentDocument.querySelectorAll(".rv-category-button")
    );
    var listPanels = Array.prototype.slice.call(
        parentDocument.querySelectorAll(".rv-mega-panel")
    );
    listButtons.forEach(function(categoryButton) {
        categoryButton.setAttribute("aria-expanded", "false");
    });
    listPanels.forEach(function(megaPanel) {
        megaPanel.classList.remove("is-open");
    });

    var isOpenResult = false;

    // [L652] Open only the requested category.
    if (isOpen && categoryKey) {
        var categoryButton = parentDocument.querySelector(
            '.rv-category-button[data-rv-category="' + categoryKey + '"]'
        );
        var megaPanel = parentDocument.querySelector(
            '.rv-mega-panel[data-rv-panel="' + categoryKey + '"]'
        );
        if (categoryButton && megaPanel) {
            categoryButton.setAttribute("aria-expanded", "true");
            megaPanel.classList.add("is-open");
            isOpenResult = true;
        }
    }

    return isOpenResult;
}

// [T007] Synchronize mobile drawer, overlay, ARIA and focus state.
// [I023] parentDocument: parent page DOM.
// [I024] mapMobileElements: mobile elements.
// [I025] isOpen: requested state.
// [O013] Return value: isOpenResult.
function updateMobileMenuStateV16(parentDocument, mapMobileElements, isOpen) {
    var isOpenResult = false;
    if (!parentDocument || !parentDocument.body || !mapMobileElements ||
        !mapMobileElements.trigger || !mapMobileElements.drawer ||
        !mapMobileElements.overlay) {
        return isOpenResult;
    }

    var restoreFocus = !isOpen &&
        parentDocument.activeElement &&
        mapMobileElements.drawer.contains(parentDocument.activeElement);

    // [L661] Synchronize class, ARIA and inert state.
    if (isOpen) {
        parentDocument.body.classList.add("rv-mobile-open");
        mapMobileElements.drawer.classList.add("is-open");
        mapMobileElements.overlay.classList.add("is-open");
        mapMobileElements.trigger.setAttribute("aria-expanded", "true");
        mapMobileElements.trigger.setAttribute("aria-label", "メニューを閉じる");
        mapMobileElements.drawer.setAttribute("aria-hidden", "false");
        mapMobileElements.drawer.removeAttribute("inert");
        isOpenResult = true;
    } else {
        parentDocument.body.classList.remove("rv-mobile-open");
        mapMobileElements.drawer.classList.remove("is-open");
        mapMobileElements.overlay.classList.remove("is-open");
        mapMobileElements.trigger.setAttribute("aria-expanded", "false");
        mapMobileElements.trigger.setAttribute("aria-label", "メニューを開く");
        mapMobileElements.drawer.setAttribute("aria-hidden", "true");
        mapMobileElements.drawer.setAttribute("inert", "");
    }

    // [L662] Restore focus to the trigger when closing from inside the drawer.
    if (restoreFocus && parentDocument.defaultView &&
        parentDocument.defaultView.getComputedStyle(mapMobileElements.trigger).display !== "none") {
        mapMobileElements.trigger.focus();
    }

    return isOpenResult;
}

// Start the v1.6 bootstrap as soon as this script is parsed.
// The parent page has already parsed the menu/footer iframe elements at this point.
// A second call on load is harmless and covers slow iframe/style edge cases.
refreshSiteNavigationV16();
window.addEventListener("load", function() {
    refreshSiteNavigationV16();
});
