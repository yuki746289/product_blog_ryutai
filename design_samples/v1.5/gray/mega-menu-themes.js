/*
 * 作成日時: 2026-09-16 20:26 JST
 * 用途: グレー系4デザイン比較ページのテーマ切替
 * 本体サイトには未適用。
 */
(function(){
  "use strict";
  var buttons=Array.prototype.slice.call(document.querySelectorAll("[data-theme-class]"));
  var themes=["theme-gray-academic","theme-soft-gray","theme-graphite","theme-mono-notes"];
  function applyTheme(theme){
    themes.forEach(function(name){document.body.classList.remove(name);});
    document.body.classList.add(theme);
    buttons.forEach(function(button){button.setAttribute("aria-pressed",button.getAttribute("data-theme-class")===theme?"true":"false");});
    try{localStorage.setItem("ryutai-gray-theme",theme);}catch(e){}
  }
  buttons.forEach(function(button){button.addEventListener("click",function(){applyTheme(button.getAttribute("data-theme-class"));});});
  var stored=null;
  try{stored=localStorage.getItem("ryutai-gray-theme");}catch(e){}
  if(stored&&themes.indexOf(stored)!==-1){applyTheme(stored);}
})();
