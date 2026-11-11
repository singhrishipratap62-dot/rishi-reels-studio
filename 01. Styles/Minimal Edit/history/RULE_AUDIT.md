# Rule audit — v1.2 restructure (2026-11-11)

Proof that nothing was lost when `SKILL.md` became the only mandatory read. Each row maps a rule (by its source ID/section) to where it lives now. "SKILL §X" = a section of `../SKILL.md`; `ref/` = `../reference/`. Sources: **L** = `LESSONS_LEARNED.md` (this pack, v1.1), **L-old** = the archived older copy (`09. Archive/Duplicates (safe to delete)/Minimal Edits (old copy)/minimal-edit-system/LESSONS_LEARNED.md`), **DS** DESIGN_SYSTEM, **ML** MOTION_LIBRARY, **TS** TEN_SCENE_PRINCIPLES, **EP** EDITING_PSYCHOLOGY, **PW** PRODUCTION_WORKFLOW, **SD** SOUND_DESIGN, **QC** QUALITY_CONTROL, **S1.1** the old SKILL.md v1.1.

The two LESSONS copies were identical except: L-old line 36 (upright-serif note), L-old §6 extra bullet (peak inside trimmed window), L-old §10 (series intro). L has "(Playfair Display Bold Italic)" in line 36 where L-old does not. All are kept below.

## LESSONS_LEARNED (both copies)

| Source | Rule | Now lives |
|---|---|---|
| L §1 | Ask style (default this pack) | SKILL §Workflow 0 |
| L §1 | Ask split-screen/multi-cam framing | SKILL §Workflow 0 |
| L §1 | Ask platform safe zone (default IG Reels) | SKILL §Workflow 0 |
| L §1 | SFX library first (`minimal-edit-system/SFX/` → `sfx/`) | SKILL §Workflow 0, §Sound |
| L §1 | Ask about a licensed music track; none → no bed | SKILL §Workflow 0, §Sound |
| L §1 | Speaker name / words to verify | SKILL §Workflow 0 |
| L §2 | Two roles, two motions; never whole lines at once | SKILL §Motion (M01/M02) |
| L §2 | Support: word by word on spoken time, rise 22 px→0 / 420 ms, opacity 0→100 / 380 ms, `cubic-bezier(0.22,1,0.36,1)` | SKILL §Motion; ref/MOTION_LIBRARY M01 |
| L §2 | Impact: char by char L→R, slide 28 px / 380 ms, blur 10→0 / 300 ms, opacity 240 ms, stagger = spoken length ÷ glyphs clamped 12–48 ms | SKILL §Motion; ref/MOTION_LIBRARY M02 |
| L §2 | Keep the blur on impact text | SKILL §Motion (M02 blur values) |
| L §2 | Reveal finishes ≥ 350 ms before caption cut; else push scene change later | SKILL §Motion |
| L §2 | Drive every word from the word-level transcript; never invent timings | SKILL §Motion heading |
| L §3 | A-roll impact words always serif (Playfair Display Bold Italic), lowercase, incl. *not* | SKILL §Captions |
| L-old §3 | Series intro: upright compared, Bold Italic shipped; default Bold Italic, upright only as alternative | SKILL §Captions; ref/DESIGN_SYSTEM §4 `[R1.2]` |
| L §3 | Bold sans impact only inside full-screen graphic scenes | SKILL §Captions |
| L §3 | Lone impact phrase: trailing word above-right, small | SKILL §Captions |
| L §3 | Support ≈ 36 % of hero (48 px with 132 px hero) | SKILL §Captions, §Look (132 proven) |
| L §3 | Line-above baseline `hero_y − 0.80 × hero_size − 8`, inset ~7 % from hero left | SKILL §Captions |
| L §3 | Line-below inset ~7 % from hero right, ~58 px under baseline, 74 px with descender (g, j, p, q, y, comma) | SKILL §Captions |
| L §3 | Split-screen: seam band y ≈ 680–1240, gradient scrim transparent→70 % black→transparent | SKILL §Captions |
| L §3 | Hero width ≤ 740 px; shrink long support lines | SKILL §Captions |
| L §4 | Safe zone x 120–960, y 250–1600, icon column x > 845 for y > 1130 | SKILL §Safe zone |
| L §4 | Applies to every text/shape/dot after push-in (105 % scale pushes edges out) | SKILL §Safe zone; ref/TESSERACT_BUILD gotchas |
| L §4 | Reuse `check_safe()` audit | SKILL §Safe zone, §Build; ref/TESSERACT_BUILD |
| L §4 | Overlay check sheet (~14 frames) before calling a draft done | SKILL §Safe zone |
| L §4 | Watch block stacks, graph end-points, labels at x = 120, hanging quote marks | SKILL §Safe zone |
| L §5 | Quote marks bracket text: open top-left of first line, close after last line bottom-right; block slightly above centre | SKILL §Motion; ref/DESIGN_SYSTEM §6, TS §6, ML M26 |
| L §5 | Sequential builds overlap: ~900 ms ease-in-out each, next ~520 ms later | SKILL §Motion (M28) |
| L §5 | Highlight box scaleX 0→100 ~480 ms ease-in-out, ~120 ms before the word; text word by word | SKILL §Motion (M25) |
| L §5 | A-roll slow push +1.2 %/s linear, every shot; punch-ins stack | SKILL §Motion (M06) |
| L §5 | Grain 0.8 light / 1.0 dark, size 1.6, plus vignette (0.18/0.35 from DS §5) | SKILL §Look; ref/TESSERACT_BUILD |
| L §5 | Short A-roll beats ≥ 0.5 s readable impact text; no micro-shots < 0.5 s | SKILL §Motion; ref/DESIGN_SYSTEM §9.8, QC |
| L §6 | Lots of sound, each quiet; every text entry gets a cue; denser = quieter | SKILL §Sound |
| L §6 | Trigger map + peak levels (Hi-Tech Click −17 trim 450 ms; flick −27…−29 ±2 dB, skip within 110 ms; Highlighter −19…−21 / box −18; Riser + Tick −19; Swoosh −16; Woosh −17; Pop different −19; Modern technology pop −21/−22; Mouse click different −22; multi flicker −23; downlifter 1.4 s −20); voice peaks ≈ −4 dBFS | SKILL §Sound; ref/SOUND_DESIGN |
| L §6 | First 5 s +3 dB, back by 6 s | SKILL §Sound |
| L §6 | Levels as target peaks in mix, not flat gains (library ≈ 0 dBFS, procedural −12) | SKILL §Sound |
| L §6 | Align sound peak, not file start; convert MP3 → WAV | SKILL §Sound |
| L-old §6 | Measure each library file's peak inside the trimmed window in the mix (Hi-Tech Click −9.6 carried over was ~8 dB off; played ≈ −23 vs −15); calibrate from effects-only render | SKILL §Sound; ref/SOUND_DESIGN Rules; ref/TESSERACT_BUILD |
| L §6 | Voice chain 75 Hz HPF → 2.5:1 at −24 dBFS → makeup → limiter −1.5 dBFS; no NR when floor ≈ −59 dB | SKILL §Sound (SD's "below about −55 dB" threshold used) |
| L §6 | Measure final mix not stem (+3 dB from trims); −15 LUFS, TP ≤ −1 dBTP | SKILL §Sound, §QC |
| L §6 | Effects-only render ±60 ms; cross-correlate lip sync (±5 ms achieved; target ≤ 10 ms from SD); drop cues past end | SKILL §Sound |
| L §6 | Always deliver `sound_cue_sheet.md` (time · sound · level · reason) | SKILL §Workflow 6, §Sound |
| L §6 | Claude can't listen: say levels are measured; Rishi checks on phone | SKILL §Sound |
| L §7.1 | mlx-whisper turbo + word timestamps; snap to silencedetect −35 dB/120 ms; JSON + SRT + table; flag < 0.7 | SKILL §Workflow 1; ref/TESSERACT_BUILD |
| L §7.2 | Plan then stop; recommend one option per beat | SKILL §Workflow 2 |
| L §7.3 | One regenerable `build.py`; clean base `.tsrct`; archive drafts in `Versions/`; revision table in `NOTES.md` | SKILL §Build, §Workflow 5; ref/TESSERACT_BUILD |
| L §7.4 | Silences > 200 ms → ~120 ms (60 ms padding); hide jumps; skip mid-A-roll jumps | SKILL §Workflow 1 |
| L §7.5 | Portrait filmstrips 270×480, black-frame detection, safe-zone overlay, sound checks | SKILL §QC; ref/TESSERACT_BUILD |
| L §7.6 | Gates plan → visuals → sound → QC | SKILL §Workflow |
| L §8 (all 14 rows) | Tesseract CLI 0.4.0 gotchas (prepend children, child-local layerTime, source-clock video keys, text wrap > ~900 px, paired position keys, one key per time, negative durations, glow field names, alpha in previews, audio layers via JSON + commit, font import, cornerRadius fraction, child activeRange fit, scale OK) | ref/TESSERACT_BUILD (verbatim) |
| L §9.1 | Default word-by-word/char-by-char from draft 1 | SKILL §Workflow 4 ("every rule below from draft 1"), §Motion |
| L §9.2 | Serif heroes default | SKILL §Captions |
| L §9.3 | Support 48 px tight | SKILL §Captions |
| L §9.4 | Safe-zone audit from draft 1 | SKILL §Workflow 4, §Safe zone |
| L §9.5 | Quote marks bracket | SKILL §Motion |
| L §9.6 | Overlap builds | SKILL §Motion |
| L §9.7 | Highlight grow visible | SKILL §Motion |
| L §9.8 | Dense quiet sound, `sfx/` first | SKILL §Sound |
| L §9.9 | Flag uncertain transcript words | SKILL §Workflow 1 |
| L §9.10 | Measure program not stem | SKILL §Sound |
| L-old §10 | Caption set + dense-quiet cue map = approved package for intros | SKILL (rules unchanged; intros use the same §Captions/§Sound) |
| L-old §10 | Graphics behind subject; card stack behind on close/standing framings, never over face | SKILL §Motion; ref/DESIGN_SYSTEM §6 |
| L-old §10 | personMatte empty → local MediaPipe selfie_multiclass matte, mirror A-roll keys, `lumaInverted` track matte; matte layer doesn't render | ref/TESSERACT_BUILD (pointer in SKILL §Motion) |
| L-old §10 | Intros: no pause trims; ~0.4 s lead | SKILL §Workflow 1; ref/PRODUCTION_WORKFLOW Stage 1 |
| L-old §10 | His overlay geometry wins for graphics he places (cards top 170 px, grid x 38); captions still obey | SKILL §Safe zone; ref/DESIGN_SYSTEM §6 (numbers) |
| L-old §10 | Shirt print: move caption block below it (standing hero y ≈ 1480–1510) | SKILL §Captions; ref/DESIGN_SYSTEM §6 |
| L-old §10 | One script per series with per-version table | SKILL §Build; ref/TESSERACT_BUILD |

## Old SKILL.md v1.1 (S1.1)

| Rule | Now lives |
|---|---|
| Design System artifact pointer + read order (`project/README.md`, `tokens.json`, sections, `components/bundle.css`) | SKILL header (sections list trimmed to the files; artifact unchanged) |
| Fixed vs variable elements | SKILL header |
| Build target Motion or Tesseract | SKILL §Build |
| Captions English + Hinglish (Roman only) + Hinglish hero rules | SKILL §Captions |
| Gate 0 ask up front | SKILL §Workflow 0 |
| Gate 1 analyse; 30 ms padding | SKILL §Workflow 1 — **superseded** by L §7.4 (60 ms padding, > 200 ms → ~120 ms) as the proven Tesseract default; 30 ms kept as tutorial value in ref/PRODUCTION_WORKFLOW |
| Gate 1 flag stray micro-words | SKILL §Workflow 1 |
| Gate 2 plan fields + recommend + STOP | SKILL §Workflow 2 |
| Gate 3 assets + licence; never substitute | SKILL §Workflow 3 |
| Gate 4 one function per scene type; texture in camera group; captions first; say draft | SKILL §Workflow 4 |
| Gate 5 revision table, one pass, ask question | SKILL §Workflow 5 |
| Gate 6 sound after visual approval | SKILL §Workflow 5–6 |
| Gate 7 QC; export 1080×1920 30 fps | SKILL §QC |
| Scene selection map; "if you can't say why → A-roll"; 1.5–3 s shots; first visual ~2 s; alternate grounds | SKILL §Scene selection |
| Captions v1.1 block | SKILL §Captions, §Motion, §Safe zone |
| Evolving the system | ref/PRODUCTION_WORKFLOW "Evolving the system" (pointer in SKILL §Learning loop) |

## Other docs' hard rules

| Source | Rule | Now lives |
|---|---|---|
| DS §1 | Philosophy (calm authority, A-roll is a scene type, literal visuals, texture premium, one kit) | SKILL intro; ref/DESIGN_SYSTEM |
| DS §2 | 9:16, 1080×1920, 30 fps | SKILL §Look |
| DS §2 | Side margin 6–8 % | **superseded** by safe zone (x ≥ 120); marked in ref/DESIGN_SYSTEM §2 |
| DS §3 | Colour tokens (#0B52F9, #1A83FB/#216FEB, legacy #0D6BD9 not mixed, paper, ink #0D0D0D, graph, text colours, grid, highlight box) | SKILL §Look (main tokens); full table ref/DESIGN_SYSTEM §3 |
| DS §3 | One accent per video; A-roll natural grade, bottom darkened | SKILL header, §Look |
| DS §4 | Inter + Playfair; hero 90–130 px, −2 to −4 % tracking; support 48 px; quote line 40–60 px | SKILL §Look/§Captions; quote-line size in ref/DESIGN_SYSTEM §4 |
| DS §4.1–4.4 | ≤ 5 words; hero centred; support asymmetric hugging a corner | SKILL §Captions |
| DS §4.5 | Serif for emotion / sans for concrete | **superseded on A-roll** by L §3 (always serif); kept for graphic scenes; marked in DS and ref/TEN_SCENE §1 |
| DS §5 | Texture library; textures move with layer; grain/vignette engine values | SKILL §Look; table ref/DESIGN_SYSTEM §5 |
| DS §6 | One focal point, ≥ 50 % negative space; center/side layout proportions | ref/DESIGN_SYSTEM §6 (scene internals trigger) |
| DS §6 | Hero y 55–70 % | SKILL §Captions |
| DS §6 | Quote marks "close top-right of block" | **superseded** by L §5 (bottom-right after last line); fixed in ref/DESIGN_SYSTEM §6 |
| DS §7–8 | Scene categories, component library | ref/DESIGN_SYSTEM; SKILL §Scene selection |
| DS §9.1–9.9 | Announce→face; one idea→one scene; shot 1.5–3 s; sync to word; text on every graphic; hard cuts vs whips; illustrations ≥ 2 s; remove micro-clips < 0.3 s + stray words; captions throughout | SKILL §Scene selection, §Motion, §Captions, §QC |
| DS §10 | Consistency checklist | SKILL §Look/§Captions/§Motion; ref/QUALITY_CONTROL |
| DS §11 | Core/optional/experimental lists | ref/DESIGN_SYSTEM §11 (core items all in SKILL) |
| ML | Default easings; nothing linear except path speed | SKILL §Motion (+ M06 exception, marked in ML) |
| ML M01, M02, M06, M25, M28 | v1.1 values | SKILL §Motion |
| ML M03 | Ghost-to-white second hero | **superseded as default** by M02 (all heroes); marked in ML |
| ML M05 | Zoom cut 115–140 % | SKILL §Motion |
| ML M18 | Graph hold ≥ 15 f | SKILL §Motion (≥ 0.5 s) |
| ML M04, M07–M24, M26, M27 + sequencing pattern + Remotion notes | ref/MOTION_LIBRARY (trigger: other motion IDs / Motion build) |
| TS §0–10 | Scene-type internals (B-roll push 102→108 %, line widths, painting focus-pull, zigzag, orbit text, photo drop, graph style, text-centric ≤ ~12 words…) | ref/TEN_SCENE_PRINCIPLES (trigger: designing a scene type) |
| TS §6 | Text-centric "word-by-word fade/blur-in" | **superseded** by M01/M02; marked in TS §6 |
| TS §10 | Graph inside x 160–840 | SKILL §Safe zone |
| EP §1, §3 | Announce→face / explain→show; per-beat framework; category table | SKILL §Scene selection; full table ref/EDITING_PSYCHOLOGY |
| EP §4 | 40–55 % A-roll; ≤ 4 s A-roll without framing change; alternate grounds; reuse visual for continuing subject; ≥ 2 s complex illustrations | SKILL §Scene selection, §Motion (reuse-visual detail in EP) |
| EP §5 | Anti-patterns incl. graphics > ~8 s | SKILL §Scene selection; ref/EDITING_PSYCHOLOGY |
| PW Stage 0–8 | Stages and gates | SKILL §Workflow |
| PW Stage 1.4 | Keep intentional pauses; remove false starts/orphans | SKILL §Workflow 1 |
| PW Stage 2 | Plan template fields ("Seen in the reels", camera, status) | SKILL §Workflow 2 (core fields); full template ref/PRODUCTION_WORKFLOW |
| PW Stage 5 | First draft 60–70 % there | ref/PRODUCTION_WORKFLOW (SKILL says "call it a draft") |
| PW Stage 8 | H.264, 1080×1920, 30 fps, AAC 48 kHz, −15 LUFS (−16 to −14), TP ≤ −1 dBTP on MP4; watch on phone | SKILL §QC, §Sound |
| PW training | Style-training meta-workflow | ref/PRODUCTION_WORKFLOW |
| SD | Source order (library → procedural → supplied music) | SKILL §Sound |
| SD | Music 18–24 dB under voice, ducked 3–6 dB | SKILL §Sound |
| SD | flick peak ~40 ms after rise; Hi-Tech Click peak on first glyph; compression 15/180 ms | SKILL §Sound (first glyph, 15/180); 40 ms in ref/SOUND_DESIGN |
| SD | Cut back to face: usually no cue; unused library list | ref/SOUND_DESIGN |
| SD | Verification 1–5 (effects-only, lip sync ≤ 10 ms, LUFS/TP/LRA on MP4, cue sheet, phone) | SKILL §Sound, §QC |
| QC | All checklist items | SKILL §QC (summary) + ref/QUALITY_CONTROL (full, opened at step 7) |
| CHANGELOG | Version history | history/CHANGELOG (+ 1.2 entry) |
| VRL | Chapter/stills/beat map | ref/VISUAL_REFERENCE_LIBRARY (paths → `../references/`) |

| 2026-11-11 | Decided: graphics behind the subject by default (matches reference/DESIGN_SYSTEM and the series-intro verdict); music note points to Consulting R1.16 if 18–24 dB is inaudible. |
