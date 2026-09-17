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

  function replaceBlockWithImage(target, imageRelativePath, guardLabel) {
    if (!target || !target.parentNode) {
      return false;
    }

    var image = parentDocument.createElement("img");
    image.src = new URL(imageRelativePath, scriptSource).href;
    image.alt = "";

    var paragraph = parentDocument.createElement("p");
    paragraph.className = "im";
    paragraph.style.textAlign = "left";
    paragraph.setAttribute("data-rv-formula-guard", guardLabel);
    paragraph.appendChild(image);

    target.parentNode.replaceChild(paragraph, target);
    return true;
  }

  if (/\/fem\/fem_7_1_1\.html$/.test(currentPath)) {
    replaceBlockWithImage(
      parentDocument.getElementById("fix-r-fem2d-mass-001"),
      "../img/fem_d_mass_tri.files/image002.png",
      "fem-7-1-1-image002"
    );
    return;
  }

  if (/\/fem\/fem_7_1_2\.html$/.test(currentPath)) {
    var imageNumbers = [
      "003", "004", "027", "032", "032", "037",
      "038", "039", "040", "041", "042"
    ];
    var blocks = Array.prototype.slice.call(
      parentDocument.querySelectorAll("#content-text .math-block")
    );

    if (blocks.length !== imageNumbers.length) {
      return;
    }

    blocks.forEach(function(block, index) {
      var imageNumber = imageNumbers[index];
      replaceBlockWithImage(
        block,
        "../img/fem_d_momentum_tri.files/image" + imageNumber + ".png",
        "fem-7-1-2-image" + imageNumber + "-" + (index + 1)
      );
    });
  }
}());
