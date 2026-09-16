/*
 * 更新日時: 2026/09/16
 * 用途: 多層ナビゲーション比較プレビュー専用JS
 * 本体サイトには未適用。
 */
(function(){
  "use strict";

  var desktopButtons = Array.prototype.slice.call(document.querySelectorAll(".mm-nav-button"));
  var megaPanels = Array.prototype.slice.call(document.querySelectorAll(".mm-mega-panel"));
  var desktopNavWrap = document.querySelector(".mm-desktop-nav-wrap");
  var mobileTrigger = document.querySelector(".mm-mobile-trigger");
  var mobileDrawer = document.querySelector(".mm-mobile-drawer");
  var mobileOverlay = document.querySelector(".mm-mobile-overlay");
  var mobileClose = document.querySelector(".mm-mobile-close");

  if(mobileDrawer){
    mobileDrawer.setAttribute("inert", "");
  }

  function closeDesktopMenus(){
    desktopButtons.forEach(function(button){
      button.setAttribute("aria-expanded", "false");
    });
    megaPanels.forEach(function(panel){
      panel.classList.remove("is-open");
    });
  }

  function openDesktopMenu(button){
    var panelId = button.getAttribute("data-menu");
    var panel = document.getElementById(panelId);
    var isAlreadyOpen = button.getAttribute("aria-expanded") === "true";

    closeDesktopMenus();
    if(isAlreadyOpen || !panel){
      return;
    }

    button.setAttribute("aria-expanded", "true");
    panel.classList.add("is-open");
  }

  desktopButtons.forEach(function(button){
    button.addEventListener("click", function(event){
      event.stopPropagation();
      openDesktopMenu(button);
    });
  });

  megaPanels.forEach(function(panel){
    panel.addEventListener("click", function(event){
      event.stopPropagation();
    });
  });

  document.addEventListener("click", function(){
    closeDesktopMenus();
  });

  document.addEventListener("keydown", function(event){
    if(event.key === "Escape"){
      closeDesktopMenus();
      closeMobileDrawer();
    }
  });

  function openMobileDrawer(){
    if(!mobileDrawer || !mobileOverlay || !mobileTrigger){
      return;
    }
    document.body.classList.add("mm-drawer-open");
    mobileDrawer.removeAttribute("inert");
    mobileDrawer.classList.add("is-open");
    mobileOverlay.classList.add("is-open");
    mobileTrigger.setAttribute("aria-expanded", "true");
    mobileDrawer.setAttribute("aria-hidden", "false");
  }

  function closeMobileDrawer(){
    if(!mobileDrawer || !mobileOverlay || !mobileTrigger){
      return;
    }
    var restoreFocus = document.activeElement && mobileDrawer.contains(document.activeElement);
    document.body.classList.remove("mm-drawer-open");
    mobileDrawer.classList.remove("is-open");
    mobileOverlay.classList.remove("is-open");
    mobileTrigger.setAttribute("aria-expanded", "false");
    mobileDrawer.setAttribute("aria-hidden", "true");
    mobileDrawer.setAttribute("inert", "");
    if(restoreFocus && window.getComputedStyle(mobileTrigger).display !== "none"){
      mobileTrigger.focus();
    }
  }

  if(mobileTrigger){
    mobileTrigger.addEventListener("click", openMobileDrawer);
  }
  if(mobileClose){
    mobileClose.addEventListener("click", closeMobileDrawer);
  }
  if(mobileOverlay){
    mobileOverlay.addEventListener("click", closeMobileDrawer);
  }

  var mobileLinks = Array.prototype.slice.call(document.querySelectorAll(".mm-mobile-drawer a"));
  mobileLinks.forEach(function(link){
    link.addEventListener("click", function(){
      closeMobileDrawer();
    });
  });

  var desktopMedia = window.matchMedia("(min-width: 768px)");
  function syncViewport(){
    if(desktopMedia.matches){
      closeMobileDrawer();
    }else{
      closeDesktopMenus();
    }
  }
  if(desktopMedia.addEventListener){
    desktopMedia.addEventListener("change", syncViewport);
  }else if(desktopMedia.addListener){
    desktopMedia.addListener(syncViewport);
  }

  if(desktopNavWrap){
    desktopNavWrap.addEventListener("mouseleave", function(){
      /* clickで開いたメニューはmouseleaveでは閉じない。意図しない消失を避ける。 */
    });
  }
})();
