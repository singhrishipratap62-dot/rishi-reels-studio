# Rishi's Reels Studio

Claude Code workspace for gradnext reels. Open Claude **here** (the studio root) and start a style with its command.

MODEL_MODE: split
<!-- split = Sonnet does execution; before creative steps the style skill asks whether to switch to Opus.
     opus-only = never ask, never hand work to Sonnet. Rishi can also just say "opus only" in a session. -->

## Styles: one command each
| Style | Command | Skill + docs | Projects | Exports |
|---|---|---|---|---|
| Consulting case reels ("Solving real consultant cases") | `/consulting-case-reel-edit` | `01. Styles/Consulting Case/` | `03. Projects/Consulting Case/` | `04. Exports/Consulting Case/` |
| Before/after comparison reel | `/before-after-reel` | `01. Styles/Before-After/` | `03. Projects/Before-After/` | `04. Exports/Before-After/` |
| IG gradnext motion explainer | `/gradnext-motion-explainer-instagram` | `01. Styles/IG Motion Explainer/` | `03. Projects/IG Motion Explainer/` | `04. Exports/IG Motion Explainer/` |
| Rishi v2 talking-head style | `/rishi-v2` | `01. Styles/Rishi Style v2/` | `03. Projects/Rishi Style v2/` | `04. Exports/Rishi Style v2/` |
| Mock case interview (Premiere) | `/mock-case-interview-edit` | `01. Styles/Mock Case Interview/` | `03. Projects/Mock Case Interview/` | `04. Exports/Mock Case Interview/` |
| Minimal editorial | `/minimal-editorial-edit` | `01. Styles/Minimal Edit/` | `03. Projects/Minimal Edit/` | `04. Exports/Minimal Edit/` |
| Build a new style from reference videos | `/reverse-engineer-style` | `01. Styles/_New Style Builder/` | — | — |

Ignore any `/anthropic-skills:` copies of these styles (old uploads in the Claude account, out of date); always use the commands above.

When Rishi names a style or a folder without the command, load that style's `SKILL.md` and read **only** it at the start. Its "Read only when…" table says when a `reference/` doc is needed. Never auto-read `history/` folders or `09. Archive/`.

## Studio rules
- Layout, toolchain, naming and retention: `02. Shared Core/STUDIO.md`. Environment gotchas: `02. Shared Core/GOTCHAS.md`. Brand: `02. Shared Core/BRAND.md`.
- Raw footage arrives in `08. Inbox/`. Move it into `03. Projects/<style>/<project>/` when the edit starts.
- Reel ID `R###_topic_YYYY-MM-DD`, numbered across all styles. Claim the next free number with a plain `mkdir` (no `-p`); if it fails, take the next one. Two terminals can be running at once.
- Never delete or overwrite anything in `04. Exports/`, a project's source cut (`cut.mp4`, `roughcut*.mp4`, `raw_*`), or plans and build scripts. `R007`–`R009` `cut.mp4` are the only copies of that footage.
- When a reel is approved, run `"06. Tools/finalize_reel.sh" "<project folder>"` (dry run first, then `--yes`) and log the space saved in `efficiency maxing.md`.
- Log every workflow or efficiency change in `efficiency maxing.md`.
- Obsidian vault is this folder; entry note `00. START HERE/Home.md`. Use `[[wikilinks]]` in new notes, never rewrite existing plain paths. After finalize, back up with `06. Tools/backup.sh` (dry run, then `--yes`); GitHub holds knowledge only, not media.

## Token habits
- One reel per session. Run `/clear` between reels. The project's `plan.md` is the hand-off.
- Look at footage through contact sheets (one grid image), not frame-by-frame reads. Analysis subagents return text, not images.
- Long jobs (whisper, renders, downloads) run in the background with a monitor. Report progress only when asked or when the job finishes.
