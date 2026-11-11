#!/usr/bin/env python3
"""Close out a finished reel: delete only regenerable intermediates, after confirming the final export exists.

usage: finalize_reel.sh "<project folder>" [--export <final.mp4>] [--yes]
  Dry run by default (prints what would go and how much space it frees). Add --yes to delete.
  The export is auto-found in "04. Exports/<style>/" by the reel ID prefix (e.g. R011_...); pass --export otherwise.

Kept always: the final export, the source cut (cut.mp4 / roughcut / raw_*.wav), plans, cue sheets, build scripts
(.py/.sh/.js/.json/.env/.md), the final project file (*.tsrct at the edit folder's top level) and sfx48/.
Deleted (regenerable): .tesseract-work media (*.tsrct copies, fxonly/preview mp4s, checks/, review stills),
consulting audio-chain WAVs, board renders, mock-case board frames/sfx stem, .work/ frame dumps.
"""
import os, re, sys, glob, shutil

def studio_root(p):
    p = os.path.abspath(p)
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): sys.exit("not inside the studio (no .studio-root above " + p + ")")
        p = os.path.dirname(p)
    return p

MEDIA = (".tsrct", ".mp4", ".mov", ".wav", ".png", ".jpg", ".jpeg", ".webm", ".npy")
CONSULT_WAV = re.compile(r"^(voice_proc|voice_chain|chain|mix|mix_raw|mus_|key_sp|prog_sp|final_mix|sfx_stem).*\.wav$")
NEVER = re.compile(r"(^|/)(cut\.mp4|raw_[^/]*\.wav|roughcut[^/]*\.mp4|vid\d+(_cut)?\.mp4|.*_matte\.mp4|sfx48/.*)$")

def candidates(proj):
    out = []
    for r, ds, fs in os.walk(proj):
        rel_r = os.path.relpath(r, proj)
        parts = rel_r.split(os.sep)
        for f in fs:
            p = os.path.join(r, f); rel = os.path.normpath(os.path.join(rel_r, f))
            if NEVER.search(rel):
                continue
            low = f.lower()
            if ".tesseract-work" in parts:
                # only project-file copies, effect/preview renders and review stills; prepared source media stays
                edit_dir = r[:r.index(".tesseract-work")]
                has_final_project = bool(glob.glob(os.path.join(glob.escape(edit_dir), "*.tsrct")))
                if (low.endswith(".tsrct") and has_final_project) or low.endswith((".png", ".jpg", ".jpeg")) or (
                        low.endswith((".mp4", ".mov")) and re.search(r"fxonly|preview|check|review|_t\d|^v0_", low)):
                    out.append(p)
            elif ".work" in parts:
                out.append(p)
            elif "board" in parts and low.endswith((".mov", ".mp4", ".webm", ".png")) and rel_r.split(os.sep)[0] == "board":
                out.append(p)
            elif "board_frames" in parts:
                out.append(p)
            elif rel_r == "." and (CONSULT_WAV.match(f) or f in ("MG_sfx.wav",) or low.endswith(("_preview.mp4", ".rendering.mp4"))):
                out.append(p)
            elif "checks" in parts and low.endswith(MEDIA):
                out.append(p)
    return out

def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        sys.exit(__doc__)
    proj = os.path.abspath(a[0]); yes = "--yes" in a
    export = a[a.index("--export") + 1] if "--export" in a else None
    if os.path.exists(os.path.join(proj, "KEEP_SOURCE.md")):
        sys.exit("This project has KEEP_SOURCE.md (its final export is missing). Restore the final first, then remove that file.")
    root = studio_root(proj)
    rel = os.path.relpath(proj, root).split(os.sep)
    if len(rel) < 3 or rel[0] != "03. Projects":
        sys.exit("project folder must be inside '03. Projects/<style>/'")
    style = rel[1]
    if not export:
        name = os.path.basename(proj)
        m = re.match(r"(R[_A-Za-z0-9]*?\d+)_", name)
        hits = sorted(glob.glob(os.path.join(root, "04. Exports", style, m.group(1) + "*.mp4"))) if m else []
        if not hits:
            sys.exit(f"No export found in '04. Exports/{style}/' for '{name}'. Pass --export <final.mp4>.")
        exact = os.path.join(root, "04. Exports", style, name + ".mp4")
        export = exact if os.path.isfile(exact) else hits[-1]
    if not os.path.isfile(export) or os.path.getsize(export) < 100_000:
        sys.exit(f"Final export missing or too small: {export}")
    export = os.path.abspath(export)
    files = [p for p in candidates(proj) if os.path.abspath(p) != export]
    total = sum(os.path.getsize(p) for p in files if os.path.isfile(p))
    print(f"Export confirmed: {os.path.relpath(export, root)}")
    for p in files[:40]:
        print(("  delete  " if yes else "  would delete  ") + os.path.relpath(p, proj))
    if len(files) > 40: print(f"  ... and {len(files) - 40} more")
    print(f"{len(files)} files, {total / 1e6:.0f} MB {'freed' if yes else 'reclaimable (dry run: add --yes)'}")
    if yes:
        for p in files: os.remove(p)
        for r, ds, fs in os.walk(proj, topdown=False):  # drop folders emptied by the cleanup
            if r != proj and not os.listdir(r): os.rmdir(r)

main()
