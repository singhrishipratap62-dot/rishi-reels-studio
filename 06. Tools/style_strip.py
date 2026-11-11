"""Usage: python -I style_strip.py <video> <start_s> <dur_s> <out.jpg> [cols] [step]
Extracts every `step`-th native frame in [start, start+dur) at 240x135 and tiles them
with frame index + time labels, for measuring animation timing.
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageDraw

vid, start, dur, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 10
step = int(sys.argv[6]) if len(sys.argv) > 6 else 1
fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                      "stream=r_frame_rate", "-of", "csv=p=0", vid], capture_output=True, text=True).stdout.strip()
num, den = map(int, fps.split("/")); fps = num / den
with tempfile.TemporaryDirectory(dir=Path(out).parent) as tmp:
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(start), "-i", vid, "-t", str(dur),
                    "-vf", f"select='not(mod(n\\,{step}))',scale=240:135", "-fps_mode", "vfr",
                    f"{tmp}/s_%04d.png"], check=True)
    frames = sorted(Path(tmp).glob("s_*.png"))
    W, H = 240, 135; rows = -(-len(frames) // cols)
    sheet = Image.new("RGB", (W * cols, H * rows), "black"); d = ImageDraw.Draw(sheet)
    for i, f in enumerate(frames):
        x, y = (i % cols) * W, (i // cols) * H
        sheet.paste(Image.open(f), (x, y))
        t = start + i * step / fps
        d.rectangle([x, y, x + 78, y + 12], fill="black"); d.text((x + 2, y + 1), f"{i * step:03d} {t:.2f}s", fill="yellow")
    sheet.save(out, quality=82)
print(f"{out}: {len(frames)} frames @ {fps:.3f}fps step {step}")
