/*
 * Created: 2026-09-16
 * Purpose: build side-by-side original-image / MathJax formula audit rows.
 * Equality is NEVER decided automatically; reviewer must perform Pass 1 and Pass 2.
 */
(function(){
  "use strict";

  var frame = document.getElementById("audit-frame");
  var pageSelect = document.getElementById("audit-page");
  var loadButton = document.getElementById("audit-load");
  var customInput = document.getElementById("audit-custom");
  var customButton = document.getElementById("audit-load-custom");
  var list = document.getElementById("audit-list");
  var status = document.getElementById("audit-status");
  var counters = {
    total: document.getElementById("count-total"),
    pass1: document.getElementById("count-pass1"),
    pass2: document.getElementById("count-pass2"),
    match: document.getElementById("count-match"),
    fix: document.getElementById("count-fix")
  };

  function storageKey(pageUrl, formulaId){
    return "ryutai-formula-audit::" + pageUrl + "::" + formulaId;
  }

  function loadRecord(pageUrl, formulaId){
    try{
      var raw = localStorage.getItem(storageKey(pageUrl, formulaId));
      return raw ? JSON.parse(raw) : {};
    }catch(error){
      return {};
    }
  }

  function saveRecord(pageUrl, formulaId, record){
    try{
      localStorage.setItem(storageKey(pageUrl, formulaId), JSON.stringify(record));
    }catch(error){
      status.textContent = "localStorageへ保存できませんでした。ブラウザ設定を確認してください。";
    }
  }

  function updateSummary(){
    var rows = Array.prototype.slice.call(list.querySelectorAll(".audit-item"));
    var values = {total: rows.length, pass1: 0, pass2: 0, match: 0, fix: 0};
    rows.forEach(function(row){
      if(row.querySelector('[data-field="pass1"]').checked){ values.pass1 += 1; }
      if(row.querySelector('[data-field="pass2"]').checked){ values.pass2 += 1; }
      if(row.querySelector('[data-field="match"]').checked){ values.match += 1; }
      if(row.querySelector('[data-field="fix"]').checked){ values.fix += 1; }
    });
    Object.keys(values).forEach(function(key){ counters[key].textContent = String(values[key]); });
  }

  function cloneRenderedFormula(sourceBlock){
    var wrapper = document.createElement("div");
    wrapper.className = "audit-rendered";
    var rendered = sourceBlock.querySelector("mjx-container");
    if(rendered){
      wrapper.appendChild(rendered.cloneNode(true));
      return wrapper;
    }

    wrapper.innerHTML = sourceBlock.innerHTML;
    return wrapper;
  }

  function makeCheckbox(labelText, field, checked){
    var label = document.createElement("label");
    var input = document.createElement("input");
    input.type = "checkbox";
    input.setAttribute("data-field", field);
    input.checked = Boolean(checked);
    label.appendChild(input);
    label.appendChild(document.createTextNode(" " + labelText));
    return label;
  }

  function buildRow(block, pageUrl, frameUrl, index){
    var formulaId = block.id || ("formula-no-id-" + (index + 1));
    var source = block.getAttribute("data-source-image") || "";
    var sourceUrl = source ? new URL(source, frameUrl).href : "";
    var record = loadRecord(pageUrl, formulaId);

    var row = document.createElement("article");
    row.className = "audit-item";
    row.setAttribute("data-formula-id", formulaId);

    var head = document.createElement("header");
    head.className = "audit-item-head";
    var title = document.createElement("h2");
    title.textContent = (index + 1) + ". " + formulaId;
    var path = document.createElement("div");
    path.className = "audit-source-path";
    path.textContent = source || "data-source-image 未設定";
    head.appendChild(title);
    head.appendChild(path);

    var compare = document.createElement("div");
    compare.className = "audit-compare";

    var sourcePane = document.createElement("section");
    sourcePane.className = "audit-pane";
    sourcePane.innerHTML = "<h3>元画像</h3>";
    if(sourceUrl){
      var image = document.createElement("img");
      image.className = "audit-source-image";
      image.src = sourceUrl;
      image.alt = formulaId + " 元画像";
      image.addEventListener("error", function(){
        var warning = document.createElement("div");
        warning.className = "audit-missing";
        warning.textContent = "元画像を読み込めません: " + source;
        sourcePane.appendChild(warning);
      }, {once:true});
      sourcePane.appendChild(image);
    }else{
      var missing = document.createElement("div");
      missing.className = "audit-missing";
      missing.textContent = "data-source-image が設定されていません。";
      sourcePane.appendChild(missing);
    }

    var renderedPane = document.createElement("section");
    renderedPane.className = "audit-pane";
    renderedPane.innerHTML = "<h3>現在のMathJax表示</h3>";
    renderedPane.appendChild(cloneRenderedFormula(block));

    compare.appendChild(sourcePane);
    compare.appendChild(renderedPane);

    var review = document.createElement("div");
    review.className = "audit-review";
    var pass1 = makeCheckbox("Pass 1", "pass1", record.pass1);
    var pass2 = makeCheckbox("Pass 2", "pass2", record.pass2);
    var match = makeCheckbox("一致OK", "match", record.match);
    var fix = makeCheckbox("要修正", "fix", record.fix);
    var note = document.createElement("textarea");
    note.setAttribute("data-field", "note");
    note.placeholder = "差異、誤記候補、補足内容など";
    note.value = record.note || "";

    [pass1, pass2, match, fix].forEach(function(element){ review.appendChild(element); });
    review.appendChild(note);

    function persist(){
      var current = {
        pass1: review.querySelector('[data-field="pass1"]').checked,
        pass2: review.querySelector('[data-field="pass2"]').checked,
        match: review.querySelector('[data-field="match"]').checked,
        fix: review.querySelector('[data-field="fix"]').checked,
        note: note.value
      };
      if(current.match && current.fix){
        current.match = false;
        review.querySelector('[data-field="match"]').checked = false;
      }
      row.classList.toggle("is-match", current.match);
      row.classList.toggle("is-fix", current.fix);
      saveRecord(pageUrl, formulaId, current);
      updateSummary();
    }

    review.addEventListener("change", persist);
    note.addEventListener("input", persist);
    row.classList.toggle("is-match", Boolean(record.match));
    row.classList.toggle("is-fix", Boolean(record.fix));

    row.appendChild(head);
    row.appendChild(compare);
    row.appendChild(review);
    return row;
  }

  function waitForMathJax(win){
    try{
      if(win.MathJax && win.MathJax.startup && win.MathJax.startup.promise){
        return win.MathJax.startup.promise.catch(function(){ return null; });
      }
    }catch(error){
      return Promise.resolve(null);
    }
    return new Promise(function(resolve){ window.setTimeout(resolve, 900); });
  }

  function renderAudit(pageUrl){
    list.innerHTML = "";
    status.textContent = "対象ページを読み込んでいます: " + pageUrl;
    Object.keys(counters).forEach(function(key){ counters[key].textContent = "0"; });

    frame.onload = function(){
      var doc;
      var win;
      try{
        doc = frame.contentDocument;
        win = frame.contentWindow;
      }catch(error){
        status.textContent = "対象ページへアクセスできません。同一オリジンのローカルURLで開いてください。";
        return;
      }

      waitForMathJax(win).then(function(){
        var blocks = Array.prototype.slice.call(doc.querySelectorAll(".math-block"));
        var frameUrl = frame.contentWindow.location.href;
        if(!blocks.length){
          status.textContent = "math-block が見つかりませんでした。未変換ページまたは対象外ページの可能性があります。";
          return;
        }

        blocks.forEach(function(block, index){ list.appendChild(buildRow(block, pageUrl, frameUrl, index)); });
        status.textContent = "読み込み完了: " + blocks.length + " 個のMathJax式を表示しています。元画像と1式ずつ照合してください。";
        updateSummary();
      });
    };

    frame.src = pageUrl;
  }

  loadButton.addEventListener("click", function(){ renderAudit(pageSelect.value); });
  customButton.addEventListener("click", function(){
    var value = customInput.value.trim();
    if(value){ renderAudit(value); }
  });

  renderAudit(pageSelect.value);
})();
