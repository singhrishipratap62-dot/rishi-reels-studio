---
name: rishi-editing-style
description: Edit a talking-head reel (9:16, real footage) in Rishi's Editing Style (v1.3: Ink blue palette + Editorial serif captions on the 15-reel reference grammar, plus signature depth moves) — A-roll alternating with UI-card proof scenes on ink/ice grounds, split pane, chapter badges, Playfair-italic hero captions, built in Remotion. Use when Rishi asks to edit a reel "in my style" / "Rishi's Editing Style".
---

# Rishi's Editing Style — edit skill (v1.2)

Turns a raw talking-head clip into a 1080x1920 reel in this style. The style was reverse-engineered from 15 reference reels and adjusted by Rishi's Stage 0 answers.

## Read first, in this order
1. `LESSONS_LEARNED.md`: Rishi's corrections `[R1.x]`. They override everything below.
2. `DECISIONS.md`: Stage 0 rules `[R1.0]` and the token mapping.
3. `DESIGN_SYSTEM.md` (tokens, type, layout, components), `SCENE_PRINCIPLES.md` (scene types and genre recipes), `MOTION_LIBRARY.md` (named moves with curves), `EDITING_PSYCHOLOGY.md` (why/when), `DEPTH_AND_ORBIT.md` (signature orbit / behind-subject / 3D moves and the rules for rationing them).
4. As needed: `PRODUCTION_WORKFLOW.md`, `SOUND_DESIGN.md`, `QUALITY_CONTROL.md`, `VISUAL_REFERENCE_LIBRARY.md`.

Precedence: LESSONS_LEARNED > DECISIONS (`[R1.3]` Ink blue + Editorial serif; `[R1.2]` depth family) > reference grammar (scene types, layout, motion curves, pacing from the 15 reels). The palette and captions are a **working starting point**: Rishi's feedback on real videos defines the final system.

## Fixed rules (do not vary without Rishi)
- 9:16, 1080x1920, 30 fps. Text inside y 250-1500 and left of x 920.
- **The A-roll is the spine.** The speaker opens the reel, says the payoff lines and closes it. Graphic beats sit between face beats.
- **Proof scenes are UI**: rounded white cards (posts, profiles, toasts, chats, product cards) on the **ice** ground (`#EAF0F8`) or `card.dark` on the **ink** ground (`#0B1224`). One ground per scene. Cards enter with blur → sharp; the A-roll defocuses under floating cards.
- **Captions (Editorial serif, `[R1.3]`)**: ≤ 5 words per group; hero = the meaning word in Playfair Display Bold Italic, lowercase, ≈ 132px, centred; support = Inter Medium ≈ 48px tight around it. Support reveals word by word (rise 22px, 420 ms); the hero reveals character by character with blur. Below the face, inside the safe zone. Details: DESIGN_SYSTEM §4.
- **Colour roles** (`[R1.3]`): one accent, blue `#3E7BFA` (badges, key word on ice, send button, glows); green `#2FD08A` only for money; red `#E5484D` only for hand-drawn scarcity marks; orange `#D97757` only for the Claude asterisk. Text `#F2F6FC` on ink, `#0B1730` on ice.
- **Motion grammar**: card entrances use a fast-start ease-out with ≤ 3% overshoot, in two speed tiers (secondary 0.35-0.45 s, hero 1.0-1.5 s). The split pane drops in 1.0 s `cubic-bezier(.7,.1,.4,.9)`. Springs are for small objects only. All values are in MOTION_LIBRARY.
- **Proof lands on or before the word** (−10…+10 f). Numbers and prices may lead by 0.7-2.4 s. Never after.
- **Pacing**: 10-14 visual changes in the first 10 s, 7-9 per 10 s in the body, 4-6 in the last stretch. Nothing static for more than ~3 s; a hold gets a slow push (1.0 → 1.04).

## Flexible (choose per reel, in the plan)
Which optional moves appear (counter, red ellipse, card wall, carousel, proof zoom, defocus bridge, drum-roll words, spring pops), blue vs cream ground per reel, chapter marker form (diamond / 1-2-3 tracker / italic ordinals), CTA form (decided per reel), genre recipe (teach / story / offer / AI-workflow, or a new mix).

## Gates (always in this order)
1. **Ask up front** (one batch): genre and goal of the reel, CTA and keyword, any must-show proof (screenshots, numbers, names), words/names to verify (Hinglish spelling), whether any SFX/music are in `assets/sfx` / `assets/music`.
2. **Analyse**: `whisper-cli -l auto` word timings, silences (`auto-editor --margin 0.15s`), stray words/retakes, the face position over time (to keep captions off the face), and landscape → vertical reframe if needed.
3. **Plan, then STOP for approval.** One row per beat: `time | script | core idea | function (hook/claim/proof/chapter/CTA) | scene type | options A/B/C | why | notes`. Plus the pacing count per 10 s and a list of assets needed.
4. **Assets**: every screenshot/UI/number has a stated source. Rebuild UIs as recreations; never reuse third-party frames from the reference reels.
5. **Build** in Remotion (see PRODUCTION_WORKFLOW; LESSONS_LEARNED G1: render where headless Chrome is allowed). Graphics first, sound off.
6. **Revise**: numbered table `# | timestamp | problem | expected | fix | status`. Fix every item in one pass. New rules go to LESSONS_LEARNED as `[R1.x]`.
7. **Sound only after visuals are approved** (SOUND_DESIGN).
8. **QC + export** (QUALITY_CONTROL): H.264 High, CRF 18, AAC 192k, −14 LUFS, into `exports/`.

## Scene selection (summary; full table in SCENE_PRINCIPLES)
| the script says… | use |
|---|---|
| opinion, personal claim, chapter intro, CTA ask | A-roll (+ chapter badge at chapter starts) |
| a rule/definition while still talking | split pane (graphic top 48%, A-roll below) |
| a principle that can be shown | full graphic: the UI *performs* the rule |
| a quantity ("hundreds", "12 clients", "₹/$ earned") | card wall or counter |
| a person/case | their real post/profile card (recreated) |
| money/result | counter or toast, green |
| deadline/scarcity/old price | red pen mark (ellipse/strike), text-only scene near the end |
| question or verdict | drum-roll words / giant word on the blue ground |

## Text rules (summary)
Captions mirror speech exactly; Hinglish in Roman script only. The italic word is the key noun, qualifier or emotional word. On graphic scenes captions move to the top band (y ≈ 260-420). Captions disappear when the UI text is the content. On-screen spelling beats ASR; ask Rishi about any uncertain word.

## Sound (summary)
Built after visual approval. ≈ 0.4 cues/s; cuts mostly dry; soft cues on pane/card moves, counters and keyword typing; quiet bed. Never name a reference sound as fact. Details: SOUND_DESIGN.md.

## Evolve the system
Every correction Rishi gives becomes a `[R1.x]` rule in LESSONS_LEARNED, updates the affected file, bumps the version (1.x = rule change, 2.0 = new visual language) and is logged in CHANGELOG as core/optional/experimental/proposed. Build-engine gotchas that cost a rebuild also go into LESSONS_LEARNED.
