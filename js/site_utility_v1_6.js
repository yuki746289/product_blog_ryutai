/**
 * Updated: 2026/09/17
 * Summary: [S008][S009] Consolidate utility links into a leading Home menu and enable hover-to-open/click-to-top desktop navigation.
 * Differences from previous version:
 * - [MOD]: Remove the separate title-under utility row after copying its links into Home.
 * - [ADD]: Add Home as the first global category with Home/intro/profile/Q&A/sitemap/link/history/old-page links.
 * - [ADD]: Open desktop mega panels on hover/focus while category clicks navigate to each category top.
 * - [ADD]: Use the site map as the click destination for the virtual Other category.
 */
"use strict";

var mapSiteUtilityV16Config = {
    styleElementId: "rv-site-utility-v1-6-style",
    appliedClassName: "rv-home-navigation-ready",
    homeCategoryKey: "home",
    homeCategoryLabel: "\u30db\u30fc\u30e0",
    oldDirectoryName: "old/",
    oldPageLabel: "\u65e7\u30da\u30fc\u30b8",
    revisionLabel: "\u4fee\u6b63\u5c65\u6b74",
    sitemapLabel: "\u30b5\u30a4\u30c8\u30de\u30c3\u30d7",
    excludedLabels: [
        "\u30e1\u30fc\u30eb",
        "\u63b2\u793a\u677f",
        "\u76f8\u4e92\u30ea\u30f3\u30af\u52df\u96c6\u4e2d"
    ],
    baseUrl: new URL(
        "../",
        document.currentScript && document.currentScript.src ? document.currentScript.src : window.location.href
    ).href
};

function refreshHeaderUtilityV16() {
    var isApplied = false;
    if (parent === self) {
        return isApplied;
    }

    var parentWindow = parent;
    var parentDocument = parentWindow.document;
    var parentBody = parentDocument.body;
    if (!parentBody) {
        return isApplied;
    }
    if (parentBody.classList.contains(mapSiteUtilityV16Config.appliedClassName)) {
        return true;
    }

    var desktopNavigation = parentDocument.querySelector(".rv-site-navigation");
    var categoryBar = desktopNavigation ? desktopNavigation.querySelector(".rv-category-bar") : null;
    var desktopUtility = parentDocument.querySelector(".rv-utility-navigation");
    var mobileDrawer = parentDocument.querySelector(".rv-mobile-drawer");
    var mobileUtility = parentDocument.querySelector(".rv-mobile-utility");
    var mobileCategories = parentDocument.querySelector(".rv-mobile-categories");
    if (!desktopNavigation || !categoryBar || !desktopUtility ||
        !mobileDrawer || !mobileUtility || !mobileCategories) {
        return isApplied;
    }

    registUtilityStylesheetV16(parentDocument);

    var listUtilityLinks = selectUtilityLinkModelsV16(desktopUtility);
    var oldPageModel = createOldPageModelV16(parentWindow);
    listUtilityLinks.push(oldPageModel);

    var homeLinkModel = selectLinkModelByLabelV16(
        listUtilityLinks,
        mapSiteUtilityV16Config.homeCategoryLabel
    );
    var sitemapLinkModel = selectLinkModelByLabelV16(
        listUtilityLinks,
        mapSiteUtilityV16Config.sitemapLabel
    );
    if (!homeLinkModel) {
        return isApplied;
    }

    registDesktopHomeCategoryV16(
        parentDocument,
        desktopNavigation,
        categoryBar,
        listUtilityLinks,
        homeLinkModel
    );
    convertDesktopCategoryLinksV16(
        parentDocument,
        desktopNavigation,
        sitemapLinkModel
    );
    registDesktopHoverNavigationV16(parentDocument, desktopNavigation);
    registMobileHomeCategoryV16(
        parentDocument,
        mobileCategories,
        listUtilityLinks,
        homeLinkModel
    );

    if (desktopUtility.parentNode) {
        desktopUtility.parentNode.removeChild(desktopUtility);
    }
    if (mobileUtility.parentNode) {
        mobileUtility.parentNode.removeChild(mobileUtility);
    }

    parentBody.classList.add(mapSiteUtilityV16Config.appliedClassName);
    isApplied = true;
    return isApplied;
}

function registUtilityStylesheetV16(parentDocument) {
    var styleElement = parentDocument.getElementById(mapSiteUtilityV16Config.styleElementId);
    if (styleElement) {
        return styleElement;
    }
    styleElement = parentDocument.createElement("link");
    styleElement.id = mapSiteUtilityV16Config.styleElementId;
    styleElement.rel = "stylesheet";
    styleElement.type = "text/css";
    styleElement.href = new URL(
        "css/site_utility_v1_6.css?v=20260917b",
        mapSiteUtilityV16Config.baseUrl
    ).href;
    parentDocument.head.appendChild(styleElement);
    return styleElement;
}

function selectUtilityLinkModelsV16(containerElement) {
    var listModels = [];
    var listLinks = Array.prototype.slice.call(containerElement.querySelectorAll("a"));
    listLinks.forEach(function(linkElement) {
        var label = (linkElement.textContent || "").replace(/^\s+|\s+$/g, "");
        if (!label || mapSiteUtilityV16Config.excludedLabels.indexOf(label) >= 0) {
            return;
        }
        listModels.push({
            text: label,
            href: linkElement.href,
            target: linkElement.target || ""
        });
    });
    return listModels;
}

function selectLinkModelByLabelV16(listModels, label) {
    var result = null;
    listModels.some(function(linkModel) {
        if (linkModel.text === label) {
            result = linkModel;
            return true;
        }
        return false;
    });
    return result;
}

function createOldPageModelV16(parentWindow) {
    var currentUrl = new URL(parentWindow.location.href);
    var baseUrl = new URL(mapSiteUtilityV16Config.baseUrl);
    var relativePath = currentUrl.pathname;
    if (relativePath.indexOf(baseUrl.pathname) === 0) {
        relativePath = relativePath.substring(baseUrl.pathname.length);
    }
    relativePath = relativePath.replace(/^\/+/, "");
    if (!relativePath) {
        relativePath = "index.html";
    } else if (relativePath.charAt(relativePath.length - 1) === "/") {
        relativePath += "index.html";
    }

    var oldPageUrl = new URL(
        mapSiteUtilityV16Config.oldDirectoryName + relativePath,
        baseUrl
    );
    oldPageUrl.search = currentUrl.search;
    oldPageUrl.hash = currentUrl.hash;
    return {
        text: mapSiteUtilityV16Config.oldPageLabel,
        href: oldPageUrl.href,
        target: "_blank"
    };
}

function registDesktopHomeCategoryV16(
    parentDocument,
    desktopNavigation,
    categoryBar,
    listUtilityLinks,
    homeLinkModel
) {
    var panelId = "rv-mega-panel-" + mapSiteUtilityV16Config.homeCategoryKey;
    var homeLink = parentDocument.createElement("a");
    homeLink.className = "rv-category-button rv-category-link rv-home-category-link";
    homeLink.href = homeLinkModel.href;
    homeLink.textContent = mapSiteUtilityV16Config.homeCategoryLabel;
    homeLink.setAttribute("data-rv-category", mapSiteUtilityV16Config.homeCategoryKey);
    homeLink.setAttribute("aria-expanded", "false");
    homeLink.setAttribute("aria-controls", panelId);
    homeLink.setAttribute("aria-haspopup", "true");
    categoryBar.insertBefore(homeLink, categoryBar.firstChild);

    var homePanel = parentDocument.createElement("section");
    homePanel.id = panelId;
    homePanel.className = "rv-mega-panel rv-home-mega-panel";
    homePanel.setAttribute("data-rv-panel", mapSiteUtilityV16Config.homeCategoryKey);

    var homeInner = parentDocument.createElement("div");
    homeInner.className = "rv-mega-inner";
    var homeHeading = parentDocument.createElement("div");
    homeHeading.className = "rv-mega-heading";
    var homeTitle = parentDocument.createElement("h2");
    homeTitle.textContent = mapSiteUtilityV16Config.homeCategoryLabel;
    homeHeading.appendChild(homeTitle);
    homeInner.appendChild(homeHeading);

    var homeGrid = parentDocument.createElement("div");
    homeGrid.className = "rv-home-link-grid";
    listUtilityLinks.forEach(function(linkModel) {
        homeGrid.appendChild(createUtilityAnchorV16(parentDocument, linkModel, "rv-home-menu-link"));
    });
    homeInner.appendChild(homeGrid);
    homePanel.appendChild(homeInner);

    var firstPanel = desktopNavigation.querySelector(".rv-mega-panel");
    if (firstPanel) {
        desktopNavigation.insertBefore(homePanel, firstPanel);
    } else {
        desktopNavigation.appendChild(homePanel);
    }
}

function convertDesktopCategoryLinksV16(parentDocument, desktopNavigation, sitemapLinkModel) {
    var listButtons = Array.prototype.slice.call(
        desktopNavigation.querySelectorAll(".rv-category-bar > button.rv-category-button")
    );
    listButtons.forEach(function(categoryButton) {
        var categoryKey = categoryButton.getAttribute("data-rv-category") || "";
        var panelId = categoryButton.getAttribute("aria-controls") || "";
        var panelElement = panelId ? parentDocument.getElementById(panelId) : null;
        var topLink = panelElement ? panelElement.querySelector(".rv-mega-heading > a") : null;
        var destination = topLink ? topLink.href : "";
        if (!destination && categoryKey === "other" && sitemapLinkModel) {
            destination = sitemapLinkModel.href;
        }
        if (!destination) {
            destination = mapSiteUtilityV16Config.baseUrl;
        }

        var categoryLink = parentDocument.createElement("a");
        categoryLink.className = categoryButton.className + " rv-category-link";
        categoryLink.href = destination;
        categoryLink.textContent = categoryButton.textContent;
        categoryLink.setAttribute("data-rv-category", categoryKey);
        categoryLink.setAttribute("aria-expanded", "false");
        categoryLink.setAttribute("aria-controls", panelId);
        categoryLink.setAttribute("aria-haspopup", "true");
        categoryButton.parentNode.replaceChild(categoryLink, categoryButton);
    });
}

function registDesktopHoverNavigationV16(parentDocument, desktopNavigation) {
    var listCategoryLinks = Array.prototype.slice.call(
        desktopNavigation.querySelectorAll(".rv-category-bar > .rv-category-link")
    );
    listCategoryLinks.forEach(function(categoryLink) {
        var categoryKey = categoryLink.getAttribute("data-rv-category");
        categoryLink.addEventListener("mouseenter", function() {
            updateDesktopMenuState(parentDocument, categoryKey, true);
        });
        categoryLink.addEventListener("focus", function() {
            updateDesktopMenuState(parentDocument, categoryKey, true);
        });
    });

    desktopNavigation.addEventListener("mouseleave", function() {
        updateDesktopMenuState(parentDocument, null, false);
    });
}

function registMobileHomeCategoryV16(
    parentDocument,
    mobileCategories,
    listUtilityLinks,
    homeLinkModel
) {
    var homeDetails = parentDocument.createElement("details");
    homeDetails.className = "rv-mobile-category rv-mobile-home-category";
    var homeSummary = parentDocument.createElement("summary");
    homeSummary.textContent = mapSiteUtilityV16Config.homeCategoryLabel;
    homeDetails.appendChild(homeSummary);

    var homeBody = parentDocument.createElement("div");
    homeBody.className = "rv-mobile-category-body rv-mobile-home-links";
    listUtilityLinks.forEach(function(linkModel) {
        homeBody.appendChild(createUtilityAnchorV16(parentDocument, linkModel, "rv-mobile-link"));
    });
    homeDetails.appendChild(homeBody);
    mobileCategories.insertBefore(homeDetails, mobileCategories.firstChild);
}

function createUtilityAnchorV16(parentDocument, linkModel, className) {
    var linkElement = parentDocument.createElement("a");
    linkElement.className = className;
    linkElement.href = linkModel.href;
    linkElement.textContent = linkModel.text;
    if (linkModel.target === "_blank") {
        linkElement.target = "_blank";
        linkElement.rel = "noopener";
    }
    return linkElement;
}

window.addEventListener("load", function() {
    if (refreshHeaderUtilityV16()) {
        return;
    }

    var parentDocument = parent !== self ? parent.document : null;
    if (!parentDocument || !parentDocument.body || typeof MutationObserver === "undefined") {
        return;
    }

    var utilityObserver = new MutationObserver(function() {
        if (refreshHeaderUtilityV16()) {
            utilityObserver.disconnect();
        }
    });
    utilityObserver.observe(parentDocument.body, {childList: true, subtree: true});
    window.setTimeout(function() {
        utilityObserver.disconnect();
    }, 10000);
});
