# Step 8: right-hand speaker column (576x1080): interviewer top, candidate bottom; subtle-corner cards + name labels. [M17, M19, M20]
# usage: 06. Tools/venv-style/bin/python speakers.py <project_dir> <t0> <t1>
#   needs case.json (speakers[].file / name / role / crop_x) + src_segments.json (timeline_map.py)
#   crop_x = left edge of a 760x720 crop in the 1280x720 source; centre the face (check a still first).
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
P = sys.argv[1]; T0 = float(sys.argv[2]); T1 = float(sys.argv[3])
C = json.load(open(os.path.join(P, "case.json")))
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root (.studio-root) not found above " + __file__)
        p = os.path.dirname(p)
    return p
ROOT = _studio_root()
SRC = os.path.join(ROOT, C["inbox_folder"])
segs = json.load(open(os.path.join(P, "src_segments.json")))
out, t = [], 0
for a, b in segs:                                   # keep only [T0, T1) of the final timeline
    d = b - a; lo, hi = max(t, T0), min(t + d, T1)
    if hi > lo: out.append((a + lo - t, a + hi - t))
    t += d
W, H, R = 544, 516, 10
m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, W - 1, H - 1), R, fill=255); m.save(os.path.join(P, "card_mask.png"))
F = "/System/Library/Fonts/Avenir Next.ttc"
def pill(name, role, fn):
    f1 = ImageFont.truetype(F, 24, index=2); f2 = ImageFont.truetype(F, 20, index=7)
    w = int(f1.getlength(name) + f2.getlength(role) + 56); im = Image.new("RGBA", (w, 44), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, 43), 6, fill=(255, 255, 255, 235)); d.text((18, 8), name, font=f1, fill=(44, 53, 82))
    d.text((28 + f1.getlength(name), 11), role, font=f2, fill=(138, 143, 160)); im.save(os.path.join(P, fn))
sp = C["speakers"]
pill(sp[0]["name"], sp[0]["role"], "pill_1.png"); pill(sp[1]["name"], sp[1]["role"], "pill_2.png")
fc = []
for s in range(2):
    labs = ""
    for i, (a, b) in enumerate(out):
        fc.append(f"[{s}:v]trim=start={a:.6f}:end={b:.6f},setpts=PTS-STARTPTS[v{s}_{i}]"); labs += f"[v{s}_{i}]"
    fc.append(f"{labs}concat=n={len(out)}:v=1:a=0,fps=30000/1001,crop=760:720:{sp[s]['crop_x']}:0,scale={W}:{H}:flags=lanczos,format=rgba[c{s}]")
fc += ["[2:v]format=gray,split=2[m0][m1]", "[c0][m0]alphamerge[r0]", "[c1][m1]alphamerge[r1]",
       f"color=c=0xE9ECFD:s=576x1080:r=30000/1001:d={T1 - T0:.4f}[bg]",
       "[bg][r0]overlay=16:16[b1]", "[b1][r1]overlay=16:548[b2]", "[b2][3:v]overlay=32:472[b3]", "[b3][4:v]overlay=32:1004,format=yuv420p[o]"]
open(os.path.join(P, "speakers_fc.txt"), "w").write(";\n".join(fc))
dst = os.path.join(P, f"speakers_{int(T0)}_{int(T1)}.mp4")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(SRC, sp[0]["file"]), "-i", os.path.join(SRC, sp[1]["file"]),
                "-loop", "1", "-i", os.path.join(P, "card_mask.png"), "-loop", "1", "-i", os.path.join(P, "pill_1.png"),
                "-loop", "1", "-i", os.path.join(P, "pill_2.png"), "-/filter_complex", os.path.join(P, "speakers_fc.txt"),
                "-map", "[o]", "-t", f"{T1 - T0:.4f}", "-c:v", "libx264", "-crf", "16", "-preset", "fast", dst], check=True)
print(len(out), "segments ->", dst)
