# Rishi's Reels Studio

Claude Code workspace for gradnext reels: one skill per editing style, shared studio rules, project plans and tooling scripts. Also an [Obsidian](https://obsidian.md) vault (open this folder as the vault; entry note `00. START HERE/Home.md`).

## What this repo is
A backup of the studio's **knowledge**: `CLAUDE.md`, style skills and reference docs (`01. Styles/`), shared rules (`02. Shared Core/`), project plans and build scripts (`03. Projects/`), tool scripts (`06. Tools/`), and the Obsidian config.

## What it is not
Videos, audio, images, PDFs, project files and toolchains are excluded by `.gitignore`. Exports and raw footage live on Google Drive. Reinstallable tooling (Python venvs, models, node_modules) is rebuilt, not backed up.

## Restore
1. `git clone <this repo> "Teaching Claude"`
2. Reinstall tools per `02. Shared Core/STUDIO.md` (venv, whisper model, ffmpeg-full, Tesseract, auto-editor).
3. Copy exports and footage back from Drive.
4. Start with `00. START HERE/README.md`.

## Backing up
`06. Tools/backup.sh` (dry run), then `06. Tools/backup.sh --yes` to commit and push.
