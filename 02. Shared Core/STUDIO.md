# Studio layout, toolchain and retention

## Layout
```
Teaching Claude/                 studio root (marker file: .studio-root)
├─ CLAUDE.md                     style router + model mode (loads every session)
├─ efficiency maxing.md          log of every efficiency change
├─ 00. START HERE/               map of the studio + migration manifest
├─ 01. Styles/<style>/           one folder per style = one skill
│    SKILL.md                    the only file read at the start of an edit
│    reference/                  deep docs, read only when SKILL.md says
│    history/                    changelog, old lessons, rule audit (never auto-read)
│    FEEDBACK_LOG.md             raw notes during a reel, folded into rules at the end
│    engine/ templates/ assets/  style-specific scripts and assets
├─ 02. Shared Core/              cross-style docs + shared engine (matte)
├─ 03. Projects/<style>/<project>/   working folders, split by style
├─ 04. Exports/<style>/              finished videos, split by style
├─ 05. Asset Library/            sfx, music, stickers, videos, photos, fonts, luts
├─ 06. Tools/                    python venv, whisper model, remotion, auto-editor, finalize_reel.sh
├─ 07. Resources & Learning/     tutorials, IG resources, prompts
├─ 08. Inbox/                    raw footage drops
└─ 09. Archive/                  unused styles, old config, duplicates (never auto-read)
```

## Toolchain
| Tool | Where | Notes |
|---|---|---|
| Python with numpy, opencv, torch, scipy, fonttools | `06. Tools/venv-style/bin/python` | Call it by its full path |
| Whisper model | `06. Tools/models/ggml-base.bin` | `whisper-cli` from Homebrew. Hindi/Hinglish: `-l auto` |
| auto-editor | `06. Tools/bin/auto-editor` | Silence removal |
| Remotion engine | `06. Tools/remotion/engine` | Consulting board port (`gen_board.py`) |
| ffmpeg-full | `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` | Needed for burned-in captions (libass) |
| Tesseract (video) CLI | `~/Library/Application Support/Tesseract/bin/tsrct` | Used by Rishi v2, Minimal, IG, Before-After |
| Person matte (RVM) | `02. Shared Core/engine/matte/matte.py` | Run with the venv python |
| Premiere Pro | `premiere-pro` MCP (user-level) | Verify the connection first |
| Reel close-out | `06. Tools/finalize_reel.sh "<project>" [--yes]` | Dry run by default |

## SFX library
The canonical library is `01. Styles/Minimal Edit/sfx/`. Other styles reference it there, and Mock keeps a 48 kHz copy in `sfx48/`. Point scripts at it; don't copy it into each project.

## Writing new scripts
Don't hard-code `../../` jumps to other top-level folders. Find the root instead:
```python
def _studio_root(p=os.path.dirname(os.path.abspath(__file__))):
    while not os.path.exists(os.path.join(p, ".studio-root")):
        if p == os.path.dirname(p): raise SystemExit("studio root not found")
        p = os.path.dirname(p)
    return p
```
```bash
ROOT="$(d="$(cd "$(dirname "$0")" && pwd)"; while [ ! -e "$d/.studio-root" ] && [ "$d" != / ]; do d="$(dirname "$d")"; done; echo "$d")"
```
Folder names contain spaces ("03. Projects"), so always quote paths in shell.

## Retention: what a finished reel keeps
- **Keep:** the final export in `04. Exports/<style>/`, the source cut (`cut.mp4`, `roughcut*.mp4`, `raw_*.wav`, mattes), plans and cue sheets, build scripts and configs, the final `.tsrct`, and `sfx48/`.
- **Delete with `finalize_reel.sh`:**
  - project-file copies inside `.tesseract-work`, plus effect-only and preview renders and review stills
  - consulting audio-chain WAVs and board renders
  - mock-case board frames and the SFX stem
  - `.work/` frame dumps
