"""Build R003 (McKinsey hourly rates) v2 as native Tesseract layers.

Writes .tesseract-work/media-layers.json (Image/Audio layers for checkout/commit),
.tesseract-work/sfx-assets.json (sound files to import) and .tesseract-work/edits.json
(action batch: shapes, text, text animators, blur effects, keyframes).
All timings come from vo-words.json (whisper word offsets of the supplied voiceover).
"""
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
FONTS = os.path.join(_studio_root(), "01. Styles/IG Motion Explainer/gradnext-design-system/fonts")
BRAND = os.path.join(_studio_root(), "01. Styles/IG Motion Explainer/_brand-build")
END_MS = 47500
VO_MS = 45792

# ---- gradnext tokens -------------------------------------------------------
def hx(h, a=1.0):
    h = h.lstrip("#"); return [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)] + [a]
RHINO, RHINO500, RHINO600 = hx("2E3558"), hx("5961ED"), hx("363EA7")
PERI, PERI600, PERI100, WHITE = hx("8C9DFF"), hx("5972FF"), hx("DEE3FF"), hx("FFFFFF")

HEAVY = ("Avenir LT Pro 55 Roman", "Bold", "AvenirLTProHeavy.otf")
BLACK = ("Avenir LT Pro 65 Medium", "Bold", "AvenirLTProBlack.otf")
MEDIUM = ("Avenir LT Pro 65 Medium", "Regular", "AvenirLTProMedium.otf")
SERIF = ("Besley", "Italic", os.path.join(BRAND, "Besley-Italic[wght].ttf"))

def text_w(font, size, s, tracking=0):
    path = font[2] if os.path.isabs(font[2]) else os.path.join(FONTS, font[2])
    out = subprocess.run(["magick", "-font", path, "-pointsize", str(size), "label:" + s,
                          "-trim", "-format", "%w", "info:"], capture_output=True, text=True)
    return int(out.stdout.strip()) + tracking / 1000 * size * (len(s) - 1)

# ---- easing ----------------------------------------------------------------
IO = (0.4, 0, 0.2, 1)          # ease in-out: brisk start, long soft settle (bars, slides)
OUT = (0.22, 1, 0.36, 1)       # quick ease-out (fades)
EXIT = (0.55, 0, 1, 0.45)      # ease-in for exits
SPR = (0.34, 1.3, 0.64, 1)     # gentle spring (re-sorts)
def bz(e): return {"type": "cubicBezier", "x1": e[0], "y1": e[1], "x2": e[2], "y2": e[3]}
LIN, HOLD = {"type": "linear"}, {"type": "hold"}
JS_BZ = ("function bz(a,b,c,d,x){if(x<=0)return 0;if(x>=1)return 1;var t=x;for(var i=0;i<10;i++){"
         "var u=1-t,X=3*a*t*u*u+3*c*t*t*u+t*t*t-x,dX=3*a*u*u+6*(c-a)*t*u+3*(1-c)*t*t;"
         "if(Math.abs(dX)<1e-6)break;t=Math.max(0,Math.min(1,t-X/dX));}var u=1-t;"
         "return 3*b*t*u*u+3*d*t*t*u+t*t*t;}")

actions, _id = [], [0]
def nid():
    _id[0] += 1; return _id[0]
_item = [1000]
def iid():
    _item[0] += 1; return _item[0]

def T(pos=(0, 0), anchor=(0, 0), scale=100, opacity=100):
    return {"anchorPoint": list(anchor), "position": list(pos), "scale": [scale, scale], "rotation": 0, "opacity": opacity}

FULL = {"start": 0, "duration": END_MS}

def group(name, parent=None, pos=(0, 0), anchor=(0, 0), insert=0):
    i = nid()
    actions.append({"type": "createFxGroupLayer", "compositionId": "main", "layerId": i, "name": name,
                    "parentLayerId": parent, "insertIndex": insert, "activeRange": FULL, "transform": T(pos, anchor)})
    return i

def rect(name, size, color, pos, parent=None, anchor=(0, 0), roundness=0, paint=None, insert=0):
    i = nid()
    r = {"size": list(size), "fillColor": color, "roundness": roundness}
    if paint: r["fillPaint"] = paint
    actions.append({"type": "createFxRectLayer", "compositionId": "main", "layerId": i, "name": name,
                    "parentLayerId": parent, "insertIndex": insert, "activeRange": FULL,
                    "transform": T(pos, anchor), "rect": r})
    return i

def lin_grad(x0, x1, stops):
    return {"type": "gradient", "gradientType": "linear", "start": [x0, 0], "end": [x1, 0],
            "stops": [{"offset": o, "color": c} for o, c in stops]}

def text(name, s, font, size, color, pos, parent=None, box=None, just="left", tracking=None,
         rng=FULL, words=None, dy=42, blur=18, word_dur=0.42):
    """words: reveal times (s, layer clock), one per space-separated word, in order.
    Each word slides up from below, sharpens out of a blur and fades in."""
    i = nid()
    st = {"text": s, "fontFamily": font[0], "fontStyle": font[1], "fontSize": size, "fillColor": color,
          "justification": just}
    if tracking is not None: st["tracking"] = tracking
    if box: st.update({"boxText": True, "boxPosition": [0, 0], "boxSize": list(box)})
    act = {"type": "createFxTextLayer", "compositionId": "main", "layerId": i, "name": name,
           "parentLayerId": parent, "insertIndex": 0, "activeRange": rng, "transform": T(pos), "sourceText": st}
    actions.append(act)
    if words is not None:
        aid, sid = iid(), iid()
        act["animators"] = [{"id": aid, "name": "Word reveal", "position": [0, dy], "opacity": 0, "blur": [blur, blur],
                             "selectors": [{"id": sid, "start": 0, "end": 999, "units": "index", "basedOn": "words",
                                            "mode": "add", "amount": 1, "shape": "square"}]}]
        tl = json.dumps([round(t, 3) for t in words])
        actions.append({"type": "setFxAnimator", "compositionId": "main",
                        "target": {"type": "styleProperty", "layerId": i, "itemId": sid, "propertyName": "start"},
                        "animator": {"type": "jsScript", "layerTimeJsCode":
                            JS_BZ + f"var W={tl},t=input.time.seconds,s=0;for(var i=0;i<W.length;i++)"
                            f"s+=bz({IO[0]},{IO[1]},{IO[2]},{IO[3]},(t-W[i])/{word_dur});return s;"},
                        "dependencies": []})
    return i

_k = [0]
def keys(layer, prop, pts, vtype="float"):
    """pts: list of (ms, value, easing tuple or dict)."""
    kf = []
    for ms, v, e in pts:
        _k[0] += 1
        kf.append({"id": f"k{_k[0]}", "layerTime": int(ms), "value": {"type": vtype, "value": v},
                   "easing": bz(e) if isinstance(e, tuple) else e})
    actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main",
                    "property": {"layerId": layer, "propertyType": prop}, "keyframes": kf})

def js(layer, prop, code):
    actions.append({"type": "setFxPropertyAnimator", "compositionId": "main",
                    "property": {"layerId": layer, "propertyType": prop},
                    "animator": {"type": "jsScript", "layerTimeJsCode": code}, "dependencies": []})

def blur_fx(layer, segs, start=0):
    """Gaussian blur on a layer's rendered output. segs: (t_ms, dur_ms, from_px, to_px, ease)."""
    eid = iid()
    actions.append({"type": "addFxLayerEffect", "compositionId": "main", "layerId": layer, "effectId": eid,
                    "effect": {"type": "gaussianBlur", "blurriness": 0}})
    S = json.dumps([[t / 1000, d / 1000, a, b, list(e)] for t, d, a, b, e in segs])
    actions.append({"type": "setFxAnimator", "compositionId": "main",
                    "target": {"type": "effectParameter", "layerId": layer, "effectId": eid, "paramName": "blurriness"},
                    "animator": {"type": "jsScript", "layerTimeJsCode":
                        JS_BZ + f"var S={S},t=input.time.seconds,v={start};for(var i=0;i<S.length;i++){{var g=S[i];"
                        "if(t<g[0])break;var e=g[4];v=g[2]+(g[3]-g[2])*bz(e[0],e[1],e[2],e[3],(t-g[0])/g[1]);}"
                        "return Math.max(0,v);"},
                    "dependencies": []})

def motion(layer, base, t_in=None, t_out=None, axis="Y", d_in=46, d_out=-36, dur_in=650, dur_out=480,
           blur_in=26, blur_out=22):
    """Blur-slide entrance and exit: position + opacity keyframes and an animated gaussian blur."""
    o, p, b = [], [], []
    if t_in is not None:
        o += [(0, 0, LIN), (t_in, 0, LIN), (t_in + dur_in * 0.7, 100, OUT)]
        p += [(0, base + d_in, LIN), (t_in, base + d_in, LIN), (t_in + dur_in, base, IO)]
        b += [(t_in, dur_in, blur_in, 0, IO)]
    else:
        o += [(0, 100, LIN)]; p += [(0, base, LIN)]
    if t_out is not None:
        o += [(t_out, 100, LIN), (t_out + dur_out, 0, EXIT)]
        p += [(t_out, base, LIN), (t_out + dur_out, base + d_out, EXIT)]
        b += [(t_out, dur_out, 0, blur_out, EXIT)]
    keys(layer, "opacity", o)
    keys(layer, "position" + axis, p)
    blur_fx(layer, b, start=blur_in if t_in is not None else 0)

# ---- sound cues (every on-screen event except captions) --------------------
# Library and levels follow Minimal Edit Style SOUND_DESIGN.md (v1.1): lots of sound, each one quiet;
# a cue's peak (not its file start) lands on the visual event; target peak dBFS per role.
LIB = json.load(open(os.path.join(HERE, "sfx-library.json")))
sfx = []
_vary = [0, -1.5, 1, -0.5, 1.5, -1]
_vn = [0]
def cue(kind, t_ms, target_db):
    f = LIB[kind]
    if kind == "flick":                       # per-word ticks vary +-2 dB so they never sound mechanical
        target_db += _vary[_vn[0] % len(_vary)]; _vn[0] += 1
    lift = 3 if t_ms < 5000 else (3 * (6000 - t_ms) / 1000 if t_ms < 6000 else 0)   # opening lift
    vol = 10 ** ((target_db + lift - f["peak_db"]) / 20)
    sfx.append([kind, t_ms - f["peak_ms"], vol, t_ms, target_db])
def flicks(times_s, db=-28):
    for t in times_s: cue("flick", t * 1000 + 40, db)

# ---- background: the supplied gradnext loop (Video layers, see media section) ----

# ---- headlines: line by line, blur-slide in and out ------------------------
def headline(name, l1, l2, t_in, t_out, y=470):
    a = text(name + " / sans", l1, HEAVY, 70, RHINO, (80, y), tracking=-40)
    b = text(name + " / serif", l2, SERIF, 76, RHINO500, (80, y + 88))
    motion(a, y, t_in, t_out)
    motion(b, y + 88, t_in + 160, t_out + 90)
    cue("hitech", t_in + 120, -17); cue("flick", t_in + 160 + 120, -27)

headline("Headline hook", "What a McKinsey partner", "bills per hour", 150, 4300)
headline("Headline rate card", "The most each level", "can bill an hour", 4750, 12700)
headline("Headline team week", "One week of a", "five-person team", 13050, 28600)
headline("Headline junior", "A 2020 price for", "one junior consultant", 28950, 38500)

# ---- hook: dropping count-up, highlighter, word-by-word sub ----------------
hook = group("Hook")
NUM_SIZE, NUM_BASE = 230, 930
w_num = text_w(BLACK, NUM_SIZE, "$1,000", -40)
w_all = text_w(BLACK, NUM_SIZE, "$1,000+", -40)
x0 = round((1080 - w_all) / 2)
CAP = 0.72 * NUM_SIZE
hl_h, hl_top = round(CAP * 0.34) + 12, round(NUM_BASE - CAP * 0.34)
hl_w = round(w_all + 18)
hl = rect("Hook highlighter", (0, hl_h), PERI, (x0 - 10, hl_top), parent=hook, roundness=3,
          paint=lin_grad(0, hl_w, [(0, PERI[:3] + [0.95]), (w_num / hl_w, PERI[:3] + [0.9]), (1, PERI[:3] + [0])]))
keys(hl, "rectSize", [(0, [0, hl_h], LIN), (2880, [0, hl_h], LIN), (3680, [hl_w, hl_h], IO)], "vector2")
keys(hl, "opacity", [(0, 0, HOLD), (2880, 100, HOLD)])   # a zero-width rounded rect still draws a hairline
num = text("Hook number", "$940", BLACK, NUM_SIZE, RHINO, (x0, NUM_BASE), parent=hook, tracking=-40)
js(num, "textContent", JS_BZ + "var t=input.time.seconds,p=bz(0.2,0.6,0.25,1,(t-0.35)/1.7),n=Math.round(940+60*p);"
   "var s=String(n);if(n>=1000)s=s.slice(0,1)+','+s.slice(1);return '$'+s;")
motion(num, NUM_BASE, 100, None, d_in=-130, dur_in=800, blur_in=40)
plus = text("Hook plus", "+", BLACK, NUM_SIZE, RHINO, (round(x0 + w_num + 4), NUM_BASE), parent=hook)
motion(plus, NUM_BASE, 2880, None, d_in=-70, dur_in=500, blur_in=30)
sub_words = [1.25, 1.42, 1.59, 1.76, 1.93]
text("Hook sub", "an hour, for one partner", MEDIUM, 46, RHINO, (0, 1000), parent=hook, box=(1080, 80),
     just="center", words=sub_words)
keys(hook, "opacity", [(0, 100, LIN), (4380, 100, LIN), (4900, 0, EXIT)])
keys(hook, "positionY", [(0, 0, LIN), (4380, 0, LIN), (4900, -70, EXIT)])
blur_fx(hook, [(4380, 520, 0, 30, EXIT)])
cue("hitech", 260, -17)
flicks([0.55, 0.72, 0.92, 1.15, 1.42, 1.75], -29)
flicks(sub_words, -28)
cue("popdiff", 2950, -19); cue("highlighter", 2900, -18)
cue("swoosh", 4500, -16)

# ---- the persistent chart --------------------------------------------------
SLOT = lambda i: 690 + i * 104
BAR_X, BAR_H, MAXW, BAR_R = 80, 44, 680, 8
RATE_SCALE = MAXW / 1586.56
WEEK_TOTAL = 10 * 1293.47 + 40 * 1016.61 + 120 * 612.13   # 127,054.70
WEEK_SCALE = MAXW / WEEK_TOTAL
BAR_DUR = 850
NAVY_GRAD = lin_grad(0, MAXW, [(0, RHINO), (1, RHINO600)])
WIPE_W, SOFT = 940, 90
PERI_WIPE = lin_grad(0, WIPE_W, [(0, PERI600[:3] + [0]), (SOFT / WIPE_W, PERI600), (0.62, PERI),
                                 ((WIPE_W - SOFT) / WIPE_W, PERI), (1, PERI[:3] + [0])])
WIPE_ON_X, WIPE_OFF_X = -SOFT, -WIPE_W - 120  # covering the bar / parked well clear of its left end

chart = group("Chart")

def fmt_js():
    return ("function f(n){n=Math.round(n);var s=String(n),o='';"
            "for(var i=0;i<s.length;i++){if(i>0&&(s.length-i)%3===0)o+=',';o+=s[i];}return '$'+o;}")

def row(name, labels, slots, phases, wipes, t_hide, peri_from_start=False):
    """labels: [(t_ms, text)] - shown words stay, new trailing words reveal one by one.
    slots: [(t_ms, slot)] re-sorts. phases: [(t_ms, dollars, scale)] bar/value moves.
    wipes: [(t_ms, 'on'|'off')] right-to-left periwinkle colour changes. t_hide: row exits."""
    g = group("Row " + name, parent=chart, pos=(0, SLOT(slots[0][1])))
    word_times, shown = [], 0
    for t, s in labels:
        n = len(s.split())
        for k in range(shown, n): word_times.append(t / 1000 + (k - shown) * 0.085)
        shown = n
    lab = text(name + " label", labels[0][1], MEDIUM, 34, RHINO, (BAR_X, 0), parent=g, words=word_times, dy=30, blur=14)
    if len(labels) > 1:
        keys(lab, "textContent", [(t, s, HOLD) for t, s in labels], "string")
    flicks(word_times, -28)
    # bar width (ease in-out), shared by the bar, its matte copy and the value text
    w_pts, x_pts, o_pts, prev = [(0, [0, BAR_H], LIN)], [(0, BAR_X + 18, LIN)], [(0, 0, HOLD)], 0
    for t, dollars, sc in phases:
        w = round(dollars * sc, 1)
        w_pts += [(t, [prev, BAR_H], LIN), (t + BAR_DUR, [w, BAR_H], IO)]
        x_pts += [(t, BAR_X + prev + 18, LIN), (t + BAR_DUR, BAR_X + w + 18, IO)]
        o_pts.append((t, 100, HOLD) if dollars > 0 else (t + BAR_DUR, 0, HOLD))
        prev = w
        if dollars > 0 and dollars != WEEK_TOTAL: cue("highlighter", t + 60, -20)
    # stacking (front to back): value, colour wipe, wipe matte (consumed), bar
    bar = rect(name + " bar", (0, BAR_H), RHINO, (BAR_X, 18), parent=g, roundness=BAR_R, paint=NAVY_GRAD)
    matte = rect(name + " bar matte", (0, BAR_H), RHINO, (BAR_X, 18), parent=g, roundness=BAR_R)
    for lyr in (bar, matte):
        keys(lyr, "rectSize", w_pts, "vector2"); keys(lyr, "opacity", o_pts)
    wipe = rect(name + " colour wipe", (WIPE_W, BAR_H), PERI, (BAR_X + WIPE_OFF_X, 18), parent=g, paint=PERI_WIPE)
    wx = [(0, BAR_X + (WIPE_ON_X if peri_from_start else WIPE_OFF_X), LIN)]
    for t, mode in wipes:
        if mode == "on":   # periwinkle enters at the right end and settles over the bar
            wx += [(t, BAR_X + MAXW + 20, HOLD), (t + 900, BAR_X + WIPE_ON_X, IO)]
            cue("highlighter", t + 80, -19)
        else:              # periwinkle recedes right to left, navy follows it in
            wx += [(t, BAR_X + WIPE_ON_X, LIN), (t + 900, BAR_X + WIPE_OFF_X, IO)]
            cue("highlighter", t + 80, -20)
    keys(wipe, "positionX", wx)
    actions.append({"type": "setFxLayerTrackMatte", "compositionId": "main", "layerId": wipe,
                    "matteLayerId": matte, "mode": "alpha"})
    val = text(name + " value", "", HEAVY, 38, RHINO, (BAR_X + 18, 56), parent=g)
    keys(val, "positionX", x_pts)
    ph = json.dumps([[t / 1000, BAR_DUR / 1000, dollars] for t, dollars, _ in phases])
    js(val, "textContent", JS_BZ + fmt_js() + f"var P={ph};var t=input.time.seconds,v=0,from=0;"
       f"for(var i=0;i<P.length;i++){{if(t<P[i][0])break;var p=bz({IO[0]},{IO[1]},{IO[2]},{IO[3]},(t-P[i][0])/P[i][1]);"
       "v=from+(P[i][2]-from)*p;from=P[i][2];}return (v<1||from===0)?'':f(v);")
    if len(slots) > 1:
        sp, prev_s = [(0, SLOT(slots[0][1]), LIN)], slots[0][1]
        for t, s_ in slots[1:]:
            sp += [(t, SLOT(prev_s), LIN), (t + 700, SLOT(s_), SPR)]; prev_s = s_
        keys(g, "positionY", sp)
    keys(g, "opacity", [(0, 100, LIN), (t_hide, 100, LIN), (t_hide + 420, 0, EXIT)])
    blur_fx(g, [(t_hide, 420, 0, 18, EXIT)])
    return g

R, W = RATE_SCALE, WEEK_SCALE
row_t = lambda i: 5000 + i * 230
row("Senior partner", [(row_t(0), "Senior partner")], [(0, 0)],
    [(row_t(0), 1586.56, R)], [(11170, "on")], 12960)
row("Partner", [(row_t(1), "Partner"), (16450, "Partner · 10 hours")],
    [(0, 1), (12960, 0), (23200, 1)],
    [(row_t(1), 1293.47, R), (12960, 0, R), (16450, 10 * 1293.47, W)], [], 28900)
row("Associate partner", [(row_t(2), "Associate partner")], [(0, 2)],
    [(row_t(2), 1133.41, R)], [], 12960)
row("Engagement manager", [(row_t(3), "Engagement manager"), (18720, "Engagement manager · 40 hours")],
    [(0, 3), (12960, 1), (23200, 2)],
    [(row_t(3), 1016.61, R), (12960, 0, R), (18720, 40 * 1016.61, W)], [], 28900)
row("Associate", [(row_t(4), "Associates"), (21010, "Associates · 3 people · 120 hours")],
    [(0, 4), (12960, 2), (23200, 3)],
    [(row_t(4), 612.13, R), (12960, 0, R), (21010, 120 * 612.13, W)], [], 28900)
row("Business analyst", [(row_t(5), "Business analyst")], [(0, 5)],
    [(row_t(5), 421.79, R)], [(7860, "on"), (10900, "off")], 12960)
row("Team week", [(23350, "Team week, at maximum rates")], [(0, 0)],
    [(23500, WEEK_TOTAL, W)], [(32660, "off")], 38500, peri_from_start=True)
row("Junior consultant", [(29900, "1 junior consultant · 2020")], [(0, 1)],
    [(32660, 67500, W)], [], 38500, peri_from_start=True)
cue("swoosh", 13050, -16)        # collapse + re-sort
cue("woosh", 23400, -18)         # re-sort for the total
cue("risertick", 23500 + BAR_DUR, -19)   # total bar lands
cue("swoosh", 29000, -16)        # collapse to total vs junior

# ---- caveat chips: slim, barely rounded --------------------------------------
chip_x = [80]
def chip(label, t_in):
    w = round(text_w(MEDIUM, 28, label)) + 40
    g = group("Chip " + label, pos=(chip_x[0], 1318))
    rect(label + " plate", (w, 50), PERI100, (0, 0), parent=g, roundness=6)
    text(label + " text", label, MEDIUM, 28, RHINO, (20, 35), parent=g)
    motion(g, 1318, t_in, 38500, d_in=30)
    cue("popdiff", t_in + 150, -19)
    chip_x[0] += w + 12
chip("Contract maximum", 5700)
chip("Derived", 23600)
chip("Reported", 32950)

# ---- $3.5 million callout: card slides in, then its words ------------------
card = group("Annual callout")
rect("Callout card", (920, 236), PERI100, (80, 952), parent=card, roundness=12)
fig_words = [36.05, 36.33, 36.62, 36.84, 37.02]
text("Callout figure", "≈ $3.5 million a year", BLACK, 76, RHINO, (80, 990), parent=card, box=(920, 100),
     just="center", tracking=-30, words=fig_words, dy=44, blur=20)
work_words = [37.3, 37.44, 37.58, 37.72, 37.86, 38.0]
text("Callout working", "$67,500 a week × 52 weeks", MEDIUM, 36, RHINO, (80, 1105), parent=card, box=(920, 60),
     just="center", words=work_words, dy=30, blur=14)
motion(card, 0, 35500, 38500, axis="X", d_in=260, d_out=0, dur_in=750, blur_in=34)
cue("woosh", 35800, -17)
cue("hitech", fig_words[1] * 1000 + 60, -17); flicks(fig_words[:1] + fig_words[2:], -28); flicks(work_words, -29)

# ---- takeaway: tighter tracking and leading --------------------------------
tk_lead = [38.72, 38.88, 39.12, 39.45, 40.11, 40.37, 40.6]
tk_a = [41.36, 41.6, 41.97]
tk_b = [42.43, 42.75, 43.0]
tk = [
    text("Takeaway lead", "So the real question for any client:", MEDIUM, 44, RHINO, (0, 724), box=(1080, 70),
         just="center", tracking=-15, words=tk_lead, dy=30, blur=14),
    text("Takeaway sans", "Is the team", HEAVY, 118, RHINO, (0, 790), box=(1080, 140), just="center",
         tracking=-55, words=tk_a, dy=50, blur=22),
    text("Takeaway serif", "worth the price?", SERIF, 124, RHINO500, (0, 908), box=(1080, 160), just="center",
         tracking=-30, words=tk_b, dy=50, blur=22),
]
flicks(tk_lead, -29); cue("hitech", tk_a[0] * 1000 + 60, -17); flicks(tk_a[1:] + tk_b, -27)
for lid in tk:
    keys(lid, "opacity", [(0, 100, LIN), (43350, 100, LIN), (43750, 0, EXIT)])
    blur_fx(lid, [(43350, 400, 0, 18, EXIT)])
cue("swoosh", 43500, -16)

# ---- closing card: words, then a half-height highlighter -------------------
cl_a, cl_b = [43.76, 44.13, 44.31], [44.71, 45.16]
CL_SERIF, CL_BASE = 108, 985
w_ci = text_w(SERIF, CL_SERIF, "consulting insights", -20)
ci_x = round((1080 - w_ci) / 2)
xh = 0.5 * CL_SERIF
cl_hl_h = round(xh * 0.58) + 10
cl_hl_w = round(w_ci + 24)
cl_hl = rect("Closing highlighter", (0, cl_hl_h), PERI, (ci_x - 12, round(CL_BASE - xh * 0.5)), roundness=3,
             paint=lin_grad(0, cl_hl_w, [(0, PERI[:3] + [0.92]), (0.78, PERI[:3] + [0.88]), (1, PERI[:3] + [0])]))
keys(cl_hl, "rectSize", [(0, [0, cl_hl_h], LIN), (45450, [0, cl_hl_h], LIN), (46250, [cl_hl_w, cl_hl_h], IO)], "vector2")
keys(cl_hl, "opacity", [(0, 0, HOLD), (45450, 100, HOLD)])
text("Closing sans", "Follow for more", HEAVY, 100, RHINO, (0, CL_BASE - 232), box=(1080, 130), just="center",
     tracking=-50, words=cl_a, dy=50, blur=22)
text("Closing serif", "consulting insights", SERIF, CL_SERIF, RHINO, (0, CL_BASE - CL_SERIF - 6), box=(1080, 150),
     just="center", tracking=-20, words=cl_b, dy=50, blur=22)
cue("hitech", cl_a[0] * 1000 + 60, -17); flicks(cl_a[1:] + cl_b, -27)
cue("highlighter", 45500, -18)
cue("techpop", 46100, -21)   # closing wordmark lands

# ---- captions: word by word, sliding up out of a blur (no sound) -----------
words = [(s["offsets"]["from"], s["offsets"]["to"], s["text"].strip())
         for s in json.load(open(os.path.join(HERE, "vo-words.json")))["transcription"] if s["text"].strip()]
phrases, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    nxt = words[i + 1] if i + 1 < len(words) else None
    if re.search(r"[.,?]$", w[2]) or nxt is None or nxt[0] - w[1] > 450:
        phrases.append(cur); cur = []
chunks = []
for ph in phrases:
    n = 1
    while True:
        size = -(-len(ph) // n)
        parts = [ph[i:i + size] for i in range(0, len(ph), size)]
        if all(len(p) <= 4 and len(" ".join(x[2] for x in p)) <= 24 for p in parts): break
        n += 1
    chunks += parts
fixed = []
for ch in chunks:
    if len(ch) == 1 and fixed and ch[0][0] - fixed[-1][-1][1] < 450 and not re.search(r"[.?]$", fixed[-1][-1][2]):
        prev = fixed[-1]
        if len(prev) <= 3 and len(" ".join(x[2] for x in prev + ch)) <= 24:
            fixed[-1] = prev + ch; continue
        if len(prev) >= 3:
            fixed[-1] = prev[:-1]; ch = prev[-1:] + ch
    fixed.append(ch)
chunks = fixed
cap_g = group("Captions")
CAP_END = 43700
for n, ch in enumerate(chunks):
    start = max(ch[0][0], 1000)
    nxt_start = chunks[n + 1][0][0] if n + 1 < len(chunks) else ch[-1][1] + 400
    end = min(nxt_start if nxt_start - ch[-1][1] < 900 else ch[-1][1] + 400, CAP_END)
    if end - start < 200: continue
    s = re.sub(r"[.,]$", "", " ".join(w[2] for w in ch))
    wt = [max(0, (w[0] - start) / 1000) for w in ch]
    text(f"Caption {n+1}", s, HEAVY, 54, RHINO, (90, 1440), parent=cap_g, box=(900, 80), just="center",
         rng={"start": int(start), "duration": int(end - start)}, words=wt, dy=26, blur=12, word_dur=0.28)

# ---- media layers (wordmarks, dots, audio) for checkout/commit -------------
media_ids = iter(range(5000, 9000))
def audio(name, asset, start_ms, dur, vol):
    return {"id": next(media_ids), "name": name, "type": "Audio",
            "playback": {"type": "windowed", "inputRange": {"start": int(max(0, start_ms)), "duration": dur},
                         "mapping": {"type": "linear", "input": {"start": int(max(0, start_ms)), "duration": dur},
                                     "output": {"start": 0, "duration": dur}}, "inputOffsetMs": 0},
            "sourceRange": {"start": 0, "duration": dur}, "sourceIntrinsicDuration": dur,
            "source": {"assetId": asset}, "volume": round(vol, 3), "captionsEnabled": False}
WM_W = 1174
wm_head, wm_close = next(media_ids), next(media_ids)
media = [
    {"type": "Image", "id": wm_head, "name": "Wordmark header", "blendMode": "normal",
     "activeRange": {"start": 0, "duration": 43900},
     "transform": T((1000, 300), (WM_W, 0), scale=15), "source": {"assetId": "wordmark-rhino", "fit": "contain"}},
    {"type": "Image", "id": wm_close, "name": "Wordmark closing", "blendMode": "normal",
     "activeRange": {"start": 0, "duration": END_MS},
     "transform": T((540, 1080), (WM_W / 2, 0), scale=26), "source": {"assetId": "wordmark-rhino", "fit": "contain"}},
    audio("Voiceover", "vo", 0, VO_MS, 1.0),
]
durs = {}
for f in sorted(os.listdir(os.path.join(HERE, "sfx"))):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          os.path.join(HERE, "sfx", f)], capture_output=True, text=True)
    durs[f[:-4]] = int(float(out.stdout) * 1000)
# one family per moment: drop a cue within 110 ms of a louder one
kept = [c for c in sfx if not any(o is not c and abs(o[3] - c[3]) < 110 and o[4] > c[4] for o in sfx)]
for name, t, vol, at, db in sorted(kept, key=lambda x: x[1]):
    media.append(audio("SFX " + name, "sfx-" + name, t, durs[name], vol))
with open(os.path.join(HERE, "sound_cue_sheet.md"), "w") as fh:
    fh.write("# R003 sound cue sheet\n\nSource: Minimal Edit Style sfx library, levels per its SOUND_DESIGN.md.\n\n"
             "| Time (s) | Sound | Target peak (dBFS) |\n|---|---|---|\n")
    for name, t, vol, at, db in sorted(kept, key=lambda x: x[3]):
        fh.write(f"| {at/1000:.2f} | {name} | {db:+.1f} |\n")
# background: the supplied 5 s gradnext loop, tiled back to back behind everything
BG_MS = 5000
for k in range(0, END_MS, BG_MS):
    d = min(BG_MS, END_MS - k)
    media.append({"type": "Video", "id": next(media_ids), "name": f"Background loop {k // BG_MS + 1}",
                  "playback": {"type": "windowed", "inputRange": {"start": k, "duration": d},
                               "mapping": {"type": "linear", "input": {"start": k, "duration": d},
                                           "output": {"start": 0, "duration": d}}, "inputOffsetMs": 0},
                  "sourceRange": {"start": 0, "duration": d}, "sourceIntrinsicDuration": BG_MS,
                  "transform": T(), "source": {"assetId": "bg-loop", "fit": "cover",
                                               "sourceRect": {"x": 0, "y": 0, "width": 1080, "height": 1920}}})
json.dump(media, open(os.path.join(HERE, "media-layers.json"), "w"), indent=1)
json.dump(sorted(durs), open(os.path.join(HERE, "sfx-assets.json"), "w"))

# media-layer motion, applied in the same action batch after the commit
keys(wm_head, "opacity", [(0, 100, LIN), (43350, 100, LIN), (43750, 0, LIN)])
keys(wm_close, "opacity", [(0, 0, LIN), (45900, 0, LIN), (46350, 100, OUT)])
keys(wm_close, "positionY", [(0, 1120, LIN), (45900, 1120, LIN), (46500, 1080, IO)])
blur_fx(wm_close, [(45900, 600, 24, 0, IO)], start=24)

json.dump(actions, open(os.path.join(HERE, "edits.json"), "w"), indent=1, ensure_ascii=False)
print(len(actions), "actions;", len(chunks), "captions;", len(sfx), "sfx cues;", len(media), "media layers")
