#!/usr/bin/env python3
"""One-command builder for the approved "Raw vs Opus 5.5" before/after reel (Tesseract).

    python3 make_before_after.py --raw raw.mp4 --edited edited.mp4 [--audio audio.mp4] \
        --keyword EDIT --out "<new project folder>"

Creates <out>/BeforeAfter.tsrct (editable, self-contained), <out>/BeforeAfter_<KEYWORD>.mp4,
and <out>/Previews/Export_frames.png. <out> must not exist yet.

Rebuild an existing project after changing knobs (no re-import):
    python3 make_before_after.py --rebuild --out "<existing project folder>" [knob flags]
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
FONT_FILE = SKILL / "assets" / "Inter-Variable.ttf"
TSRCT = os.environ.get("TSRCT") or str(Path.home() / "Library/Application Support/Tesseract/bin/tsrct")

# ----------------------------------------------------------------------------- CLI
ap = argparse.ArgumentParser()
ap.add_argument("--raw"); ap.add_argument("--edited"); ap.add_argument("--audio",
    help="file whose audio is the final mix (any video/audio). Default: the edited video's audio")
ap.add_argument("--keyword", default="EDIT")
ap.add_argument("--out", required=True)
ap.add_argument("--rebuild", action="store_true", help="re-layout an existing project folder")
ap.add_argument("--raw-label", default="Raw")
ap.add_argument("--edited-label", default="Opus 5.5")
ap.add_argument("--line1", default="Follow & comment ")
ap.add_argument("--line2", default="for the full guide")
ap.add_argument("--tilt", type=float, default=-16.0,
    help="raw card 3D yaw in degrees; negative = inner edge recedes behind the edited card")
ap.add_argument("--raw-scale", type=float, default=1.0, help="extra scale on the raw card size")
ap.add_argument("--saturation", type=float, default=-0.65, help="raw card grade, -1 = grayscale")
ap.add_argument("--fade", type=float, default=1.0, help="raw card fade strength multiplier (0 = none)")
ap.add_argument("--no-export", action="store_true")
A = ap.parse_args()

OUT = Path(A.out).resolve()
W = OUT / ".tesseract-work"
P = OUT / "BeforeAfter.tsrct"
STATE = W / "state.json"

def run(*cmd, capture=True):
    r = subprocess.run([str(c) for c in cmd], capture_output=capture, text=True)
    if r.returncode != 0:
        sys.exit(f"FAILED: {' '.join(map(str, cmd))}\n{r.stdout}\n{r.stderr}")
    return r.stdout

def probe_ms(f, stream=None):
    args = ["ffprobe", "-v", "error"]
    if stream: args += ["-select_streams", stream]
    args += ["-show_entries", "format=duration", "-of", "default=nw=1:nk=1", f]
    return int(float(run(*args).strip()) * 1000)

def last_json(s):
    return json.loads([l for l in s.strip().splitlines() if l.startswith("{")][-1])

# ----------------------------------------------------------------------------- setup
if not A.rebuild:
    if not (A.raw and A.edited):
        sys.exit("--raw and --edited are required for a new project")
    raw, edited = Path(A.raw).resolve(), Path(A.edited).resolve()
    audio = Path(A.audio).resolve() if A.audio else edited
    for f in (raw, edited, audio):
        if not f.exists(): sys.exit(f"missing input: {f}")
    OUT.mkdir(parents=False, exist_ok=False)          # claim a fresh folder atomically
    W.mkdir(); (OUT / "Previews").mkdir(); (W / "checks").mkdir()

    run(TSRCT, "project", "create", "--project", P)
    raw_info = last_json(run(TSRCT, "project", "import-video", "--project", P, "--file", raw, "--asset-id", "raw"))
    ed_info = last_json(run(TSRCT, "project", "import-video", "--project", P, "--file", edited, "--asset-id", "edited"))
    mix = W / "final-mix.wav"
    run("ffmpeg", "-v", "error", "-y", "-i", audio, "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", mix)
    run(TSRCT, "project", "import-asset", "--project", P, "--file", mix, "--asset-id", "finalmix", "--kind", "audio")
    run(TSRCT, "project", "import-font", "--project", P, "--file", FONT_FILE)
    mix_ms = probe_ms(str(mix))
    # 30 fps-aligned duration: shortest of the picture sources (audio is trimmed to it)
    dur = min(raw_info["durationMs"], ed_info["durationMs"])
    dur = round(int(dur * 30 / 1000 + 1e-6) * 1000 / 30)
    state = dict(dur=dur, raw_ms=raw_info["durationMs"], ed_ms=ed_info["durationMs"],
                 mix_ms=mix_ms, split_x=688.0, sources=dict(raw=str(raw), edited=str(edited), audio=str(audio)))
    for name, info in (("raw", raw_info), ("edited", ed_info)):
        if (info["width"], info["height"]) != (1080, 1920):
            print(f"note: {name} is {info['width']}x{info['height']} (cover-fit into its card)")
    if abs(raw_info["durationMs"] - ed_info["durationMs"]) > 200 or abs(mix_ms - ed_info["durationMs"]) > 400:
        print(f"WARNING: durations differ raw={raw_info['durationMs']} edited={ed_info['durationMs']} "
              f"audio={mix_ms} ms - confirm the three files share one timeline")
else:
    state = json.load(open(STATE))
json.dump(state, open(STATE, "w"), indent=1)
DUR_MS = state["dur"]

# ----------------------------------------------------------------------------- layout helpers
FONT = "Inter"
def hexc(h, a=1.0):
    h = h.lstrip("#"); return [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)] + [a]
ORANGE, INK, PEACH = hexc("#E2703F"), hexc("#141414"), hexc("#F4E2D5")

def tf(pos=(0, 0), anchor=(0, 0), rot=0.0, opacity=100, scale=(100, 100)):
    return {"anchorPoint": list(anchor), "position": list(pos), "scale": list(scale),
            "rotation": rot, "opacity": opacity}
def active(): return {"start": 0, "duration": DUR_MS}
def windowed():
    return {"type": "windowed", "inputRange": {"start": 0, "duration": DUR_MS},
            "mapping": {"type": "linear", "input": {"start": 0, "duration": DUR_MS},
                        "output": {"start": 0, "duration": DUR_MS}}, "inputOffsetMs": 0}
_id = [0]
def nid(): _id[0] += 1; return _id[0]

def rect(name, x, y, w, h, color, radius=0.0, rot=0.0, anchor=None, opacity=100, paint=None, shadow=None):
    # NOTE: rect.position is the rect's TOP-LEFT in layer space (not its centre)
    lyr = {"type": "Rect", "id": nid(), "name": name, "blendMode": "normal", "activeRange": active(),
           "transform": tf((x, y), anchor or (0, 0), rot, opacity),
           "rect": {"size": [w, h], "position": [0, 0], "fillColor": color, "roundness": radius}}
    if paint: lyr["rect"]["fillPaint"] = paint
    if shadow: lyr["dropShadow"] = shadow
    return lyr

def text(name, s, x, y, size, color, weight=500, just="left", tracking=-20):
    return {"type": "Text", "id": nid(), "name": name, "blendMode": "normal", "activeRange": active(),
            "transform": tf((x, y)),
            "sourceText": {"text": s, "fontFamily": FONT, "fontStyle": "Regular", "fontSize": size,
                           "fillColor": color, "strokeWidth": 0, "justification": just, "tracking": tracking,
                           "fontVariations": {"id": nid(), "axes": {"wght": weight, "opsz": 32}}}}

def starburst(prefix, cx, cy, rays, color, opacity=100):
    return [rect(f"{prefix} ray {i+1}", cx, cy, r1 - r0, w, color, radius=w / 2, rot=ang,
                 anchor=(-r0, w / 2), opacity=opacity) for i, (ang, r0, r1, w) in enumerate(rays)]

def shadow(alpha, blur, dy, dx=0):
    return {"color": [0, 0, 0, alpha], "blurRadius": blur, "spreadRadius": 0,
            "offset": [dx, dy], "blendMode": "normal", "enabled": True}

# ----------------------------------------------------------------------------- geometry (1080x1920)
FRONT = dict(x=383, y=425, w=538, h=956, r=0.165)          # edited card. cornerRadius is NOT px
_BW, _BH = round(340 * A.raw_scale), round(604 * A.raw_scale)
BACK = dict(x=100 - (_BW - 340) / 2, y=FRONT["y"] + FRONT["h"] / 2 - _BH / 2, w=_BW, h=_BH, r=0.2)
BACK_C = (BACK["x"] + BACK["w"] / 2, BACK["y"] + BACK["h"] / 2)   # vertical centre == edited centre
CAP_Y1, CAP_Y2 = 1484, 1560

def on_back_plane(lyr):
    """Pivot on the raw card centre with the same 3D yaw, so the layer lies on the card's plane."""
    t = lyr["transform"]; px, py = t["position"]; ax, ay = t["anchorPoint"]
    t["anchorPoint"] = [ax + BACK_C[0] - px, ay + BACK_C[1] - py]
    t["position"] = list(BACK_C); t["rotationY"] = A.tilt
    return lyr

def build(split_x):
    _id[0] = 0
    L = []
    L.append(rect("Background", 0, 0, 1080, 1920, hexc("#F2F2F2"), paint={
        "type": "gradient", "gradientType": "linear", "start": [0, 0], "end": [1080, 1920],
        "stops": [{"offset": 0, "color": hexc("#E6E6E6")}, {"offset": 0.45, "color": hexc("#F6F6F6")},
                  {"offset": 1, "color": hexc("#EDEDED")}]}))
    spec = [(-100, 760), (-62, 640), (-28, 820), (8, 700), (40, 780), (76, 620),
            (110, 760), (146, 680), (182, 800), (216, 640), (250, 740)]
    L += starburst("Bg burst", 540, 900, [(a, 150, r1, 118) for a, r1 in spec], PEACH, opacity=42)
    L.append(rect("Centre haze", 0, 0, 1080, 1920, [1, 1, 1, 0], paint={
        "type": "gradient", "gradientType": "radial", "start": [540, 900], "end": [540, 1500],
        "stops": [{"offset": 0, "color": [1, 1, 1, 0.55]}, {"offset": 1, "color": [1, 1, 1, 0]}]}))
    # raw card: desaturated + faded, tilted inward
    L.append({"type": "Video", "id": nid(), "name": "Raw card", "blendMode": "normal",
        "playback": windowed(), "sourceRange": {"start": 0, "duration": DUR_MS},
        "sourceIntrinsicDuration": state["raw_ms"], "volume": 0.0,
        "cornerRadius": BACK["r"], "dropShadow": shadow(0.30, 38, 18, dx=10),
        "effects": [{"id": nid(), "enabled": True, "effect": {
            "type": "primaryGrade", "semanticVersion": 1, "temperature": 0.0, "tint": 0.0,
            "exposure": 0.1 * A.fade, "contrast": -0.35 * A.fade, "blacks": 0.35 * A.fade,
            "shadows": 0.0, "highlights": 0.0, "whites": 0.0,
            "saturation": A.saturation, "vibrance": 0.0}}],
        "transform": dict(tf(BACK_C, (BACK["w"] / 2, BACK["h"] / 2)), rotationY=A.tilt),
        "source": {"assetId": "raw", "fit": "cover",
                   "sourceRect": {"x": 0, "y": 0, "width": BACK["w"], "height": BACK["h"]}}})
    ph = 70; pw = 96 + 19 * len(A.raw_label)
    px, py = BACK["x"] + 3, BACK["y"] - ph - 11
    L.append(on_back_plane(rect("Raw pill", px, py, pw, ph, hexc("#1E1E1E"), radius=ph / 2,
        shadow=shadow(0.25, 16, 6), paint={"type": "gradient", "gradientType": "linear",
        "start": [0, 0], "end": [0, ph], "stops": [{"offset": 0, "color": hexc("#3A3A3A")},
                                                   {"offset": 1, "color": hexc("#151515")}]})))
    L.append(on_back_plane(rect("Raw rec dot", px + 20, py + ph / 2 - 11, 22, 22, hexc("#E5322D"), radius=11)))
    L.append(on_back_plane(text("Raw label", A.raw_label, px + 54, py + 46, 33, [1, 1, 1, 1], tracking=-10)))
    # edited card (front)
    L.append({"type": "Video", "id": nid(), "name": f"Edited card ({A.edited_label})", "blendMode": "normal",
        "playback": windowed(), "sourceRange": {"start": 0, "duration": DUR_MS},
        "sourceIntrinsicDuration": state["ed_ms"], "volume": 0.0,
        "cornerRadius": FRONT["r"], "dropShadow": shadow(0.34, 56, 24, dx=-14),
        "transform": tf((FRONT["x"], FRONT["y"])),
        "source": {"assetId": "edited", "fit": "cover",
                   "sourceRect": {"x": 0, "y": 0, "width": FRONT["w"], "height": FRONT["h"]}}})
    oh = 114; ow = 140 + 22 * len(A.edited_label)
    ox, oy = FRONT["x"] + 7, FRONT["y"] - oh - 21
    L.append(rect("Opus pill", ox, oy, ow, oh, hexc("#1E1E1E"), radius=oh / 2, shadow=shadow(0.28, 22, 8),
        paint={"type": "gradient", "gradientType": "linear", "start": [0, 0], "end": [ow, oh],
               "stops": [{"offset": 0, "color": hexc("#4A3A33")}, {"offset": 0.5, "color": hexc("#262323")},
                         {"offset": 1, "color": hexc("#141414")}]}))
    L += starburst("Opus icon", ox + 66, oy + oh / 2,
                   [(a, 10, 34 if i % 2 == 0 else 30, 5.5) for i, a in enumerate(range(0, 360, 30))], ORANGE)
    L.append(text("Opus label", A.edited_label, ox + 116, oy + 73, 46, [1, 1, 1, 1], tracking=-30))
    # caption: black part right-justified + orange keyword left-justified, meeting at split_x
    L.append(text("Caption line 1 (black)", A.line1, split_x, CAP_Y1, 60, INK, just="right", tracking=-35))
    L.append(text("Caption keyword", f"\u201c{A.keyword.upper()}\u201d", split_x, CAP_Y1, 60, ORANGE,
                  weight=700, tracking=-20))
    L.append(text("Caption line 2", A.line2, 540, CAP_Y2, 60, INK, just="center", tracking=-35))
    L.append({"type": "Audio", "id": nid(), "name": "Final mix", "playback": windowed(),
              "sourceRange": {"start": 0, "duration": DUR_MS}, "sourceIntrinsicDuration": state["mix_ms"],
              "volume": 1.0, "source": {"assetId": "finalmix"}})
    ed = W / "editable.json"
    run(TSRCT, "project", "checkout", "--project", P, "--output", ed)
    doc = json.load(open(ed))
    doc["duration"] = DUR_MS / 1000
    doc.pop("backgroundColor", None)   # browser editor needs absent/black; Background layer covers canvas
    doc["composition"]["layers"] = list(reversed(L))
    json.dump(doc, open(ed, "w"), indent=1)
    run(TSRCT, "project", "commit", "--project", P, "--file", ed)

def caption_centre():
    """Rendered x-centre of caption line 1 (dark/orange pixels in its band)."""
    png = W / "checks" / "caption.png"
    run(TSRCT, "preview", "--project", P, "--time", "0.5", "--output", png)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(png), "-vf", "crop=1080:80:0:1432,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    cols = [x for x in range(1080) if any(raw[y * 1080 + x] < 175 for y in range(80))]
    return (cols[0] + cols[-1]) / 2 if cols else None

# ----------------------------------------------------------------------------- build + centre caption
split = state.get("split_x", 688.0)
build(split)
for _ in range(3):
    c = caption_centre()
    if c is None or abs(c - 540) <= 2: break
    split -= (c - 540); build(split)
state["split_x"] = split; json.dump(state, open(STATE, "w"), indent=1)
run(TSRCT, "preview", "--project", P, "--time", "3", "--output", OUT / "Previews" / "Layout.png")

if not A.no_export:
    mp4 = OUT / f"BeforeAfter_{A.keyword.upper()}.mp4"
    run(TSRCT, "export", "--project", P, "--output", mp4)
    n = int(DUR_MS / 1000 * 30)
    sel = "+".join(f"eq(n,{f})" for f in (15, n // 2, n - 8))
    run("ffmpeg", "-v", "error", "-y", "-i", mp4, "-vf", f"select='{sel}',scale=360:-2,tile=3x1",
        "-frames:v", "1", OUT / "Previews" / "Export_frames.png")
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", subprocess.run(["ffmpeg", "-hide_banner", "-i", str(mp4), "-vn",
        "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr)
    spec = run("ffprobe", "-v", "error", "-show_entries", "stream=width,height,r_frame_rate:format=duration",
               "-of", "compact", mp4).strip().replace("\n", " | ")
    print(json.dumps({"export": str(mp4), "spec": spec, "integratedLUFS": lufs[-1] if lufs else None,
                      "durationMs": DUR_MS, "captionSplitX": round(split, 1),
                      "frames": str(OUT / "Previews" / "Export_frames.png")}, indent=1))
else:
    print(json.dumps({"project": str(P), "layout": str(OUT / "Previews" / "Layout.png")}))
