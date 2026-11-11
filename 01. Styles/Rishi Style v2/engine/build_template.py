"""Rishi v2 · build template (from roughcut_v3 draft 4).

A HELPING HAND, NOT A TEMPLATE YOU MUST FOLLOW. Every scene below is the exact recipe that Rishi approved for
roughcut_v3; copy, retime, drop or rewrite scenes freely for a new video. Rishi's per-video feedback always wins.

How to use for a new edit (see engine/README.md):
  1. Fill CONFIG (or pass a JSON config path as argv[1]).
  2. Retime / replace the scene blocks (search "# B1", "# B3 + B4", ...) to match the new script's beats.
  3. Run from the edit's .tesseract-work folder:  python build_template.py [config.json]
     -> writes editable.json + edits.json + sound_cue_sheet.md; then tsrct commit + apply + export.
"""
import json, math, os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

# ---------------------------------------------------------------- CONFIG (per video)
CONFIG = {
    "editable_orig": "editable.orig.json",          # tsrct checkout of the clean base project (assets already imported)
    "words": "../../roughcut_v3_words.json",         # word timings [{s,e,w}] on the ROUGH-CUT clock (tools/roman_captions.py)
    "face": "../../roughcut_v3.face.json",           # tools/face_track.py output (nose track for the B&W beat)
    "sfx_meta": "sfx_meta.json",                     # tools/sfx_prep.py output (peak level/time per SFX)
    "fonts_dir": "../fonts",                         # Inter 300-700 + Playfair Display 500/700 italic TTFs
    "cue_sheet": "../sound_cue_sheet.md",
    "duration": 33.4,
}
if len(sys.argv) > 1 and sys.argv[1].endswith('.json'):
    CONFIG.update(json.load(open(sys.argv[1])))
from lib import *
from fontTools.ttLib import TTFont

b = Build()
doc = json.load(open(CONFIG['editable_orig']))
DUR = CONFIG['duration']
WORDS = json.load(open(CONFIG['words']))
SFX = json.load(open(CONFIG['sfx_meta']))

E1 = {"type": "cubicBezier", "x1": 0.22, "y1": 1, "x2": 0.36, "y2": 1}        # soft ease-out (word rise, entrances)
ES = {"type": "cubicBezier", "x1": 0.45, "y1": 0.05, "x2": 0.2, "y2": 1}      # smooth in-out for big moves
EX = {"type": "cubicBezier", "x1": 0.55, "y1": 0, "x2": 0.75, "y2": 0.4}      # smooth exit
F_PFB = ("Playfair Display", "Bold Italic")
ICE, RTXT, RACC, RCARD = hexc('EAF0F8'), hexc('F2F6FC'), hexc('3E7BFA'), hexc('121C38')
INKD, MUTE_ICE, MUTE_INK, TEAL, GREEN = hexc('0B1730'), hexc('4A5878'), hexc('9AA8C7'), hexc('2FB58A'), hexc('2FD08A')
SUP = [0.949, 0.965, 0.988, 0.85]
CARD_G = ((hexc('FFFFFF'), hexc('E6E8EC')), ([0, 0], [300, 700]))

_fonts = {}


def width(txt, font, size):
    f = os.path.join(CONFIG['fonts_dir'], {'pfb': 'playfair-display-700-italic.ttf', 'med': 'inter-500-normal.ttf', 'reg': 'inter-400-normal.ttf',
         'semi': 'inter-600-normal.ttf', 'bold': 'inter-700-normal.ttf'}[font])
    if f not in _fonts:
        t = TTFont(f)
        _fonts[f] = (t['hmtx'].metrics, t.getBestCmap(), t['head'].unitsPerEm)
    m, cmap, upm = _fonts[f]
    return sum(m.get(cmap.get(ord(c), 'space'), (upm // 2, 0))[0] for c in txt) * size / upm


CUES = []


def cue(t, name, db, why=''):
    if 0 <= t <= DUR - 0.1:
        CUES.append([t, name, db, why])


def audio_layers():
    out, kept = [], []
    for t, n, db, why in sorted(CUES):
        if n == 'flick' and any(abs(k[0] - t) < 0.11 for k in kept):
            continue
        kept.append([t, n, db, why])
    for t, n, db, why in kept:
        boost = 3 if t < 5 else (3 * (6 - t) if t < 6 else 0)
        m = SFX[n]
        start = max(0, t - m['peak_t'])
        dur = min(m['dur'], DUR - start - 0.02)
        if dur <= 0.05:
            continue
        out.append({"type": "Audio", "id": b.id(), "name": f"SFX {n} @{t:.2f}", "source": {"assetId": "sfx-" + n},
                    "sourceRange": {"start": 0, "duration": ms(dur)}, "sourceIntrinsicDuration": ms(m['dur']),
                    "volume": round(10 ** ((db + boost - m['peak_db']) / 20), 4),
                    "playback": {"type": "windowed", "inputRange": {"start": ms(start), "duration": ms(dur)},
                                 "mapping": {"type": "linear", "input": {"start": ms(start), "duration": ms(dur)}, "output": {"start": 0, "duration": ms(dur)}},
                                 "inputOffsetMs": 0}})
    with open(CONFIG['cue_sheet'], 'w') as f:
        f.write("# roughcut_v3 sound cue sheet (Rishi v2)\nVoice: rough-cut audio, 75 Hz high-pass, −1.5 dB. SFX from 01. Styles/Minimal Edit/sfx; swooshes/wooshes now full-length with fade-in (F28). Levels = target peaks in the mix (first 5 s +3 dB). Set by measurement; check on a phone.\n\n| time (s) | sound | peak dBFS | reason |\n|---|---|---|---|\n")
        for t, n, db, why in kept:
            f.write(f"| {t:.2f} | {n} | {db + (3 if t < 5 else 0)} | {why} |\n")
    return out


def vclip(name, abs_start, a_rel, d, x=540, y=960, s=100, radius=0.0, effects=None, crop=None):
    L = {"type": "Video", "id": b.id(), "name": name, "blendMode": "normal",
         "playback": {"type": "windowed", "inputRange": {"start": ms(a_rel), "duration": ms(d)},
                      "mapping": {"type": "linear", "input": {"start": ms(a_rel), "duration": ms(d)}, "output": {"start": 0, "duration": ms(d)}},
                      "inputOffsetMs": ms(abs_start + a_rel)},
         "sourceRange": {"start": ms(abs_start + a_rel), "duration": ms(d)}, "sourceIntrinsicDuration": 33400,
         "transform": tf(x, y, 540, 960, s=s), "cornerRadius": radius,
         "source": {"assetId": "aroll", "fit": "cover", "sourceRect": {"x": 0, "y": 0, "width": W, "height": H}}}
    if crop:
        L["source"]["cropRect"] = crop
    if effects:
        L["effects"] = effects
    return L


def wrapclip(clip, name, d, effects=None, x=540, y=960, s=100):
    g = b.group(name, 0, d, [clip], x=x, y=y, ax=540, ay=960, s=s)
    if effects:
        g["effects"] = effects
    return g


def M(x, y): return {"type": "moveTo", "x": x, "y": y}
def Lt(x, y): return {"type": "lineTo", "x": x, "y": y}
def Z(): return {"type": "close"}
def poly(pts): return [M(*pts[0])] + [Lt(*p) for p in pts[1:]] + [Z()]


def tick(name, a, d, x, y, c=RACC, s=1.0, w=7):
    return b.shape(name, a, d, [M(0, 18 * s), Lt(14 * s, 32 * s), Lt(40 * s, 2 * s)], stroke=(c, w * s), x=x, y=y)


def grain(amount=0.8):
    b.neff += 1
    return {"id": b.neff, "enabled": True, "effect": {"type": "grain", "amount": amount, "size": 1.6, "softness": 0.5, "seed": 7}}


def blurfx(L, t0, px, dur):
    e = b.blur(px)
    L.setdefault("effects", []).append(e)
    b.blur_in(L, e, t0, px, dur)


def reveal(L, t0=0.0, dur=0.65, dy=40, line=3, blur=18):
    """F4/F13/F20: a thin line opens from its centre into the rectangle, unblurs and rises a little. No pop."""
    b.kf(L, "scaleY", [(t0, line, LIN), (t0 + dur, 100, ES)])
    b.kf(L, "scaleX", [(t0, 96, LIN), (t0 + dur, 100, ES)])
    b.kf(L, "opacity", [(t0, 0, LIN), (t0 + dur * 0.35, 100, E1)])
    base = L["transform"]["position"][1]
    b.kf(L, "positionY", [(t0, base + dy, LIN), (t0 + dur, base, ES)])
    blurfx(L, t0, blur, dur * 0.9)


def exit_(L, t0, dur=0.55, dx=0, dy=0, blur=14):
    bx, by = L["transform"]["position"]
    if dx:
        b.kf(L, "positionX", [(t0, bx, LIN), (t0 + dur, bx + dx, EX)])
    if dy:
        b.kf(L, "positionY", [(t0, by, LIN), (t0 + dur, by + dy, EX)])
    b.kf(L, "opacity", [(t0, 100, LIN), (t0 + dur, 0, EX)])
    e = b.blur(0)
    L.setdefault("effects", []).append(e)
    b.effect_js(L, e, "blurriness", f"const t=input.time.seconds;return t<{t0}?0:{blur}*Math.min(1,(t-{t0})/{dur});")


def rise(L, t0, base_y, dy=26, dur=0.5):
    b.kf(L, "positionY", [(t0, base_y + dy, LIN), (t0 + dur, base_y, E1)])
    b.kf(L, "opacity", [(t0, 0, LIN), (t0 + dur * 0.85, 100, E1)])


def word_text(name, a, d, x, y, txt, font, size, color, t_local=0.0, just="left"):
    L = b.text(name, a, d, x, y, txt, font, size, color, just=just)
    rise(L, t_local, y)
    return L


def card_rect(name, a, d, x, y, w, h, r=28):
    """white → light-grey gradient card + soft vignette overlay (F16/F20: no blue tint)"""
    base = b.rect(name, a, d, x, y, w, h, WHITE, round_=r, ax=0, ay=0, grad=((hexc('FFFFFF'), hexc('E4E6EA')), ([0, 0], [w * 0.4, h])))
    vig = b.rect(name + " vignette", a, d, x, y, w, h, [0, 0, 0, 0], round_=r, ax=0, ay=0)
    vig["rect"]["fillPaint"] = {"type": "gradient", "gradientType": "radial", "start": [w / 2, h / 2], "end": [w * 0.75, h * 0.95],
                                "stops": [{"offset": 0, "color": [0, 0, 0, 0]}, {"offset": 0.7, "color": [0, 0, 0, 0.0]}, {"offset": 1, "color": [0, 0, 0, 0.07]}]}
    return [vig, base]


SH = lambda: {"blendMode": "normal", "blurRadius": 30, "color": [0.043, 0.07, 0.14, 0.16], "offset": [0, 14], "spreadRadius": 0, "enabled": True}
scenes, rootfx = [], []

# =====================================================================
# B1 · hook 0.72–2.87 (F1 smooth 0.72→2.0, F2 logo from behind head, F4 premium clip reveal)
A1, D1 = 0.72, 2.15
CY = 460
RX, RY, RW, RH = 815, 830, 270, 480
rclip = vclip("Result: me, premium grade", A1, 1.4, D1 - 1.4, x=RX, y=RY, s=RW / W * 100, effects=[b.huesat(14, 2)])
rshade = b.rect("Result shade", 1.4, D1 - 1.4, RX - RW / 2, RY - RH / 2, RW, RH, [0, 0, 0, 0], ax=0, ay=0, grad=(([0, 0, 0, 0], [0, 0, 0, 0.55]), ([0, RH * 0.45], [0, RH])))
rword = b.text("Result word", 1.4, D1 - 1.4, RX, RY + RH / 2 - 40, "taste", F_PFB, 58, WHITE, just="center")
rframe = b.rect("Result frame", 1.4, D1 - 1.4, RX, RY, RW + 14, RH + 14, WHITE, round_=18)
res_g = b.group("Result (my clip)", 0, D1, [rword, rshade, rclip, rframe], x=RX, y=RY, ax=RX, ay=RY)
res_g["dropShadow"] = {"blendMode": "normal", "blurRadius": 30, "color": [0, 0, 0, 0.3], "offset": [0, 16], "spreadRadius": 0, "enabled": True}
reveal(res_g, 1.43, 0.6)
cue(A1 + 1.6, 'highlighter', -22, 'result card opens (line → rectangle)')
send = b.rect("Send", 0, D1, 920, 1500, 84, 84, RACC, round_=42)
b.scale_kf(send, [(1.36, 100, LIN), (1.40, 86, LIN), (1.52, 100, E1)])
arrow = b.shape("Send arrow", 0, D1, [M(920, 1520), Lt(920, 1480), M(902, 1498), Lt(920, 1480), Lt(938, 1498)], stroke=(WHITE, 7))
cue(A1 + 1.36, 'click', -21, 'send pressed')
prompt = "edit this like a pro"
pw = width(prompt, 'reg', 44)
pt = b.text("Prompt", 0, D1, 410, 1200, "", F_REG, 44, INKD)
keys = [(0, "", HOLD)] + [(0.83 + 0.45 * i / len(prompt), prompt[:i], HOLD) for i in range(1, len(prompt) + 1)]
b.actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main", "property": {"layerId": pt["id"], "propertyType": "textContent"},
                  "keyframes": [{"id": f"pt{j}", "layerTime": ms(t), "easing": e, "value": {"type": "string", "value": v}} for j, (t, v, e) in enumerate(keys)]})
plh = b.text("Placeholder", 0, D1, 410, 1290, "Message Claude…", F_REG, 32, hexc('9AA3B5'))
b.kf(plh, "opacity", [(0.8, 100, LIN), (0.9, 0, LIN)])
cue(A1 + 0.85, 'typing', -25, 'prompt typing')
hl = b.rect("Highlighter", 0, D1, 400, 1162, pw + 22, 54, hexc('FFD68A'), round_=8, ax=0, ay=0)
b.kf(hl, "scaleX", [(1.28, 0, LIN), (1.48, 100, ES)])
cue(A1 + 1.3, 'highlighter', -21, 'highlighter swipe on prompt')
clip1 = wrapclip(vclip("Footage", A1, 0, D1, radius=0.06), "Footage → attachment", D1)
b.scale_kf(clip1, [(0, 100, LIN), (1.28, 23.5, ES)])
b.kf(clip1, "positionX", [(0, 540, LIN), (1.28, 250, ES)])
b.kf(clip1, "positionY", [(0, 960, LIN), (1.28, 1325, ES)])
cue(A1 + 0.62, 'woosh_long', -19, 'footage shrinks into chat (smooth)')
# v4 opening (O1): Claude logo (white disc + shadow) top-left and my video card top-right slide out diagonally from behind my head
def logo_disc(name, a, d, x, y):
    disc = b.shape("Logo disc", 0, 10, [], fill=WHITE, ellipse=([x, y], [176, 176]))
    lg = b.image("Claude logo", 0, 10, x, y, 118, 118, "logo-claude")
    g = b.group(name, a, d, [lg, disc], x=x, y=y, ax=x, ay=y)
    g["dropShadow"] = {"blendMode": "normal", "blurRadius": 34, "color": [0, 0, 0, 0.38], "offset": [0, 10], "spreadRadius": 2, "enabled": True}
    return g


LX, LY, VX, VY, VS = 250, 610, 830, 620, 20.4
logoA = logo_disc("Claude logo (from behind head)", 0, A1, LX, LY)
b.kf(logoA, "positionX", [(0, 540, LIN), (0.6, LX, ES)])
b.kf(logoA, "positionY", [(0, 660, LIN), (0.6, LY, ES)])
b.scale_kf(logoA, [(0, 62, LIN), (0.6, 100, ES)])
b.kf(logoA, "opacity", [(0, 0, LIN), (0.12, 100, E1)])
b.js(logoA, "rotation", "return 6*Math.sin(input.time.seconds*2*Math.PI/3);")
vcard = [vclip("My video (card)", 0, 0, 1.05, x=VX, y=VY, s=VS), b.rect("Video card frame", 0, 10, VX, VY, W * VS / 100 + 14, H * VS / 100 + 14, WHITE, round_=18)]
vidA = b.group("My video card (from behind head)", 0, A1, vcard, x=VX, y=VY, ax=VX, ay=VY)
vidA["dropShadow"] = {"blendMode": "normal", "blurRadius": 34, "color": [0, 0, 0, 0.4], "offset": [0, 12], "spreadRadius": 2, "enabled": True}
b.kf(vidA, "positionX", [(0, 540, LIN), (0.6, VX, ES)])
b.kf(vidA, "positionY", [(0, 660, LIN), (0.6, VY, ES)])
b.scale_kf(vidA, [(0, 62, LIN), (0.6, 100, ES)])
b.kf(vidA, "opacity", [(0, 0, LIN), (0.12, 100, E1)])
rootfx += [logoA, vidA]
cue(0.3, 'woosh_long', -21, 'logo + video slide out from behind head')
# after 0.72 s (no matte needed: both sit clear of the head): logo flies to the header and keeps a slow spin; video card drifts off
logoB = logo_disc("Claude logo → header", 0, D1, LX, LY)
b.kf(logoB, "positionX", [(0, LX, LIN), (1.1, 150, ES)])
b.kf(logoB, "positionY", [(0, LY, LIN), (1.1, CY + 60, ES)])
b.scale_kf(logoB, [(0, 100, LIN), (1.1, 47, ES)])
b.js(logoB, "rotation", "return 6*Math.sin((input.time.seconds+0.72)*2*Math.PI/3);")
vcard2 = [vclip("My video (card)", A1, 0, 0.45, x=VX, y=VY, s=VS), b.rect("Video card frame", 0, 10, VX, VY, W * VS / 100 + 14, H * VS / 100 + 14, WHITE, round_=18)]
vidB = b.group("My video card (drifts off)", 0, 0.45, vcard2)
exit_(vidB, 0.0, 0.42, dx=120, dy=-60, blur=14)
card = [plh, b.rect("Input", 0, D1, 100, 1080, 880, 500, hexc('FAFBFD'), round_=28, stroke=(hexc('E3E7EE'), 3), ax=0, ay=0),
        b.rect("Header rule", 0, D1, 70, CY + 120, 940, 2, hexc('E3E7EE'), ax=0, ay=0),
        b.text("Claude", 0, D1, 200, CY + 74, "Claude", F_SEMI, 42, INKD),
        b.rect("Chat card", 0, D1, 70, CY, 940, 1140, WHITE, round_=36, ax=0, ay=0)]
card_g = b.group("Chat card", 0, D1, card, x=540, y=1030, ax=540, ay=1030)
card_g["dropShadow"] = SH()
b.scale_kf(card_g, [(0.1, 94, LIN), (1.1, 100, ES)])
b.kf(card_g, "opacity", [(0.1, 0, LIN), (0.6, 100, E1)])
s1 = b.group("B1 Hook chat", A1, D1, [logoB, vidB, res_g, clip1, send, arrow, pt, hl, card_g,
                                      b.rect("Ice", 0, D1, 0, 0, W, H, ICE, ax=0, ay=0, effects=[grain(0.8)])])
scenes.append(s1)
cue(2.87, 'flicker', -21, 'snap to black & white + tracking')

# =====================================================================
# B3 + B4 · split pane 5.33–12.21 (F7 framing, F8 captions in white, F9–F14)
AP, DP, PH = 5.33, 6.88, 940
GH_SZ = 34
names6 = ['video-editor.md', 'caption-pro.md', 'hooks.md', 'motion-kit.md', 'color-grade.md', 'b-roll.md']
fs = min(28, 28 * 206 / max(width(n, 'med', 28) for n in names6))
wall = []
for i, f in enumerate(names6):
    r, c = divmod(i, 3)
    x, y = 70 + c * 320, 380 + r * 116
    t0 = 0.69 + i * 0.18
    ls = [b.text("File", 0, 10, x + 70, y + 58, f, F_MED, round(fs, 1), INKD),
          b.image("GitHub", 0, 10, x + 40, y + 48, GH_SZ, GH_SZ, "logo-github-k"),
          b.rect("Card", 0, 10, x, y, 300, 96, WHITE, round_=16, stroke=(hexc('D9DDE3'), 2), ax=0, ay=0)]
    g = b.group("Skill card " + f, t0, DP - t0, ls, x=x + 150, y=y + 48, ax=x + 150, ay=y + 48)
    rise(g, 0, y + 48, dy=34, dur=0.55)
    blurfx(g, 0, 10, 0.45)
    wall.append(g)
    cue(AP + t0 + 0.15, 'pop', -24 + (i % 2), 'skill card settles')
for i, (n, st) in enumerate([('awesome-edits', '12.4k'), ('reel-templates', '8.1k'), ('ai-video-tools', '21k')]):
    y = 616 + i * 94
    t0 = 1.52 + i * 0.2
    ls = [b.text("Stars", 0, 10, 870, y + 52, "★ " + st, F_REG, 28, MUTE_INK, just="right"),
          b.text("Repo", 0, 10, 290, y + 52, n, F_SEMI, 32, RTXT),
          b.image("GitHub", 0, 10, 250, y + 40, 40, 40, "logo-github-w"),
          b.rect("Repo card", 0, 10, 200, y, 700, 80, RCARD, round_=16, ax=0, ay=0)]
    g = b.group("Repo card " + n, t0, DP - t0, ls)
    g["dropShadow"] = {"blendMode": "normal", "blurRadius": 24, "color": [0, 0, 0, 0.22], "offset": [0, 10], "spreadRadius": 0, "enabled": True}
    b.kf(g, "positionX", [(0, 820, LIN), (0.75, 0, E1)])
    b.fade_in(g, 0, 0.3)
    wall.append(g)
    cue(AP + t0 + 0.2, 'swoosh_long', -26, 'repo card glides in')
wall_g = b.group("B3 wall", 0, DP, list(reversed(wall)), x=540, y=600, ax=540, ay=600)
exit_(wall_g, 2.77, 0.5, dy=-40, blur=12)        # F12: leaves smoothly while the next set arrives
T4 = 3.15
DT = DP - T4
doc_lines = [("design-skill.md", F_SEMI, 32, INKD), ("## taste", F_MED, 26, RACC), ("palette · type · pacing", F_REG, 26, MUTE_ICE),
             ("## captions", F_MED, 26, RACC), ("serif hero · 48 px support", F_REG, 26, MUTE_ICE), ("## motion", F_MED, 26, RACC),
             ("ease-out · no bounce", F_REG, 26, MUTE_ICE), ("## sound", F_MED, 26, RACC), ("dense but quiet", F_REG, 26, MUTE_ICE)]
dl = [word_text("Doc line", 0, DT, 112, 442 + i * 44 + (10 if i else 0), t_, f_, s_, c_, t_local=0.77 + i * 0.12) for i, (t_, f_, s_, c_) in enumerate(doc_lines)]
doc_g = b.group("design-skill.md", 0, DT, dl + card_rect("Doc card", 0, DT, 80, 380, 440, 470, 22), x=300, y=615, ax=300, ay=615)
doc_g["dropShadow"] = SH()
reveal(doc_g, 0.22, 0.7)
cue(AP + T4 + 0.3, 'highlighter', -22, 'design-skill.md opens (line → rectangle)')
for i in range(len(doc_lines)):
    cue(AP + T4 + 0.77 + i * 0.12, 'flick', -30, 'doc line')
OX, OY, K = 800, 600, 0.85
blob = b.shape("Painted figure", 0, DT, [M(OX - 20 * K, OY - 150 * K), {"type": "cubicTo", "c1x": OX + 80 * K, "c1y": OY - 170 * K, "c2x": OX + 130 * K, "c2y": OY - 60 * K, "x": OX + 110 * K, "y": OY + 20 * K},
                                        {"type": "cubicTo", "c1x": OX + 95 * K, "c1y": OY + 90 * K, "c2x": OX + 40 * K, "c2y": OY + 150 * K, "x": OX - 30 * K, "y": OY + 140 * K},
                                        {"type": "cubicTo", "c1x": OX - 110 * K, "c1y": OY + 130 * K, "c2x": OX - 140 * K, "c2y": OY + 40 * K, "x": OX - 120 * K, "y": OY - 40 * K},
                                        {"type": "cubicTo", "c1x": OX - 100 * K, "c1y": OY - 120 * K, "c2x": OX - 70 * K, "c2y": OY - 145 * K, "x": OX - 20 * K, "y": OY - 150 * K}, Z()],
                 grad=((hexc('5D8BFF'), hexc('0839B0')), ([OX - 120, OY - 150], [OX + 110, OY + 140])), effects=[grain(1.0)])
halo = b.shape("Halo", 0, DT, [], fill=[0.24, 0.48, 0.98, 1], ellipse=([OX, OY], [360, 360]), effects=[b.blur(55)])
halo["shape"]["fills"][0]["opacity"] = 0.22
fig = b.group("Centre illustration", 0, DT, [blob, halo], x=OX, y=OY, ax=OX, ay=OY)
b.scale_kf(fig, [(0.07, 72, LIN), (0.75, 100, ES)])
b.kf(fig, "opacity", [(0.07, 0, LIN), (0.45, 100, E1)])
blurfx(fig, 0.07, 18, 0.6)
b.js(fig, "rotation", "return 3*Math.sin(input.time.seconds*1.2);")
cue(AP + T4 + 0.1, 'woosh_long', -23, 'illustration paints in')
orbit = []
for k, w in enumerate(['palette', 'practice', 'rhythm', 'sound design', 'pacing', 'texture', 'timing', 'typography']):
    ww = width(w, 'med', 24)
    o = b.text("Orbit " + w, 0.15, DT - 0.15, 0, 0, w, F_MED, 24, INKD, ax=ww / 2, ay=-10)
    ph = k * math.pi / 4
    TH = f"const t=input.time.seconds;const th={ph}+2*Math.PI*(1.1*(1-Math.exp(-t/0.9))+0.05*t);"   # F14: fast start, settles slow
    b.js(o, "positionX", TH + f"return {OX}+205*Math.cos(th);")
    b.js(o, "positionY", TH + f"return {OY}+150*Math.sin(th);")
    b.js(o, "opacity", TH + f"return Math.min(1,Math.max(0,(t-{0.06*k})/0.5))*(55+45*Math.sin(th));")
    orbit.append(o)
taste_g = b.group("B4 taste", T4, DT, orbit + [fig, doc_g])
pane = b.group("Split pane", AP, DP, [taste_g, wall_g, b.rect("Pane edge", 0, DP, 0, PH - 3, W, 6, [0, 0, 0, 0.12], ax=0, ay=0),
                                      b.rect("Pane ice", 0, DP, 0, 0, W, PH, ICE, ax=0, ay=0, effects=[grain(0.8)])])
b.kf(pane, "positionY", [(0, -PH, LIN), (1.0, 0, ES), (6.18, 0, LIN), (6.88, -PH, EX)])
cue(AP + 0.5, 'swoosh_long', -18, 'pane swipes down')
cue(11.86, 'swoosh_long', -20, 'pane lifts')
scenes.append(pane)

# =====================================================================
# B5 · proof 12.72–14.56 : timeline card behind head (F16), cut hidden in zoom (F15, on the A-roll)
A5, D5 = 12.72, 1.84
lanes = []
seg = {0: [(300, 950)], 1: [(300, 380), (395, 470), (485, 600), (615, 700), (715, 820), (835, 950)],
       2: [(330, 470), (560, 690), (760, 900)], 3: [(320, 350), (420, 445), (520, 560), (640, 660), (740, 780), (880, 905)]}
gcol = [(hexc('7FA2F2'), hexc('C9D8FA')), (hexc('2F6BF0'), hexc('8FB1F7')), (hexc('5C83DA'), hexc('B4C7EE')), (hexc('A9BBDF'), hexc('DCE4F3'))]
for i, lab in enumerate(['A-roll', 'captions', 'graphics', 'sfx']):
    y = 430 + i * 64
    ls = [b.text("Lane " + lab, 0, 10, 130, y + 30, lab, F_MED, 26, MUTE_ICE)]
    ls += [b.rect("Clip", 0, 10, x0, y, x1 - x0, 40, gcol[i][0], round_=7, ax=0, ay=0, grad=(gcol[i], ([0, 0], [x1 - x0, 40]))) for x0, x1 in seg[i]]
    g = b.group("Lane " + lab, 0.45 + i * 0.1, D5 - 0.45 - i * 0.1, ls)
    b.kf(g, "positionX", [(0, -40, LIN), (0.45, 0, E1)])
    b.fade_in(g, 0, 0.3)
    lanes.append(g)
    cue(A5 + 0.45 + i * 0.1, 'flick', -27, 'lane slides in')
play = b.rect("Playhead", 0.7, D5 - 0.7, 300, 410, 4, 280, hexc('E5484D'), ax=0, ay=0)
b.kf(play, "positionX", [(0, 300, LIN), (D5 - 0.7, 900, LIN)])
pill = [b.text("Pill role", 0, D5, 196, 330, "edited this entire video", F_REG, 26, hexc('7A8295')),
        b.text("Pill name", 0, D5, 196, 298, "Claude", F_BOLD, 32, INKD),
        b.image("Claude mark", 0, D5, 156, 305, 50, 50, "logo-claude"),
        b.rect("Pill sep", 0, D5, 120, 372, 840, 2, hexc('DDE1E7'), ax=0, ay=0)]
tl = b.group("Timeline card", 0, D5, [play] + lanes + pill + card_rect("Card", 0, D5, 90, 250, 900, 460, 14), x=540, y=480, ax=540, ay=480)
tl["dropShadow"] = {"blendMode": "normal", "blurRadius": 30, "color": [0, 0, 0, 0.22], "offset": [0, 12], "spreadRadius": 0, "enabled": True}
reveal(tl, 0, 0.7)
cue(A5 + 0.15, 'woosh_long', -20, 'timeline card behind head')
s5 = b.group("B5 Timeline behind head", A5, D5, [tl])
scenes.append(s5)

# =====================================================================
# B6 · slop wall 14.56–17.45 (F17 starts on "why", slow, holds; F18 white tiles "slop")
A6, D6 = 14.56, 2.89
TW, THt, GAP = 300, 533.33, 30
myx, myy = 540, 623 + THt / 2
tiles = []
k = 0
for row in range(4):
    for col in range(3):
        if (row, col) == (1, 1):
            continue
        x, y = 60 + col * (TW + GAP), 60 + row * (THt + GAP)
        ang = (k * 47) % 180
        p0 = [TW / 2 - 200 * math.cos(math.radians(ang)), THt / 2 - 200 * math.sin(math.radians(ang))]
        p1 = [TW / 2 + 200 * math.cos(math.radians(ang)), THt / 2 + 200 * math.sin(math.radians(ang))]
        sweep = b.rect("Sweep", 0, 10, x, y, TW, THt, [1, 1, 1, 0], round_=8, ax=0, ay=0, grad=(([1, 1, 1, 0], [1, 1, 1, 0.75]), ([0, 0], [TW, THt])))
        b.js(sweep, "opacity", f"return 50+50*Math.sin(input.time.seconds*0.9+{k * 0.7});")     # gradient drifts very slowly
        txt = b.text("slop", 0, 10, x + TW / 2, y + THt / 2 + 26, "slop", F_BOLD, 76, hexc('6B7079'), just="center")
        txt["dropShadow"] = {"blendMode": "normal", "blurRadius": 10, "color": [1, 1, 1, 0.8], "offset": [0, -3], "spreadRadius": 0, "enabled": True}
        ls = ([] if (row, col) == (2, 1) else [txt]) + [sweep, b.rect("Tile", 0, 10, x, y, TW, THt, WHITE, round_=8, ax=0, ay=0, grad=((hexc('FFFFFF'), hexc('C8CCD2')), (p0, p1)))]
        g = b.group(f"Slop tile {k+1}", 0, D6, ls, effects=[b.blur(2.5)])
        tiles.append(g)
        k += 1
glow = b.rect("My tile glow", 0, D6, myx, myy, TW + 24, THt + 24, WHITE, round_=14, effects=[b.blur(26)])
b.kf(glow, "opacity", [(0.9, 0, LIN), (1.5, 70, E1)])
myclip = vclip("Me (tile 2 from top)", A6, 0, D6, x=myx, y=myy, s=TW / W * 100, radius=0.035)
BX, BY = 540, 1186 + THt / 2           # tile directly below me
wcap = []
for wi in range(71, 86):
    w_ = WORDS[wi]['w']
    ta_ = WORDS[wi]['s'] - A6
    tb_ = (WORDS[wi + 1]['s'] if wi < 85 else A6 + D6) - A6
    Sz = min(96, 96 * 250 / max(1, width(w_, 'pfb', 96)))
    L = b.text("Wall word " + w_, max(0, ta_), tb_ - max(0, ta_), BX, BY + Sz * 0.32, w_, F_PFB, round(Sz, 1), [0, 0, 0, 1], just="center")
    b.kf(L, "opacity", [(0, 0, LIN), (0.12, 100, E1)])
    wcap.append(L)
    cue(WORDS[wi]['s'] + 0.03, 'flick', -27, 'wall word')
cam = b.group("Wall camera", 0, D6, wcap + [myclip, glow] + tiles, x=540, y=960, ax=myx, ay=myy, s=360)
b.scale_kf(cam, [(0, 360, LIN), (1.45, 100, ES), (D6, 102.5, LIN)])
b.kf(cam, "positionY", [(0, 960, LIN), (1.45, myy, ES)])
cue(A6 + 0.75, 'swoosh_long', -18, 'slow zoom out to the wall')
cue(A6 + 1.45, 'flicker', -24, 'wall settles')
s6 = b.group("B6 Slop wall", A6, D6, [cam, b.rect("Wall bg", 0, D6, 0, 0, W, H, hexc('0D0E12'), ax=0, ay=0)])
scenes.append(s6)

# =====================================================================
# B7 + B8 · PiP layout 18.50–27.55 (v4: rounded PiP, one card with swapping contents, return after "intervention")
A7, D7 = 18.50, 9.05
PUN = 1.18                            # headspace-cropped framing (also used on the A-roll around the PiP)
PUNY = 1920 - 960 * PUN
PS = 32
PY_ = 1270


def rrect(x, y, w, h, r):
    k = 0.5523 * r
    C = lambda c1x, c1y, c2x, c2y, ex, ey: {"type": "cubicTo", "c1x": c1x, "c1y": c1y, "c2x": c2x, "c2y": c2y, "x": ex, "y": ey}
    return [M(x + r, y), Lt(x + w - r, y), C(x + w - r + k, y, x + w, y + r - k, x + w, y + r), Lt(x + w, y + h - r),
            C(x + w, y + h - r + k, x + w - r + k, y + h, x + w - r, y + h), Lt(x + r, y + h),
            C(x + r - k, y + h, x, y + h - r + k, x, y + h - r), Lt(x, y + r), C(x, y + r - k, x + r - k, y, x + r, y), Z()]


clip7 = vclip("Me (headspace cropped)", A7, 0, D7, x=540, y=PUNY, s=PUN * 100)
pip = wrapclip(clip7, "Me → PiP → full", D7)
pip["masks"] = [{"id": 1, "mode": "add", "opacity": 100, "inverted": False, "feather": [0, 0], "path": {"commands": rrect(0, 0, W, H, 100)}}]
GROW = 8.25                            # 26.75 s: after "intervention" and its caption
b.scale_kf(pip, [(0, 100, LIN), (0.9, PS, ES), (GROW, PS, LIN), (GROW + 0.8, 100, ES)])
b.kf(pip, "positionX", [(0, 540, LIN), (0.9, 540, ES), (GROW, 540, LIN), (GROW + 0.8, 540, ES)])
b.kf(pip, "positionY", [(0, 960, LIN), (0.9, PY_, ES), (GROW, PY_, LIN), (GROW + 0.8, 960, ES)])
pw_, ph_ = W * PS / 100, H * PS / 100
pipb = b.rect("PiP border", 0.75, GROW - 0.7, 540, PY_, pw_ + 12, ph_ + 12, WHITE, round_=36)
pipb["dropShadow"] = {"blendMode": "normal", "blurRadius": 30, "color": [0.55, 0.62, 1.0, 0.9], "offset": [0, 0], "spreadRadius": 4, "enabled": True}
b.kf(pipb, "opacity", [(0, 0, LIN), (0.3, 100, E1), (GROW - 0.9, 100, LIN), (GROW - 0.75, 0, LIN)])
cue(A7 + 0.45, 'woosh_long', -19, 'smooth move into the PiP')
cue(A7 + GROW + 0.4, 'woosh_long', -20, 'back to full screen after "intervention"')
# ---- the card (stays the whole time); header stays, contents swap
hdr = [word_text("Header", 0, 10, 214, 334, "Claude", F_SEMI, 40, INKD, t_local=0.25)]
ci = b.image("Claude mark", 0, 10, 172, 320, 52, 52, "logo-claude"); b.fade_in(ci, 0.25, 0.3); hdr.append(ci)
hdr.append(word_text("Awake", 0, 10, 930, 332, "awake", F_SEMI, 28, TEAL, t_local=0.35, just="right"))
dot = b.shape("Awake dot", 0, 10, [], fill=TEAL, ellipse=([822, 322], [16, 16])); b.fade_in(dot, 0.35, 0.3); hdr.append(dot)
hdr.append(b.rect("Header rule", 0, 10, 140, 372, 800, 2, hexc('DDE1E7'), ax=0, ay=0))
ca = []
fg = b.group("Folder icon", 0, 10, [b.rect("Folder tab", 0, 10, 150, 412, 24, 10, hexc('E9C95A'), round_=3, ax=0, ay=0), b.rect("Folder", 0, 10, 150, 418, 46, 32, hexc('E9C95A'), round_=6, ax=0, ay=0)])
b.fade_in(fg, 0.5, 0.3); ca.append(fg)
ca.append(word_text("Folder", 0, 10, 214, 446, "paper-stage-edit/", F_SEMI, 34, INKD, t_local=0.5))
cue(A7 + 0.8, 'flick', -27, 'folder row')
picks = {'RULEBOOK.md': (1.59, ["what", "to", "do"]), 'LOOKBOOK.md': (2.04, ["how", "to", "do", "it"])}
for i, n in enumerate(['SKILL.md', 'RULEBOOK.md', 'LOOKBOOK.md', 'SOUND.md']):
    y = 478 + i * 72
    t0 = 0.65 + i * 0.12
    if n in picks:
        tc, lab = picks[n]
        tl_ = tc - 0.3
        hlr = b.rect("Row highlight", 0, 10, 120, y, 840, 70, hexc('E3F6EE'), round_=12, ax=0, ay=0)
        b.kf(hlr, "opacity", [(tl_, 0, LIN), (tl_ + 0.25, 100, E1)])
        tk = tick("Tick", 0, 10, 900, y + 18)
        b.scale_kf(tk, [(tl_, 60, LIN), (tl_ + 0.25, 100, E1)]); b.kf(tk, "opacity", [(tl_, 0, LIN), (tl_ + 0.15, 100, E1)])
        lw = sum(width(w + ' ', 'semi', 28) for w in lab) + 30
        lp = b.rect("Label pill", 0, 10, 540, y + 13, lw, 46, INKD, round_=12, ax=0, ay=0)
        b.kf(lp, "opacity", [(tl_ + 0.04, 0, LIN), (tl_ + 0.25, 100, E1)])
        ca += [hlr, tk, lp]
        xx = 556
        for j, w in enumerate(lab):
            ca.append(word_text("Label word", 0, 10, xx, y + 46, w, F_SEMI, 28, WHITE, t_local=tl_ + 0.08 + j * 0.1))
            cue(A7 + tc + 0.08 + j * 0.1, 'flick', -29, 'label word')
            xx += width(w + ' ', 'semi', 28)
        cue(A7 + tc, 'hitech', -19, 'tick: ' + n)
    ic = b.rect("File icon", 0, 10, 158, y + 14, 30, 42, hexc('DDE2E9'), round_=5, ax=0, ay=0); b.fade_in(ic, t0, 0.3)
    ca += [ic, word_text("File row", 0, 10, 214, y + 48, n, F_REG, 34, INKD, t_local=t0)]
    cue(A7 + 0.3 + t0, 'flick', -28, 'file row')
PY7 = 800
ca.append(b.rect("Progress track", 0, 10, 150, PY7, 620, 20, hexc('DEE2E7'), round_=10, ax=0, ay=0))
pf = b.rect("Progress fill", 0, 10, 150, PY7, 620, 20, RACC, round_=10, ax=0, ay=0)
b.kf(pf, "scaleX", [(2.2, 3, LIN), (3.2, 100, ES)])
ca.append(pf)
pct = b.text("100%", 0, 10, 800, PY7 + 22, "100%", F_BOLD, 34, RACC); b.kf(pct, "opacity", [(3.15, 0, LIN), (3.4, 100, E1)]); ca.append(pct)
cue(A7 + 2.5, 'highlighter', -21, 'progress fills (slower)')
cue(A7 + 3.5, 'risertick', -20, 'progress lands at 100%')
contA = b.group("Contents A (files)", 0, 10, list(reversed(ca)))
exit_(contA, 3.5, 0.6, dx=-300, blur=14)          # v4: only the contents slide left + blur + fade
cue(A7 + 3.85, 'swoosh_long', -21, 'card contents swap')
# contents B: pipeline, word by word, evenly spaced in the card body
pl = []
ticks_t = [23.6, 24.0, 24.45, 24.85, 25.19]
ROWY = [438, 526, 614, 702, 790]
for i, lab in enumerate(['Analyse', 'Plan', 'Build', 'Captions', 'Export']):
    y = ROWY[i]
    tr = 3.95 + i * 0.15
    pl.append(word_text("Step " + lab, 0, 10, 180, y + 15, lab, F_MED, 42, INKD, t_local=tr))
    cue(A7 + 0.3 + tr, 'flick', -28, 'step label')
    if i < 4:
        sep = b.rect("Row rule", 0, 10, 160, y + 44, 760, 1.5, hexc('E1E4E9'), ax=0, ay=0)
        b.kf(sep, "opacity", [(tr, 0, LIN), (tr + 0.4, 100, E1)])
        pl.append(sep)
    ring = b.shape("Pending", 0, 10, [], stroke=(hexc('C3C9D3'), 4), ellipse=([880, y], [36, 36]))
    tt = ticks_t[i] - (A7 + 0.3)
    b.kf(ring, "opacity", [(tr, 0, LIN), (tr + 0.3, 100, E1), (tt, 100, LIN), (tt + 0.06, 0, LIN)])
    tk = tick("Tick " + lab, 0, 10, 860, y - 18)
    b.scale_kf(tk, [(tt, 50, LIN), (tt + 0.25, 100, E1)]); b.kf(tk, "opacity", [(tt, 0, LIN), (tt + 0.12, 100, E1)])
    pl += [ring, tk]
    if i < 4:
        cue(ticks_t[i], 'techpop', -20, 'tick ' + lab)
contB = b.group("Contents B (pipeline)", 0, 10, pl)
cardA = b.group("Card (stays)", 0.3, D7 - 0.3, [contB, contA] + hdr + card_rect("Card", 0, 10, 110, 250, 860, 620, 28), x=540, y=560, ax=540, ay=560)
cardA["dropShadow"] = SH()
reveal(cardA, 0.3, 0.7)
exit_(cardA, GROW - 0.3 - 0.45, 0.42, dy=-50, blur=14)
cue(A7 + 0.55, 'highlighter', -23, 'Claude card opens')
s7 = b.group("B7+B8 PiP layout", A7, D7, [cardA, pip, pipb,
                                         b.rect("Board bg", 0, D7, 0, 0, W, H, WHITE, ax=0, ay=0, grad=((hexc('F4F5F7'), hexc('E2E4E8')), ([0, 0], [0, H])), effects=[grain(0.6)])])
scenes.append(s7)

# =====================================================================
# B9 · CTA 29.10–32.55 (F24 smoother + longer, F25 tap + green tick, F26 single-line captions)
A9, D9 = 29.10, 4.3
cb = b.blur(0)
inner9 = vclip("Me (moves up, blurred)", A9, 0, D9, effects=[cb])
b.effect_js(inner9, cb, "blurriness", "let t=input.time.seconds;if(t>20)t-=%s;return t<0.8?24*Math.max(0,t)/0.8:24;" % A9)
clip9 = wrapclip(inner9, "Me (move + blur)", D9)
b.kf(clip9, "positionX", [(0, 540, LIN), (D9, 540, LIN)])
b.kf(clip9, "positionY", [(0, 960, LIN), (0.8, 560, ES)])
dim = b.rect("Dim", 0, D9, 0, 0, W, H, [0, 0, 0, 1], ax=0, ay=0)
b.kf(dim, "opacity", [(0, 0, LIN), (0.8, 45, ES)])
SY = 980
sh = [b.rect("Sheet", 0, D9, 0, SY, W, 1000, hexc('1C1C1E'), round_=40, ax=0, ay=0),
      b.rect("Handle", 0, D9, 495, SY + 22, 90, 10, hexc('5A5A5E'), round_=5, ax=0, ay=0),
      b.text("Comments", 0, D9, 540, SY + 86, "Comments", F_BOLD, 34, WHITE, just="center"),
      b.image("Avatar", 0, D9, 106, SY + 166, 84, 84, "avatar2"),
      b.rect("Field", 0, D9, 168, SY + 124, 712, 84, hexc('1C1C1E'), round_=42, stroke=(hexc('3A3A3C'), 3), ax=0, ay=0)]
ph_ = b.text("Placeholder", 0, D9, 204, SY + 178, "Add a comment…", F_REG, 32, hexc('8E8E93'))
press = {'E': 0.45, 'D': 0.65, 'I': 0.85, 'T': 1.05}
b.kf(ph_, "opacity", [(0.43, 100, HOLD), (0.45, 0, HOLD)])
typed = b.text("Typed", 0, D9, 204, SY + 180, "", F_SEMI, 36, WHITE)
tk_ = [(0, "", HOLD)]
s_ = ""
for ch, t in press.items():
    s_ += ch
    tk_.append((t, s_, HOLD))
b.actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main", "property": {"layerId": typed["id"], "propertyType": "textContent"},
                  "keyframes": [{"id": f"ty{j}", "layerTime": ms(t), "easing": e, "value": {"type": "string", "value": v}} for j, (t, v, e) in enumerate(tk_)]})
caret = b.rect("Caret", 0, D9, 204, SY + 146, 3, 44, RACC, ax=0, ay=0)
cw = [width(s_[:i], 'semi', 36) for i in range(5)]
b.js(caret, "positionX", "const t=input.time.seconds;const P=%s;const W=%s;let i=0;for(const p of P){if(t>=p)i++;}return 206+W[i];" % (json.dumps(list(press.values())), json.dumps(cw)))
b.js(caret, "opacity", "const t=input.time.seconds;return t>1.25?0:((Math.floor(t/0.5)%2==0||t<1.1)?100:0);")
TAP = 1.25
sendb = b.rect("Send", 0, D9, 950, SY + 166, 74, 74, RACC, round_=37)
b.kf(sendb, "fillColor", [(TAP + 0.04, RACC, LIN), (TAP + 0.2, GREEN, E1)], color=True)
b.scale_kf(sendb, [(TAP, 100, LIN), (TAP + 0.06, 86, LIN), (TAP + 0.3, 100, E1)])
sarrow = b.shape("Send arrow", 0, D9, [M(950, SY + 184), Lt(950, SY + 148), M(934, SY + 164), Lt(950, SY + 148), Lt(966, SY + 164)], stroke=(WHITE, 6))
b.kf(sarrow, "opacity", [(TAP + 0.05, 100, LIN), (TAP + 0.12, 0, LIN)])
stick = tick("Send tick", TAP + 0.1, D9 - TAP - 0.1, 930, SY + 148, c=WHITE, s=1.0, w=6)
b.scale_kf(stick, [(0, 50, LIN), (0.25, 100, E1)]); b.fade_in(stick, 0, 0.12)
tapdot = b.shape("Tap dot", TAP - 0.02, 0.6, [], fill=[1, 1, 1, 1], ellipse=([950, SY + 166], [96, 96]), effects=[b.blur(6)])
tapdot["shape"]["fills"][0]["opacity"] = 0.55
b.scale_kf(tapdot, [(0, 55, LIN), (0.45, 125, E1)])
b.kf(tapdot, "opacity", [(0, 0, LIN), (0.08, 100, LIN), (0.5, 0, E1)])
tapdot["transform"]["anchorPoint"] = [950, SY + 166]; tapdot["transform"]["position"] = [950, SY + 166]
sh += [ph_, typed, caret, sendb, sarrow, stick, tapdot]
cue(A9 + TAP, 'click', -20, 'tap on send')
cue(A9 + TAP + 0.12, 'pop', -20, 'send turns green ✓')
KY = SY + 240
sh.append(b.rect("Keyboard", 0, D9, 0, KY, W, 1920 - KY, hexc('2C2C2E'), ax=0, ay=0))
sug = b.text("Suggestion", 0, D9, 540, KY + 62, "", F_REG, 34, WHITE, just="center")
b.actions.append({"type": "setFxPropertyKeyframes", "compositionId": "main", "property": {"layerId": sug["id"], "propertyType": "textContent"},
                  "keyframes": [{"id": f"sg{j}", "layerTime": ms(t), "easing": HOLD, "value": {"type": "string", "value": ('"' + v + '"') if v else ""}} for j, (t, v, e) in enumerate(tk_)]})
sh += [sug, b.text("Sug L", 0, D9, 180, KY + 62, "edit", F_REG, 34, hexc('B0B0B5'), just="center"),
       b.text("Sug R", 0, D9, 900, KY + 62, "Edit", F_REG, 34, hexc('B0B0B5'), just="center"),
       b.rect("Sep", 0, D9, 360, KY + 26, 2, 50, hexc('48484A'), ax=0, ay=0), b.rect("Sep", 0, D9, 720, KY + 26, 2, 50, hexc('48484A'), ax=0, ay=0)]
KW, KH, KG = 94, 108, 12
kpos = {}
for letters, x0, y in [("QWERTYUIOP", 16, KY + 110), ("ASDFGHJKL", 69, KY + 235), ("ZXCVBNM", 159, KY + 360)]:
    for i, ch in enumerate(letters):
        x = x0 + i * (KW + KG)
        kpos[ch] = (x, y)
        sh += [b.rect("Key " + ch, 0, D9, x, y, KW, KH, hexc('6C6C70'), round_=14, ax=0, ay=0),
               b.text("Key label " + ch, 0, D9, x + KW / 2, y + 72, ch, F_REG, 46, WHITE, just="center")]
for lab, x, w_ in [("shift", 16, 125), ("del", 939, 125)]:
    sh.append(b.rect("Key " + lab, 0, D9, x, KY + 360, w_, KH, hexc('48484A'), round_=14, ax=0, ay=0))
sh += [b.rect("Key 123", 0, D9, 16, KY + 485, 230, KH, hexc('48484A'), round_=14, ax=0, ay=0),
       b.text("123", 0, D9, 131, KY + 553, "123", F_REG, 36, WHITE, just="center"),
       b.rect("Space", 0, D9, 258, KY + 485, 564, KH, hexc('6C6C70'), round_=14, ax=0, ay=0),
       b.text("space", 0, D9, 540, KY + 553, "space", F_REG, 36, WHITE, just="center"),
       b.rect("Return", 0, D9, 834, KY + 485, 230, KH, hexc('48484A'), round_=14, ax=0, ay=0),
       b.text("return", 0, D9, 949, KY + 553, "return", F_REG, 36, WHITE, just="center")]
pops = []
for ch, t in press.items():
    x, y = kpos[ch]
    pk = [b.text("Pop letter", 0, 0.18, x + KW / 2, y - 40, ch, F_REG, 72, WHITE, just="center"),
          b.rect("Pop bubble", 0, 0.18, x - 13, y - 130, KW + 26, 150, hexc('8E8E93'), round_=18, ax=0, ay=0),
          b.rect("Key lit", 0, 0.18, x, y, KW, KH, hexc('8E8E93'), round_=14, ax=0, ay=0)]
    pops.append(b.group("Key press " + ch, t, 0.18, pk))
    cue(A9 + t, 'click', -24, 'key ' + ch)
sheet = b.group("Comments sheet", 0, D9, pops + list(reversed(sh)))
b.kf(sheet, "positionY", [(0, 1000, LIN), (0.8, 0, E1), (3.95, 0, LIN), (4.3, 1000, EX)])
cue(A9 + 0.3, 'swoosh_long', -18, 'comment sheet + keyboard rise (smooth)')
cue(A9 + 4.05, 'swoosh_long', -21, 'sheet slides down as the video ends')
s9 = b.group("B9 Comments CTA", A9, D9, [sheet, dim, clip9, b.rect("Under", 0, D9, 0, 0, W, H, hexc('0D0E12'), ax=0, ay=0)])
scenes.append(s9)

# =====================================================================
# A-roll motion (one JS for video + matte): B&W tracking 2.87–5.33, split reframe, cut-hiding zoom, PiP-matched framings
f = json.load(open(CONFIG['face']))
nose = [(s['t'], s['nose'][0], s['nose'][1]) for s in f['samples'] if 2.5 <= s['t'] <= 6.0]
N = json.dumps(nose)
HELP = ("function e(x){x=Math.min(1,Math.max(0,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;}"
        f"const N={N};function nz(t,i){{const tl=t-0.13;let v=N[0][i];for(let k=0;k<N.length-1;k++){{if(tl>=N[k][0]&&tl<=N[k+1][0]){{const q=(tl-N[k][0])/(N[k+1][0]-N[k][0]);v=N[k][i]+(N[k+1][i]-N[k][i])*q;}}}}return v;}}")
TRK = "function trS(t){return 110*(1+0.008*(t-2.87));}"
SCALE_JS = ("const t=input.time.seconds;" + HELP + TRK +
            "if(t<0.72)return 100*(1+0.012*t);if(t<2.87)return 100;if(t<5.33)return trS(t);"
            "if(t<6.33)return trS(5.33)+(100-trS(5.33))*e((t-5.33)/1.0);if(t<12.2)return 100;"
            "if(t<12.9)return 100+12*e((t-12.2)/0.7);if(t<13.9)return 112*(1+0.006*(t-12.9));"
            "if(t<14.56)return 112*1.006+(100-112*1.006)*e((t-13.9)/0.66);if(t<17.45)return 100;"
            f"if(t<18.5)return {PUN * 100};if(t<27.55)return {PUN * 100};if(t<28.4)return {PUN * 100}+(100-{PUN * 100})*e((t-27.55)/0.85);"
            "if(t<29.1)return 100*(1+0.01*(t-28.4));return 100*(1+0.01*Math.max(0,t-32.55));")
POSX_JS = ("const t=input.time.seconds;" + HELP +
           "function tx(t){return 540+(nz(t,1)-N[0][1])*0.3*1080+4*Math.sin(t*5.2+1);}"
           "if(t>=2.87&&t<5.33)return tx(t);if(t>=5.33&&t<6.33)return tx(5.33)+(540-tx(5.33))*e((t-5.33)/1.0);return 540;")
POSY_JS = ("const t=input.time.seconds;" + HELP +
           "function ty(t){return 960+(nz(t,2)-N[0][2])*0.3*1920+4*Math.sin(t*5.2+2);}"
           "let dy=0;if(t>=5.33&&t<6.33)dy=460*e((t-5.33)/1.0);else if(t>=6.33&&t<11.51)dy=460;else if(t>=11.51&&t<12.21)dy=460*(1-e((t-11.51)/0.7));"
           "if(t>=2.87&&t<5.33)return ty(t);if(t>=5.33&&t<6.33)return ty(5.33)+(960+dy-ty(5.33))*e((t-5.33)/1.0);"
           f"if(t>=17.45&&t<27.55)return {PUNY};if(t>=27.55&&t<28.4)return {PUNY}+(960-{PUNY})*e((t-27.55)/0.85);"
           "return 960+dy;")


def aroll_motion(L):
    b.js(L, "scaleX", SCALE_JS); b.js(L, "scaleY", SCALE_JS)
    b.js(L, "positionX", POSX_JS); b.js(L, "positionY", POSY_JS)


vid = b.video("A-roll · roughcut_v3 (silent; voice is its own track)", 0, DUR, 0, "aroll", 33400, vol=None)
vid.pop("volume"); vid["transform"] = tf(540, 960, 540, 960); aroll_motion(vid)
matte = b.video("Person matte (RVM)", 0, DUR, 0, "matte", 33400, vol=None)
matte.pop("volume"); matte["transform"] = tf(540, 960, 540, 960); aroll_motion(matte)
for lyr in (s5, logoA, vidA):
    lyr["trackMatte"] = {"layer": matte["id"], "mode": "lumaInverted"}
adj_blur, adj_sat = b.blur(0), b.huesat(0)
adj = {"type": "Adjustment", "id": b.id(), "name": "Mono beat (F5)", "blendMode": "normal", "activeRange": {"start": 0, "duration": ms(DUR)},
       "transform": tf(0, 0, 0, 0), "effects": [adj_blur, adj_sat]}
b.effect_js(adj, adj_blur, "blurriness", "const t=input.time.seconds;return (t>=2.87&&t<2.97)?10*(1-(t-2.87)/0.1):0;")
b.effect_js(adj, adj_sat, "saturation", "const t=input.time.seconds;if(t<2.87)return 0;if(t<6.0)return -100;if(t<6.45)return -100*(1-(t-6.0)/0.45);return 0;")
grad_ = b.rect("Bottom gradient (captions)", 0, DUR, 0, 1152, W, 768, [0, 0, 0, 0], ax=0, ay=0, grad=(([0, 0, 0, 0], [0, 0, 0, 0.45]), ([0, 0], [0, 768])))

# =====================================================================
# Captions (F3 no clipping, F8 split in white, F26 single line in CTA/PiP, F27 centred + char cap)
GROUPS = [(0, 2, [2]), (3, 6, [6]), (7, 9, []), (10, 13, [10, 11]), (14, 18, [16, 17]), (19, 23, [22, 23]),
          (24, 28, [28]), (29, 31, []), (32, 36, [33]), (37, 40, []), (41, 43, [43]), (44, 46, [45, 46]), (47, 49, []),
          (50, 54, [54]), (55, 57, [55, 56]), (58, 60, []), (61, 64, [64]), (65, 66, [66]), (67, 70, [69]),
          (86, 89, [89]),
          (90, 93, []), (94, 96, []), (97, 99, []), (100, 102, []), (103, 105, []), (106, 109, []), (110, 111, []),
          (112, 113, []), (114, 118, []), (119, 121, []), (122, 125, []), (126, 127, []), (128, 128, []), (129, 130, []), (131, 131, []),
          (132, 136, []), (137, 141, [140, 141])]


def mode(t):
    if 0.72 <= t < 2.87: return 'top'
    if 5.33 <= t < 11.51: return 'split'
    if 18.5 <= t < 26.7: return 'line_ink'
    return 'normal'


GEOM = {'normal': dict(H=132, base=1420, sup=48, hc=WHITE, sc=SUP), 'split': dict(H=100, base=330, sup=40, hc=INKD, sc=MUTE_ICE),
        'top': dict(H=110, base=372, sup=42, hc=INKD, sc=MUTE_ICE),
        'wall': dict(H=132, base=1420, sup=48, hc=RACC, sc=hexc('2F5FD0')),
        'line_ink': dict(size=54, base=922, c=INKD), 'line_white': dict(size=60, base=935, c=WHITE)}
caps = []
starts = [WORDS[g[0]]['s'] for g in GROUPS]
for gi, (i0, i1, hero) in enumerate(GROUPS):
    t0 = WORDS[i0]['s']
    last_e = WORDS[i1]['e']
    nxt = starts[gi + 1] if gi + 1 < len(GROUPS) else DUR
    t1 = nxt if nxt - last_e < 0.6 else last_e + 0.45
    t1 = min(t1, DUR)
    m_ = mode(t0)
    G = GEOM[m_]
    words = [WORDS[i] for i in range(i0, i1 + 1)]
    if m_.startswith('line'):                       # one line of Playfair, centred, word by word
        S = G['size']
        txt = ' '.join(w['w'] for w in words)
        tw_ = width(txt, 'pfb', S)
        if tw_ > 820:
            S = S * 820 / tw_; tw_ = 820
        xx = 540 - tw_ / 2
        for w in words:
            caps.append(word_text("Line " + w['w'], w['s'], t1 - w['s'], xx, G['base'], w['w'], F_PFB, round(S, 1), G['c']))
            cue(w['s'] + 0.04, 'flick', -28, 'caption word')
            xx += width(w['w'] + ' ', 'pfb', S)
        continue
    S = G['sup']
    if hero:
        htxt = ' '.join(WORDS[i]['w'] for i in hero)
        above = [WORDS[i] for i in range(i0, hero[0])]
        below = [WORDS[i] for i in range(hero[-1] + 1, i1 + 1)]
        Hs = G['H']
        hw = width(htxt, 'pfb', Hs)
        if hw > 740:
            Hs = Hs * 740 / hw; hw = 740
        base = G['base']
        hs, he = WORDS[hero[0]]['s'], WORDS[hero[-1]]['e']
        stag = max(0.014, min(0.045, (he - hs) / max(1, len(htxt))))
        if hs + stag * len(htxt) + 0.4 > t1 - 0.35:
            stag = max(0.012, (t1 - 0.35 - 0.4 - hs) / max(1, len(htxt)))
        x = 540 - hw / 2
        first = True
        for j, c in enumerate(htxt):
            gw = width(c, 'pfb', Hs)
            ta = hs + j * stag
            if c != ' ' and ta < t1 - 0.05:
                L = b.text("Hero glyph " + c, ta, t1 - ta, x, base, c, F_PFB, round(Hs, 1), G['hc'])
                b.kf(L, "positionX", [(0, x - 24, LIN), (0.42, x, E1)])
                b.kf(L, "opacity", [(0, 0, LIN), (0.28, 100, E1)])
                blurfx(L, 0, 8, 0.32)
                caps.append(L)
                if first:
                    cue(ta + 0.02, 'hitech', -17, 'hero: ' + htxt)
                    first = False
            x += gw
        for lst, yline in ((above, base - 0.8 * Hs - 8), (below, base + (S + 14))):
            if not lst:
                continue
            ltxt = ' '.join(w['w'] for w in lst)
            xx = 540 - width(ltxt, 'med', S) / 2
            for w in lst:
                if w['s'] < t1 - 0.05:
                    ts_ = max(t0, w['s'])
                    caps.append(word_text("Support " + w['w'], ts_, t1 - ts_, xx, yline, w['w'], F_MED, S, G['sc']))
                    cue(w['s'] + 0.04, 'flick', -28 + (len(caps) % 3) - 1, 'support word')
                xx += width(w['w'] + ' ', 'med', S)
    else:
        S = S + 6
        txt = ' '.join(w['w'] for w in words)
        xx = 540 - width(txt, 'med', S) / 2
        for w in words:
            if w['s'] < t1 - 0.05:
                caps.append(word_text("Support " + w['w'], w['s'], t1 - w['s'], xx, G['base'] - 30, w['w'], F_MED, S, G['sc']))
                cue(w['s'] + 0.04, 'flick', -28 + (len(caps) % 3) - 1, 'support word')
            xx += width(w['w'] + ' ', 'med', S)
for wi in range(142, 161):            # v4: CTA captions one word at a time, Playfair, above "Comments"
    w_ = WORDS[wi]['w']
    ta_ = WORDS[wi]['s']
    tb_ = WORDS[wi + 1]['s'] if wi < 160 else DUR
    Sz = min(78, 78 * 820 / max(1, width(w_, 'pfb', 78)))
    caps.append(word_text("CTA word " + w_, ta_, tb_ - ta_, 540, 935, w_, F_PFB, round(Sz, 1), WHITE, just="center"))
    cue(ta_ + 0.03, 'flick', -28, 'CTA word')
cap_g = b.group("Captions (editorial serif, centred)", 0, DUR, caps)

voice = {"type": "Audio", "id": b.id(), "name": "Voice (rough cut, HPF 75 Hz, −1.5 dB)", "source": {"assetId": "sfx-voice"},
         "sourceRange": {"start": 0, "duration": 33400}, "sourceIntrinsicDuration": ms(SFX['voice']['dur']), "volume": 1.0,
         "playback": {"type": "windowed", "inputRange": {"start": 0, "duration": 33400},
                      "mapping": {"type": "linear", "input": {"start": 0, "duration": 33400}, "output": {"start": 0, "duration": 33400}}, "inputOffsetMs": 0}}
layers = [cap_g] + list(reversed(scenes)) + rootfx + [grad_, adj, matte, vid, voice] + audio_layers()
save(doc, layers, b.actions, DUR)
print("layers", b.nid - 100, "actions", len(b.actions), "caption layers", len(caps), "cues", len([l for l in layers if l['type'] == 'Audio']) - 1)
