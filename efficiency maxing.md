# Efficiency Maxing

The running log for making my Claude editing workflow faster, smaller and cheaper in tokens. Every suggestion and every implemented change goes here.
Status: `proposed` · `in progress` · `done` · `skipped` · `needs Rishi`.

Last updated: 2026-11-11

---

## 1. Findings snapshot (audit of 2026-11-11, before any changes)

### What I actually use
| Area | Activity | Status |
|---|---|---|
| Consulting case reels | R006–R011, the most mature pack | **Active** |
| Before-After | R012, leanest pack | **Active** |
| IG gradnext Motion Explainer | IG gradnext 003–006 | **Active** |
| Rishi v2 ("Updated Rishi's editing style", was in Azma's style) | Video 1, 2, 5 (in progress) | **Active** |
| Mock case interview (Premiere) | 1 long edit | **Active** |
| Minimal Edit | 4 edits, dormant since 3 Nov | **Active** (kept) |
| Daniel Presley, Azma Paper Stage, Claude Edits, Rishi v1.3 + copy, Creative OS | Unused or superseded | Archived |

### Where tokens went
- About 8.6M output tokens on **Opus** vs 2.0M on Sonnet; the default model was `opus[1m]`.
- About 2 billion cache-read tokens, from long sessions re-reading big docs.
- Words of docs each style forced Claude to read **before** starting an edit:

| Style | Before |
|---|---|
| Rishi v2 | about 11,000 |
| Minimal | about 2,800 (often about 13,000 with the deep docs) |
| Consulting | about 6,900, plus board.html and the previous plan |
| Mock | about 3,600 |

- The same rules (brand, loudness, safe zone, captions, sound) were rewritten in every pack, with conflicting numbers.
- Only Before-After was a real installed skill.

### Where storage went (about 22 GB)
- About 2 GB of exact duplicates (the SFX library existed 17 times).
- About 5.5 GB of regenerable intermediates.
- About 2.3 GB of toolchains (needed).

---

## 2. Suggestions and status

| # | Suggestion | Saves | Status |
|---|---|---|---|
| S0 | Create this log | — | **done** |
| S1 | Archive unused styles, never delete them. `09. Archive/` has a README saying what each item is and whether it's safe to delete after uploading to Drive. | Clutter; 3.7 GB can leave the laptop after upload | **done** (Drive upload: **needs Rishi**) |
| S2 | Storage cleanup | 3 GB so far | **done**, part 1 (see §3). More in §4 |
| S3 | `06. Tools/finalize_reel.sh` close-out, which every skill runs after approval | Stops re-bloating | **done** |
| S4 | Shared core in `02. Shared Core/`: STUDIO, GOTCHAS, BRAND, matte engine | Lessons learned once, no re-teaching | **done** |
| S5 | Token diet: SKILL.md is the only mandatory read; deep docs in `reference/` with triggers; history in `history/`; a rule audit per pack | About 70–85 % fewer startup tokens | **done** |
| S6 | One command per style, usable from anywhere (links in `~/.claude/skills/`) | Time | **done** |
| S7 | Parameterised build engines (one engine plus a small per-reel config instead of rewriting 700-line scripts) | Big per-reel token and time savings | **proposed**. Deliberately not done today; it changes code paths and needs one test reel per style |
| S8 | Model split: Sonnet by default in this studio only; skills ask before creative steps; `MODEL_MODE: opus-only` override | The largest token saver | **done** |
| S9 | Config cleanup: old launcher, `.claude-home` and generic `reel-*` skills archived; stale Premiere MCP flag removed; root CLAUDE.md is now a router | Fewer surprises | **done** |
| S10 | Session habits (cheat sheet, §5) | Tokens, time | **done** (written into CLAUDE.md) |
| S11 | 291 MB of byte-identical duplicate subagent logs in `~/.claude/projects/…Rishi-s-Editing-Style/5cae8427…/subagents` | 291 MB | **done**: replaced with verified clones; history intact |
| S12 | Numbered, style-split structure (`00. START HERE … 09. Archive`; each style has sibling folders in Styles, Projects and Exports) | Findability | **done** |
| S13 | GitHub backup of the knowledge: repo initialised, `.gitignore` keeps all media and toolchains out (about 26 MB of skills, docs and scripts) | Safety | **done**: first local commit `2dcdaab` (2,339 files, 14 MB). Pushing needs a private GitHub repo from Rishi |

---

## 3. Change log

| Date | Change | Where | Result |
|---|---|---|---|
| 2026-11-11 | Audit; this file created | root | — |
| 2026-11-11 | **Restructure.** 93 moves, no copies; 68,731 files before, all present after (+4 small copies). The old → new list is in `00. START HERE/MIGRATION_MANIFEST.csv`. `DIff Acc`, `Azma's style`, `Minimal Edits` and `Claude Edits` are gone as top-level folders. | whole studio | Findability |
| 2026-11-11 | **Path repair.** 439 text files updated. Engines now find the root via the `.studio-root` marker instead of `../../` jumps, so they survive future moves. Old consulting rebuild scripts made safe for paths with spaces. Toolchain links relinked. | engines, `06. Tools` | Nothing broke |
| 2026-11-11 | **Verification of the move.** 0 syntax errors. R011 board engine re-run → events **byte-identical** to the original. Before-After rebuilt from the moved script → same spec and loudness (−14.2 LUFS), SSIM 0.998 vs the original render. Whisper model, matte model, fonts, brand, MBB sticker and mock footage all resolve. **Caught:** the consulting board silently drops the MBB logos if the sticker path breaks; fixed before it could happen. | — | Quality kept |
| 2026-11-11 | **Token diet** (4 parallel agents, each with a rule audit in `history/RULE_AUDIT.md`). Mandatory startup read: Consulting 6,860 → 1,612 words; Rishi v2 11,036 → 1,834; Minimal about 2,840 (13k with deep docs) → 1,781; Mock 3,619 → 1,593. Reversed or duplicated rules resolved (later rule wins; listed in each audit). Minimal also recovered 8 rules that existed only in the old duplicate copy. | `01. Styles/*` | About 70–85 % fewer startup tokens |
| 2026-11-11 | **Independent quality review** of the diet: no lost approval gates and no wrong numbers. Small gaps fixed: Rishi v2 IG safe zone + QC safe-zone check + options precedence; Consulting retake-detection rule + face-card framing; Minimal "shrink long support lines". | SKILL.md files | Quality kept |
| 2026-11-11 | IG Explainer and Before-After: new paths, Model gate, close-out step. Before-After builds now go to `03. Projects/Before-After/R0XX…/` and exports to `04. Exports/Before-After/`. | those SKILLs | — |
| 2026-11-11 | New Style Builder: saved-styles list updated; new styles are now created in the lean pack format and registered as a command | `01. Styles/_New Style Builder` | Future styles start lean |
| 2026-11-11 | **7 style commands registered** (links in `~/.claude/skills/`) | global skills | One command per style |
| 2026-11-11 | **Model.** `"model": "sonnet"` in `Teaching Claude/.claude/settings.json` (studio only; other projects keep Opus). `MODEL_MODE: split` in root CLAUDE.md. | settings, CLAUDE.md | Token saver |
| 2026-11-11 | **Duplicates → APFS clones.** 104 groups; every path keeps an independent file, data stored once; each clone verified by checksum. | whole studio | 1.93 GB |
| 2026-11-11 | **finalize_reel** run on approved reels with confirmed exports: R011, R012, IG R003–R005 | `03. Projects` | 1.07 GB |
| 2026-11-11 | Unique files rescued from the old Minimal copy (4 reference reels, 3 tutorial reels, links, IG safe-zone image, 2 .tsrct versions) | Minimal pack, Asset Library, Resources | Duplicates folder is now truly deletable |
| 2026-11-11 | Disk free on the data volume: 5.1 GB → 6.7 GB measured (clone savings can take a little while to show in Finder) | — | +1.6 GB measured |
| 2026-11-11 | **Decisions on open items** (Rishi: "decide, do what feels right"). See §4 for each decision and why. | various | — |
| 2026-11-11 | R007–R009 protected: `KEEP_SOURCE.md` in each project; `finalize_reel.py` now refuses any project that has one | `03. Projects/Consulting Case` | Their only footage can't be cleaned up by accident |
| 2026-11-11 | Plain-language **Studio Guide.pdf** (7 pages: structure, before → now map, how-tos, what's safe to delete) | `00. START HERE/Studio Guide.pdf` | Easy orientation |
| 2026-11-11 | Duplicate subagent logs (S11) → verified APFS clones; git repo got its first local commit on `main` | `~/.claude/projects`, root | Disk free now **7.5 GB** (was 5.1) |
| 2026-11-11 | **Batch intake + one shared options board** for six same-topic Rishi v2 reels (vid6–12). Intake (romanise, face track, matte) done once for all; one board with per-section "fits" lines replaces six boards. Storyboard and build stay one reel per session, using `Batch vid6-12/plan.md` as the hand-off. | `03. Projects/Rishi Style v2/Batch vid6-12/` | About 5 fewer options-board passes |
| 2026-11-11 | **Obsidian + GitHub structure.** Vault at the studio root with `.obsidian/` config (wikilinks, noise hidden: `06. Tools`, `09. Archive`, node_modules, work dirs; ~160 notes). New notes only: `Home.md`, a `Hub - <style>.md` per style, `Hub - Shared Core.md`, generated `Projects Index.md`, three templates. No SKILL.md, plan or reference doc edited. `06. Tools/build_vault_index.py` refreshes project lists; `06. Tools/backup.sh` commits and pushes (dry run default). Root `README.md`, `.gitattributes`, Obsidian state added to `.gitignore`. | root, `00. START HERE`, `01. Styles/*`, `06. Tools` | Easier linking and navigation; backup routine |

---

## 4. Decisions taken (2026-11-11) and what's still open

**Decided:**
1. **R007–R009 missing finals:** kept everything, because `cut.mp4` + `run_build.sh` can rebuild each reel. Each project is marked with `KEEP_SOURCE.md`, which `finalize_reel` respects. *If you find the finals, drop them in `04. Exports/Consulting Case/` and delete the marker.*
2. **Mock case "<seq> RAW" backup step: kept.** It only adds a safety copy before the destructive silence cut, matches rule M2 ("every stage on a duplicate") and doesn't change the output.
3. **Minimal Edit, graphics behind the subject: by default** on close and standing framings, never over the face. This matches the design system and your latest shipped edit (series intro). You can still ask otherwise per video.
4. **Minimal Edit music level:** kept 18–24 dB as the starting point, plus a rule that if it's inaudible on your phone, raise it (Consulting settled at 13 dB). This guards against the problem without changing a look you've approved.
5. **Old `/anthropic-skills:` uploads:** I can't delete these from your Claude account from here. Root CLAUDE.md now tells Claude to ignore them and use the local commands.
6. **S7 (engine rewrite): deferred on purpose.** It changes the code every reel depends on. The quality rule says not to ship it without a full test render per style, which today would cost about 3 GB of free disk and long renders. The next reel in each style is the natural test.
7. **Archive upload to Drive: not done.** 3.7 GB of video can't go through the Drive connector sensibly. The archive stays local and nothing is lost.
8. **Mock MG intermediates and Rishi v2 Video 1 drafts:** kept, because a Premiere project or the in-progress Rishi v2 work may still use them.

**Still needs you (only you can do these):**
- Push the backup: create a private GitHub repo, then run `git remote add origin <url> && git push -u origin main` in `Teaching Claude`.
- Optional: upload `09. Archive/` to Drive, then delete it locally (frees up to 3.7 GB).
- Optional: delete the old style uploads from your Claude account settings.

---

## 5. Cheat sheet

### How to work now
- Open `claude` in `Teaching Claude/`, then type the style command (table in `00. START HERE/README.md`).
- It runs on Sonnet. Before creative steps it asks to switch to Opus; say "opus only" to skip the question for a session.
- Give feedback freely: it goes into the style's `FEEDBACK_LOG.md` and is folded into the rules when the reel is approved.

### Session habits that save tokens
- **One reel per session.** Run `/clear` between reels; the reel's `plan.md` is the hand-off.
- **Batch feedback** into one message, and approve with short replies ("approve", "go sound").
- **Ask for contact sheets** (a grid of frames in one image) instead of single frames.
- **Long renders and transcriptions** run in the background, so don't ask for progress turn by turn.
- **Close every approved reel** with `06. Tools/finalize_reel.sh` (dry run, then `--yes`).
- **Run `/fewer-permission-prompts` once** in this folder to allowlist the repeated ffmpeg, whisper and python calls.
