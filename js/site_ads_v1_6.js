// Created: 2026-09-20 20:07 JST
// Modernize legacy AdSense placements without editing every public HTML page.
// Runs inside footer.html and modifies the same-origin parent page.

(function () {
  "use strict";

  var PUBLISHER_ID = "ca-pub-4382202381956938";
  var MAIN_SLOT = "8802800686";
  var TOP_SLOT = "4832539076";
  var ATTEND_SLOT = "3994918548";
  var ADSENSE_SRC = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + PUBLISHER_ID;

  function getParentWindow() {
    try {
      if (!parent || parent === self || !parent.document) return null;
      void parent.document.documentElement;
      return parent;
    } catch (e) {
      return null;
    }
  }

  function ensureStyle(doc) {
    if (doc.getElementById("rv-adsense-style-v1-6")) return;
    var style = doc.createElement("style");
    style.id = "rv-adsense-style-v1-6";
    style.textContent =
      ".rv-adsense-slot{width:100%;margin:18px 0 24px;overflow:hidden;text-align:center;box-sizing:border-box;}" +
      ".rv-adsense-slot>.adsbygoogle{max-width:100%;}" +
      "ins.adsbygoogle[data-ad-status=\"unfilled\"]{display:none!important;}";
    doc.head.appendChild(style);
  }

  function ensureAdSenseScript(doc) {
    var scripts = doc.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
      var src = scripts[i].getAttribute("src") || "";
      if (src.indexOf("pagead2.googlesyndication.com/pagead/js/adsbygoogle.js") !== -1) {
        return;
      }
    }
    var script = doc.createElement("script");
    script.async = true;
    script.src = ADSENSE_SRC;
    script.crossOrigin = "anonymous";
    doc.head.appendChild(script);
  }

  function queueAd(win) {
    try {
      win.adsbygoogle = win.adsbygoogle || [];
      win.adsbygoogle.push({});
    } catch (e) {
      // Ad blockers or an unavailable AdSense script must not break the page.
    }
  }

  function createResponsiveAd(doc, slot) {
    var wrap = doc.createElement("div");
    wrap.className = "rv-adsense-slot";

    var ins = doc.createElement("ins");
    ins.className = "adsbygoogle";
    ins.style.display = "block";
    ins.setAttribute("data-ad-client", PUBLISHER_ID);
    ins.setAttribute("data-ad-slot", slot);
    ins.setAttribute("data-ad-format", "auto");
    ins.setAttribute("data-full-width-responsive", "true");

    wrap.appendChild(ins);
    return wrap;
  }

  function createFixedAd(doc, slot, width, height) {
    var wrap = doc.createElement("div");
    wrap.className = "rv-adsense-slot";

    var ins = doc.createElement("ins");
    ins.className = "adsbygoogle";
    ins.style.display = "inline-block";
    ins.style.width = width + "px";
    ins.style.height = height + "px";
    ins.setAttribute("data-ad-client", PUBLISHER_ID);
    ins.setAttribute("data-ad-slot", slot);

    wrap.appendChild(ins);
    return wrap;
  }

  function removeAdvertisementHeadings(doc) {
    var headings = doc.getElementsByTagName("h2");
    var targets = [];
    for (var i = 0; i < headings.length; i++) {
      if ((headings[i].textContent || "").replace(/\s+/g, "").trim() === "広告") {
        targets.push(headings[i]);
      }
    }
    for (var j = 0; j < targets.length; j++) {
      targets[j].parentNode.removeChild(targets[j]);
    }
  }

  function replaceLegacyIframeAds(doc, win) {
    var frames = Array.prototype.slice.call(doc.getElementsByTagName("iframe"));
    for (var i = 0; i < frames.length; i++) {
      var frame = frames[i];
      var src = (frame.getAttribute("src") || "").split("?")[0].split("#")[0];
      if (!/(^|\/)ad(?:_top|_google)?\.html$/i.test(src)) continue;

      var slot = /ad_top\.html$/i.test(src) ? TOP_SLOT : MAIN_SLOT;
      var ad = createResponsiveAd(doc, slot);
      var holder = frame.parentNode;

      if (holder && holder.tagName && holder.tagName.toLowerCase() === "p" &&
          holder.children.length === 1 && (holder.textContent || "").trim() === "") {
        holder.parentNode.replaceChild(ad, holder);
      } else if (holder) {
        holder.replaceChild(ad, frame);
      }
      queueAd(win);
    }
  }

  function replaceLegacyAttendAd(doc, win) {
    var box = doc.getElementById("content-attend");
    if (!box) return;
    var text = box.textContent || "";
    var html = box.innerHTML || "";
    if (html.indexOf("show_ads.js") === -1 && text.indexOf("3994918548") === -1 && html.indexOf("3994918548") === -1) {
      return;
    }
    while (box.firstChild) box.removeChild(box.firstChild);
    box.appendChild(createFixedAd(doc, ATTEND_SLOT, 120, 600));
    queueAd(win);
  }

  function init() {
    var win = getParentWindow();
    if (!win) return;
    var doc = win.document;
    if (!doc.head || !doc.body) return;

    ensureStyle(doc);
    ensureAdSenseScript(doc);
    removeAdvertisementHeadings(doc);
    replaceLegacyIframeAds(doc, win);
    replaceLegacyAttendAd(doc, win);
  }

  init();
})();
