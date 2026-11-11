# QUALITY CONTROL: Rishi's Editing Style (v1.1, exact reference copy `[R1.1]`)

Tick every box before export. Anything Rishi has corrected (`LESSONS_LEARNED.md`) overrides a line here. Items marked *pilot* use values that are still proposed or [EST].

## Identity
- [ ] Fonts are Inter (stand-in for the reference grotesque) + Playfair Display Italic (stand-in for the reference italic serif) only `[R1.1]`
- [ ] Colours come from the reference tokens in `DESIGN_SYSTEM.md` §3 only (blue ground `#4279BB→#205AA4`, cream `#EBE7E1`, white cards, white/grey captions, navy text, badge blue `≈#2F80FF`, Claude orange `≈#D97757`, scarcity red `≈#E83A3A`, money green `≈#2FD26B`). No rishi.docx token anywhere (`#f4f1ea`, `#141414`, `#e2432a`, General Sans) *pilot: confirm [EST] hexes*
- [ ] Red appears only as a hand-drawn scarcity/negation mark; green only on money/price/positive results
- [ ] No glows, glass, gradients, holograms, orbit, font-cycle, particles in the default build (Family A is experimental, off unless Rishi asks)
- [ ] One ground per scene; blue ground has soft vertical light streaks + faint grid; cream has faint grid + soft vignette
- [ ] No third-party faces, logos, thumbnails or UI captures from the reference reels; UIs are recreations; every screenshot/number has a stated source

## Structure
- [ ] The reel opens on the face or on proof at frame 0 (no intro card/logo)
- [ ] Hook is a counted promise, number-first, person + result, or a provocative question
- [ ] Every claim has an artifact on or before the word (−10…+10 f; numbers/prices may lead by 0.7-2.4 s); nothing lands after the word
- [ ] The face returns at least every two graphic scenes (no three graphic scenes in a row)
- [ ] Each numbered chapter opens with the chapter marker (diamond / tracker / italic ordinal); each chapter has a different visual vocabulary
- [ ] At most 2 type beats (drum-roll / giant word / deadline line) in the reel
- [ ] A quantity claim is a wall or a counter; a rule is performed on screen (change on screen equals the spoken number)
- [ ] The CTA is the form chosen in the plan; the reel ends on the face or the action UI, calm

## Pacing
- [ ] 10-14 visual changes in the first 10 s; 7-9 per 10 s in the body; 4-6 in the last stretch (count from the plan table)
- [ ] Hard cut every ≈ 4-8 s (reference median 6.7 s); a visual state change every ≈ 1.6-2.3 s
- [ ] Nothing static for more than ~3 s (a hold gets a build, count or push 1.0 → 1.04)
- [ ] No pause > 0.3 s on the A-roll (silence trimmed, margin 0.15 s)
- [ ] Scene mix roughly A-roll ≈ 45%, full graphic ≈ 45%, split ≈ 10% (adjust per script)

## Layout & motion
- [ ] 1080×1920, 30 fps; text inside y 250-1500 and left of x 920 (IG safe zone)
- [ ] Captions follow the reference build: Inter mixed sizes (connectors ≈ 32px, key words Bold ≈ 46-48px), one Playfair Italic word (≈ 56-58px) per group; words grey `≈#8E8E8E` until spoken, then white; lines stack on A-roll (≤ 3), single line at the top of blue panes; mirror speech; Hinglish in Roman script only
- [ ] No captions on full Claude-UI scenes or while the Comments sheet is up (reference behaviour)
- [ ] A-roll graded toward the reference: dark, cool, low-key, darker lower third; skin checked against the source
- [ ] A-roll captions sit around y ≈ 1150-1230 and never cover the face; on graphic scenes captions move to the top band (y ≈ 260-420) or disappear when the UI text is the content
- [ ] Card entrances use the ease-out grammar (≤ 3% overshoot) in two tiers (secondary 0.35-0.45 s, hero 1.0-1.5 s); springs only on small objects (peak ≤ 1.25×)
- [ ] Split pane: drop 1.0 s `PANE_IN`, expand 0.85 s `PANE_EXP`, lift 0.97 s `PANE_OUT`; seam at y ≈ 922; face kept in the lower pane
- [ ] Exits are faster than entrances (6-10 f) or the scene is replaced by a cut/pane
- [ ] No motion blur, shake, whip pans or flashes
- [ ] Only one overlay on the A-roll at a time

## Sound (after visual approval only)
- [ ] Sound built only after Rishi approved the visuals
- [ ] ≈ 0.4 cues/s on average; cuts mostly dry; soft cues on pane/card moves, counters, keyword typing (see `SOUND_DESIGN.md`)
- [ ] Speech stays clearly above the music bed; integrated loudness −14 LUFS
- [ ] No sound type is claimed from the references (never verified)

## Export
- [ ] `ffprobe`: 1080×1920, 30 fps, H.264 High, yuv420p, AAC 192k
- [ ] Loudness −14 LUFS integrated (check with `ffmpeg -af ebur128`), true peak ≤ −1 dBTP *proposed*
- [ ] File named `R###_topic_YYYY-MM-DD.mp4` in `exports/`
- [ ] Watched once end-to-end at full speed on a phone-size preview; captions legible; no cut-off text under the IG top bar or right icon column

## Revision loop record
- [ ] Every revision item is in the numbered table (`# | timestamp | problem | expected | fix | status`) and closed in one pass
- [ ] New rules from Rishi's feedback are in `LESSONS_LEARNED.md` as `[R1.x]` and the affected file + `CHANGELOG.md` updated
