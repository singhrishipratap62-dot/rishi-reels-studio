"""Build R003 (McKinsey hourly rates) as native Tesseract layers.

Writes .tesseract-work/media-layers.json (Image/Audio layers for checkout/commit)
and .tesseract-work/edits.json (action batch for shapes, text and animation).
Timings come from vo-words.json (whisper word offsets of the supplied voiceover).
"""
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
FONTS = os.path.join(_studio_root(), "01. Styles/IG Motion Explainer/gradnext-design-system/fonts")
END_MS = 47500
VO_MS = 45792

# ---- gradnext tokens -------------------------------------------------------
def hx(h, a=1.0):
    h = h.lstrip("#"); return [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)] + [a]
RHINO, PERI, PERI100, RHINO500, WHITE = hx("2E3558"), hx("8C9DFF"), hx("DEE3FF"), hx("5961ED"), hx("FFFFFF")

HEAVY = ("Avenir LT Pro 55 Roman", "Bold", "AvenirLTProHeavy.otf")
BLACK = ("Avenir LT Pro 65 Medium", "Bold", "AvenirLTProBlack.otf")
MEDIUM = ("Avenir LT Pro 65 Medium", "Regular", "AvenirLTProMedium.otf")
FUTURA = ("Futura-Bold", "Regular", "Futura Bold.ttf")
SERIF = ("Besley", "Italic", None)

def text_w(font, size, s):
    out = subprocess.run(["magick", "-font", os.path.join(FONTS, font[2]), "-pointsize", str(size),
                          "label:" + s, "-format", "%w", "info:"], capture_output=True, text=True)
    return int(out.stdout.strip())

EASE_OUT = {"type": "cubicBezier", "x1": 0.22, "y1": 1, "x2": 0.36, "y2": 1}
SPRING = {"type": "cubicBezier", "x1": 0.34, "y1": 1.35, "x2": 0.64, "y2": 1}
LIN = {"type": "linear"}
HOLD = {"type": "hold"}

actions, _id = [], [0]
def nid():
    _id[0] += 1; return _id[0]

def T(pos=(0, 0), anchor=(0, 0), scale=100, opacity=100):
    return {"anchorPoint": list(anchor), "position": list(pos), "scale": [scale, scale], "rotation": 0, "opacity": opacity}

FULL = {"start": 0, "duration": END_MS}

def group(name, parent=None, pos=(0, 0), anchor=(0, 0)):
    i = nid()
    actions.append({"type": "createFxGroupLayer", "compositionId": "main", "layerId": i, "name": name,
                    "parentLayerId": parent, "insertIndex": 0, "activeRange": FULL, "transform": T(pos, anchor)})
    return i

def rect(name, size, color, pos, parent=None, anchor=(0, 0), roundness=0, paint=None, insert=0, rng=FULL):
    i = nid()
    r = {"size": list(size), "fillColor": color, "roundness": roundness}
    if paint: r["fillPaint"] = paint
    actions.append({"type": "createFxRectLayer", "compositionId": "main", "layerId": i, "name": name,
                    "parentLayerId": parent, "insertIndex": insert, "activeRange": rng,
                    "transform": T(pos, anchor), "rect": r})
    return i

def text(name, s, font, size, color, pos, parent=None, box=None, just="left", tracking=None, rng=FULL):
    i = nid()
    st = {"text": s, "fontFamily": font[0], "fontStyle": font[1], "fontSize": size, "fillColor": color,
          "justification": just}
    if tracking is not None: st["tracking"] = tracking
    if box:
        st.update({"boxText": True, "boxPosition": [0, 0], "boxSize": list(box)})
    actions.append({"type": "createFxTextLayer", "compositionId": "main", "layerId": i, "name": name,
                    "parentLayerId": parent, "insertIndex": 0, "activeRange": rng,
                    "transform": T(pos), "sourceText": st})
    return i

_k = [0]
def keys(layer, prop, pts, vtype="float"):
    """pts: list of (ms, value, easing)."""
    kf = []
    for ms, v, e in pts:
        _k[0] += 1
        kf.append({"id": f"k{_k[0]}", "layerTime": int(ms), "value": {"type": vtype, "value": v}, "easing": e})
    actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main",
                    "property": {"layerId": layer, "propertyType": prop}, "keyframes": kf})

def js(layer, prop, code):
    actions.append({"type": "setFxPropertyAnimator", "compositionId": "main",
                    "property": {"layerId": layer, "propertyType": prop},
                    "animator": {"type": "jsScript", "layerTimeJsCode": code}, "dependencies": []})

def fade(layer, t_in=None, t_out=None, dur=350, rise=None, base_y=0):
    o = []
    if t_in is not None: o += [(t_in, 0, LIN), (t_in + dur, 100, EASE_OUT)]
    else: o += [(0, 100, LIN)]
    if t_out is not None: o += [(t_out, 100, LIN), (t_out + dur, 0, LIN)]
    keys(layer, "opacity", o)
    if rise and t_in is not None:
        keys(layer, "positionY", [(t_in, base_y + rise, LIN), (t_in + dur + 150, base_y, EASE_OUT)])

# ---- background: Background 03 (white with a periwinkle-100 foot) ----------
rect("Background 03", (1080, 1920), WHITE, (0, 0), roundness=0, insert={"type": "append"},
     paint={"type": "gradient", "gradientType": "linear", "start": [0, 0], "end": [0, 1920],
            "stops": [{"offset": 0, "color": WHITE}, {"offset": 0.55, "color": WHITE}, {"offset": 1, "color": PERI100}]})

# ---- header: small-caps topic tag (wordmark is an Image layer) -------------
tag = text("Topic tag", "CONSULTING FEES", FUTURA, 28, RHINO, (80, 332), tracking=120)
fade(tag, t_out=43400)

# ---- headlines (one italic serif phrase per scene) -------------------------
def headline(name, l1, l2, t_in, t_out, y=470):
    g = group(name)
    text(name + " / sans", l1, HEAVY, 70, RHINO, (80, y), parent=g, tracking=-40)
    text(name + " / serif", l2, SERIF, 76, RHINO500, (80, y + 88), parent=g)
    fade(g, t_in, t_out, rise=28 if t_in is not None else None)
    return g

headline("Headline hook", "What a McKinsey partner", "bills per hour", None, 4500)
headline("Headline rate card", "The most each level", "can bill an hour", 4800, 12750)
headline("Headline team week", "One week of a", "five-person team", 13000, 28650)
headline("Headline junior", "A 2020 price for", "one junior consultant", 28950, 38550)

# ---- hook: big number ------------------------------------------------------
hook = group("Hook number")
text("Hook $1,000+", "$1,000+", BLACK, 230, RHINO, (0, 720), parent=hook, box=(1080, 300), just="center", tracking=-40)
ul = rect("Hook underline", (560, 16), PERI, (540, 968), parent=hook, anchor=(280, 8), roundness=8)
keys(ul, "scaleX", [(2880, 0, LIN), (3380, 100, EASE_OUT)])
text("Hook sub", "an hour, for one partner", MEDIUM, 46, RHINO, (0, 1010), parent=hook, box=(1080, 80), just="center")
keys(hook, "opacity", [(4400, 100, LIN), (4800, 0, LIN)])
keys(hook, "positionY", [(4400, 0, LIN), (4800, -40, EASE_OUT)])

# ---- the persistent chart --------------------------------------------------
SLOT = lambda i: 690 + i * 104
BAR_X, BAR_H, MAXW = 80, 44, 680
RATE_SCALE = MAXW / 1586.56
WEEK_TOTAL = 10 * 1293.47 + 40 * 1016.61 + 120 * 612.13   # 127,054.7
WEEK_SCALE = MAXW / WEEK_TOTAL

chart = group("Chart")

def fmt_js():
    return ("function f(n){n=Math.round(n);var s=String(n),o='';"
            "for(var i=0;i<s.length;i++){if(i>0&&(s.length-i)%3===0)o+=',';o+=s[i];}return '$'+o;}")

def row(name, label_pts, slot_pts, phases, colors, row_opacity):
    """phases: list of (t_ms, dur_ms, dollars, scale). Bar width, value text and count-up share them."""
    g = group("Row " + name, parent=chart, pos=(0, SLOT(slot_pts[0][1])))
    lab = text(name + " label", label_pts[0][1], MEDIUM, 34, RHINO, (BAR_X, 0), parent=g)
    if len(label_pts) > 1:
        keys(lab, "textContent", [(t, s, HOLD) for t, s in label_pts], "string")
    bar = rect(name + " bar", (0, BAR_H), RHINO, (BAR_X, 18), parent=g, roundness=12)
    val = text(name + " value", "", HEAVY, 38, RHINO, (BAR_X + 18, 56), parent=g)
    # bar width + value x (keyframed with the same ease so the value rides the bar end)
    w_pts, x_pts, prev = [(0, [0, BAR_H], LIN)], [(0, BAR_X + 18, LIN)], 0
    for t, d, dollars, sc in phases:
        w = round(dollars * sc, 1)
        w_pts += [(t, [prev, BAR_H], LIN), (t + d, [w, BAR_H], EASE_OUT)]
        x_pts += [(t, BAR_X + prev + 18, LIN), (t + d, BAR_X + w + 18, EASE_OUT)]
        prev = w
    keys(bar, "rectSize", w_pts, "vector2")
    # a zero-width rounded rect still draws a sliver: hide the bar while collapsed
    o_pts, prev = [(0, 0, HOLD)], 0
    for t, d, dollars, sc in phases:
        if dollars > 0: o_pts.append((t, 100, HOLD))
        else: o_pts.append((t + d, 0, HOLD))
    keys(bar, "opacity", o_pts)
    keys(val, "positionX", x_pts)
    # count-up text: rise with ease-out, then lock
    ph = json.dumps([[t / 1000, d / 1000, dollars] for t, d, dollars, _ in phases])
    js(val, "textContent", fmt_js() + f"var P={ph};var t=input.time.seconds,v=0,from=0;"
       "for(var i=0;i<P.length;i++){if(t<P[i][0])break;var p=Math.min(1,(t-P[i][0])/P[i][1]);"
       "p=1-Math.pow(1-p,3);v=from+(P[i][2]-from)*p;from=P[i][2];}"
       "return (v<1||from===0)?'':f(v);")
    keys(bar, "fillColor", [(t, c, LIN) for t, c in colors], "color")
    if len(slot_pts) > 1:   # hold each slot, then re-sort with a gentle spring
        sp, prev_s = [(0, SLOT(slot_pts[0][1]), LIN)], slot_pts[0][1]
        for t, s_ in slot_pts[1:]:
            sp += [(t, SLOT(prev_s), LIN), (t + 600, SLOT(s_), SPRING)]; prev_s = s_
        keys(g, "positionY", sp)
    keys(g, "opacity", row_opacity)
    return g

R = RATE_SCALE
row("Senior partner", [(0, "Senior partner")], [(0, 0)],
    [(5000, 500, 1586.56, R), (12960, 300, 0, R)],
    [(0, RHINO), (11170, RHINO), (11470, PERI), (12800, PERI), (12960, RHINO)],
    [(0, 100, LIN), (12960, 100, LIN), (13260, 0, LIN)])
row("Partner", [(0, "Partner"), (16450, "Partner · 10 hours")],
    [(0, 1), (12960, 0), (23200, 1)],
    [(5120, 500, 1293.47, R), (12960, 300, 0, R), (16450, 500, 10 * 1293.47, WEEK_SCALE),
     (28900, 300, 0, WEEK_SCALE)],
    [(0, RHINO)], [(0, 100, LIN), (28900, 100, LIN), (29200, 0, LIN)])
row("Associate partner", [(0, "Associate partner")], [(0, 2)],
    [(5240, 500, 1133.41, R), (12960, 300, 0, R)], [(0, RHINO)],
    [(0, 100, LIN), (12960, 100, LIN), (13260, 0, LIN)])
row("Engagement manager", [(0, "Engagement manager"), (18720, "Engagement manager · 40 hours")],
    [(0, 3), (12960, 1), (23200, 2)],
    [(5360, 500, 1016.61, R), (12960, 300, 0, R), (18720, 500, 40 * 1016.61, WEEK_SCALE),
     (28900, 300, 0, WEEK_SCALE)],
    [(0, RHINO)], [(0, 100, LIN), (28900, 100, LIN), (29200, 0, LIN)])
row("Associate", [(0, "Associate"), (12960, "Associates"), (21010, "3 associates · 120 hours")],
    [(0, 4), (12960, 2), (23200, 3)],
    [(5480, 500, 612.13, R), (12960, 300, 0, R), (21010, 500, 120 * 612.13, WEEK_SCALE),
     (28900, 300, 0, WEEK_SCALE)],
    [(0, RHINO)], [(0, 100, LIN), (28900, 100, LIN), (29200, 0, LIN)])
row("Business analyst", [(0, "Business analyst")], [(0, 5)],
    [(5600, 500, 421.79, R), (12960, 300, 0, R)],
    [(0, RHINO), (7860, RHINO), (8160, PERI), (11000, PERI), (11300, RHINO)],
    [(0, 100, LIN), (12960, 100, LIN), (13260, 0, LIN)])
row("Team week", [(0, "Team week, at maximum rates")], [(0, 0)],
    [(23500, 2700, WEEK_TOTAL, WEEK_SCALE)],
    [(0, PERI), (32660, PERI), (32960, RHINO)],
    [(0, 0, LIN), (23300, 0, LIN), (23700, 100, EASE_OUT)])
row("Junior consultant", [(0, "1 junior consultant · 2020")], [(0, 1)],
    [(32660, 900, 67500, WEEK_SCALE)],
    [(0, PERI)], [(0, 0, LIN), (29900, 0, LIN), (30300, 100, EASE_OUT)])
keys(chart, "opacity", [(0, 0, LIN), (4700, 0, LIN), (5000, 100, EASE_OUT), (38550, 100, LIN), (38900, 0, LIN)])

# ---- caveat chips ----------------------------------------------------------
chip_x = [80]
def chip(label, t_in):
    w = text_w(MEDIUM, 28, label) + 44
    g = group("Chip " + label, pos=(chip_x[0], 1318))
    rect(label + " pill", (w, 50), PERI100, (0, 0), parent=g, roundness=25)
    text(label + " text", label, MEDIUM, 28, RHINO, (22, 35), parent=g)
    keys(g, "opacity", [(0, 0, LIN), (t_in, 0, LIN), (t_in + 300, 100, EASE_OUT), (38550, 100, LIN), (38900, 0, LIN)])
    keys(g, "scaleX", [(t_in, 90, LIN), (t_in + 350, 100, SPRING)])
    keys(g, "scaleY", [(t_in, 90, LIN), (t_in + 350, 100, SPRING)])
    chip_x[0] += w + 14
chip("Contract maximum", 5600)
chip("Derived", 23500)
chip("Reported", 32900)

# ---- $3.5 million callout --------------------------------------------------
card = group("Annual callout", pos=(540, 1070), anchor=(540, 1070))
rect("Callout card", (920, 230), PERI100, (80, 955), parent=card, roundness=24)
text("Callout figure", "≈ $3.5 million a year", BLACK, 76, RHINO, (80, 990), parent=card, box=(920, 100), just="center", tracking=-30)
text("Callout working", "$67,500 a week × 52 weeks", MEDIUM, 36, RHINO, (80, 1105), parent=card, box=(920, 60), just="center")
keys(card, "opacity", [(0, 0, LIN), (35860, 0, LIN), (36160, 100, EASE_OUT), (38550, 100, LIN), (38900, 0, LIN)])
keys(card, "scaleX", [(35860, 88, LIN), (36360, 100, SPRING)])
keys(card, "scaleY", [(35860, 88, LIN), (36360, 100, SPRING)])

# ---- takeaway --------------------------------------------------------------
tk = group("Takeaway")
a = text("Takeaway lead", "So the real question for any client:", MEDIUM, 50, RHINO, (0, 700), parent=tk, box=(1080, 80), just="center")
b = text("Takeaway sans", "Is the team", HEAVY, 104, RHINO, (0, 800), parent=tk, box=(1080, 130), just="center", tracking=-40)
c = text("Takeaway serif", "worth the price?", SERIF, 112, RHINO500, (0, 935), parent=tk, box=(1080, 150), just="center")
for lyr, t0 in ((a, 38900), (b, 39350), (c, 41970)):
    fade(lyr, t0, None, rise=30, base_y={a: 700, b: 800, c: 935}[lyr])
keys(tk, "opacity", [(0, 100, LIN), (43450, 100, LIN), (43750, 0, LIN)])

# ---- closing card ----------------------------------------------------------
cl = group("Closing card")
text("Closing sans", "Follow for more", HEAVY, 92, RHINO, (0, 760), parent=cl, box=(1080, 120), just="center", tracking=-40)
text("Closing serif", "consulting insights", SERIF, 100, RHINO500, (0, 880), parent=cl, box=(1080, 140), just="center")
fade(cl, 43760, None, rise=30)

# ---- captions from the voiceover word timings ------------------------------
words = [(s["offsets"]["from"], s["offsets"]["to"], s["text"].strip())
         for s in json.load(open(os.path.join(HERE, "vo-words.json")))["transcription"] if s["text"].strip()]
# phrases end at punctuation or a pause; each phrase splits into balanced 2-4 word lines
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
# no orphan single words: merge into the previous line if it fits, else borrow its last word
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
    text(f"Caption {n+1}", s, HEAVY, 54, RHINO, (90, 1440), parent=cap_g, box=(900, 80), just="center",
         rng={"start": int(start), "duration": int(end - start)})

json.dump(actions, open(os.path.join(HERE, "edits.json"), "w"), indent=1, ensure_ascii=False)

# ---- media layers (wordmarks + audio) for checkout/commit ------------------
media_ids = iter(range(900, 999))
def audio(name, asset, start_ms, dur, vol):
    return {"id": next(media_ids), "name": name, "type": "Audio",
            "playback": {"type": "windowed", "inputRange": {"start": int(start_ms), "duration": dur},
                         "mapping": {"type": "linear", "input": {"start": 0, "duration": dur},
                                     "output": {"start": 0, "duration": dur}}, "inputOffsetMs": 0},
            "sourceRange": {"start": 0, "duration": dur}, "sourceIntrinsicDuration": dur,
            "source": {"assetId": asset}, "volume": vol, "captionsEnabled": False}
WM_W, WM_H = 1174, 312
media = [
    {"type": "Image", "id": next(media_ids), "name": "Wordmark header", "blendMode": "normal",
     "activeRange": {"start": 0, "duration": 43760},
     "transform": T((1000, 300), (WM_W, 0), scale=15), "source": {"assetId": "wordmark-rhino", "fit": "contain"}},
    {"type": "Image", "id": next(media_ids), "name": "Wordmark closing", "blendMode": "normal",
     "activeRange": {"start": 43900, "duration": END_MS - 43900},
     "transform": T((540, 1150), (WM_W / 2, 0), scale=30), "source": {"assetId": "wordmark-rhino", "fit": "contain"}},
    audio("Voiceover", "vo", 0, VO_MS, 1.0),
]
for t in (2880, 36330, 43760): media.append(audio("SFX pop", "sfx-pop", t - 20, 250, 0.45))
for t in (12960, 23200, 28900): media.append(audio("SFX whoosh", "sfx-whoosh", t - 250, 600, 0.3))
for t in (5000, 16450, 18720, 21010, 23500, 32660): media.append(audio("SFX tick", "sfx-tick", t, 120, 0.4))
json.dump(media, open(os.path.join(HERE, "media-layers.json"), "w"), indent=1)
print(len(actions), "actions;", len(chunks), "caption chunks;", len(media), "media layers")
for ch in chunks: print(ch[0][0], " ".join(w[2] for w in ch))
