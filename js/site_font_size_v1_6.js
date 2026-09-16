/**
 * Updated: 2026/09/17
 * Summary: [S007] Add a three-step font-size selector to the v1.6 site header.
 * Differences from previous version:
 * - [ADD]: Normal / Large / Extra Large selector in the upper-right header area.
 * - [ADD]: Persist selected size in localStorage when available.
 * - [ADD]: Inject the dedicated font-size stylesheet into the parent page.
 * - [MOD]: None. This is a new shared JavaScript file.
 * - [DEL]: None.
 */
"use strict";

// [V002] Shared configuration for the v1.6 font-size selector.
var mapSiteFontSizeV16Config = {
    controlId: "rv-font-size-control-v16",
    styleElementId: "rv-font-size-v1-6-style",
    storageKey: "rv-font-size-v16",
    defaultSize: "normal",
    listSizes: [
        {key: "normal", label: "\u666e\u901a", className: "rv-font-normal"},
        {key: "large", label: "\u5927", className: "rv-font-large"},
        {key: "xlarge", label: "\u7279\u5927", className: "rv-font-xlarge"}
    ],
    styleUrl: new URL(
        "../css/site_font_size_v1_6.css",
        document.currentScript && document.currentScript.src ? document.currentScript.src : window.location.href
    ).href
};

// [F007] Register the font-size selector in the parent page header.
// [O014] Return value: isRegistered.
function registFontSizeControlV16() {
    // [L701] Run only inside the shared footer iframe.
    var isRegistered = false;
    if (parent === self) {
        return isRegistered;
    }

    var parentWindow = parent;
    var parentDocument = parentWindow.document;
    var parentBody = parentDocument.body;
    var headerElement = parentDocument.getElementById("header");
    if (!parentBody || !headerElement) {
        return isRegistered;
    }

    // [L702] Inject the font-size stylesheet only once.
    var stylesheetLink = parentDocument.getElementById(mapSiteFontSizeV16Config.styleElementId);
    if (!stylesheetLink) {
        stylesheetLink = parentDocument.createElement("link");
        stylesheetLink.id = mapSiteFontSizeV16Config.styleElementId;
        stylesheetLink.rel = "stylesheet";
        stylesheetLink.type = "text/css";
        stylesheetLink.href = mapSiteFontSizeV16Config.styleUrl;
        parentDocument.head.appendChild(stylesheetLink);
    }

    // [L703] Reuse an existing selector when the footer iframe is reloaded.
    var controlElement = parentDocument.getElementById(mapSiteFontSizeV16Config.controlId);
    if (!controlElement) {
        controlElement = parentDocument.createElement("div");
        controlElement.id = mapSiteFontSizeV16Config.controlId;
        controlElement.className = "rv-font-size-control";
        controlElement.setAttribute("role", "group");
        controlElement.setAttribute("aria-label", "\u6587\u5b57\u30b5\u30a4\u30ba");

        var labelElement = parentDocument.createElement("span");
        labelElement.className = "rv-font-size-label";
        labelElement.textContent = "\u6587\u5b57\u30b5\u30a4\u30ba";
        controlElement.appendChild(labelElement);

        mapSiteFontSizeV16Config.listSizes.forEach(function(sizeConfig) {
            var sizeButton = parentDocument.createElement("button");
            sizeButton.type = "button";
            sizeButton.className = "rv-font-size-button";
            sizeButton.setAttribute("data-rv-font-size", sizeConfig.key);
            sizeButton.setAttribute("aria-pressed", "false");
            sizeButton.textContent = sizeConfig.label;
            sizeButton.addEventListener("click", function() {
                updateFontSizeStateV16(parentWindow, parentDocument, sizeConfig.key, controlElement);
            });
            controlElement.appendChild(sizeButton);
        });

        headerElement.appendChild(controlElement);
    }

    // [L704] Apply the saved size, falling back to Normal.
    var selectedSize = selectStoredFontSizeV16(parentWindow);
    updateFontSizeStateV16(parentWindow, parentDocument, selectedSize, controlElement);
    isRegistered = true;
    return isRegistered;
}

// [T008] Apply one font-size state and synchronize buttons/storage.
// [I026] parentWindow: parent browsing context.
// [I027] parentDocument: parent page DOM.
// [I028] sizeKey: requested size key.
// [I029] controlElement: font-size selector element.
// [O015] Return value: appliedSizeKey.
function updateFontSizeStateV16(parentWindow, parentDocument, sizeKey, controlElement) {
    // [L711] Reject unknown keys and fall back to the default.
    var appliedSizeKey = mapSiteFontSizeV16Config.defaultSize;
    var selectedConfig = null;
    mapSiteFontSizeV16Config.listSizes.forEach(function(sizeConfig) {
        if (sizeConfig.key === sizeKey) {
            selectedConfig = sizeConfig;
        }
    });
    if (!selectedConfig) {
        mapSiteFontSizeV16Config.listSizes.forEach(function(sizeConfig) {
            if (sizeConfig.key === mapSiteFontSizeV16Config.defaultSize) {
                selectedConfig = sizeConfig;
            }
        });
    }
    if (!selectedConfig || !parentDocument || !parentDocument.body) {
        return appliedSizeKey;
    }

    // [L712] Keep exactly one size class on the parent body.
    mapSiteFontSizeV16Config.listSizes.forEach(function(sizeConfig) {
        parentDocument.body.classList.remove(sizeConfig.className);
    });
    parentDocument.body.classList.add(selectedConfig.className);
    appliedSizeKey = selectedConfig.key;

    // [L713] Synchronize aria-pressed state.
    if (controlElement) {
        var listButtons = Array.prototype.slice.call(
            controlElement.querySelectorAll("[data-rv-font-size]")
        );
        listButtons.forEach(function(sizeButton) {
            var isSelected = sizeButton.getAttribute("data-rv-font-size") === appliedSizeKey;
            sizeButton.setAttribute("aria-pressed", isSelected ? "true" : "false");
        });
    }

    // [L714] Persist the choice when storage is available.
    try {
        parentWindow.localStorage.setItem(mapSiteFontSizeV16Config.storageKey, appliedSizeKey);
    } catch (error) {
        /* Storage may be blocked; visual switching still works. */
    }

    return appliedSizeKey;
}

// [T009] Read the stored font-size preference safely.
// [I030] parentWindow: parent browsing context.
// [O016] Return value: storedSizeKey.
function selectStoredFontSizeV16(parentWindow) {
    // [L721] Use the default when storage is unavailable or invalid.
    var storedSizeKey = mapSiteFontSizeV16Config.defaultSize;
    try {
        var storedValue = parentWindow.localStorage.getItem(mapSiteFontSizeV16Config.storageKey);
        var isAllowed = mapSiteFontSizeV16Config.listSizes.some(function(sizeConfig) {
            return sizeConfig.key === storedValue;
        });
        if (isAllowed) {
            storedSizeKey = storedValue;
        }
    } catch (error) {
        storedSizeKey = mapSiteFontSizeV16Config.defaultSize;
    }
    return storedSizeKey;
}

window.addEventListener("load", function() {
    registFontSizeControlV16();
});
