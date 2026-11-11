# Rishi's AI Editing System: Knowledge Base

Written 2026-11-09 by Claude after reading every connected folder (`Documents/Teaching Claude/` incl. `Azma's style/`, ``, `Minimal Edits/`, `Claude Edits/`, the Joseph transcripts).
**Purpose:** the single source of truth for making Instagram resources (the "comment EDIT" funnel and later paid products). Read this instead of re-exploring the folders. Only open a source file when you need an exact value it points to.

Evidence tags used below: **[V]** verified (the file/output exists on disk), **[D]** stated in the docs (not re-run or watched by Claude), **[R]** Rishi's own rule/verdict, **[X]** abandoned or superseded.

---

## 0. How to use this file
- Making a new resource → read §1, §2, §4, §5, §14–§18. Pull specifics (values, rules, stories) from §6–§12.
- Need an exact number (caption size, ease curve, LUFS) → it's in §6–§8; the source path is given so you can verify.
- Never publish anything marked "private study" (§16).
- Update §18 when resource decisions change, and §2 when a new style system is built.

---

## 1. Context and goals
- Creator: Rishi, Instagram **@rishi.docx** (AI explainer reels; talking head + AI-voiceover). Also runs gradnext content (consulting-prep startup, always written lowercase "gradnext").
- Videos: 9:16, 1080×1920, 30 fps, ~17–35 s, mostly **Hinglish** spoken to camera (lav mic, marble wall, green jacket in roughcut_v3/vid2).
- The funnel: a reel shows Claude edited the video → "comment EDIT" → auto-DM (Super Profile) → resource; emails collected through Super Profile's automation.
- First resource is for **vid2** (`Azma's style/Video Projects/Video 2/`), a 17 s reel. Exact spoken promise (romanised): *"maine ye poori video claude se edit ki hai… mujhe ye cheez seekhne mein hafte ya mahine lag gaye… end-to-end usse badhiya edit kaise karwa sakte ho, warna har doosri video toh slow lagti hai… comment kar do 'edit' and I will send you a resource jisse aap ye poori cheez step by step seekh sakte ho."* → the resource must be **step by step**.
- Companion reel: roughcut_v3 (`Azma's style/Video Projects/Video 1/`), thesis **"Claude can edit your videos only once you teach it your taste."** Structure: naive belief → "aisa kuch nahi hota" → people hoard skills/repos → thesis: taste / design skill → proof: this video was edited by Claude → contrast with "Claude slop" → "I taught it what to do, how to do it" → iterations → autonomy → CTA comment EDIT.
- Resource constraints set by Rishi (2026-11-09): **English**; share a **meta understanding / rough system only**; **no skill files, no engine code, no HTML templates** for now. Future resources will point the same way (shared method), possibly one per video plus a blended one.
- Long-term: build credibility and an audience around AI video editing, then monetise (products, templates, systems). No paid launch yet.

---

## 2. Inventory: every editing system built (≈ Oct 28 – Nov 9, 2026)

| System | Built from | Format | Build engine | Status | Location |
|---|---|---|---|---|---|
| **reverse-engineer-style** (meta skill) | Joseph's method + Rishi's process | — | — | The process that produced every pack below [V] | `Daniel Presley Editing Style/reverse engineer style SKILL.md` (also a saved skill) |
| **Daniel Priestley Editing Style** v1.0 | 28 YouTube videos | 16:9 + 9:16 | Claude Motion demo | Pack + Motion demo; no production edit found [V] | `Daniel Presley Editing Style/` |
| **Rishi's Editing Style** v1.3 | 15 reels by an editing-education creator (topics like "3 editing mistakes", "Claude replicates editing style", "$282k program", "lifetime offer 299") | 9:16 | Remotion (planned) | Measured teardowns done; pilot never finished; parts reused in v2 [V][X] | `Rishi's Editing Style/` (teardown/, engine/matte, engine/measure-scripts) |
| **Minimal Editorial** v1.1 (Arthur Brooks look) | Reference reels + Joseph's Arthur Brooks tutorial | 9:16 | Tesseract (first edit), Motion artifact optional | 4 real edits with versioned renders [V] | `Minimal Edits/minimal-edit-system/` (+ copy `01. Styles/Minimal Edit/`; Design System artifact NDguL5ottfkuCUcQQKzCoP) |
| **Consulting case reel edit** v1.4 (gradnext) | 2 of Rishi's own finished reels | 9:16 | ffmpeg + HTML/CSS board rendered by Playwright | **Most production-proven**: R003–R010 made; finals in `exports/` [V] | `01. Styles/Consulting Case/` |
| **Mock case interview edit** v1.0 (gradnext) | One real 4 Nov mock case | 16:9 long form, 2 cams | Premiere Pro via MCP | One edit done; Premiere MCP removed 2026-11-05 [V][X] | `01. Styles/Mock Case Interview/` |
| **gradnext motion explainer** | gradnext design system | 9:16 AI-voiceover | Tesseract | Plugin + R003–R006 projects [V] | `01. Styles/IG Motion Explainer/` |
| **Prompt-to-Reel** (rishi.docx) | 6 reference reels | 9:16 | Motion artifact / Tesseract | Style catalog + "16 effects" project [V] | `Claude Edits/` |
| **Paper Stage** (@asmaijazkhann) | 15 reels | 9:16 | Motion artifact | Full skill pack built, then **rejected on first use** ("too generic") [V][X] | `Azma's style/skill/`, `plan.md`, `breakdown/`, `work/` |
| **Rishi v2** (current) | Blend of Minimal + Rishi v1.3 + Priestley + Paper Stage | 9:16 Hinglish | **Tesseract CLI 0.4.0** | **Live system.** roughcut_v3 drafts 1–4, vid2 draft 1 rendered [V] | `Azma's style/Video Projects/Updated Rishi's editing style/` |
| **Creative OS** | Copy-only index of the above | — | — | 870 files copied, ~61 empty placeholder folders [V] | `Creative OS/` |
| Basic reel skills | — | 9:16 | ffmpeg / auto-editor / whisper | rough-cut, captions, export, premiere-handoff [V] | `.claude/skills/` |

**The story in one line:** 7+ style systems in ~2 weeks; 5 build engines tried (Motion artifact, Remotion, Premiere MCP, ffmpeg+Playwright, Tesseract); the winners are Tesseract for talking-head style edits and ffmpeg+Playwright for templated series.

---

## 3. Folder map (what lives where)
```
Teaching Claude/
  NoteGPT_Transcript_*.txt        Joseph (Ultimate Editors) tutorials: "Premium IG reels with Claude", "Iman Gadzhi style"
  Minimal Edits/                  Arthur Brooks refs, Joseph minimal-style transcript, minimal-edit-system/ (pack, sfx/, edits/)
  Claude Edits/                   Prompt-to-Reel refs, _style_system/, rishi/ plugin, "Prompt to Reel - 16 Effects" Tesseract project
  Stills/                         ~127 stills from reference videos (private study)
  Azma's style/                   plan.md (Paper Stage project), Videos/ (15 refs), work/ (stills, sheets, strips, transcripts, keys),
                                  breakdown/ (KEYS, NOTES, PLACEMENT), skill/ (paper-stage-edit), sfx/ (22 sorted SFX)
    Video Projects/
      Updated Rishi's editing style/   ← Rishi v2 pack (SKILL, learnings, DECISIONS, design/caption/motion/scene/sound/QC docs, engine/, templates/, assets/)
      Video 1/                         roughcut_v3: SRT, face.json, PLAN, STORYBOARD, drafts v1–v4 (each its own folder)
      Video 2/                         vid2: SRT, roman_map, matte, face.json, vid2_edit_v1 (draft1.mp4, .tsrct, cue sheet, MP3 stems)
      _tesseract-editor/               official browser editor (parked)
                         "Reels Studio" Claude Code workspace (CLAUDE.md, start-claude.sh isolates config)
    01. Styles/Consulting Case/    pack + engine/ (cut.py, islands.py, align.py, render.js, board.html, compose.sh, sfx.py, qc.py…)
    01. Styles/Mock Case Interview/     pack + engine/ + sfx48/
    01. Styles/Minimal Edit/, Rishi's Editing Style/, Daniel Presley Editing Style/, 01. Styles/IG Motion Explainer/
    Creative OS/                  00–12 numbered knowledge base (copies)
    .claude-home/skills/          tesseract-video, tesseract-motion, tesseract-editor, tesseract-design, impeccable
    tools/                        venvs, style_strip.py, style_audio.py, claude-tools/INSTALL-STATUS.md
    exports/ projects/ inbox/ assets/
  Resources for IG/               ← this file + resources
```

---

## 4. The core method: teaching Claude a style (the real asset)
Origin: Joseph (Ultimate Editors) tutorials → formalised by Rishi in `reverse-engineer-style` SKILL and `Azma's style/plan.md`. Rishi's version adds measurement, token discipline and a correction loop.

### 4.1 Stage 0: ask before analysing
Style name + creator; what to copy (whole identity or parts: captions, colour/type, scenes, motion, sound, pacing); how strictly (exact clone / core fixed / loose); brand relationship (standalone or fused with rishi.docx/gradnext); video type (talking head, green screen, AI voiceover, mute UI demo, split screen, podcast); languages (Hinglish = Roman script only); build target; sound sources; any tutorials. Answers → `DECISIONS.md` as [R1.0].

### 4.2 Stage 1: capture references (cheaply)
- 7–20 best reels (+ any tutorial). ffprobe each; name R1..Rn.
- Transcripts with word timestamps (mlx-whisper / whisper-cli), snapped to `silencedetect`; flag confidence < 0.7. (Azma: laptop Whisper too slow → Rishi supplied one combined SRT, Claude split it per video.)
- Cut detection: `ffmpeg -vf "select='gt(scene,0.3)',showinfo"` → shot lengths.
- **Contact sheets are what Claude looks at:** `fps=1,scale=270:480,tile=6x5` (Azma: scene-change stills at 360 px, deduped, 12 per sheet with filename on each tile; 2,222 stills → 212 sheets → 82 thinned sheets).
- **Motion strips:** 0.5–2 s cut at native fps around an animation, tiled into one image, 1–2 per animation type. Measure timings from native frames only.
- Keep one best still per scene type. Third-party stills = private study.

### 4.3 Stage 2: analyse (with evidence tags [OBS] [TX] [EST] [INF] [R])
Tokens (pixel medians for colours; font candidates; sizes as ratios), caption logic, **scene taxonomy discovered from the refs (not a preset list)**, motion library (M## with from→to, duration, delay, easing), textures, editing psychology (line → scene → why), pacing (avg shot, first visual, share of graphics), core vs optional vs experimental, gaps.
- Azma example numbers: ~50 % runtime graphics, ~11 cuts/min, median graphic 2 s, A-roll stretches median 2.8 s / max ~8 s, first graphic ≤ 3 s in 12/15 videos. 22 named keys (K01–K22) × 12 animation types.
- Rishi v1.3 example: 15 reels torn down frame by frame; animation curves fitted (track.py + ease_fit.py, rmse gate ≤ .05 = [MEAS]).

### 4.4 Stage 3: audio by measurement (Claude can't hear)
Demucs stems → librosa onsets aligned to visual events → peak/LUFS per cue → cue character (duration, brightness, attack) → match to library files → cue-group table marked measured/matched/unverified → Rishi listens on a phone and corrects. (Azma: exact-file matching of 22 SFX found no confirmed matches, so the trigger map came from timing analysis: sound on ~1 in 4–5 graphic entries.)

### 4.5 Stage 4: write the knowledge pack
README, SKILL, DECISIONS, LESSONS_LEARNED, DESIGN_SYSTEM, SCENE_PRINCIPLES (or Joseph-style RULEBOOK + LOOKBOOK + REFS_INDEX), MOTION_LIBRARY, EDITING_PSYCHOLOGY, PRODUCTION_WORKFLOW, SOUND_DESIGN, QUALITY_CONTROL, VISUAL_REFERENCE_LIBRARY, CHANGELOG. Written section by section.
- Joseph's vocabulary: **rule book** (sizes, spacing, layout, curves, speed) + **lookbook** (shapes, colours, gradients, icons, assets) + reference library (every animation saved with keyframe sheet).
- Paper Stage load order (good pattern for token economy): RULEBOOK + REFS_INDEX always; LOOKBOOK sections only for keys used; refs/ only for first builds; SOUND at sound step; last 20 lines of LESSONS before planning.

### 4.6 Stage 5: package the edit skill
Fixed vs flexible rules, gates, scene selection summary, text rules, sound summary, "evolve the system" rule. Proposed as a saved skill.

### 4.7 Stage 6: pilot edit + correction loop (where taste actually transfers)
First draft is only partly right (Joseph/Minimal tutorial: "expect 60–70 %"). Every Rishi correction → LESSONS_LEARNED as [R1.x], outranks every estimate; update the affected file; bump version (1.x rules, 2.0 visual-language change). Engine gotchas logged too.

### 4.8 Joseph's method vs Rishi's (for positioning)
| | Joseph (Ultimate Editors) | Rishi |
|---|---|---|
| References | Upload 14–20 videos + a Figma breakdown board into Claude | Local extraction → contact sheets + strips + measured stats; Claude never reads raw frames one by one |
| Output | Rule book + lookbook + 225-animation library → skill | Same pack shape + DECISIONS/LESSONS precedence + evidence tags |
| Planning | Claude suggests, human plans ("AI isn't creative enough to plan alone") | Same, plus HTML options board (≥5 per frame type) → storyboard |
| Build | Claude/Remotion | Tesseract / ffmpeg+Playwright, regenerable build script |
| Sound | "Premium sound design" | Measured, dense-but-quiet cue system with effects-only verification |
| Proof of failure | Not shown | Paper Stage built and rejected; 4 drafts; 28-point feedback round |
| Monetisation | Skills sold inside the "AI editing fundamentals" masterclass (Ultimate Editors) | Not yet |

---

## 5. The per-edit loop (shared by every pack)
1. **Ask up front only what's missing** (style, framing, safe zone, SFX library, licensed music, words/names to verify, CTA keyword).
2. **Analyse:** word timings, silences, retakes, ASR fixes (case logic: numbers must add up; lakh/crore).
3. **Plan, then STOP.** One row per beat: time · exact line · core idea · function · options A/B/C (or ≥5) · why · notes. Never animate before approval.
4. **Assets** with source + licence; real logos; never fake an article or quote.
5. **Build** from one regenerable script; each draft in a new folder; previews/filmstrips checked by Claude.
6. **Revise:** notes → numbered table (timestamp · problem · expected · fix · status); storyboard first for non-trivial changes; fix all in one pass.
7. **Sound only after visuals are approved** (Rishi v2 later merged sound into draft 2+).
8. **QC + export,** report what was checked and what wasn't ("Claude can't listen").
9. **Append LESSONS.**

Human vs Claude vs code:
- **Rishi:** rough cut (Gling/manual), recording, picks on the options board, taste notes, supplying photos/logos/music, phone listening check.
- **Claude:** transcript cleanup, planning, scene choice, all graphics/layout/motion code, caption timing, sound placement and levels, QC, documentation, lessons.
- **Code (on the laptop):** SRT remap, face tracking, person matte, rendering, loudness, black/silence detection, OCR checks.

---

## 6. Rishi v2: the live talking-head system (most detail)
Pack: `Azma's style/Video Projects/Updated Rishi's editing style/`. Entry `SKILL.md` (name `rishi-v2`); narrative `learnings.md` (read first). Distilled from roughcut_v3 drafts 1–4 + 5 style "books". "Defaults, not rules": Rishi's notes on the current video always win.

### 6.1 Pipeline (Stage 0 → 6)
0. **Intake:** rough cut + original recording + SRT of the original (Hindi script, mixed English).
   - `engine/tools/srt_remap.py`: original SRT → rough-cut SRT by **spectral audio matching** (raw waveform matching failed because the cut audio is processed); warns on chunks straddling cuts.
   - Romanise: `roman_map.json` (exactly as spoken) → `roman_captions.py` → `words.json`. Devanagari nukta letters are precomposed (U+095B) → match keys by NFD.
   - `face_track.py` (OpenCV YuNet) → `<video>.face.json` (chin_y for captions, nose for B&W tracking).
   - Person matte (RVM, `02. Shared Core/engine/matte/matte.py`) if behind-the-head graphics are planned; new matte per cut. Tesseract's built-in personMatte gave an empty matte.
   - Head/tail and silence trims: just do them (silencedetect + cut on a quiet frame) and report; don't ask.
1. **Options board** (local HTML, STOP): every frame type (hook, reaction, list, thesis, proof, contrast, explanation, iteration, CTA, caption style) × ≥5 drawn phone-frame options over real stills; Keep/Maybe/No + notes + "Copy my picks". Rishi pastes back mixes ("B baseline + bits of A and C").
2. **Storyboard** (local HTML): before/after stills per beat, timings, F-numbers, **assumptions box**; ambiguous motion → 5 interpretations as 5-frame strips (0.00/0.15/0.30/0.50/0.72 s). Silence after a storyboard = approved, unless "storyboard only".
3. **Build in Tesseract** in a new folder `<name>_edit_vN` (claimed with `mkdir`, no `-p`). Build order: captions → scenes in time order → A-roll motion → sound cues. Review: portrait filmstrips 270×480 of changed beats.
4. **Feedback rounds:** voice-transcribed paragraphs → numbered F-list → storyboard → next draft folder.
5. **Sound** + effects-only check (`fx_check.py`).
6. **QC + delivery:** MP4 + editable `.tsrct` + `Previews/Filmstrip-draftN.jpg` + `sound_cue_sheet.md` (+ SFX-only / voice-only MP3s on request). Report checked vs not checked. Append LESSONS.

### 6.2 Decisions (D1–D23, Rishi verdicts)
No Claude artifacts ever; review = local HTML + PNG · options board before anything (≥5 per frame type) · storyboard before every build · captions romanised Hinglish exactly as spoken, Inter for Latin, no Devanagari font · caption hero Playfair Bold Italic white + Inter support, bottom gradient, **no blue hero** · centred, ≤ ~22 chars/line · **smoothness above all; pops/snaps are defects** · every card enters with "line → rectangle + blur + small slide" · white cards = white→light-grey gradient + vignette, never blue-tinted · subtle corners (tiles ≈8 px, cards 14–36) · real logos (Claude, GitHub, Instagram) stored for reuse · his face sticker as avatar · split screen with full hair line visible · organic painted blob, not a circle ("a circle has no personality") · behind-head graphics use the real matte, no visible gap · wall scene one-word black Playfair · PiP: rounded, headspace cropped, one card stays and its contents swap · CTA: comments sheet + full keyboard, face blurred above, tap + green tick, held to last frame · sound dense but quiet, long smooth swooshes · each draft in a new folder · investigations timeboxed to 2–3 min; structural changes need feasibility report + approval · browser GUI editor parked · **every export 1080×1920 / 30 fps, never 720p**.
Rejected: Paper Stage as main look; text on reaction beats ("nope."); blue captions on light scenes; white on white; fade/scale pops; snappy sheet/keyboard; blank white beat > ~1 s; separate behind-head scene when a PiP is up; big rounded tile corners; face pushed too low in the split; over-correcting ("a little" = ≈30 px, not 120).

### 6.3 Captions (`CAPTION_SYSTEM.md`)
- Text: romanised Hinglish exactly as spoken; English words lowercase; punctuation as pauses; flag words across cuts.
- Grouping: ≤5 words, ≤ ~22 chars/line; hero = meaning word (noun, verdict, key term); never split compound verbs.
- A-roll mode: hero Playfair Display Bold Italic lowercase 132 px white, centred, baseline y 1420, ≤740 px wide; support Inter Medium 48 px white 85 % centred above (baseline = hero − 0.8×size − 8) and below (hero + size + 14); bottom gradient transparent → 45 % black over bottom 40 %.
- Reveals: support word by word on spoken time (rise 26 px + fade, 0.5 s, ease (0.22,1,0.36,1)); hero letter by letter (slide −24 px 0.42 s + fade 0.28 s + blur 8→0 0.32 s; stagger = spoken length ÷ letters, 14–45 ms; finish ≥0.35 s before group ends). Hard cut between groups.
- Context modes: light ground (ink #0B1730 hero, #4A5878 support, just above the card) · split pane (hero 100 px at top of white pane, baseline 330) · PiP single line (Playfair 54 px between card and PiP) · wall one-word (black Playfair inside the tile under the face) · CTA one-word (white Playfair ≤78 px above "Comments").
- Repeated phrase with one changed word → keep the support line, swap the hero only.
- Glitch: blur without `layerSize: [1080,1920]` clips glyphs to a baseline strip.

### 6.4 Design tokens (`DESIGN_SYSTEM.md`)
Safe zone x 120–960, y 250–1600, keep right icon column clear below y 1130. Colours: ice #EAF0F8 (+grain 0.8), ink #0B1224, ink.text #0B1730, muted #4A5878 / #9AA8C7, accent #3E7BFA, card.dark #121C38, card.white #FFFFFF→#E4E6EA + vignette, board #F4F5F7→#E2E4E8, wall.bg #0D0E12, green #2FD08A (sent only), highlighter #FFD68A, Claude orange only via real logo, blob #5D8BFF→#0839B0. Type: Playfair Display Bold Italic (heroes) + Inter (everything else); fontsource latin subset lacks ✓ ↑ ● → draw as shapes. Card radius 22–36, tiles ≈8, shadow 0 14 30 rgba(11,18,36,.16), grain 0.6–1.0. Layout grids for chat card, split pane (940 px pane, face shifted down 460 px), behind-head card (x 90–990, y 250–710), wall (3×4 tiles 300×533), PiP (32 % at 540,1270), comments sheet (top y 980, keyboard from 1220).

### 6.5 Motion (`MOTION_LIBRARY.md`)
Eases: E1 (0.22,1,0.36,1) entrances · ES (0.45,0.05,0.2,1) big moves · EX (0.55,0,0.75,0.4) exits · hold for typing. Never linear (except drifts), no overshoot/bounce.
R01 line→rectangle reveal (scaleY 3→100 %, scaleX 96→100, 0.6–0.7 s, rise 40 px, blur 18→0) for every card · R02 slide-blur exit · R03 word rise · R04 hero letter build · R05 shrink face into UI (1.28 s) · R06 slide-out from behind the head (matte) · R07 logo ±6° slow spin · R08 pane drop/lift · R09 card stagger · R10 glide from right · R11 orbit fast→slow · R12 blob paint-in · R13 B&W nose-track (sat −100, scale 110 %, follows nose with lag + wiggle) · R14 cut-hiding zoom (100→112 % across a jump cut) · R15 wall zoom-out (360→100 % over 1.45 s, starts exactly on the trigger word) · R16 PiP in/out · R17 contents swap · R18 progress fill · R19 sheet rise · R20 tap + success tick · R21 key press · R22 typing · R23 highlighter swipe · R24 tile breathe · R25 A-roll slow push +1.2 %/s.

### 6.6 Scene library (`SCENE_LIBRARY.md`)
S1 opening twin slide-out (logo disc + video card from behind the head) · S2 hook "shrink into the chat" (face becomes the attachment in a Claude chat card; prompt types; highlighter; send; result card shows his own clip graded warmer) · S3 B&W nose-tracked beat on "no / doesn't work like that" (no words) · S4 split pane list (skill cards then dark repo cards) · S5 split pane doc + organic blob with ~8 orbiting words (palette, practice, rhythm, sound design, pacing, texture, timing, typography) · S6 behind-the-head timeline card (lanes: A-roll, captions, graphics, sfx; Claude name pill) · S7 wall zoom-out of "slop" tiles, his face one tile · S8 PiP + card (file list SKILL.md / RULEBOOK.md "what to do" / LOOKBOOK.md "how to do it" → progress 100 %; then Analyse · Plan · Build · Captions · Export ticks) · S9 comments-sheet CTA typing E·D·I·T, tap, green tick, held to end. Plus option pools (5+ ideas per frame type, tagged by source book).
vid2 additions: reel timer (ring + countdown from behind the head to the corner, held all reel); "show the real work" (real past drafts + real skill-file cards with GitHub mark) for effort beats; DM "resource" card enters on the green tick.

### 6.7 Editing psychology (`EDITING_PSYCHOLOGY.md`)
Face is the spine (graphics sit around the face or carry it inside them) · announce on the face, explain with a picture · show his real world (real tools, files, own clip) · premium = calm + smooth; speed comes from cutting on words, not fast animation · every graphic says the spoken word. Beat → scene table (hook→S1+S2, reaction→S3, list→S4, thesis→S5, proof→S6, contrast→S7, steps→S8, iteration→S8 swap, CTA→S9, opinion/joke→A-roll). Pacing: first graphic ≤ ~0.7 s; graphics ≈45–55 % of runtime; ≤ ~8 s plain A-roll; cut on the trigger word, return to face after the line ends; no empty white beats; hide jump cuts in motion; hold finished states ≥0.5 s; CTA held to the end. Anti-patterns: decorative graphics, >2 moving focal points, pops, cutting away from the face on the verdict, generic AI-looking mock-ups.

### 6.8 Sound (`SOUND_DESIGN.md`)
"Lots of sound, each one quiet" (from Minimal). Voice: already mastered cut → 75 Hz HPF −1.5 dB, separate Audio layer (A-roll video silent). Raw voice chain: 75 Hz HPF → 2.5:1 at −24 dBFS → makeup → limiter −1.5. Cue map: hitech on caption hero (−17 dBFS) · flick on each support word/list row (−27 to −30, skipped within 110 ms of a bigger cue) · long swoosh/woosh on big transitions, **peak on the move's midpoint** (−17 to −21) · pop on card settles · techpop on ticks · highlighter on swipes/line→rect/progress · risertick at 100 % · flicker · click · typing. First 5 s +3 dB. Align each file's **peak** (from `sfx_meta.json`), not its start. ≈170 cues in 33 s is normal. Mix ≈ −15.5 LUFS, TP ≤ −1 dBTP, measured on the final MP4. Effects-only render: every cue within ±60 ms. vid2: voice raw −7.3 LUFS → −15.8.

### 6.9 Depth / behind the head (`DEPTH_AND_MATTE.md`)
RVM matte video → root Video layer with the **same transform JS as the A-roll** → graphic gets `trackMatte {mode: lumaInverted}`. Card high (y 250–710) so the head covers only its lower-middle. Hand off to a non-matted copy before the face moves (shrink/PiP). 1–3 moments per reel.

### 6.10 Review formats (`REVIEW_FORMATS.md`)
Self-contained HTML, phone-frame mock-ups with CSS `cqw`, real stills/logos, Google Fonts, sticky "Copy my picks" + "Download picks .txt", Keep/Maybe/No + notes, state in localStorage (try/catch), "my pick" marker; checked in headless Chromium (`node --check` on the script; an apostrophe once broke a page) + PNG snapshot. Mock-ups are sketches: say so (Rishi reads them literally).

### 6.11 QC (`QUALITY_CONTROL.md`)
Process (storyboard shared, new folder, every F-item addressed) · captions (exact romanisation, centred, ≤22 chars, glyphs whole, right mode, never over a card) · look (line→rect entries, grey-only whites, subtle corners, real logos, no gap around head) · motion (nothing snappy: big moves 0.8–1.45 s, entrances 0.5–0.7 s; no blank beat > 1 s; jump cuts hidden; CTA held) · audio (100 % cues within ±60 ms, −15.5 LUFS, TP ≤ −1, voice not doubled) · export (ffprobe 1080×1920/30, blackdetect = 0, filmstrip saved, honest report).

### 6.12 Tesseract (CLI 0.4.0) notes (`TESSERACT_NOTES.md`, `engine/README.md`)
Tesseract = Mirage's local editing/render engine (`mirage-hq/tesseract`, `tsrct` CLI; skills tesseract-video/motion/editor/design in `.claude-home/skills/`). Portable `.tsrct` project, one FX composition, native text/shape/group/video/audio layers, keyframes + JS animators, WGSL shaders, colour grading, filmstrip/preview, H.264/ProRes export. No transcription, no generative video.
Pipeline: `create` → `import-video` (aroll, matte) → `import-font` → `import-asset` (logos, avatar, sfx) → copy to `base.tsrct` → `checkout` → build script writes `editable.json` + `edits.json` → copy base over project → `commit` → `apply` → `filmstrip`/`preview` → `export` (1080p). Always rebuild from clean base.
Gotchas: `playback.mapping.input.start` is on the parent clock (= inputRange.start) or late groups never render · `rect.position` is local top-left · keyframes on nested Video clips → wrap in a Group · every gaussianBlur needs `layerSize` · shape fill alpha via `fills[0].opacity` · cropRect doesn't crop → scale + mask · mask cornerRadius ignored → cubic Bézier rrect · Inter subset lacks ✓↑● · matte = lumaInverted + mirrored JS · omit volume on picture copies · typing via textContent hold keys · JS animators read layer-local time · one key per time per property · effect params via `setFxLayerEffectParamAnimator`.
Engine: `lib.py` (builder) + `build_template.py` (whole draft 4 as one config + 9 scene blocks + A-roll motion + caption modes + cue system); claimed byte-identical to draft 4 [D]. Tools: srt_remap, roman_captions, face_track (+YuNet), sfx_prep, fx_check. Python deps: numpy, opencv-python-headless, fonttools.
Browser editor (official tesseract-editor + web runtime) can open/save `.tsrct`; needs Chrome or Brave flag; parked.

---

## 7. Consulting case reel edit (gradnext series, production-proven)
Pack: `01. Styles/Consulting Case/` (SKILL v1.4, LESSONS with 45 entries). Raw one-camera talking head in → finished reel out, end to end in Rishi's Claude terminal. Engine: **ffmpeg + HTML/CSS board rendered frame by frame by Playwright**; Tesseract (the OCR tool, not Mirage) only for QC.
- **Fixed format (exact clone of his own reels):** 4 scenes: S1 hook (white top panel: header "Solving real consultant cases · Part NN" + gradnext; case photo; question in light grey with each word darkening as spoken; real McKinsey/BCG/Bain logo strip; subtle blur-in on the panel only) → S2 one punch-in (~1.3x, eased 110→100 %) on "This is a real <firm> case" → S3 board scene (gradnext background loop; self-building case board: FACTS phase with clarifying-question tree, then SOLVE phase with method tabs and a ₹ number line floor/ceiling/answer; face card with glow; one-line 2–4-word caption) → S4 end card ("Follow for Part NN+1").
- **Automatic cut:** speech islands from a 20 ms RMS envelope, whisper per island, retake detection (keep the LAST complete take), no pause > 0.3 s, 40 ms head / 60 ms tail handles, 8–12 ms crossfades. ASR fixed with case logic. `align.py` aligns to the corrected script.
- **One approval stop only:** `plan.md` beat table (time · spoken · board action · motion) + retakes + ASR corrections + hook image + licence + arithmetic check.
- **Build:** `render.js` (Playwright, deterministic `seek(t)`, chunks of 400 frames, retries for hung screenshots) → `compose.sh` → `speed_music.sh` (final at 1.2x, music bed 13 dB under voice, pitch kept) → `compose_green.sh`. Deliverables: final, `_1x`, `_green` (graphics on #00FF00), `_raw` + placement guide. All 1080×1920, never 4K.
- **QC script `qc.py`:** blackdetect, silencedetect, OCR readability, punch-in count, timings, arithmetic, part number, video vs audio stream duration, LUFS + true peak, sharpness after blur-in.
- **Beat → visual framework:** quantity over time → progress bar; money → ₹ count-up; physical object → line icon/photo; count → unit grid; cost build-up → stacked bar; A vs B → two boxes; unknown asked → "? ?" placeholder filled when answered; method result → chip → marker on number line.
- **Hard-won engine lessons (good content):** never write 4K intermediates (disk filled); whisper timestamps drift ~1 s on long files → per-island transcription; Playwright→ffmpeg pipe silently truncated a reel (QC caught it: never skip QC); chrome-headless screenshot hangs randomly; ffmpeg per-segment fps drift lost 0.5 s of picture; gblur `sigmaV` must be sent too; AAC adds 0.3–0.5 dB true peak; ffmpeg crop-zoom wobbles → render zooms as sub-pixel affine transforms; Mac idling made renders 60× slower; Claude Code sandbox blocks Metal/VideoToolbox (run whisper on CPU, encodes outside the sandbox); two reels can be edited in parallel terminals with separate R### folders; one reel ≈1.7 GB of project files.
- Outputs on disk [V]: `exports/R003_mckinsey-hourly-rates…mp4`, `R004_mbb-revenue…`, `R005_india-consulting-hub…`, `R010_motorcycle-growth…_1x.mp4`, placement guides R006–R009, projects R006–R010.

## 8. Minimal Editorial (Arthur Brooks look)
Pack: `Minimal Edits/minimal-edit-system/` (v1.1). Built from Joseph's Arthur Brooks tutorial + references; first real edit: "First principles in consulting" (Kashish podcast clip, 34 s, Riverside split screen), then the 30-day series intro (4 versions, italic vs upright captions compared; italic shipped).
- **10 scene principles:** cinematic captions · B-roll + text (paper texture, dark/blurred edges) · paintings (public domain + paint/paper texture + text around the subject) · line + text · line + illustration (horizon marker / zigzag / line to subject) · text-centric with quote marks · centre illustration · side illustration · object callout · graphs. Plus A-roll + captions (~45 % of runtime) with zoom cuts and a constant +1.2 %/s push.
- **Captions (source of Rishi v2's captions):** Inter + Playfair Italic; ≤5 words; support word by word (rise 22 px/420 ms), hero character by character with blur; finish ≥350 ms before the cut; support 36 % of hero size, tight to it.
- **Safe zone (Rishi's IG template):** x 120–960, y 250–1600, icon column x > 845 below y 1130; `check_safe()` audits every element after camera push.
- **Sound (origin of "dense but quiet"):** v1 with 27 procedural cues judged "average at best"; v2 with 103 cues from his library approved. Hi-Tech Click (impact), flick (support), Highlighter (lines), Riser+Tick (arrival), Swoosh/Woosh (transitions), pops, clicks; first 5 s +3 dB; measure each file's peak inside the trimmed window (an inherited peak value was 8 dB off).
- Tutorial benchmark timings (57 s edit): cuts + plan doc 15 min · human planning 15 min · build 60 min · revisions 10 min · sound 15 min. First draft "60–70 % there".
- Outputs [V]: `edits/first-principles-kashish/FirstPrinciples_v2_sound.mp4`, `edits/series-intro-v1/…`, `edits/series-intro-versions/Intro_V1–V4.mp4`, `edits/series-intro-30days/…`.

## 9. Paper Stage (@asmaijazkhann) — the instructive failure
Plan: `Azma's style/plan.md`. Phase A (train) fully done in one day (2026-11-08) across 6 sessions with model routing (Sonnet for extraction/sorting, Opus for style study/skill). Output: `paper-stage-edit` skill: RULEBOOK (density 40–45 % graphics, first graphic ≤2 s, trigger map line → key), LOOKBOOK, REFS_INDEX, 18 active keys (K01 caption-whisper, K02 focus-return, K03 mono-beat, K04 ink-headline, K06 paper-stage, K07 avatar-cutout, K08 face-sticker, K09 cursor-click, K10 stack-in, K11 counter-build, K14 colour-broll, K15 article-highlight, K16 chart-build, K17 ui-mock, K18 quote-card, K19 object-lowerthird, K20 timeline-rail), SOUND, LESSONS, face_track tool. Dropped keys: memes, podcast split, today-card, gold-tag.
**What happened:** first edit (roughcut_v3 draft 1) in Paper Stage was "not as good as I aimed"; the look was too generic for Rishi. He also deleted the Motion artifact ("We never create an artifact"). The fix: an options board mixing five style books → Rishi v2. Lesson: **copying one creator closely doesn't give you *your* style; taste emerges from choosing across options and correcting drafts.**

## 10. Other systems (short)
- **Rishi's Editing Style v1.3:** 15 reels from an editing-education creator, torn down with measured curves (`teardown/V##/BREAKDOWN.md` + `animations.json`, `SYNTHESIS.md`). Ink-blue palette, editorial serif captions, UI-card proof scenes on ice/ink grounds, split pane, signature depth family (orbit, behind-subject, matte). Built for Remotion; pilot never shipped. Its tokens/scenes live on inside Rishi v2. The reference creator's own reels sell an editing program (price-drop / lifetime-offer closers): useful monetisation research.
- **Daniel Priestley:** 28 videos; cream paper cards, serif + sans, blue = idea / crimson = number, numbered arc-wipe chapters, glowing PiP whiteboard, name pills, quote cards; no captions on the speaker. Motion demo artifact BDZx9noBfRT4SdBLoHyTn1. Ideas borrowed into v2: name pill, framed screen + highlighter, whiteboard + PiP.
- **Mock case interview (16:9, Premiere MCP):** 2 speakers/2 cameras, 30–45 min. Silence only when both tracks silent > 1 s; batch ripple-removes ≤50 ranges, end → start; self-assessment segment cut; Whisper word-level with speaker labels; 4–8-word captions; 70/30 case board + stacked speakers; stop after a pilot chapter. Never use Premiere's own transcript cuts (inaccurate); `overwrite_clip`, never `add_to_timeline`. Premiere MCP removed 2026-11-05 (backup config in `06. Tools/claude-tools/premiere-mcp-removed-backup.md`).
- **gradnext motion explainer:** topic/post → ONE Claude doc (TTS-ready script ~140–165 words at 2.6 words/s, figures check table, scene-by-scene cues) → ElevenLabs VO → Tesseract build from `templates/build_reel.py` keyed to whisper word offsets. Look: gradnext loop background, Avenir LT Pro + Besley Italic, periwinkle highlighter over the bottom 30–35 % of glyphs, word reveal out of blur for all text. gradnext design system only.
- **Prompt-to-Reel (rishi.docx):** "/slash-command typed in an app UI → result takes over"; style catalog A1–A10 explainer styles, B1–B7 talking-head transformations (over-the-shoulder proof cards, glass graph, freeze-frame sticker, tier list, text-behind, colour grade wipe, behind-the-person); built in ink + paper versions; keyword asked at the end.
- **Creative OS:** copy-only index (13 sections) with manifest and sha256 verification; many empty placeholders; useful as a map, not as a working system.
- **Basic Reels Studio skills:** reel-rough-cut (auto-editor `--margin 0.15s` + whisper-cli `-l auto`), reel-captions (ffmpeg subtitles burn-in, Montserrat Black), reel-export (1080×1920, 30 fps, CRF 18, −14 LUFS), premiere-handoff.

---

## 11. Toolchain, dependencies, where things run
- **Claude surfaces:** Claude Code in an isolated workspace (`start-claude.sh` sets `CLAUDE_CONFIG_DIR` to `.claude-home`; `CLAUDE.md` folder rules; `settings.json` sandbox + deny edits outside), and Cowork with the laptop shell (device_bash) for heavy work. Rishi prefers local compute over cloud to save tokens.
- **Local tools:** ffmpeg-full (has libass; plain ffmpeg lacks subtitles/drawtext), ffprobe, mediainfo, auto-editor, whisper-cli (whisper.cpp, ggml-base) / mlx-whisper (whisper-turbo), ImageMagick, yt-dlp, Node + Playwright (headless Chromium), Python venvs (numpy, opencv, librosa, fonttools, pysrt), OpenCV YuNet face model, RVM matte, Demucs (audio study), Tesseract OCR (QC), Tesseract CLI 0.4.0 (Mirage, build engine).
- **Installed but not central:** Manim CE/GL, Remotion CLI (npx), remotion/manim/motion-canvas skills, youtube-clipper, Playwright MCP, claude-code-video-toolkit clone (`06. Tools/claude-tools/INSTALL-STATUS.md`).
- **External services:** ElevenLabs (voice clone for AI-voiceover reels), Gling (rough cuts), Google Fonts/fontsource, Wikimedia/Unsplash/Pexels for licensed images.
- **Sandbox gotchas:** Claude Code sandbox blocks Metal/VideoToolbox; background jobs die between device_bash calls (run foreground, <170 s, resumable); deleting files on the laptop is blocked (stale files left for Rishi); images pasted in chat don't reach disk.

## 12. How Rishi works and what he likes (taste profile)
- Reviews **visually** (local HTML + PNG), never long chat tables; wants **≥5 options** and mixes them.
- Feedback = long voice-transcribed paragraphs with timestamps; his words: "smooth" (most frequent, good), "snappy"/"pop" (bad), "premium", "subtle", "a little" (= small), "decent" (okay, not great). Notices every glitch (half glyphs, black bars, oval gaps, white on white, uneven padding).
- Wants honesty about checks ("Claude can't listen"), every draft kept, timeboxed investigations, approval before structural changes, short chat output with file links.
- Visual taste: premium minimal, calm, smooth long eases, face as the spine, real logos/files over stand-ins, serif-hero captions, grey-scale whites, subtle corners, dense-but-quiet sound.
- Brand separation: rishi.docx styling never in gradnext content and vice versa.

## 13. Token economy and model routing (teachable on its own)
- Claude never reads raw frames one by one: contact sheets (12–30 tiles), motion strips only for 1–2 examples per animation type.
- All ffmpeg/Whisper/sorting on the laptop; cloud only for viewing images.
- SRT for study, word-level JSON only for builds.
- Index files (REFS_INDEX, last 20 lines of LESSONS) are what edits load; the full library only for chosen scenes.
- New chat per phase; a single `plan.md` with checkboxes + session log is the handoff between chats ("Continue from the next unchecked step. Use the model listed for that step.").
- Opus for style study, new scene types and "doesn't feel like her" fixes; Sonnet for extraction, sorting, reused templates and small fixes.
- Regenerable build scripts mean revisions don't re-explain the whole edit.

---

## 14. Proof assets usable in content (Rishi's own material only)
- vid2: `Video 2/vid2.mp4` (raw), `vid2_cut.mp4`, `vid2_edit_v1/vid2_draft1.mp4`, `Previews/Filmstrip-draft1.jpg`, `sound_cue_sheet.md`, SFX-only / voice-only MP3s, storyboard pages in `Video 2/storyboard/`.
- roughcut_v3: drafts 1→4 in `Video 1/roughcut_v3_edit…_v4/` (each with MP4, filmstrips, cue sheets), storyboards v1–v4 + options board in `Video 1/storyboard/`, `references/stills/` of approved frames in the v2 pack (these are Rishi's own frames).
- Numbers worth quoting: 4 drafts and a 28-point feedback round on one 33 s reel; ≈170 sound cues in 33 s; 7+ style systems in ~2 weeks; 2,222 stills → 82 contact sheets for one style study; 45 logged corrections on the consulting system; 8 consulting reels shipped (R003–R010).
- The rejected Paper Stage draft 1 vs final draft 4 = the "taste" story.
- Real skill-file names shown on screen in the reel (SKILL.md, RULEBOOK.md, LOOKBOOK.md): naming them publicly is fine; their contents are not shared.

## 15. Verified vs claimed vs abandoned
- **Verified on disk:** consulting finals R003–R005, R010; roughcut_v3 drafts 1–4; vid2 draft 1; Minimal Editorial versions; every pack/skill/engine file listed above.
- **Claimed in docs, not re-checked by Claude:** byte-identical rebuild of draft 4; render quality; loudness numbers; whether any reel was posted and how it performed.
- **Abandoned / superseded:** Claude Motion artifact and Remotion as build targets for talking-head edits; Premiere MCP; Paper Stage as a look; Priestley (no production edit); Rishi v1.3 pilot; browser GUI editor (parked).

## 16. Rights and IP rules (hard)
- Reference reels, stills, contact sheets, strips and breakdowns of other creators (Azma/@asmaijazkhann, Arthur Brooks, Daniel Priestley, the v1.3 reference creator, Prompt-to-Reel refs, Joseph's tutorials) are **private study only**. Never publish them or put their faces/logos/UI captures into outputs. The packs say so in their READMEs.
- Public resources use Rishi's own footage, drafts, screenshots of his own tools/pages, and generic examples.
- Naming the creators whose style was studied: avoid by default (describe "a minimal editorial style", "a creator I admire"); ask Rishi before naming anyone.
- Licensed assets only (fonts: Inter + Playfair Display are SIL OFL; stock from Wikimedia/Unsplash/Pexels with source logged).

## 17. Competitive context
- **Joseph (Ultimate Editors)** publicly teaches "train Claude on any editing style" (Iman Gadzhi style, Arthur Brooks minimal style, his own 5-key short-form style) and sells the skill files inside an "AI editing fundamentals" masterclass. Same comment/link funnel. Rishi's process started from his transcripts, so a generic "how to train Claude on a style" resource reads second-hand.
- Rishi's angles that Joseph doesn't show: the **taste thesis** (Claude produces slop until you teach it *your* taste); **documented failure** (a full style built and rejected; 4 drafts); **measurement where Claude is blind** (sound by numbers, effects-only check); **token economy** for people on normal plans; **Hinglish/Indian creator** context (romanised captions exactly as spoken); **series at scale** (consulting reels template); honest "what's human, what's Claude" split.

## 18. Resource decisions so far
- vid2 resource promise: step by step, English, meta level. No skill files, engine code or HTML templates (for now).
- Delivery: comment EDIT → Super Profile auto-DM → link; emails captured there.
- Recommended direction (2026-11-09): "Teach Claude Your Taste" playbook built on the vid2/roughcut_v3 story, a Style Card exercise, the gated edit loop, generic starter prompts, an honest can/can't list, two tool paths (no-code vs Claude Code). Alternatives: Style Card mini-kit; "Behind the edit" teardown.
- **Free vs advanced vs paid boundary:**
  - Free: the method, style-card fields, the gate structure, the lessons-log habit, generic prompts, the vid2 story and failures, principles (dense-but-quiet sound, smoothness, face as spine, safe zone).
  - Advanced (later, maybe paid): exact commands for contact sheets/strips, full prompt set per stage, annotated skeletons of skill files, sound cue map + levels.
  - Paid / private: real skill packs, engine code (build_template, srt_remap, face_track, fx_check, consulting engine), options-board and storyboard templates, Tesseract gotchas, ongoing updates/support.
- Project copy of these decisions: Claude project doc `resource-ecosystem/edit-resource-strategy.md`.
- Resource files live in this folder (`Resources for IG/`), numbered with this file as `00_`. Created 2026-11-09 (Rishi picked items 1, 3, 4 ×2, 5, 6, 8 from a 10-item menu): `01` Teach Claude Your Taste playbook · `02` Prompt Pack · `03` Premium Captions · `04` Sound Design for AI Edits · `05` Breakdown VID2 (vid2) · `06` Breakdown VID1 (roughcut_v3) · `07` Reverse-Engineer Any Editing Style. Not made yet from the menu: Style Card kit, safe-zone/export checklist, "what failed" case study, series-from-one-template.

## 19. Open questions / gaps
- Is the **no-code path** (plain Claude chat or Cowork without a local shell) actually workable end to end? Untested: everything so far ran through a local shell. Test before promising it.
- Target audience not chosen yet (freelance editors vs creators editing their own reels).
- Whether vid2 and roughcut_v3 are posted, and their numbers.
- Music: no licensed bed used in Rishi v2 yet.
- Paper Stage skill and plan still describe the old Motion workflow (superseded by Rishi v2).

## 20. Glossary
- **A-roll:** the talking-head footage. **B-roll:** cutaway footage.
- **Style pack / book:** the folder of docs that describes one editing style (rules, look, motion, sound, lessons).
- **Skill:** the SKILL.md entry point Claude loads to run a pack.
- **Key / scene type:** a named reusable visual (e.g. K15 article highlight, S7 wall zoom-out).
- **Rule book / lookbook:** Joseph's terms: rules (sizes, timing, when) vs look (shapes, colours, assets).
- **Options board:** HTML page of ≥5 drawn options per frame type for picking.
- **Storyboard:** HTML page of the picked mix, frame by frame, before building.
- **F-list:** numbered feedback items. **LESSONS / [R1.x]:** logged corrections that outrank defaults.
- **Contact sheet:** many downscaled frames tiled into one image so Claude can study a video cheaply. **Motion strip:** a short native-fps frame sequence tiled to measure an animation.
- **Matte:** a black/white video of the person used to put graphics behind the head.
- **Dense but quiet:** many sound cues, each low in level.
- **Tesseract:** Mirage's local video editing/render CLI (`tsrct`) — not the OCR tool of the same name, which is used only for QC.
