# PRODUCTION WORKFLOW: Rishi's Editing Style (v1.0)

Practical pipeline for one reel, from raw clip to `exports/`. Gates follow `SKILL.md`; this file adds the numbers, the plan template, the folder layout and the Remotion build recipe. Pacing numbers come from the 15 reference reels (`SYNTHESIS.md`) [EST unless marked].

## 1. Pacing targets
| metric | target | source |
|---|---|---|
| visual changes, first 10 s | 10-14 | [EST] counted from reference timelines |
| visual changes per 10 s, body | 7-9 | [EST] |
| visual changes per 10 s, CTA stretch | 4-6 | [EST] |
| hard cut | every ≈ 4-8 s (median 6.7 s) | [MEAS] events.md, 15 reels |
| new visual state | every ≈ 1.6-2.3 s | [EST] |
| reel length | 45-70 s in the references (48-69 s) | [MEAS] |
| scene mix | A-roll ≈ 45%, full graphic ≈ 45%, split ≈ 10% | [EST] SYNTHESIS §3 |
| nothing static | > 3 s gets a build, count or push (1.0 → 1.04) | [INF] |
| silence | no pause > 0.3 s on the A-roll (auto-editor margin 0.15 s) | CLAUDE.md |

## 2. Reel template (9:16), beat order
`hook (0-5 s: face or proof at frame 0, counted promise / number / person+result / question)` → `chapters (each: A-roll + marker, then a proof/demo scene 7-13 s, payoff back on the face)` → `recap or climax proof (one longer calmer move)` → `CTA (last 5-8 s)`.
Genre recipes (teach / story / offer / AI-workflow / consulting case) are in `SCENE_PRINCIPLES.md`; choose or mix per reel. These are patterns, not limits `[R1.0]`.

## 3. Folders and names (from the workspace `CLAUDE.md`)
| what | where |
|---|---|
| raw footage | `inbox/` |
| working files | `projects/<REEL_ID>/` (recommended: `analysis/`, `plan/`, `assets/`, `remotion/`, `render/`) |
| final renders | `exports/` |
| reusable assets | `assets/` (`fonts`, `sfx`, `music`, `stickers`, `luts`, `photos`, `videos`) |
| scripts | `tools/` (whisper model `tools/models/ggml-base.bin`) |
| Reel ID | `R###_topic_YYYY-MM-DD` (e.g. `R012_resume-tips_2026-11-02`) |
Consulting-case reels have their own edit skill (`Consulting case reel edit/SKILL.md`); use this style for them only if Rishi asks ("consulting case fits Story" in `DECISIONS.md` #13).

## 4. Plan table (gate 3: STOP for approval)
One row per beat:
| time | script (exact words) | core idea | function (hook / claim / proof / chapter / CTA) | scene (S1-S8) | options A / B / C | why | assets / source | notes |
|---|---|---|---|---|---|---|---|---|
Add under the table: the pacing count per 10 s, the ground per scene (blue / cream), which single emphasis each frame gets (italic / red / green), the CTA form, and the asset list with a source for every screenshot, number and name. Beats that rest on [EST] reference values are flagged *pilot*.

## 5. Build pipeline
1. **Ask** (one batch): genre/goal, CTA + keyword, must-show proof, words/names to verify (Hinglish spelling), SFX/music available.
2. **Analyse**
   - Words: `whisper-cli -m tools/models/ggml-base.bin -l auto -ml 1 -sow -ojf -oj -osrt -of words -f <audio.wav>` (16 kHz mono wav from `ffmpeg -i in.mp4 -ac 1 -ar 16000 a.wav`). Output has word-level timings; ASR errors are expected (Hindi/Hinglish): on-screen spelling is decided with Rishi.
   - Silences/retakes: `auto-editor in.mp4 --margin 0.15s -o out.mp4` (if the command is not found on PATH, ask Rishi to install it or fall back to `ffmpeg -af silencedetect=n=-35dB:d=0.3` and cut by hand in the plan).
   - Face position over time (to keep captions and cards off the face): sample frames with `ffmpeg -vf fps=2` and check the face box; note where the face sits in the lower 48% for the split.
   - Landscape source (e.g. `Video Projects/Vid 1.mp4`, 1920×1080): crop a 9:16 window (608×1080) around the face and scale to 1080×1920, or keep the 16:9 clip inside the lower pane of a split; decide in the plan.
3. **Plan** → Rishi approves.
4. **Assets**: rebuild each UI as a recreation (React/CSS) using tokens; place fonts in `assets/fonts/` (Inter and Playfair Display Italic: Google Fonts, SIL OFL; copies already downloaded in `pilot/vid1/`). Never reuse reference-reel frames.
5. **Build in Remotion** (1080×1920, 30 fps). Use the workspace Remotion skills (`remotion-best-practices`, `remotion-create`, `remotion-captions`, `remotion-studio`, `remotion-render`) for project setup and API details. Recommended structure:
   - `tokens.ts`: colours, type sizes, spacing from `DESIGN_SYSTEM.md`.
   - `motion.ts`: the `EASE_*`/`PANE_*` beziers and `prog()` from `MOTION_LIBRARY.md`.
   - `Captions.tsx`: reads the words JSON; groups of 1-4 words (≤ 2 lines); the plan marks the one italic key word per group and the bold words.
   - One component per scene type (`Aroll`, `Split`, `Demo`, `ProofCard`, `Wall`, `Counter`, `TypeBeat`, `Cta`) and one per recipe move (`PaneDrop`, `CardSnap`, `HeroSettle`, …).
   - A-roll via `<OffthreadVideo>`; each beat is a `<Sequence from={frame} durationInFrames={n}>`; trigger frames = word start frame ± offset from the plan.
   - Graphics first, sound off.
6. **Review in Remotion Studio** at 30 fps; then render a draft and send it to Rishi.
7. **Revise**: numbered table, one pass; log new rules as `[R1.x]`.
8. **Sound** after visual approval (`SOUND_DESIGN.md`).
9. **Render + export**
   - `npx remotion render <CompId> out/raw.mp4 --codec=h264 --crf=18 --pixel-format=yuv420p`
   - Loudness: two-pass `loudnorm` to −14 LUFS, then AAC 192k: `ffmpeg -i out/raw.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -c:v copy -c:a aac -b:a 192k exports/<REEL_ID>.mp4` (measure first with `-af loudnorm=print_format=json`).
   - Run `QUALITY_CONTROL.md`.

## 6. Default export spec (workspace `CLAUDE.md`)
9:16, 1080×1920, 30 fps, H.264 High, CRF 18, AAC 192k, −14 LUFS. No 4K deliverables.

## 7. Time budget guide *(estimates, not measured)*
Analyse 10-15 min · plan 15-20 min + approval · assets/components 30-60 min (less once the component library exists) · first build 45-90 min · revision pass 15-30 min · sound 20-30 min · QC/export 10 min. The first reel is slower because the component library is built then.
