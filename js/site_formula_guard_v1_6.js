/**
 * Updated: 2026/09/17
 * Summary: Keep unverified MathJax formulas off normal pages during strict source audit.
 *
 * This guard intentionally changes only the rendered DOM. Legacy article files keep
 * their original encoding and audit candidate pages remain untouched.
 */
"use strict";

(function applyFormulaGuardV16() {
  if (parent === self) {
    return;
  }

  var parentWindow = parent;
  var parentDocument = parentWindow.document;
  var currentPath = parentWindow.location.pathname;
  var scriptSource = document.currentScript && document.currentScript.src ?
    document.currentScript.src : window.location.href;

  if (!/\/fem\/fem_7_1_1\.html$/.test(currentPath)) {
    return;
  }

  var target = parentDocument.getElementById("fix-r-fem2d-mass-001");
  if (!target) {
    return;
  }

  var image = parentDocument.createElement("img");
  image.src = new URL(
    "../img/fem_d_mass_tri.files/image002.png",
    scriptSource
  ).href;
  image.alt = "";

  var paragraph = parentDocument.createElement("p");
  paragraph.className = "im";
  paragraph.style.textAlign = "left";
  paragraph.setAttribute("data-rv-formula-guard", "image002");
  paragraph.appendChild(image);

  target.parentNode.replaceChild(paragraph, target);
}());
