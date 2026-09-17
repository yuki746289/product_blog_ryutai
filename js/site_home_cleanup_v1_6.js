/**
 * Updated: 2026/09/17
 * Summary: Clean obsolete top-page blocks, remove legacy ad spacing, and add renewal notice.
 * - [DEL]: Main contents link list and legacy Yahoo site-search block.
 * - [DEL]: Legacy right-column ad area on the renewed top page.
 * - [ADD]: Site renewal notice below the existing announcements.
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

  function registRenewalNotice() {
    if (parentDocument.getElementById("rv-renewal-notice-v16")) {
      return;
    }

    var nextHeading = selectHeading("\u6570\u5024\u8a08\u7b97\u306b\u3064\u3044\u3066");
    if (!nextHeading) {
      return;
    }

    var noticeBlock = parentDocument.createElement("section");
    noticeBlock.id = "rv-renewal-notice-v16";
    noticeBlock.className = "rv-renewal-notice";

    var noticeHeading = parentDocument.createElement("h3");
    noticeHeading.textContent = "\u30b5\u30a4\u30c8\u30ea\u30cb\u30e5\u30fc\u30a2\u30eb\u306b\u3064\u3044\u3066";
    noticeBlock.appendChild(noticeHeading);

    var noticeText = parentDocument.createElement("p");
    noticeText.textContent =
      "AI\u3092\u7528\u3044\u3066\u30b5\u30a4\u30c8\u3092\u30ea\u30cb\u30e5\u30fc\u30a2\u30eb\u3057\u307e\u3057\u305f\u3002" +
      "ChatGPT\u3068GitHub\u3092\u7d44\u307f\u5408\u308f\u305b\u3001\u624b\u4f5c\u696d\u3067\u306e\u30b3\u30fc\u30c7\u30a3\u30f3\u30b0\u3092\u884c\u308f\u305a\u306b\u66f4\u65b0\u3057\u3066\u3044\u307e\u3059\u3002" +
      "\u5f93\u6765\u753b\u50cf\u3067\u63b2\u8f09\u3057\u3066\u3044\u305f\u6570\u5f0f\u306f\u3001\u539f\u753b\u50cf\u3068\u306e\u4e00\u81f4\u78ba\u8a8d\u3092\u884c\u3044\u306a\u304c\u3089LaTeX\uff08MathJax\uff09\u5f62\u5f0f\u3078\u9806\u6b21\u5909\u63db\u3057\u3066\u3044\u307e\u3059\u3002";
    noticeBlock.appendChild(noticeText);

    contentMain.insertBefore(noticeBlock, nextHeading);
  }

  removeSectionByHeading("\u30e1\u30a4\u30f3\u30b3\u30f3\u30c6\u30f3\u30c4");
  removeSectionByHeading("\u30b5\u30a4\u30c8\u5185\u691c\u7d22");

  var contentAttend = parentDocument.getElementById("content-attend");
  if (contentAttend && contentAttend.parentNode) {
    contentAttend.parentNode.removeChild(contentAttend);
  }

  registRenewalNotice();
}());
