# Case-board renderer for the 16:9 mock-case layout (left 70% = 1344x1080).
# Visual language from the 01. Styles/Consulting Case board (white card, lavender, navy, Avenir Next,
# elements appear on the word that says them). Writes unique frames + an ffmpeg concat list.
# HARD-CODED to the 4 Nov beer case: copy to <project>/board.py and rewrite CHAPTERS + beats per case.
# usage: 06. Tools/venv-style/bin/python board.py <project_dir> <t0> <t1>
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

P, T0, T1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
FPS = 30000 / 1001
W, H = 1344, 1080
NAVY, INK, GREY = (44, 53, 82), (43, 47, 58), (138, 143, 160)
ACC, ACC_L, ACC_LL = (86, 112, 252), (227, 230, 253), (238, 240, 254)
HILITE = (255, 236, 196)
F = "/System/Library/Fonts/Avenir Next.ttc"
FACE = {"bold": 0, "demi": 2, "med": 5, "reg": 7}
_fc = {}
def font(size, w="med"):
    k = (size, w)
    if k not in _fc: _fc[k] = ImageFont.truetype(F, size, index=FACE[w])
    return _fc[k]

# ---------- layout ----------
CX, CY, CW, CH = 40, 100, 1272, 800          # board card
LX, LW = 88, 580                              # left column (beat visual)
RX, RW = 716, 552                             # right column (tree)
TOP = 182                                     # first content row

# ---------- primitives (each returns an RGBA image) ----------
def text_img(s, size, w="med", color=INK, pad=2):
    f = font(size, w); b = f.getbbox(s)
    im = Image.new("RGBA", (int(f.getlength(s)) + pad * 2, b[3] + pad * 2 + size // 5), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((pad, pad), s, font=f, fill=color)
    im.info["snd"] = "text"; return im

def label(s):  # small uppercase grey label
    im = text_img(s.upper(), 17, "demi", GREY); im.info["snd"] = "label"; return im

def pill(s, fill=ACC_L, outline=None, color=NAVY, size=22, w="demi", h=40, padx=16):
    f = font(size, w); tw = int(f.getlength(s))
    im = Image.new("RGBA", (tw + padx * 2, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, im.width - 1, h - 1), 6, fill=fill, outline=outline, width=2 if outline else 0)
    d.text((padx, (h - size * 1.36) / 2), s, font=f, fill=color)
    return im

def box(w, h, fill=(255, 255, 255, 255), outline=ACC_L, r=8, width=2):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=fill, outline=outline, width=width)
    im.info["snd"] = "none"; return im

def option_card(letter, title, sub, w=LW, h=150):
    im = box(w, h, fill=(255, 255, 255, 255), outline=ACC_L, width=3); d = ImageDraw.Draw(im)
    d.rounded_rectangle((24, 30, 76, 82), 8, fill=ACC); f = font(30, "demi")
    d.text((50 - f.getlength(letter) / 2, 34), letter, font=f, fill=(255, 255, 255))
    d.text((100, 26), title, font=font(32, "demi"), fill=NAVY)
    d.text((100, 78), sub, font=font(22, "med"), fill=GREY)
    im.info["snd"] = "pop"; return im

def channel_card(title, sub, w=LW, h=130):
    im = box(w, h, fill=ACC_LL + (255,), outline=None, width=0); d = ImageDraw.Draw(im)
    d.text((28, 18), title, font=font(40, "demi"), fill=NAVY)
    d.text((28, 76), sub, font=font(24, "med"), fill=GREY)
    im.info["snd"] = "pop"; return im

def chip(s, w=None, big=False, hi=False):
    size = 30 if big else 26
    f = font(size, "demi"); tw = int(f.getlength(s)); w = w or tw + 44
    h = 64 if big else 56
    fill = HILITE + (255,) if hi else (255, 255, 255, 255)
    im = box(w, h, fill=fill, outline=ACC_L, r=8, width=2)
    ImageDraw.Draw(im).text((22, (h - size * 1.36) / 2), s, font=f, fill=NAVY)
    im.info["snd"] = "result" if hi else "pop"; return im

def check_row(s, w=LW):
    im = Image.new("RGBA", (w, 46), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 7, 32, 39), 5, fill=ACC)
    d.line((8, 23, 14, 30, 25, 15), fill=(255, 255, 255), width=4, joint="curve")
    d.text((48, 4), s, font=font(26, "med"), fill=INK)
    return im

def bar(w, h, color):
    im = Image.new("RGBA", (max(w, 2), h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, max(w, 2) - 1, h - 1), 4, fill=color)
    return im

def big_number(s, size=120):
    im = text_img(s, size, "demi", NAVY, pad=4); im.info["snd"] = "count"; return im

def mug_icon(sz=150):
    im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0)); d = ImageDraw.Draw(im); s = sz / 150
    d.rounded_rectangle((20*s, 40*s, 100*s, 140*s), 6*s, outline=ACC, width=int(6*s), fill=ACC_LL)
    d.rectangle((26*s, 70*s, 94*s, 134*s), fill=(255, 214, 120))
    for cx, cy, r in ((35, 38, 16), (60, 30, 20), (86, 38, 16)):
        d.ellipse(((cx-r)*s, (cy-r)*s, (cx+r)*s, (cy+r)*s), fill=(255, 255, 255), outline=ACC, width=int(5*s))
    d.arc((86*s, 62*s, 134*s, 118*s), -90, 90, fill=ACC, width=int(7*s))
    im.info["snd"] = "icon"; return im

def arrow(w=40):
    im = Image.new("RGBA", (w, 30), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line((2, 15, w - 10, 15), fill=GREY, width=3); d.polygon(((w - 12, 6), (w - 2, 15), (w - 12, 24)), fill=GREY)
    im.info["snd"] = "none"; return im

def strike(w):
    im = Image.new("RGBA", (w, 6), (0, 0, 0, 0)); ImageDraw.Draw(im).rectangle((0, 0, w, 5), fill=(214, 92, 92))
    return im

# ---------- word timing ----------
WORDS = json.load(open(os.path.join(P, "words.json")))
def at(phrase, after=0.0):
    p = [x.lower() for x in phrase.split()]
    for i in range(len(WORDS) - len(p)):
        if WORDS[i]["start_ms"] / 1000 >= after and [w["word"].lower().strip(".,?!") for w in WORDS[i:i+len(p)]] == p:
            return WORDS[i]["start_ms"] / 1000
    raise SystemExit("phrase not found: " + phrase)

# ---------- elements ----------
ELS = []
def add(img, x, y, tin, tout=None, motion="rise", count=None, grow=False, snd=None):
    if snd is None:
        snd = "count" if count else "bar" if grow else img.info.get("snd", "pop")
    ELS.append(dict(img=img, x=x, y=y, tin=tin, tout=tout, motion=motion, count=count, grow=grow, snd=snd))
    return ELS[-1]

CLEARS = []
def group(items, tout):  # set exit time for a beat group (left column replaced)
    for e in items: e["tout"] = tout
    CLEARS.append(tout)

# chapter tabs
CHAPTERS = [("Problem", 0.0), ("Clarify", at("clarifying questions")), ("Structure", at("structure the discussion")),
            ("Option A · Kegs", at("starting with the kegs")), ("Option B · Canning", at("let's look at the other")),
            ("Recommend", at("what do you like", 1255)), ("Feedback", at("sounds good aditya", 1495))]

# ---- Ch1 Problem ----
g = []
g.append(add(label("Your client"), LX, TOP, at("your client is")))
g.append(add(text_img("Craft beer manufacturer", 46, "demi", NAVY), LX, TOP + 30, at("beer manufacturer")))
g.append(add(mug_icon(130), LX, TOP + 110, at("craft beers")))
g.append(add(text_img("Makes its own craft beers · US", 24, "med", GREY), LX + 150, TOP + 160, at("craft beers")))
g.append(add(label("Volume, last 3 years"), LX, TOP + 290, at("100K barrels")))
g.append(add(bar(116, 48, ACC_L + (255,)), LX, TOP + 326, at("100K barrels"), grow=True))
g.append(add(text_img("100K barrels", 24, "demi", GREY), LX + 132, TOP + 334, at("100K barrels")))
g.append(add(bar(400, 48, ACC + (255,)), LX, TOP + 390, at("500K"), grow=True))
g.append(add(text_img("500K barrels", 24, "demi", NAVY), LX + 416, TOP + 398, at("500K")))
t = at("two channels"); group(g, t)
g = []
g.append(add(label("Two distribution channels"), LX, TOP, t))
g.append(add(channel_card("Kegs", "Sold directly to restaurants & bars"), LX, TOP + 36, at("restaurants")))
g.append(add(channel_card("Cans", "Sold in cases to wine & liquor shops"), LX, TOP + 186, at("wine shops")))
t = at("$20 million"); group(g, t)
g = []
g.append(add(label("Money to invest"), LX, TOP, t))
g.append(add(None, LX, TOP + 26, t, count=("${}M", 20, 0)))
g.append(add(text_img("to improve cost & process efficiency", 26, "med", GREY), LX, TOP + 190, at("cost and process")))
t = at("two options"); group(g, t)
g = []
g.append(add(label("Two options"), LX, TOP, t))
g.append(add(option_card("A", "Buy the kegs upfront", "instead of leasing them"), LX, TOP + 36, at("purchase them")))
g.append(add(option_card("B", "Upgrade the canning system", "package cans faster"), LX, TOP + 206, at("canning system")))
ROOT_T = at("which one")
add(box(RW, 66, outline=NAVY, width=3, r=8), RX, TOP - 10, ROOT_T, snd="hero")
add(text_img("Which option should get the $20M?", 27, "demi", NAVY), RX + 22, TOP + 4, ROOT_T)

# right column: facts + clarifying questions (rows persist)
ROWY = lambda k: TOP + 100 + k * 50
add(label("Case facts & clarifying questions"), RX, TOP + 72, at("500K"))
def row(k, q, a, tq, ta):
    add(pill(q, fill=ACC_L + (255,)), RX, ROWY(k), tq)
    add(pill(a, fill=(255, 255, 255, 255), outline=ACC, color=INK, w="med"), RX + int(font(22, "demi").getlength(q)) + 48, ROWY(k), ta)
row(0, "Volume", "500K barrels a year", at("500K"), at("500K") + 0.4)
row(1, "Channels", "Kegs · Cans", at("two channels"), at("wine shops"))
row(2, "Budget", "$20M to invest", at("$20 million"), at("$20 million") + 0.4)
row(3, "Target?", "Best cost savings, now", at("specific targets"), at("whichever leads"))
row(4, "Market?", "US only", at("geographies do they"), at("US", after=145))
row(5, "Channel split?", "60% cans · 40% kegs", at("contribution"), at("60% goes"))
row(6, "Margins?", "Not known", at("sort of margins"), at("not at this"))

# ---- Ch2 Clarify (left) ----
t = at("value chain"); group(g, t)
g = []
g.append(add(label("Value chain"), LX, TOP, t))
x = LX
for i, s in enumerate(["Brew", "Kegs / Cans", "Bars & stores"]):
    c = pill(s, fill=ACC_LL + (255,), size=24, h=48)
    g.append(add(c, x, TOP + 36, t + 0.15 * i)); x += c.width + 8
    if i < 2: g.append(add(arrow(34), x, TOP + 46, t + 0.15 * i + 0.07)); x += 42
tc = at("60% goes")
g.append(add(label("Production split · 500K barrels"), LX, TOP + 140, tc))
g.append(add(bar(336, 60, ACC + (255,)), LX, TOP + 176, tc, grow=True))
g.append(add(bar(220, 60, NAVY + (255,)), LX + 342, TOP + 176, at("40% goes"), grow=True))
g.append(add(text_img("60% cans", 24, "demi", ACC), LX, TOP + 246, tc))
g.append(add(text_img("40% kegs", 24, "demi", NAVY), LX + 342, TOP + 246, at("40% goes")))
g.append(add(big_number("300K", 64), LX, TOP + 290, at("300,000")))
g.append(add(text_img("barrels in cans", 22, "med", GREY), LX, TOP + 378, at("300,000")))
g.append(add(big_number("200K", 64), LX + 342, TOP + 290, at("200K barrels")))
g.append(add(text_img("barrels in kegs", 22, "med", GREY), LX + 342, TOP + 378, at("200K barrels")))

# ---- Ch3 Structure ----
t = at("structure the discussion"); group(g, t)
g = []
g.append(add(label("Aditya's approach"), LX, TOP, t))
nodes = [("1  Upfront investment · $20M", at("initial investment")),
         ("2  Cost today vs after = savings", at("current costs")),
         ("3  Time horizon & NPV", at("NPV calculation"))]
for i, (s, tt) in enumerate(nodes):
    g.append(add(chip(s, w=LW), LX, TOP + 40 + i * 80, tt))
tn = at("not go to")
g.append(add(strike(300), LX + 60, TOP + 40 + 2 * 80 + 27, tn, grow=True))
g.append(add(pill("Skip NPV", fill=(253, 228, 228, 255), color=(170, 60, 60)), LX + 400, TOP + 40 + 2 * 80 + 8, tn))
g.append(add(pill("Focus: cost savings", fill=HILITE + (255,)), LX, TOP + 290, at("cost savings for")))
g.append(add(pill("Assume the full $20M in both", fill=ACC_LL + (255,)), LX, TOP + 350, at("full 20 million")))

# ---- Ch4 Kegs ----
t = at("starting with the kegs"); group(g, t)
g = []
g.append(add(label("Option A · Buy the kegs"), LX, TOP, t))
for i, (s, tt) in enumerate([("200K barrels × 2 kegs = 400K kegs", at("two kegs")),
                             ("Lease: $10 per keg a year", at("$10 a year")),
                             ("400K × $10 = $4M a year", at("$4 million")),
                             ("$20M ÷ 400K kegs = $50 a keg", at("$50 per"))]):
    g.append(add(chip(s, w=LW), LX, TOP + 40 + i * 72, tt))
t = at("useful life"); group(g, t)
g = []
g.append(add(label("Things to consider"), LX, TOP, t))
items = [("Useful life: 10 years", at("10 years", after=440)), ("Exit costs in the lease: ignore", at("so we can ignore those")),
         ("Opportunity cost of the $20M", at("opportunity cost")), ("Same keg quality", at("quality of kegs")),
         ("Storage & upkeep", at("storage")), ("Damage or loss: replacements", at("damage or loss")),
         ("Depreciation vs lease payments", at("depreciation")), ("Exit value after 10 years", at("exit value"))]
for i, (s, tt) in enumerate(items):
    g.append(add(check_row(s), LX, TOP + 40 + i * 50, tt))
t = at("replace 5%"); group(g, t)
g = []
g.append(add(label("Option A · Savings"), LX, TOP, t))
for i, (s, tt, hi) in enumerate([("Replace 5% of kegs a year", t, False),
                                 ("5% × $20M = $1M a year", at("$1 million"), False),
                                 ("Lease today = $4M a year", at("lease costs were"), False),
                                 ("$4M − $1M = $3M saved a year", at("$3 million"), False),
                                 ("$3M × 10 yrs − $20M = $10M", at("$10 million", after=630), True)]):
    g.append(add(chip(s, w=LW, big=hi, hi=hi), LX, TOP + 40 + i * 72, tt))
group(g, at("let's look at the other"))

# scoreboard strip (bottom of card)
SB_T, SB_Y = at("starting with the kegs"), CY + CH - 150
add(label("Scoreboard · 10-year savings"), LX, SB_Y, SB_T)
for i, nm in enumerate(["A · Kegs", "B · Canning"]):
    add(box(560, 86, fill=ACC_LL + (255,), outline=None, width=0, r=8), LX + i * 600, SB_Y + 30, SB_T)
    add(text_img(nm, 26, "demi", NAVY), LX + 24 + i * 600, SB_Y + 52, SB_T)
add(text_img("?", 40, "demi", GREY), LX + 480, SB_Y + 42, SB_T, tout=at("$10 million", after=630))
add(text_img("?", 40, "demi", GREY), LX + 1080, SB_Y + 42, SB_T)
add(None, LX + 400, SB_Y + 40, at("$10 million", after=630), count=("${}M", 10, 1))


# ---------- extra primitives for ch5-7 ----------
def wrap(s, f, maxw):
    lines, cur = [], ""
    for w_ in s.split():
        t_ = (cur + " " + w_).strip()
        if f.getlength(t_) <= maxw: cur = t_
        else: lines.append(cur); cur = w_
    return lines + [cur]

def quote_card(s, w=1176, size=34, sub=None):
    f = font(size, "demi"); lines = wrap(s, f, w - 80); lh = int(size * 1.35)
    h = 48 + lh * len(lines) + (40 if sub else 0)
    im = box(w, h, fill=HILITE + (255,), outline=None, width=0, r=8); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 7, h), fill=ACC)
    y = 24
    if sub: d.text((40, y - 4), sub.upper(), font=font(17, "demi"), fill=GREY); y += 36
    for ln in lines: d.text((40, y), ln, font=f, fill=NAVY); y += lh
    im.info["snd"] = "result"; return im

def cell(s, w, h=52, fill=(255, 255, 255, 255), color=NAVY, size=26, weight="demi"):
    im = box(w, h, fill=fill, outline=ACC_L, r=6); f = font(size, weight)
    ImageDraw.Draw(im).text(((w - f.getlength(s)) / 2, (h - size * 1.36) / 2), s, font=f, fill=color)
    im.info["snd"] = "pop"; return im

def row_label(s, w, h=52):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((4, (h - 24 * 1.36) / 2), s, font=font(24, "med"), fill=INK)
    im.info["snd"] = "text"; return im

def sub_row(s, w=LW):
    im = Image.new("RGBA", (w, 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle((48, 17, 60, 21), fill=GREY); d.text((72, 4), s, font=font(22, "med"), fill=GREY)
    im.info["snd"] = "label"; return im

# ---- Ch5 Option B: Canning ----
t = at("let's look at the other")
g = []
g.append(add(label("Option B · Upgrade the canning system"), LX, TOP, at("upgrading the canning", 650)))
g.append(add(chip("1 barrel = 14 cases of cans", w=LW), LX, TOP + 40, at("14 cases", 650)))
g.append(add(chip("300K barrels × 14 = 4.2M cases", w=LW), LX, TOP + 112, at("4.2 million cases", 650)))
t = at("explain the difference", 650); group(g, t)
g = []
g.append(add(label("Old vs new machine"), LX, TOP, t))
CW1, CW2 = 196, 180
g.append(add(cell("Old", CW2, fill=ACC_LL + (255,)), LX + CW1 + 12, TOP + 34, t))
g.append(add(cell("New", CW2, fill=ACC + (255,), color=(255, 255, 255)), LX + CW1 + CW2 + 22, TOP + 34, at("new system", 700)))
rows = [("Operators", "4", "4", at("four operators", 700), at("new system", 700) + 0.6),
        ("Cases / hour", "600", "1,200", at("600 cases a hour", 700), at("1,200 cases", 700)),
        ("Wastage", "10%", "7%", at("10% wastage", 700), at("about 7%", 700)),
        ("Cost", "$10M", "$20M", at("$10 million when", 700), at("$20 million", 735))]
for i, (nm, o, n_, to, tn_) in enumerate(rows):
    y = TOP + 96 + i * 60
    g.append(add(row_label(nm, CW1), LX, y, to))
    g.append(add(cell(o, CW2, weight="med"), LX + CW1 + 12, y, to))
    g.append(add(cell(n_, CW2, weight="med"), LX + CW1 + CW2 + 22, y, tn_))
g.append(add(chip("Sell old machine: +$1.3M salvage", w=LW), LX, TOP + 350, at("$1.3 million", 760)))
g.append(add(chip("Net investment = $20M − $1.3M = $18.7M", w=LW), LX, TOP + 420, at("$18.7", 770)))
t = at("$25 an hour", 1040); group(g, t)
g = []
g.append(add(label("Annual cost · old vs new"), LX, TOP, t))
g.append(add(pill("Labour $25 / hour", fill=ACC_LL + (255,)), LX, TOP + 32, t))
g.append(add(pill("Wasted case = $20", fill=ACC_LL + (255,)), LX + 250, TOP + 32, at("about $20", 1050)))
g.append(add(cell("Old", CW2, fill=ACC_LL + (255,)), LX + CW1 + 12, TOP + 92, at("7,000 hours", 1060)))
g.append(add(cell("New", CW2, fill=ACC + (255,), color=(255, 255, 255)), LX + CW1 + CW2 + 22, TOP + 92, at("3,500", 1080)))
rows = [("Labour hours", "7,000", "3,500", at("7,000 hours", 1060), at("3,500", 1080)),
        ("Labour cost", "$700K", "$350K", at("$700K", 1120), at("$350K", 1130)),
        ("Wastage", "$8.4M", "$5.9M", at("$8.4 million", 1150), at("$5.9 million", 1170)),
        ("Total a year", "$9.1M", "$6.25M", at("$9.1 million", 1190), at("6.25 million", 1200))]
for i, (nm, o, n_, to, tn_) in enumerate(rows):
    y = TOP + 154 + i * 60
    g.append(add(row_label(nm, CW1), LX, y, to))
    g.append(add(cell(o, CW2, weight="med"), LX + CW1 + 12, y, to))
    g.append(add(cell(n_, CW2, weight="med"), LX + CW1 + CW2 + 22, y, tn_))
g.append(add(chip("Saves $2.85M a year", w=LW, big=True, hi=True), LX, TOP + 404, at("$2.85 million", 1210)))
t = at("$28.5 million", 1220); group(g, t)
g = []
g.append(add(label("Option B · 10-year savings"), LX, TOP, t))
g.append(add(chip("$2.85M × 10 years = $28.5M", w=LW), LX, TOP + 40, t))
g.append(add(chip("Investment ≈ $18.5M (after salvage)", w=LW), LX, TOP + 112, at("$18.5 million", 1230)))
g.append(add(chip("$28.5M − $18.5M = $10M", w=LW, big=True, hi=True), LX, TOP + 184, at("$18.5 million", 1230) + 1.2))
B_T = at("$18.5 million", 1230) + 1.2
for e in ELS:
    if e["x"] == LX + 1080 and e["y"] == SB_Y + 42: e["tout"] = B_T   # B "?" placeholder makes way for the number
add(None, LX + 1000, SB_Y + 40, B_T, count=("${}M", 10, 1))
TIE_T = at("exactly the same", 1240)
add(pill("Tie", fill=HILITE + (255,), size=22), LX + 560 - 32, SB_Y - 6, TIE_T, snd="result")
t = at("what do you like", 1255); group(g, t)

# ---- Ch6 Recommend ----
g = []
g.append(add(label("Next steps Aditya proposes"), LX, TOP, at("operational feasibility", 1265)))
g.append(add(check_row("Operational feasibility"), LX, TOP + 40, at("operational feasibility", 1265)))
g.append(add(check_row("Risks of each option"), LX, TOP + 90, at("operational feasibility", 1265) + 2.2))
g.append(add(check_row("Scenario analysis"), LX, TOP + 140, at("scenario analysis", 1275)))
t = at("final recommendation", 1295); group(g, t)
g = []
g.append(add(label("Before recommending"), LX, TOP, t))
g.append(add(chip("Is demand growing, or flat?", w=LW), LX, TOP + 40, at("increase in demand", 1320)))
g.append(add(label("Kashish: volume, last 3 years"), LX, TOP + 140, at("grown from 100K", 1350)))
g.append(add(bar(116, 48, ACC_L + (255,)), LX, TOP + 176, at("grown from 100K", 1350), grow=True))
g.append(add(text_img("100K barrels", 24, "demi", GREY), LX + 132, TOP + 184, at("grown from 100K", 1350)))
g.append(add(bar(400, 48, ACC + (255,)), LX, TOP + 240, at("grown from 100K", 1350) + 1.4, grow=True))
g.append(add(text_img("500K barrels", 24, "demi", NAVY), LX + 416, TOP + 248, at("grown from 100K", 1350) + 1.4))
t = at("my recommendation to the client", 1370); group(g, t)
g = []
g.append(add(label("Recommendation"), LX, TOP, t))
g.append(add(text_img("Upgrade the canning system", 40, "demi", NAVY), LX, TOP + 28, t + 1.0))
g.append(add(check_row("Expands capacity for growth"), LX, TOP + 100, at("expand our capacity", 1390)))
g.append(add(text_img("Today: 7,000 hrs ÷ 365 ≈ 20 of 24 hours a day", 22, "med", GREY), LX + 48, TOP + 150, at("7,000 hours a year", 1400)))
g.append(add(bar(LW - 48, 30, ACC_LL + (255,)), LX + 48, TOP + 186, at("20 hours a day", 1410), snd="none"))
g.append(add(bar(int((LW - 48) * 20 / 24), 30, ACC + (255,)), LX + 48, TOP + 186, at("20 hours a day", 1410), grow=True))
g.append(add(pill("Near full capacity", fill=HILITE + (255,)), LX + 48, TOP + 228, at("close to capacity", 1410)))
g.append(add(check_row("Saves $2.85M a year, every year"), LX, TOP + 290, at("2.8 million", 1440) - 4))
g.append(add(text_img("Risk: wastage 10% to 7% swings $2.8M a year", 22, "med", GREY), LX + 48, TOP + 340, at("2.8 million", 1440)))
g.append(add(chip("Kegs: safer, predictable $10M, no growth upside", w=LW), LX, TOP + 390, at("purchasing kegs outright", 1455)))
VERDICT_T = at("canning upgrade", 1480)
add(pill("Recommended", fill=ACC + (255,), color=(255, 255, 255), size=22), LX + 600 + 560 - 160, SB_Y - 6, VERDICT_T, snd="result")

# ---- Ch7 Feedback: full-card scorecard ----
FB_T = at("sounds good aditya", 1495)
group(g, FB_T)
for e in ELS:
    if e["tout"] is None: e["tout"] = FB_T
add(label("Interviewer feedback"), LX, TOP - 8, FB_T + 0.4)
add(text_img("Strengths", 34, "demi", NAVY), LX, TOP + 20, at("did well in", 1500))
add(check_row("Analytical thinking"), LX, TOP + 78, at("analytical thinking", 1505))
add(check_row("Business insights"), LX, TOP + 126, at("analytical thinking", 1505) + 1.6)
for i, (s_, tt) in enumerate([("Spotted exit costs in the lease", at("exit costs", 1515)),
                              ("Depreciation & storage for kegs", at("depreciation", 1520)),
                              ("Salvage value of the old machine", at("old machinery", 1545)),
                              ("Capacity insight: 20 hrs a day", 1586.4)]):
    add(sub_row(s_), LX, TOP + 178 + i * 42, tt)
WO_T = at("few things which", 1640)
add(text_img("Work on", 34, "demi", NAVY), RX, TOP + 20, WO_T)
for i, (s_, tt, hi_) in enumerate([("1  Bring your personality in", at("personality slightly", 1680), False),
                                   ("2  Clarifying Qs: stay on cost", at("clarification questions again", 1700), False),
                                   ("3  Comprehensive first structure", at("initial structure", 1720), False),
                                   ("4  Communication: record yourself", at("record yourself", 1805), False),
                                   ("5  Lead the case: give the next step", 1844.0, True),
                                   ("6  Use the case data, not assumptions", at("nitpick", 1905), False)]):
    add(chip(s_, w=RW, hi=hi_), RX, TOP + 78 + i * 58, tt)
QY = TOP + 440
q1 = add(quote_card("Did the interviewer enjoy speaking to you?", sub="The key KPI in an interview"), LX, QY, at("key kpi", 1600), tout=WO_T)
q2 = add(quote_card("Work on: 1 communication · 2 approach · 3 personality", sub="Summary"), LX, QY, 1949.1, tout=at("framing issue", 2000))
q3 = add(quote_card("“To be comprehensive, I'd like to look at operational capabilities next. Does that sound good?”", size=30,
                    sub="How to frame the next step"), LX, QY, at("being comprehensive", 2010))

# ---------- static base ----------
def base_img():
    im = Image.new("RGB", (W, H)); px = im.load()
    a, b, c = (253, 253, 253), (233, 236, 253), (214, 220, 252)
    for y in range(H):
        for x in range(0, W, 4):
            u, v = x / W, y / H
            col = tuple(int(a[k] * (1 - u) * (1 - v) + b[k] * u * (1 - v) + c[k] * (1 - u) * v + b[k] * u * v) for k in range(3))
            for dx in range(4):
                if x + dx < W: px[x + dx, y] = col
    d = ImageDraw.Draw(im)
    for y in range(18, H, 36):
        for x in range(18, W, 36): d.ellipse((x - 1.2, y - 1.2, x + 1.2, y + 1.2), fill=(205, 210, 245))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((CX + 4, CY + 10, CX + CW + 4, CY + CH + 14), 14, fill=(120, 130, 210, 40))
    im = Image.alpha_composite(im.convert("RGBA"), sh)
    ImageDraw.Draw(im).rounded_rectangle((CX, CY, CX + CW, CY + CH), 12, fill=(255, 255, 255, 255))
    d = ImageDraw.Draw(im)
    d.text((CX + 48, CY + 26), "Mock case interview · Beer client", font=font(19, "med"), fill=GREY)
    g_ = "gradnext"; d.text((CX + CW - 48 - font(26, "demi").getlength(g_), CY + 20), g_, font=font(26, "demi"), fill=NAVY)
    return im

def tabs_img(active):
    im = Image.new("RGBA", (W, 60), (0, 0, 0, 0)); d = ImageDraw.Draw(im); x = CX
    for i, (nm, _) in enumerate(CHAPTERS):
        on = i == active; f = font(19, "demi" if on else "med"); tw = int(f.getlength(nm))
        d.rounded_rectangle((x, 12, x + tw + 44, 50), 6, fill=ACC if on else (255, 255, 255, 200))
        d.ellipse((x + 14, 27, x + 22, 35), fill=(255, 255, 255) if on else GREY)
        d.text((x + 30, 18), nm, font=f, fill=(255, 255, 255) if on else GREY); x += tw + 56
    return im

def ease(p): return 1 - (1 - p) ** 3

def render_count(spec, p):
    fmt, val, _ = spec; v = val * (0.6 + 0.4 * ease(p))
    s = fmt.format(int(round(v)) if p < 1 else val)
    return big_number(s, 120 if spec[2] == 0 else 52)

BASE = base_img(); TABS = [tabs_img(i) for i in range(len(CHAPTERS))]
DUR_IN, DUR_OUT, COUNT = 0.22, 0.25, 0.45

def frame_state(t):
    st = []
    ch = max(i for i, (_, s) in enumerate(CHAPTERS) if s <= t)
    st.append(("tab", ch))
    for i, e in enumerate(ELS):
        if t < e["tin"]: continue
        if e["tout"] is not None and t >= e["tout"] + DUR_OUT: continue
        pin = min(1, (t - e["tin"]) / (COUNT if e["count"] else DUR_IN))
        if e["grow"]: pin = min(1, (t - e["tin"]) / 0.5)
        pout = 0 if e["tout"] is None or t < e["tout"] else min(1, (t - e["tout"]) / DUR_OUT)
        st.append((i, round(pin, 3), round(pout, 3)))
    return tuple(st)

def draw(state):
    im = BASE.copy()
    im.alpha_composite(TABS[state[0][1]], (0, 32))
    for i, pin, pout in state[1:]:
        e = ELS[i]
        src = render_count(e["count"], pin) if e["count"] else e["img"]
        a = ease(pin) * (1 - pout)
        dy = 0 if e["grow"] or e["count"] else int(round(8 * (1 - ease(pin))))
        if e["grow"]:
            wv = max(1, int(src.width * ease(pin))); src = src.crop((0, 0, wv, src.height)); a = 1 - pout
        if a <= 0: continue
        if a < 1:
            src = src.copy(); al = src.getchannel("A").point(lambda v: int(v * a)); src.putalpha(al)
        im.alpha_composite(src, (int(e["x"]), int(e["y"] + dy)))
    return im.convert("RGB")

out = os.path.join(P, "board_frames"); os.makedirs(out, exist_ok=True)
for f_ in os.listdir(out): os.remove(os.path.join(out, f_))
n0, n1 = int(round(T0 * FPS)), int(round(T1 * FPS))
prev, cur_file, cur_n, lst, k = None, None, 0, [], 0
for n in range(n0, n1):
    s = frame_state(n / FPS)
    if s != prev:
        if cur_file: lst.append((cur_file, cur_n))
        cur_file = os.path.join(out, f"f{k:05d}.png"); draw(s).save(cur_file, compress_level=1); k += 1; cur_n = 0; prev = s
    cur_n += 1
lst.append((cur_file, cur_n))
with open(os.path.join(P, "board_concat.txt"), "w") as fh:
    for fn, cnt in lst: fh.write(f"file '{fn}'\nduration {cnt / FPS:.6f}\n")
    fh.write(f"file '{lst[-1][0]}'\n")
ev = [dict(t=round(e["tin"], 3), snd=e["snd"]) for e in ELS if T0 <= e["tin"] < T1]
ev += [dict(t=round(t, 3), snd="clear") for t in CLEARS if T0 <= t < T1]
ev += [dict(t=round(s, 3), snd="chapter") for _, s in CHAPTERS if T0 < s < T1]
json.dump(sorted(ev, key=lambda x: x["t"]), open(os.path.join(P, f"events_{int(T0)}_{int(T1)}.json"), "w"))
print(f"{k} unique frames for {n1 - n0} frames; {len(ELS)} elements")
