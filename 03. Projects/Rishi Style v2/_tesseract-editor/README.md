# Tesseract browser editor (official example, runtime 0.4.0)

Set up 2026-11-09. Download-only saving: no browser settings changed.

## Open it
```sh
cd "/Users/rishi/Documents/Teaching Claude/03. Projects/Rishi Style v2/_tesseract-editor"
python3 -m http.server 8767 --bind 127.0.0.1      # leave this running
```
Then in Brave: http://localhost:8767 → **Choose** a `.tsrct` → edit → **Download** saves an edited copy.
Stop the server: `pkill -f "http.server 8767"`.

## Rules
- Work on a **copy** of a project, never on the only version. Download gives a new file; tell Claude its path so Claude continues from it (and stops regenerating that draft from the build script).
- The editor can change: layer names, text, font size, fill colour, position, scale, rotation, opacity on **non-animated** layers. Animated or scripted properties show ◇ and are locked. Export still happens via Claude / the `tsrct` CLI (always 1080p).

## Folder
- `index.html`, `app.js`, `style.css`: official example editor (copied from the tesseract-editor skill, unchanged).
- `runtime/`: tesseract-0.4.0-web runtime (checksum verified).
- `dl/`: the downloaded archive + checksum.
- `test/`: Phase 1 test files (a copy of roughcut_v3_v4 + browser-saved versions). Safe to delete.
