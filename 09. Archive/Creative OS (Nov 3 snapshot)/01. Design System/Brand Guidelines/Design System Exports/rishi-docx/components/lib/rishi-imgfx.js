/* rishi-imgfx: ImageGenerate engine for rishi.docx. A plain-canvas rebuild of the idea behind img-fx "Image generation" (MIT, (c) Jakub Antalik / Libraries.dev): a churning pixel mosaic that resolves into the photo. No WebGL, no dependencies, deterministic per frame. */
(function () {
  var PAL = {
    paper: { bg: "#F4F1EA", cells: ["#E3DED3", "#D6D0C3", "#C4BEB1", "#9C978C", "#141414"], weights: [5, 4, 3, 2, 1] },
    ink: { bg: "#141414", cells: ["#1F1F1F", "#2B2B2B", "#3A3A3A", "#6B6B6B", "#F4F1EA"], weights: [5, 4, 3, 2, 1] }
  };
  var SIGNAL = "#E2432A";
  function hash(a, b, c) { var h = Math.sin(a * 127.1 + b * 311.7 + (c || 0) * 74.7) * 43758.5453; return h - Math.floor(h); }
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function isInk(c, th) { if (th === "ink") return true; if (th === "paper") return false; var n = c.closest && c.closest("[data-theme]"); return !!n && n.getAttribute("data-theme") === "ink"; }
  function pick(pal, h) { var tot = 0, i; for (i = 0; i < pal.weights.length; i++) tot += pal.weights[i]; var x = h * tot; for (i = 0; i < pal.weights.length; i++) { x -= pal.weights[i]; if (x < 0) return pal.cells[i]; } return pal.cells[0]; }
  function cover(img, w, h, fy) { var iw = img.naturalWidth || img.width, ih = img.naturalHeight || img.height, s = Math.max(w / iw, h / ih), sw = w / s, sh = h / s; return [(iw - sw) / 2, (ih - sh) * (fy == null ? 0.25 : fy), sw, sh]; }
  var small = document.createElement("canvas");
  /* render one frame. o: {to, from?, p 0..1, size|w,h, cell (css px, default 28), theme, radius, focusY, redCell (default true)}; t seconds drives the churn flicker (10 fps steps). */
  function render(canvas, o, t) {
    var w = o.w || o.size || 360, h = o.h || o.size || w, dpr = Math.min(3, o.dpr || (window.devicePixelRatio || 1) * (o.scale || 1));
    if (canvas.width !== Math.round(w * dpr)) { canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr); }
    canvas.style.width = w * (o.scale || 1) + "px"; canvas.style.height = h * (o.scale || 1) + "px";
    var ctx = canvas.getContext("2d"), pal = PAL[isInk(canvas, o.theme) ? "ink" : "paper"], cell = o.cell || 28, p = clamp(o.p == null ? 1 : o.p);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, w, h); ctx.save();
    var r = o.radius || 0; ctx.beginPath(); if (r && ctx.roundRect) ctx.roundRect(0, 0, w, h, r); else ctx.rect(0, 0, w, h); ctx.clip();
    ctx.fillStyle = pal.bg; ctx.fillRect(0, 0, w, h);
    var cols = Math.ceil(w / cell), rows = Math.ceil(h / cell), tick = Math.floor((t || 0) * 10);
    var to = o.to, from = o.from, ctoS = to && cover(to, w, h, o.focusY), cfrS = from && cover(from, w, h, o.focusY), low = null;
    if (to && p > 0.4 && p < 1) { small.width = cols; small.height = rows; var sc = small.getContext("2d"); sc.imageSmoothingEnabled = true; sc.drawImage(to, ctoS[0], ctoS[1], ctoS[2], ctoS[3], 0, 0, cols, rows); low = small; }
    var red = o.redCell === false ? -1 : Math.floor(hash(tick, 7, 3) * cols * rows);
    for (var j = 0; j < rows; j++) for (var i = 0; i < cols; i++) {
      var x = i * cell, y = j * cell, cw = Math.min(cell, w - x), ch = Math.min(cell, h - y), id = j * cols + i;
      var rv = 0.55 * hash(i, j, 1) + 0.45 * ((i / cols + j / rows) / 2);
      var leave = 0.25 * rv, arrive = 0.45 + 0.45 * rv, mode = "churn";
      if (from && p < leave) mode = "from"; else if (to && p >= arrive + 0.1) mode = "to"; else if (to && p >= arrive) mode = "pix";
      if (mode === "to" || mode === "from") {
        var im = mode === "to" ? to : from, s = mode === "to" ? ctoS : cfrS, k = s[2] / w;
        ctx.drawImage(im, s[0] + x * k, s[1] + y * k, cw * k, ch * k, x, y, cw, ch);
      } else if (mode === "pix") {
        ctx.imageSmoothingEnabled = false; ctx.drawImage(low, i, j, 1, 1, x, y, cw, ch);
      } else {
        var on = hash(i, j, tick) > 0.18;
        if (on) { ctx.fillStyle = id === red ? SIGNAL : pick(pal, hash(i, j, tick + 11)); ctx.fillRect(x, y, cw, ch); }
      }
    }
    ctx.restore();
  }
  var cache = {};
  function load(u) { return cache[u] || (cache[u] = new Promise(function (res, rej) { var im = new Image(); im.onload = function () { res(im); }; im.onerror = rej; im.src = u; })); }
  /* mount: image 0 generates from the mosaic, then every cycle swaps to the next image through the mosaic. seconds. */
  function mount(canvas, o) {
    o = Object.assign({ size: 360, cell: 28, theme: "auto", generate: 3, swap: 3.2, hold: 1.6 }, o || {});
    var imgs = [], raf = 0, alive = true, t0 = performance.now() / 1e3;
    Promise.all((o.images || []).map(load)).then(function (a) { imgs = a; t0 = performance.now() / 1e3; });
    function loop() {
      if (!alive) return; var t = performance.now() / 1e3 - t0;
      if (imgs.length) {
        var n = 0, u = t, D = o.generate;
        while (u >= D + o.hold) { u -= D + o.hold; n++; D = o.swap; }
        render(canvas, Object.assign({}, o, { to: imgs[n % imgs.length], from: n > 0 ? imgs[(n - 1) % imgs.length] : null, p: Math.min(1, u / D) }), t);
      }
      raf = requestAnimationFrame(loop);
    }
    loop();
    return { set: function (p) { Object.assign(o, p); }, destroy: function () { alive = false; cancelAnimationFrame(raf); } };
  }
  window.RishiImageFX = { render: render, load: load, mount: mount, SIGNAL: SIGNAL };
})();
