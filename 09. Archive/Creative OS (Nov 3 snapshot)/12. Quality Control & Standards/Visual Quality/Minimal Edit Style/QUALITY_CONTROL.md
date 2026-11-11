# Quality Control — v1.1

Tick every box before delivery.

## Planning
- [ ] Every beat has a function label and a reason for its scene choice
- [ ] Announcements on A-roll; explanations visualised
- [ ] Human approved the plan before build

## Typography
- [ ] Only Inter + Playfair Display (or approved alternates)
- [ ] ≤ 5 words per caption group; one hero per group (pairs deliberate)
- [ ] Hero on the meaning word; **A-roll heroes in serif italic** (bold sans only inside graphic scenes) — v1.1
- [ ] Support text tucked asymmetrically; nothing centred by default except hero
- [ ] Support text 48 px (≈ 36 % of hero), tight to the hero: above inset from the left, below inset from the right — v1.1
- [ ] **Everything** (text, shapes, dots, graph ends) inside the Instagram Reels safe zone: x 120–960, y 250–1600, icon column (x > 845, y > 1130) clear, checked after scene push-ins. Safe-zone audit passes and the overlay sheet has been reviewed — v1.1
- [ ] No typos; captions match audio word-for-word

## Colour & texture
- [ ] One accent blue (#0B52F9 family) throughout
- [ ] Every graphic has paper/paint/cloth/noise texture; no flat vectors
- [ ] Textures move with their layer; paint texture not overpowering
- [ ] B-roll has paper texture + darkened + blurred edges
- [ ] A-roll bottom darkened enough for white captions

## Composition
- [ ] One focal point per frame; ample negative space
- [ ] Center illustrations bleed from bottom; side layouts balanced
- [ ] Text never covers faces/focal subject
- [ ] Quote marks on text-centric scenes, **bracketing** the text block (open top-left of first line, close after last line) — v1.1

## Motion
- [ ] No linear easing (except path speed and the constant A-roll push)
- [ ] Support text reveals word by word on spoken times (M01); impact text character by character, left to right with blur (M02) — v1.1
- [ ] Every hero fully revealed ≥ 350 ms before its caption cuts — v1.1
- [ ] Multi-part builds overlap with no dead time (M28); highlight boxes grow visibly from zero (M25) — v1.1
- [ ] Constant subtle push-in on every A-roll shot (M06) — v1.1
- [ ] Every visual element lands on its trigger word
- [ ] Camera follows lines/balls; never loses the line head
- [ ] Graphs/illustrations held ≥ 0.5 s after complete; complex visuals ≥ 2 s
- [ ] Hard cuts to/from A-roll; whips only between graphics
- [ ] No micro-clips < 0.3 s; no stray words

## Pacing
- [ ] First visual by ~2 s
- [ ] Average shot 1.5–3 s; no static stretch > 4 s on A-roll without a framing change
- [ ] Alternating background tones between consecutive graphics

## Audio
- [ ] Silences cut with padding; breaths/attacks not clipped
- [ ] Voice clear above music at all times; final program −15 LUFS (−16 to −14), true peak ≤ −1 dBTP, measured on the exported MP4 — v1.1
- [ ] A sound on every text entry: Hi-Tech Click on impact words, quiet flicks on support words, Highlighter on every line extension. Library (`SFX/`) checked first — v1.1
- [ ] Denser layers quieter (see SOUND_DESIGN v1.1 levels); first 5 s lifted +3 dB; no stacked cues within ~110 ms; no clipping
- [ ] Effects-only render confirms every cue within ±60 ms of the cue sheet; voice cross-correlated for lip sync (≤ 10 ms) — v1.1
- [ ] `sound_cue_sheet.md` delivered

## Assets & export
- [ ] Every asset in the asset list has a source + licence/permission
- [ ] 1080×1920, 30 fps, H.264, AAC 48 kHz
- [ ] Watched once full-screen on a phone with sound on and once muted
