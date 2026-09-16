/**
 * Updated: 2026/09/17
 * Summary: [S008] Refine the v1.6 header utility navigation and add a same-page legacy link.
 * Differences from previous version:
 * - [ADD]: Hide obsolete utility links in the new UI.
 * - [ADD]: Add an old-page link after revision history.
 * - [ADD]: Resolve the old-page URL to the same relative path under /old/.
 * - [ADD]: Load dedicated utility-navigation CSS.
 */
"use strict";

// [V003] Utility-navigation configuration. Japanese labels use Unicode escapes.
var mapSiteUtilityV16Config = {
    styleElementId: "rv-site-utility-v1-6-style",
    oldLinkClassName: "rv-utility-old-page",
    oldDirectoryName: "old/",
    oldPageLabel: "\u65e7\u30da\u30fc\u30b8",
    revisionLabel: "\u4fee\u6b63\u5c65\u6b74",
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

// [F008] Apply header utility cleanup, sizing CSS, and the matching legacy-page link.
// [O017] Return value: isApplied.
function refreshHeaderUtilityV16() {
    var isApplied = false;
    if (parent === self) {
        return isApplied;
    }

    var parentWindow = parent;
    var parentDocument = parentWindow.document;
    var desktopUtility = parentDocument.querySelector(".rv-utility-navigation");
    var mobileUtility = parentDocument.querySelector(".rv-mobile-utility");
    if (!desktopUtility || !mobileUtility) {
        return isApplied;
    }

    // [L731] Load the utility-specific stylesheet only once.
    var styleElement = parentDocument.getElementById(mapSiteUtilityV16Config.styleElementId);
    if (!styleElement) {
        styleElement = parentDocument.createElement("link");
        styleElement.id = mapSiteUtilityV16Config.styleElementId;
        styleElement.rel = "stylesheet";
        styleElement.type = "text/css";
        styleElement.href = new URL(
            "css/site_utility_v1_6.css?v=20260917a",
            mapSiteUtilityV16Config.baseUrl
        ).href;
        parentDocument.head.appendChild(styleElement);
    }

    var listContainers = [desktopUtility, mobileUtility];
    listContainers.forEach(function(containerElement) {
        // [L732] Remove obsolete links from the new navigation only; legacy pages remain unchanged.
        var listLinks = Array.prototype.slice.call(containerElement.querySelectorAll("a"));
        listLinks.forEach(function(linkElement) {
            var label = (linkElement.textContent || "").replace(/^\s+|\s+$/g, "");
            if (mapSiteUtilityV16Config.excludedLabels.indexOf(label) >= 0) {
                linkElement.parentNode.removeChild(linkElement);
            }
        });

        // [L733] Avoid duplicate old-page links when initialization is retried.
        var existingOldLink = containerElement.querySelector("." + mapSiteUtilityV16Config.oldLinkClassName);
        if (existingOldLink) {
            existingOldLink.parentNode.removeChild(existingOldLink);
        }

        // [L734] Build the same relative page path under /old/.
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

        var oldLink = parentDocument.createElement("a");
        oldLink.className = mapSiteUtilityV16Config.oldLinkClassName;
        oldLink.href = oldPageUrl.href;
        oldLink.textContent = mapSiteUtilityV16Config.oldPageLabel;
        oldLink.target = "_blank";
        oldLink.rel = "noopener";
        oldLink.title = "\u73fe\u5728\u306e\u30da\u30fc\u30b8\u3068\u540c\u3058\u5834\u6240\u306e\u65e7\u7248\u3092\u65b0\u3057\u3044\u30bf\u30d6\u3067\u958b\u304d\u307e\u3059";

        // [L735] Insert immediately after revision history when it exists.
        var revisionLink = null;
        Array.prototype.slice.call(containerElement.querySelectorAll("a")).some(function(linkElement) {
            var label = (linkElement.textContent || "").replace(/^\s+|\s+$/g, "");
            if (label === mapSiteUtilityV16Config.revisionLabel) {
                revisionLink = linkElement;
                return true;
            }
            return false;
        });

        if (revisionLink && revisionLink.nextSibling) {
            containerElement.insertBefore(oldLink, revisionLink.nextSibling);
        } else {
            containerElement.appendChild(oldLink);
        }
    });

    isApplied = true;
    return isApplied;
}

window.addEventListener("load", function() {
    if (refreshHeaderUtilityV16()) {
        return;
    }

    // Navigation creation can finish after its stylesheet load. Observe briefly and apply once ready.
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
