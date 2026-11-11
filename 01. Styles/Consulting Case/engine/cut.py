#!/usr/bin/env python3
"""Render a cut from an edit list.
edl.json: {"sources": {"A": "path.mov", ...}, "segments": [["A", start, end, "note"], ...]}
Outputs cut.mp4 (1440x2560 working res, 30000/1001 fps, h264 videotoolbox high bitrate, AAC 48k)
Audio: 10 ms fade in/out at each join (no clicks).
usage: cut.py edl.json out.mp4 [--native]
  --native: source resolution, no scaling (the "raw trimmed" deliverable), 50 Mb/s.
Video is padded (last frame cloned) to the audio length: per-segment fps conversion loses ~0.5 s (lesson E1.12).
"""
import json, subprocess, sys
edl = json.load(open(sys.argv[1])); out = sys.argv[2]; native = '--native' in sys.argv
srcs = list(edl["sources"].items()); idx = {k: i for i, (k, _) in enumerate(srcs)}
args = ["/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg", "-v", "error", "-y"]
for _, p in srcs: args += ["-i", p]
fc = []; cat = ""
for n, (s, a, b, *_) in enumerate(edl["segments"]):
    i = idx[s]; d = b - a; f = 0.010
    sc = "" if native else ",scale=1440:2560:flags=lanczos"
    fc.append(f"[{i}:v:0]trim={a:.4f}:{b:.4f},setpts=PTS-STARTPTS,fps=30000/1001{sc}[v{n}]")
    fc.append(f"[{i}:a:0]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,afade=t=in:d={f},afade=t=out:st={d-f:.4f}:d={f}[a{n}]")
    cat += f"[v{n}][a{n}]"
fc.append(f"{cat}concat=n={len(edl['segments'])}:v=1:a=1[vc][a];[vc]tpad=stop_mode=clone:stop=30[v]")
args += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-shortest", "-fps_mode", "cfr", "-r", "30000/1001",
         "-c:v", "h264_videotoolbox", "-b:v", "50M" if native else "25M", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", out]
subprocess.run(args, check=True)
