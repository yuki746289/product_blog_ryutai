/**
 * Updated: 2026/09/17
 * Summary: Remove obsolete duplicate sections from the v1.6 top page only.
 * - [DEL]: Main contents link list.
 * - [DEL]: Legacy Yahoo site-search block.
 * - [KEEP]: Legacy /old/ pages are unchanged.
 */
"use strict";

(function cleanupTopPageV16() {
    if (parent === self) {
        return;
    }

    var parentWindow = parent;
    var parentDocument = parentWindow.document;
    var scriptSource = document.currentScript && document.currentScript.src ?
        document.currentScript.src : window.location.href;
    var siteBaseUrl = new URL("../", scriptSource);
    var currentUrl = new URL(parentWindow.location.href);
    var siteBasePath = siteBaseUrl.pathname;
    var currentPath = currentUrl.pathname;

    var isTopPage = currentPath === siteBasePath ||
        currentPath === siteBasePath + "index.html";
    if (!isTopPage) {
        return;
    }

    var contentMain = parentDocument.getElementById("content-main");
    if (!contentMain) {
        return;
    }

    function removeSectionByHeading(sectionLabel) {
        var headings = Array.prototype.slice.call(contentMain.querySelectorAll("h2"));
        var targetHeading = null;
        headings.some(function(headingElement) {
            var label = (headingElement.textContent || "").replace(/^\s+|\s+$/g, "");
            if (label === sectionLabel) {
                targetHeading = headingElement;
                return true;
            }
            return false;
        });

        if (!targetHeading) {
            return false;
        }

        var previousElement = targetHeading.previousElementSibling;
        if (previousElement && previousElement.tagName === "BR") {
            previousElement.parentNode.removeChild(previousElement);
        }

        var currentNode = targetHeading;
        while (currentNode) {
            var nextNode = currentNode.nextSibling;
            if (currentNode !== targetHeading &&
                currentNode.nodeType === 1 &&
                currentNode.tagName === "H2") {
                break;
            }
            contentMain.removeChild(currentNode);
            currentNode = nextNode;
        }
        return true;
    }

    removeSectionByHeading("\u30e1\u30a4\u30f3\u30b3\u30f3\u30c6\u30f3\u30c4");
    removeSectionByHeading("\u30b5\u30a4\u30c8\u5185\u691c\u7d22");
}());
