# First principles · build notes

**Current revision:** v2 with sound: `FirstPrinciples_v2_sound.mp4`. Visuals are from draft 3. See the revision log and the sound section below.
- Editable project: `FirstPrinciples.tsrct`. Footage, Inter and Playfair Display are embedded.
- Render: `FirstPrinciples_draft1.mp4` (1080×1920, 30 fps, H.264/AAC, 32.73 s).
- Rebuild from scratch: `.tesseract-work/build.py` regenerates the whole timeline (footage JSON plus the native graphics batch) from `v0_empty.tsrct`.

## What's in draft 1
- 9 pause trims (1.48 s removed). Every trim is hidden either under a graphic or at a zoom cut (108 % on "a lot of people", 110 % on "faltering").
- 10 split-screen caption groups on the seam band, over a dark gradient.
- 4 native scenes:
  - Blue quote: "I don't know *anything*".
  - White: foundation blocks → climb line → **solution**.
  - Black: three stages, industry → *homework* → **ANSWER**.
  - Dark graph: the confidence line drops, with a LACK OF CONFIDENCE highlight and client / interview markers.
- Paper grain and vignette on every graphic scene. A 5-frame fade to black at the end.

## Deviations from the approved plan
- Ending: the source has only 170 ms after "answer", so there's no extra 400 ms tail. It ends with a short fade instead.
- Beat 8 hold extended to 26.68 s (source) so **ANSWER** stays up for at least 0.5 s. That shortens the "You will start faltering" A-roll to 0.62 s.
- The textures are a fine engine grain, not the rough/painted paper scans from the reference reels. Real paper texture images could be layered in if you supply them.

## Checks done
- Rendered filmstrips at 1 s intervals and at key frames. Ran black-frame detection on the export (none found).
- Confirmed the export is 1080×1920 at 30 fps.
- Measured loudness: −26.1 LUFS integrated, not yet normalised. That's for the sound pass.
- Not done: I haven't listened to the trim joins. They all sit inside −35 dB silences with 60 ms padding, but check by ear.

## Revision log
Draft 2 (2026-11-02). Current: `FirstPrinciples_draft2.mp4`. Draft 1 is archived in `Versions/`.

| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 1 | all | Support text appears all at once | Word by word | One layer per word, each on its spoken time. It rises 22 px while its opacity eases up | done |
| 2 | all | Impact text appears all at once | Character by character, left to right | One layer per glyph. Each slides in 28 px from the left, unblurs 10→0 and fades up, staggered across the word's spoken length. Blur kept | done |
| 3 | 0:00 and every caption | Support text small and floating | Bigger and tucked closer to the impact word | Support 36→48 px, sitting just above the ascenders. The line above is inset from the impact word's left edge, the line below from its right | done |
| 4 | 0:02 | Sans "FIRST PRINCIPLE" with "thinking" below | Serif impact word, "thinking" on top | *first principle* in serif, "thinking," above it on the right | done |
| 5 | 0:04 | Quote marks separate from the text | Quote marks bracket the text, block sits higher | Block moved up (baselines 790/960/1050). “ hugs the first line, ” closes after "about this." | done |
| 6 | 0:05–0:07 | Blocks pause between pops | One continuous, smooth build | Blocks rise 90 px with ease-in-out over 0.9 s, starting every 0.52 s so the moves overlap | done |
| 7 | 0:12 | "come to a" far from "solution" | Same tight layout as the captions | 48 px, tucked over "solution" | done |
| 8 | 0:15 | Sans "NOT" | Serif | *not comfortable* as one serif impact phrase | done |
| 9 | 0:27 | Highlight box seems to start halfway | Box grows from nothing; text word by word | Box scaleX 0→100 over 480 ms ease-in-out, from 120 ms before "lack". LACK / OF / CONFIDENCE each arrive on their spoken word | done |
| 10 | A-roll | Static frame | Very subtle constant zoom-in | +1.2 %/s linear push on every A-roll segment | done |
| 11 | 0:26 | *faltering* only half revealed before the cut | Fully readable | Graph scene starts 260 ms later (source 27.56 s) | done (self-found) |
| 12 | A-roll captions | Sans impact words (INDUSTRY, SOME WORK) | Serif, per your notes | All caption impact words are serif. Graphic scenes keep bold sans for contrast | done |

Draft 3 (2026-11-02). Current: `FirstPrinciples_draft3.mp4`. Draft 2 is archived in `Versions/`.

| # | Timestamp | Problem | Expected | Fix | Status |
|---|---|---|---|---|---|
| 13 | 0:16 and all | Text reaches the frame edge; outside the Instagram Reels safe zone | Everything inside the safe zone | The build now audits every element against the safe zone: x 120–960, y 250–1600, plus the icon column (x > 845 below y 1130), allowing for scene push-ins. Caption heroes capped at 740 px, long support lines shrink to fit. Changes: quote block smaller; block stack narrowed and lifted; graph moved inside x 160–840; LACK OF CONFIDENCE box 62 px; stages moved up; two labels re-placed. Checked visually with the template overlaid (`Previews/draft3_safezone_check.png`) | done |

Safe-zone audit note: the one remaining flag is the closing quote mark at 0:04. The audit draws its box down to the baseline, but the glyph sits high, so the visible mark is well inside (see the overlay check).

## Sound pass (v1, 2026-11-02)
- **Voice:** `assets/audio/voice_clean_v1.wav`, made from the source audio. The recipe is in `assets/audio/RECIPE.md`: 75 Hz high-pass, 2.5:1 compression, +15.5 dB and a −1.5 dBFS limiter. No noise reduction was needed (pause floor −59 dB). It's placed as native Audio layers that mirror the footage cuts. The footage's own audio is disabled, so nothing plays twice.
- **Effects:** 27 procedural accents from the Tesseract sound helper: soft taps on impact words; a click when the quote marks appear; whooshes on the graphic-to-graphic cut and the highlight box; pops as the blocks settle; a riser and ping on "solution"; a low impact into the stages scene; clicks on the stage dots; and a downlifter under the confidence drop. Every effect is its own Audio layer with editable gain. The timing list is `sound_cue_sheet.md`.
- **Music:** none. No licensed track was supplied, and the helper doesn't make music. I can add a bed and duck it under the voice if you send one.
- **Mix:** whole-mix trim 0.74. The export measures −15.3 LUFS integrated, −3.9 dBTP true peak and 3.1 LU loudness range (report: `.tesseract-work/checks/loudness-v1b.json`).
- **Sync:** cross-correlated against the source file, the new voice track is within ~5 ms (correlation 0.92–0.94 at five points).
- **Not verified by ear:** I can't play audio here. Effect levels and the voice treatment are set from measurements, so check them on a phone with sound on.

## Sound pass v2 (your notes)
| # | Note | Fix | Status |
|---|---|---|---|
| S1 | Effects too quiet; opening should be livelier | Every cue now has a target peak level in the mix rather than a flat gain. Impact clicks −17 dBFS, transitions −16/−17, line draws −19/−21, word flicks −27 to −29 (voice peaks ≈ −4). Everything in the first 5 s gets +3 dB, easing back to normal by 6 s | done |
| S2 | More effects; sound whenever text appears | 65 quiet flicks, one per support word, landing as the word rises in. Skipped where they'd clash with a bigger cue | done |
| S3 | Impact text needs its own high-tech click | Hi-Tech Click from your SFX folder on all 19 impact words (captions and graphics), trimmed to 450 ms so the tail doesn't smear | done |
| S4 | Use the SFX folder; more depth, not clutter | 10 library sounds: Hi-Tech Click, flick, Highlighter, Riser + Tick, Swoosh, Woosh, Pop different, Modern technology pop, Mouse click different, multi flicker (`assets/audio/library/`). The denser the layer, the quieter it is | done |
| S5 | 0:22 blue line needs sound as it extends | Highlighter on each of the three spine extensions. Also used on the climb line, the graph line and the highlight box. The climb ends on the Riser + Tick's tick | done |

- **Totals:** 103 cues (was 27). Mix: −15.2 LUFS integrated, −3.5 dBTP true peak.
- **Placement check:** an effects-only render confirmed every cue sounds within ±60 ms of its cue-sheet time. One tick past the end of the video was removed.
- **Not verified by ear:** I can't play audio here, so levels are still set from measurements.
