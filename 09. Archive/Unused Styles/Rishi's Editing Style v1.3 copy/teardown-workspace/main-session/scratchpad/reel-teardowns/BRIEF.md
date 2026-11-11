# Brief: frame-by-frame reverse-engineering of ONE reference reel

You are a senior motion designer + editor doing a forensic teardown of one Instagram reel (720x1280, 30 fps, ~50-70 s).
Rishi wants to build his own editing style from 15 such reels (same creator family: talking head in a dark blue studio
+ "Apple-style" UI motion graphics: glass/holographic panels, 3D floating cards, orbit animations, script-serif + sans
kinetic captions, light cream/ice-blue graphic scenes, search bars, sliders, numbered badges...). His bar: "10x better
than a normal reverse-engineering". A previous attempt (vibes-level descriptions) was judged not good enough. So:
**measure, don't describe.** Every animation needs frames, durations, properties, from→to values, easing, and a reason.

## Your inputs (all in `$REF/<VID>/`, where REF=/Users/rishi/Documents/Teaching Claude/DIff Acc/Rishi's Editing Style copy/teardown-workspace/main-session/scratchpad/reel-teardowns)
- `src.mp4` — the reel (symlink). Read-only. Never copy it elsewhere.
- `strips/strip_XXX.XXs.jpg` — EVERY native frame, 60 frames (2 s) per image, each tile labelled `#frame time`. **Look at every strip, in order. This is the frame-by-frame pass; do not skip strips.**
- `sheets/sheet_NN.jpg` — 2 fps overview (start here for orientation).
- `events.md` — auto index of hard cuts and motion bursts from a per-frame difference signal (`motion.csv`: diff, luma, diff_top/mid/bot thirds, cut_chi). Use it to find every animation; verify visually.
- `words.json` / `words.srt` (word-level whisper, may contain ASR errors), `sent.txt` (sentences).
- `audio.json` — full-mix onset analysis (strong onsets = likely SFX hits: time, duration, attack, spectral centroid, peak) and cut↔onset alignment.

## Tools (python = "/Users/rishi/Documents/Teaching Claude/DIff Acc/tools/venv-style/bin/python" -I ; scripts in $BIN = <scratchpad>/bin)
- Full-res frame: `$BIN/frame.sh src.mp4 <frame#> out.png [w:h:x:y crop]` — use to read small text, fonts, colours, glows, edges. Save to `$REF/<VID>/work/`.
- Element tracker: `python $BIN/track.py src.mp4 f0 f1 x0 y0 x1 y1 --ref <cleanFrame#|bgcolor:R,G,B> [--thr 25]` → per-frame bbox centre/size/area/luma/sharpness of the pixels that differ from the reference inside the region. Use it to get REAL keyframe curves (position, scale, opacity proxy via area/luma, blur via sharpness). Pick regions that isolate one element; on talking-head footage use a nearby clean frame of the same shot as ref.
- Easing fit: `python $BIN/ease_fit.py track.csv <col> --f0 N --f1 N` → duration, overshoot %, best free cubic-bezier, ranked named easings with RMSE.
- PIL/numpy in that python for colour sampling (report hex), measuring glow radius, blur, gradient stops, letter heights.
- ffmpeg/ffprobe available. Do not install anything. Do not write outside `$REF/<VID>/`.
Measure at least the 8-12 most important/representative animations with track.py + ease_fit.py; for the rest estimate from strips (count frames) and tag [EST].

## Evidence tags (mandatory on every claim)
[MEAS] measured with a tool (give the numbers) · [OBS] seen directly in frames (give frame #) · [EST] estimated by counting frames / eyeballing · [INF] your interpretation. Never present an estimate as a measurement. Coordinates: give % of frame (x% of width, y% of height) AND px in 1080x1920 (= source px × 1.5).

## Write `$REF/<VID>/BREAKDOWN.md` with exactly these sections
1. **Overview** — topic/hook (1 line), duration, structure (hook → body → CTA with times), share of runtime per scene type, avg shot length, # of distinct animations, overall look in 3 lines.
2. **Beat-by-beat timeline** — table, one row per beat/visual change, covering the whole video with no gaps:
   `frames (start–end) | time | spoken words | screen: layers back→front (bg, footage framing, cutout?, graphics, text) | animations (IDs from §3) | camera (zoom %, position) | sound onset? | WHY (job + mechanism: what the viewer must feel/know; curiosity gap, pattern break, emphasis, proof, etc.)`
3. **Animation catalogue** — one entry per distinct animation (ID `<VID>-A01`, …). For each:
   element · trigger (which spoken word, offset in frames from word onset) · start/end frame · duration (frames + ms) ·
   properties animated (position x/y, scale, rotation 2D/3D rotateX/Y, perspective, opacity, blur, mask/wipe direction,
   colour, glow, letter/word stagger) with from → to values · easing (named + cubic-bezier, measured or EST) · overshoot/spring? ·
   motion blur present? · how it exits (and exit timing) · what it's simultaneous with · reusable name (e.g. "glass panel rise",
   "card morph to search bar", "orbit ring", "word darken") · re-buildability notes (how you'd rebuild it in HTML/CSS/Remotion).
   Include micro-animations: caption word entrances, cursor/typing, number count-ups, glows pulsing, background drift, parallax.
4. **Text & typography system** — every text style used: font family guess (+ confidence; candidates e.g. SF Pro / Inter / Playfair /
   script like "Edwardian Script"/"Great Vibes"/"Pinyon Script"), weight, size (cap height as % of frame H), colour hex, tracking,
   case, alignment, position. The RULE for which word becomes script/serif/italic/coloured vs plain sans; words per caption
   group; how lines stack/overlap (e.g. small sans word nested inside big script word); entrance/exit per style; where captions
   sit relative to the face; when captions are absent.
5. **Colour, light & material** — background hexes (A-roll grade, cream/ice graphic grounds, solid colour cards), accents, gradients,
   glows (colour, radius px, opacity), shadows, glass/holographic panel recipe (fill, border, inner glow, blur behind), grain/vignette,
   colour grade of the footage.
6. **Depth & 3D** — perspective cards (angles, vanishing point), card fields/parallax layers, depth of field / blur on far layers,
   orbit animations (radius, speed deg/s, direction, tilt, how cards keep facing camera), graphics BEHIND the subject (person
   cutout/matte?) or in front, face-in-circle / face-in-card treatments, rounded corners (radius as % of card width), borders.
7. **Camera & transitions** — every transition type with frames (hard cut, morph, zoom-through, whip, wipe, card fly-in, iris,
   blur dissolve, flash), zooms/punch-ins/push-ins on footage (scale %, duration, easing), framing changes, shake.
8. **Assets used** — UI recreations (search bar, IG profile, slider, progress steps, app windows), screenshots, thumbnails, icons,
   3D objects, stock — and what was likely built vs captured.
9. **Sound ↔ picture** — map audio.json onsets to visual events (Δ ms). Music presence estimate. Which events get SFX.
10. **Editing psychology** — why each scene type was chosen for its line; the selection rule you infer
    (condition → action → reason); pacing curve (hook energy vs body vs CTA); patterns of rhythm (e.g. A-roll ↔ graphic alternation).
11. **Signature moves** — the 5-10 things that most define this reel's style, ranked, each with the exact recipe.
12. **Gaps / uncertain** — what you could not determine and why.

Also write `$REF/<VID>/animations.json`: array of {id, name, category, element, start_f, end_f, dur_ms, props:{prop:[from,to]}, easing, bezier, overshoot_pct, trigger_word, evidence}.

Return to me (final message, ≤ 400 words): the 10 most important findings + the list of distinct reusable animation names you found. The files are the real deliverable; be exhaustive there (expect BREAKDOWN.md to be long: 600-1500 lines is fine).
Do not quote long transcript passages back; do not reproduce the creator's assets anywhere outside your work folder.

## Token budget (Rishi asked for optimal, not extreme, token use)
- Read each strip image ONCE, in order. Strips whose 2 s span has no event in events.md and no visible change may be glanced once and noted as "static A-roll" — that still counts as covered.
- Pull full-res frames (frame.sh) only when a strip tile is too small to read the detail you need; crop to the region.
- Measure 8-12 animations with track.py/ease_fit.py; print only the columns you need (cut -d, -f...). Never cat whole CSVs or motion.csv.
- Don't re-read files you already wrote. Write BREAKDOWN.md section by section with concise tables, not prose.
- If your folder already has a work/ dir with files from an earlier interrupted run, reuse them instead of redoing.
