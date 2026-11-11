# Quality control: before every delivery

## Process
- [ ] A storyboard was shared for this round (or the change was trivial and is mentioned)
- [ ] Built in a **new** draft folder; previous drafts untouched
- [ ] Every F-item addressed or explained

## Captions
- [ ] Romanised Hinglish exactly as spoken; words near cuts flagged
- [ ] Centre-aligned, ≤ ~22 chars per line, ≤5 words
- [ ] Hero letters render whole (no baseline-strip glitch); reveal finishes before the cut
- [ ] Right mode per scene (A-roll white / light-ground ink / split top / PiP line / wall one-word black / CTA one-word)
- [ ] Never over a card, never white-on-white, never blue on light scenes

## Look
- [ ] Every card enters with line → rectangle + blur + slide (no pop)
- [ ] White elements: white → grey gradient + vignette, no blue tint
- [ ] Corners subtle (tiles ≈8 px)
- [ ] Real logos, real filenames, his own clip/sticker where relevant
- [ ] Split: content clear of the pane edge, full hair line visible, no black bar
- [ ] Behind-head: no gap/oval, matte aligned
- [ ] PiP: rounded corners on the video itself, headspace cropped

## Motion and pacing
- [ ] Nothing snappy: big moves 0.8–1.45 s, entrances 0.5–0.7 s, smooth curves
- [ ] No empty white beat longer than ~1 s; exits overlap entrances
- [ ] Zooms/transitions start on the trigger word; returns happen after the line ends
- [ ] Jump cuts hidden (cut-hiding zoom)
- [ ] CTA sheet held to the final frame

## Audio
- [ ] Effects-only check: 100 % of cues within ±60 ms
- [ ] Final ≈ −15.5 LUFS (−16…−14), TP ≤ −1 dBTP
- [ ] Voice not doubled (A-roll video silent)
- [ ] Cue sheet written; SFX-only + voice-only MP3s if asked

## Export
- [ ] **1080×1920, 30 fps** (ffprobe), duration matches the rough cut
- [ ] `blackdetect` = 0
- [ ] Filmstrip of the export saved in `Previews/`
- [ ] Report lists what was checked and what wasn't (no listening)
