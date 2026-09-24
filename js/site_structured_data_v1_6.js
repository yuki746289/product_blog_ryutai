/**
 * Created: 2026-09-24 16:37 JST
 * Summary: Add shared favicon metadata and BreadcrumbList structured data
 *          from the existing visible breadcrumb navigation.
 */
"use strict";

(function registerSearchAppearanceV16() {
  if (parent === self) {
    return;
  }

  var parentWindow = parent;
  var parentDocument = parentWindow.document;
  if (!parentDocument || !parentDocument.head || !parentDocument.body) {
    return;
  }

  var parentUrl = new URL(parentWindow.location.href);
  if (parentUrl.pathname.indexOf("/old/") !== -1) {
    return;
  }

  var scriptSource = document.currentScript && document.currentScript.src ?
    document.currentScript.src : window.location.href;
  var siteRoot = new URL("../", scriptSource);

  // Keep the browser favicon consistent on every renewed page.
  if (!parentDocument.querySelector('link[rel~="icon"]')) {
    var iconLink = parentDocument.createElement("link");
    iconLink.rel = "icon";
    iconLink.type = "image/x-icon";
    iconLink.sizes = "64x64";
    iconLink.href = new URL("favicon.ico", siteRoot).href;
    parentDocument.head.appendChild(iconLink);
  }

  // Build search breadcrumb data from the breadcrumb users already see.
  if (parentDocument.getElementById("rv-breadcrumb-jsonld-v1-6")) {
    return;
  }

  var breadcrumbLinks = Array.prototype.slice.call(
    parentDocument.querySelectorAll("#header > ul li a")
  );

  if (breadcrumbLinks.length < 2) {
    return;
  }

  var items = [];
  breadcrumbLinks.forEach(function(anchor, index) {
    var name = (anchor.textContent || "").replace(/^\s+|\s+$/g, "");
    if (!name) {
      return;
    }
    if (index === 0 && name.toLowerCase() === "index") {
      name = "ホーム";
    }

    items.push({
      "@type": "ListItem",
      "position": items.length + 1,
      "name": name,
      "item": new URL(anchor.getAttribute("href") || anchor.href, parentWindow.location.href).href
    });
  });

  if (items.length < 2) {
    return;
  }

  var jsonLd = parentDocument.createElement("script");
  jsonLd.id = "rv-breadcrumb-jsonld-v1-6";
  jsonLd.type = "application/ld+json";
  jsonLd.textContent = JSON.stringify({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items
  });
  parentDocument.head.appendChild(jsonLd);
}());
