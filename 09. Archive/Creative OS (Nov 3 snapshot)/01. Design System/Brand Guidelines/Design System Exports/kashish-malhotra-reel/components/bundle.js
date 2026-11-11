/* @ds-bundle: {"format":4,"namespace":"KMReel","components":[{"name":"RisingCaption"}]} */
(function () {
  var clamp01 = function (x) { return x < 0 ? 0 : x > 1 ? 1 : x; };
  var seg = function (t, a, b) { return clamp01((t - a) / (b - a)); };
  var ease = function (x) { return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  var lerp = function (a, b, p) { return a + (b - a) * p; };

  // timings, in seconds: the same values as the timing tokens
  var T = { lead: 0.12, rise: 0.32, swap: 0.18, morph: 0.32, pillIn: 0.28, pillOut: 0.22, hold: 0.45, joinGap: 0.6, breakGap: 0.35, maxChars: 20 };
  var PX = { rise: 64, exit: 46, padX: 42, maxLine: 880, font: 58 };

  function parseTime(s) { var p = s.trim().split(':'); var r = p[2].split(','); return (+p[0]) * 3600 + (+p[1]) * 60 + (+r[0]) + (+r[1]) / 1000; }

  // SRT text -> [{w, t, e, hl}]: each cue's time shared across its words by length
  function wordsFromSrt(srt, fixes) {
    fixes = fixes || {};
    var words = [];
    srt.replace(/\r/g, '').trim().split(/\n\s*\n/).forEach(function (blk) {
      var L = blk.trim().split('\n'); if (L.length < 3) return;
      var ab = L[1].split('-->'), a = parseTime(ab[0]), b = parseTime(ab[1]);
      var ws = L.slice(2).join(' ').trim().split(/\s+/).map(function (w) { return fixes[w] || w; });
      var tot = 0; ws.forEach(function (w) { tot += w.length + 1; });
      var acc = 0;
      ws.forEach(function (w) {
        var st = a + (b - a) * acc / tot; acc += w.length + 1;
        words.push({ w: w, t: st, e: a + (b - a) * acc / tot, hl: /[0-9%]/.test(w) });
      });
    });
    return words;
  }

  // words -> phrases: break after . ? !, after a comma once 2+ words, at ~20 characters, or at a pause
  function phrasesFromWords(words, end) {
    var out = [], cur = [];
    words.forEach(function (w) {
      if (cur.length) {
        var prev = cur[cur.length - 1], chars = 0;
        cur.forEach(function (x) { chars += x.w.length + 1; }); chars += w.w.length;
        var gap = w.t - prev.e, last = prev.w.slice(-1);
        var keepTail = /[.?!,]$/.test(w.w) && chars <= 26 && gap < 0.2;
        if (/[.?!]/.test(last) || (last === ',' && cur.length >= 2) || (chars > T.maxChars && !keepTail) || gap > T.breakGap) { out.push(cur); cur = []; }
      }
      cur.push(w);
    });
    if (cur.length) out.push(cur);
    return out.map(function (p, i) {
      var o = { t0: p[0].t, end: p[p.length - 1].e, words: p };
      var next = out[i + 1] ? out[i + 1][0].t : null;
      if (next !== null && next - o.end < T.joinGap) { o.hide = next; o.join = true; }
      else if (next === null) { o.hide = end != null ? end + 1 : o.end + 999; o.join = false; }
      else { o.hide = next - o.end > 0.9 ? o.end + T.hold : (o.end + next) / 2; o.join = false; }
      return o;
    });
  }

  // build the caption layer inside `host` (a 1080x1920 stage); returns render(T)
  function mount(host, phrases, opts) {
    opts = opts || {};
    var doc = host.ownerDocument;
    var layer = doc.createElement('div'); layer.className = 'kmr-cap';
    var pill = doc.createElement('div'); pill.className = 'kmr-cap-pill';
    var clip = doc.createElement('div'); clip.className = 'kmr-cap-clip';
    layer.appendChild(pill); layer.appendChild(clip); host.appendChild(layer);
    var ph = phrases.map(function (p) {
      var line = doc.createElement('div'); line.className = 'kmr-cap-line';
      p.words.forEach(function (w) { var s = doc.createElement('span'); s.className = 'kmr-cap-w' + (w.hl ? ' kmr-cap-hl' : ''); s.textContent = w.w; line.appendChild(s); });
      clip.appendChild(line);
      var wd = line.offsetWidth;
      if (wd > PX.maxLine) { line.style.fontSize = (PX.font * PX.maxLine / wd).toFixed(2) + 'px'; wd = line.offsetWidth; }
      line.style.opacity = 0;
      return { p: p, line: line, wd: wd, ws: Array.prototype.map.call(line.children, function (x) { return x.style; }) };
    });
    return function render(t) {
      var cur = null, prev = null;
      for (var i = 0; i < ph.length; i++) if (ph[i].p.t0 - T.lead <= t) { prev = cur; cur = ph[i]; }
      ph.forEach(function (q) { if (q !== cur && q !== prev) q.line.style.opacity = 0; });
      if (!cur || t >= cur.p.hide) { pill.style.opacity = 0; if (cur) cur.line.style.opacity = 0; if (prev) prev.line.style.opacity = 0; return; }
      var joined = prev && prev.p.join && prev.p.hide >= cur.p.t0 - 0.01;
      var app = joined ? 1 : ease(seg(t, cur.p.t0 - 0.16, cur.p.t0 + 0.12));
      var dis = cur.p.join ? 0 : ease(seg(t, cur.p.hide - T.pillOut, cur.p.hide));
      var wp = joined ? ease(seg(t, cur.p.t0 - 0.12, cur.p.t0 + 0.2)) : 1;
      pill.style.width = (lerp(joined ? prev.wd : cur.wd, cur.wd, wp) + 2 * PX.padX).toFixed(1) + 'px';
      pill.style.opacity = app * (1 - dis);
      pill.style.transform = 'translateX(-50%) scale(' + lerp(0.94, 1, app) * lerp(1, 0.96, dis) + ')';
      if (prev) {
        var x = joined ? ease(seg(t, cur.p.t0 - 0.12, cur.p.t0 + 0.06)) : 1;
        prev.line.style.opacity = 1 - x;
        prev.line.style.transform = 'translateX(-50%) translateY(' + (-PX.exit * x) + 'px)';
      }
      cur.line.style.opacity = 1 - dis;
      cur.line.style.transform = 'translateX(-50%)';
      cur.p.words.forEach(function (w, j) {
        var p = ease(seg(t, w.t - T.lead, w.t - T.lead + T.rise));
        cur.ws[j].opacity = Math.min(1, p * 1.5);
        cur.ws[j].transform = 'translateY(' + ((1 - p) * PX.rise).toFixed(2) + 'px)';
      });
    };
  }

  window.KMReel = {
    RisingCaption: { timing: T, sizes: PX, wordsFromSrt: wordsFromSrt, phrasesFromWords: phrasesFromWords, mount: mount },
  };
})();
