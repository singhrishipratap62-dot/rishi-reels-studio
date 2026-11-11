# LESSONS_LEARNED: Rishi's Editing Style

Rishi's corrections and build-engine gotchas. This file outranks every other file in the pack (see `SKILL.md` precedence). Empty at v1.0.

## How to add an entry
- Number corrections `[R1.1]`, `[R1.2]`, … in the order given (v1.0 decisions are `[R1.0]` in `DECISIONS.md`).
- One row per correction: what was wrong, the rule now, which pack file was updated, date.
- Update the affected file in the same pass, bump the version (1.x = rule change, 2.0 = new visual language) and log it in `CHANGELOG.md`.
- Build-engine gotchas that cost a rebuild (Remotion, fonts, render flags) go in the second table.

## Corrections `[R1.x]`
| id | date | correction (Rishi's words, short) | rule now | files updated |
|---|---|---|---|---|
| [R1.1] | 2026-11-06 | "Not good… looks really bland. Copy the references' design styles, animations, graphics, every style, all the colours, exactly. Do not include rishi.docx at all. My colours come later, by iteration." | The reference style is copied exactly: reference grounds (blue #4279BB→#205AA4 with light streaks; cream #EBE7E1), white UI cards with blur depth, reference caption build (grey→white words, mixed sizes, white italic serif word), diamond badge, dark Comments sheet CTA, orange Claude asterisk, dark/cool graded A-roll. No rishi.docx token, font or rule. Rishi's colours are added later as explicit `[R1.x]` iterations. | DECISIONS (rows 4-9, 14 + token table superseded), DESIGN_SYSTEM, SKILL, CHANGELOG |

## Build gotchas
| id | date | problem | fix |
|---|---|---|---|
| G1 | 2026-11-06 | Remotion: headless Chrome fails inside Claude Code's sandbox ('Target closed', icudtl.dat / GPU crash), also from the engine's own folder | Build target stays Remotion (Rishi). Render with Chrome allowed: approve the out-of-sandbox render command, or run `npx remotion render` in Rishi's own terminal. Tesseract (`tsrct` 0.4.0) renders in-sandbox and is the fallback only if Rishi asks |
| G2 | 2026-11-06 | (fallback only) Tesseract text has one font per layer (no mixed-font runs) | One text layer per caption word; measure widths with PIL on the same font files (matches render within ~1.5%) |
| G3 | 2026-11-06 | `tsrct filmstrip` squashes 9:16 frames into landscape tiles | Review with `tsrct preview` per timestamp + PIL contact sheet at 9:16 |
| G4 | 2026-11-06 | `fontVariations` is `{id, axes:{wght:500}}`, not a list | Use the object form |


## How this file learns (set 2026-11-06)
The design system is a starting point. After each real video, Rishi's notes go into a numbered table (timestamp · problem · expected · fix · status); every durable correction becomes `[R1.n]` below and outranks DECISIONS and the reference grammar. Expect the first video to change colours, captions, motion and scene choices.

## Corrections
_(none yet)_
