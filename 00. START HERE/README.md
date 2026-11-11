# Start here

For a friendly walkthrough, open **`Studio Guide.pdf`** in this folder.

The studio was restructured on 11 Nov 2026. Every old path → new path is listed in `MIGRATION_MANIFEST.csv` in this folder, and the full log of efficiency changes is in `../efficiency maxing.md`.

## Start an edit
1. Open the terminal in this folder's parent (`Teaching Claude`) and run `claude`.
2. Drop raw footage in `08. Inbox/`, or give Claude its path.
3. Type the style command:

| You want… | Type |
|---|---|
| a "Solving real consultant cases" reel | `/consulting-case-reel-edit` |
| a raw-vs-edited comparison reel | `/before-after-reel` |
| a gradnext motion explainer from a topic | `/gradnext-motion-explainer-instagram` |
| a Rishi v2 talking-head edit | `/rishi-v2` |
| a mock case interview edit in Premiere | `/mock-case-interview-edit` |
| a minimal editorial talking-head edit | `/minimal-editorial-edit` |
| a new style built from reference videos | `/reverse-engineer-style` |

4. Claude reads only that style's `SKILL.md`. It runs on **Sonnet** by default here, and before creative steps it asks whether to switch to Opus. To skip the question for a session, say "opus only". To skip it permanently, set `MODEL_MODE: opus-only` in `../CLAUDE.md`.
5. When the reel is approved, Claude runs `06. Tools/finalize_reel.sh` to clear the regenerable working files.

## Where things are
| Folder | What's inside |
|---|---|
| `01. Styles/` | One folder per style. Each has `SKILL.md` (rules), `reference/` (deep docs), `history/` (changelog and rule audit), `FEEDBACK_LOG.md`, `engine/` |
| `02. Shared Core/` | `STUDIO.md` (layout, tools, retention), `GOTCHAS.md` (environment traps), `BRAND.md` (gradnext), `engine/matte` |
| `03. Projects/<style>/` | Working folders for each video, grouped by style |
| `04. Exports/<style>/` | Finished videos, grouped by style |
| `05. Asset Library/` | Music, stickers, background loop, photos, fonts, platform guides |
| `06. Tools/` | Python venv, whisper model, Remotion, auto-editor, `finalize_reel.sh`, `dedupe_clone.py` |
| `07. Resources & Learning/` | IG lead-magnet resources, tutorial transcripts, prompts |
| `08. Inbox/` | New raw footage |
| `09. Archive/` | Unused styles (Daniel Presley, Azma Paper Stage, Claude Edits, Rishi v1.3), the Creative OS snapshot, old config, duplicates. Claude never reads it unless asked |

## Teaching Claude a correction
Just tell Claude during the edit. It logs the note in the style's `FEEDBACK_LOG.md`. When the reel is approved, it folds the lasting rule into `SKILL.md` and removes any rule the note reverses.

## Obsidian
Open `Teaching Claude` as a vault in Obsidian. Start at `Home.md` (this folder); each style has a `Hub - <style>.md` linking its skill, reference docs, feedback log and projects. Link new notes with `[[wikilinks]]`. `06. Tools/build_vault_index.py` refreshes the project lists (`backup.sh` runs it).

## Backing up
- **Knowledge (GitHub).** This folder is a git repo, and `.gitignore` keeps out every video, audio, project file and toolchain, so a commit is about 26 MB of skills, docs and scripts.
  - First time: `gh auth login`, then `gh repo create rishi-reels-studio --private --source=. --remote=origin --push` (or add a remote by hand).
  - After that: `06. Tools/backup.sh` (dry run), then `06. Tools/backup.sh --yes`.
- **Media (Google Drive).** Upload `04. Exports/` and, if you want, `09. Archive/`.
