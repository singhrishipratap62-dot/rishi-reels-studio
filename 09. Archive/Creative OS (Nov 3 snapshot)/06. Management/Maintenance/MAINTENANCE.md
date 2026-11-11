# Maintenance

How to keep Creative OS accurate as work continues.

## After each reel
1. Copy useful notes (NOTES.md, sound cue sheet, edit plan, transcript) into `08/<type>/<project>/`. Copy the final render to `08/Completed Projects/` if under about 100 MB, otherwise log its path.
2. Add any corrections you received to `04/User Feedback/`.
3. If something worked well enough to reuse, copy it into `02`, `07` or `09`.
4. Add rows to `MANIFEST.csv` and, for important items, lines to `MASTER_INDEX.md`.

## Monthly (or every 10 reels)
- Read recent feedback entries and fold durable ones into `LESSONS_LEARNED.md` or `DECISIONS.md`. Note the date.
- Refresh `MASTER_INDEX.md`; remove dead lines.
- Check `MANIFEST.csv` for `path-only` rows whose originals have moved or been deleted. Fix the path or note the loss.
- Re-run the integrity check below.
- Update `FOLDER_INDEX.md` if folders were added. Empty folders that gain files should lose their `_README.md` pointer.

## Integrity check
Verify copies against the manifest:
```
cd "Creative OS"
python3 -I - <<'EOF'
import csv, hashlib, os
root = os.path.abspath("..")
def h(p):
    s = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): s.update(b)
    return s.hexdigest()
bad = 0
for r in csv.DictReader(open("06. Management/Master Index/MANIFEST.csv")):
    if r["status"] == "copied":
        a, b = os.path.join(root, r["original_path"]), os.path.join(root, r["creative_os_path"])
        if os.path.exists(a) and os.path.exists(b) and h(a) != h(b):
            print("differs (original changed since copy?):", r["original_path"]); bad += 1
print("differences:", bad)
EOF
```
A difference usually means the original was edited after copying. Decide whether to refresh the copy as a new version (do not overwrite).

## Restoring things that were not copied
- **Python environment (`tools/venv-style`)**: used by the reverse-engineering scripts. Recreate with `python3 -m venv` or `uv venv`, then install what the scripts import: `Pillow`, `imagehash`, `numpy`, `librosa` (from the `import` lines in `style_*.py`). The exact original versions were not recorded.
- **auto-editor**: `uv tool install auto-editor` or `pip install auto-editor`.
- **Whisper model**: download `ggml-base.bin` for whisper.cpp into `tools/models/` (the workspace `CLAUDE.md` names this path).
- **Premiere MCP**: the source `.mcp.json` declares a `premiere-pro` server; configuration is in the workspace and was deliberately not copied.
- **Raw reference videos and large `.tsrct` files**: open from the original path in `MANIFEST.csv`. If you move or delete originals, update the manifest first.

## Safe-change rules
- Add, don't overwrite. Add a new version with a date in the name instead.
- Never move or rename originals in the workspace as part of maintaining this system.
- Keep copies in sync only on purpose; Creative OS is a snapshot, not a mirror.
