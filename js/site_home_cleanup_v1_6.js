/**
 * Updated: 2026/09/20
 * Summary: Clean obsolete top-page blocks and remove legacy ad spacing.
 * - [DEL]: Main contents link list and legacy Yahoo site-search block.
 * - [DEL]: Legacy right-column ad area on the renewed top page.
 * - [MOD]: Renewal notice is now maintained directly in index.html to avoid duplicate rendering.
 * - [KEEP]: Legacy /old/ pages are unchanged.
 */
"use strict";

(function refreshTopPageV16() {
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

  var parentBody = parentDocument.body;
  var contentMain = parentDocument.getElementById("content-main");
  if (!parentBody || !contentMain) {
    return;
  }

  parentBody.classList.add("rv-top-page-v16");

  function selectHeading(sectionLabel) {
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

    return targetHeading;
  }

  function removePreviousBreaks(targetElement) {
    var previousElement = targetElement ? targetElement.previousElementSibling : null;
    while (previousElement && previousElement.tagName === "BR") {
      var breakElement = previousElement;
      previousElement = breakElement.previousElementSibling;
      breakElement.parentNode.removeChild(breakElement);
    }
  }

  function removeSectionByHeading(sectionLabel) {
    var targetHeading = selectHeading(sectionLabel);
    if (!targetHeading) {
      return false;
    }

    removePreviousBreaks(targetHeading);

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

  var contentAttend = parentDocument.getElementById("content-attend");
  if (contentAttend && contentAttend.parentNode) {
    contentAttend.parentNode.removeChild(contentAttend);
  }

}());
