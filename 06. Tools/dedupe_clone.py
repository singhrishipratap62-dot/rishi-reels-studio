#!/usr/bin/env python3
"""Replace byte-identical duplicate files (>= 1 MB) under the studio with APFS clones of one copy.

Every path keeps an independent file (copy-on-write), so scripts and projects behave exactly as before,
but identical data is stored once. Dry run unless --run. Skips toolchains (node_modules, venvs).
usage: dedupe_clone.py [--run] [folder]   (folder defaults to the studio root)
"""
import hashlib, os, subprocess, sys
from collections import defaultdict

RUN = "--run" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
here = os.path.dirname(os.path.abspath(__file__))
root = args[0] if args else os.path.dirname(here)
SKIP = {"node_modules", "venv-style", ".uv-python", "uv-tools", "venv", ".git"}

def sha(p, n=1 << 20):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(n), b""): h.update(b)
    return h.hexdigest()

def already_clone(a, b):
    # same device + identical first extent is hard to read portably; fall back to inode check for hardlinks only
    sa, sb = os.stat(a), os.stat(b)
    return sa.st_ino == sb.st_ino

by_size = defaultdict(list)
for r, ds, fs in os.walk(root):
    ds[:] = [d for d in ds if d not in SKIP]
    for f in fs:
        p = os.path.join(r, f)
        if os.path.islink(p): continue
        s = os.path.getsize(p)
        if s >= 1 << 20: by_size[s].append(p)

saved = 0; groups = 0
for s, ps in sorted(by_size.items(), reverse=True):
    if len(ps) < 2: continue
    by_hash = defaultdict(list)
    for p in ps: by_hash[sha(p)].append(p)
    for h, same in by_hash.items():
        if len(same) < 2: continue
        # keep the copy outside the archive if there is one, so live paths own the original
        same.sort(key=lambda p: ("09. Archive" in p, len(p)))
        keep, dups = same[0], same[1:]
        groups += 1
        print(f"{s/1e6:8.1f} MB x{len(same)}  keep: {os.path.relpath(keep, root)}")
        for d in dups:
            if already_clone(keep, d): continue
            print(f"            clone -> {os.path.relpath(d, root)}")
            saved += s
            if RUN:
                tmp = d + ".clonetmp"
                subprocess.run(["cp", "-c", "-p", keep, tmp], check=True)
                if sha(tmp) != h: os.remove(tmp); sys.exit(f"verify failed for {d}")
                os.replace(tmp, d)
print(f"\n{groups} duplicate groups, {saved/1e9:.2f} GB {'reclaimed' if RUN else 'reclaimable (dry run: add --run)'}")
