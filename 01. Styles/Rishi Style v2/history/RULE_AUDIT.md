# Rule audit: v2.1 → v2.2 restructure (2026-11-11)

Proof that nothing was lost when SKILL.md became the only mandatory read. Every rule, number and ID from the old docs is mapped to where it now lives.
Keys: **SK §X** = `SKILL.md` section X (Workflow steps as SK §W0–W7). **ref/X** = `reference/X.md`. **hist/X** = `history/X.md`. "superseded by …" = replaced by a later verdict (reason given). Files moved, never deleted; reference/ docs keep their full tables.

## A. Conflicts resolved (later verdict wins)
| # | Conflict | Resolution | Now in |
|---|---|---|---|
| C1 | Support line below hero: `hero + size + 14` (CAPTION §3, v2.0) vs `hero + 0.55 × support size` (CAPTION §6, Style Lab 2026-11-09) | v2.1 wins (Rishi: "hai" was "very far below"). Old value struck through in ref | SK §Captions; ref/CAPTION_SYSTEM §3 (annotated), §6 |
| C2 | Hard cut between caption groups (CAPTION §3) vs C-out soft exit (MOTION v2.1) | C-out wins (Style Lab) | SK §Captions; ref/CAPTION_SYSTEM §3 (annotated); ref/MOTION_LIBRARY C-out |
| C3 | Default accent: `accent` #3E7BFA "(default)" (DESIGN §6 table) vs D26 "default to `accent.duo` if unstated" | D26 wins (explicit verdict, same day, more specific) | SK §Look; ref/DESIGN_SYSTEM §6 (annotated) |
| C4 | R39 fan: rise 0.5 s, split ±16°, 0.8 s (Style Lab) vs vid5: tops ≈ y 180, ±255 px / ±12°, rise 0.7 s + split 1.1 s | vid5 (2026-11-10) wins | SK §Depth; ref/MOTION_LIBRARY R39 (annotated); ref/DEPTH_AND_MATTE §5 |
| C5 | R41 giant word "3× hero size" vs vid5 "baseline ≈ y 445 at 360 px, rise ≤0.7 s" | Both kept: vid5 adds placement + timing at 360 px | SK §Depth (pointer); ref/MOTION_LIBRARY R41; ref/DEPTH_AND_MATTE §5 |
| C6 | CTA DM: vid2 "DM resource card enters on the tick, middle, left → right, above caption" vs vid5 "DM reads as a message notification ('rishi sent you a file') sliding left → right on the tick" | vid5 refinement wins; position/timing from vid2 kept | SK §Scenes; ref/SCENE_LIBRARY S9 |
| C7 | Silence trims: vid2 "don't ask, just cut them" vs vid5 "a pause that carries a joke/beat is not dead air" | Merged: cut dead silence without asking; keep beat pauses and report which | SK §W0; ref/PRODUCTION_WORKFLOW Stage 0 |
| C8 | Options per frame type: "5 options each" / "≥5" (D2, REVIEW) vs D24 "re-offer every liked option even past 5" | Merged: ≥5 plus every previously liked option, Keeps first | SK §W1; ref/REVIEW_FORMATS v2.1 |
| C9 | Draft 3 F2 "logo flies into the chat header" / F26 "CTA one line of Playfair" vs draft 4 (logo + video card slide out from behind head, white disc; CTA one word at a time) | Draft 4 wins | SK §Captions (CTA mode); ref/SCENE_LIBRARY S1, ref/CAPTION_SYSTEM §4 |
| C10 | Exit duration: learnings §3.4 "0.5–0.6 s" vs R02 "0.42–0.6 s" | R02 (the measured library value) | SK §Motion; ref/MOTION_LIBRARY R02 |
| C11 | Card radius: learnings "≈14–36 px", D10 "cards 14–36", DESIGN §4 "22–36 (timeline 14)" | Consistent: 14–36 px range, per-card values in DESIGN | SK §Look; ref/DESIGN_SYSTEM §4 |
| C12 | Caption grouping: CAPTION "≤5 words" vs `roman_captions.py` "≤4 words" | Rule stays ≤5; the tool's ≤4 sits inside it (code unchanged) | SK §Captions; ref/CAPTION_SYSTEM §2 note |
| C13 | Old SKILL "Log what changes in LESSONS_LEARNED.md"; PRODUCTION Stage 6 "append to LESSONS_LEARNED" | Superseded by the learning loop: `FEEDBACK_LOG.md` → fold → `history/CHANGELOG.md` | SK §Learning loop; ref/PRODUCTION_WORKFLOW Stage 6 |
| C14 | Intake input "rough cut from Rishi" vs vid2/vid5 practice (raw video cut by Claude) | Both accepted: raw or rough cut | SK §W0 |
| C15 | build_template.py still encodes v2.0 (hard caption cut, wide support gap, plain R01–R03) | Code left unchanged (byte-identical promise); SKILL tells the builder to add v2.1 upgrades | SK §Engine; engine/README.md |

## B. DECISIONS.md (hist/DECISIONS)
| ID | Rule | Now in |
|---|---|---|
| Precedence 1–4 | Rishi's notes > [R] verdicts > pack tokens > source books | SK intro (condensed: notes > SKILL > reference/); full order in hist/DECISIONS |
| D1 | No Claude artifacts; local HTML (+PNG); builds in Tesseract | SK §Working rules |
| D2 | Options board first, ≥5 options, he mixes | SK §W1 |
| D3 | Storyboard before every build/revision; silence = approved unless "storyboard only" | SK §W2, §W4 |
| D4 | Romanised Hinglish exactly as spoken; no Devanagari font | SK §Captions |
| D5 | Playfair Bold Italic hero + Inter support, white hero, gradient, no blue hero | SK §Captions |
| D6 | Centre-aligned, ≈22 chars/line | SK §Captions |
| D7 | Smoothness above all; pops/snaps are defects | SK §Working rules, §Motion |
| D8 | Every card: line → rectangle + blur + small slide | SK §Motion (R01) |
| D9 | White cards white → light grey + vignette, never blue | SK §Look |
| D10 | Subtle corners (tiles ≈8, cards 14–36) | SK §Look |
| D11 | Real logos stored in assets/logos | SK §W0, §Look |
| D12 | Face sticker as avatar | SK §Look |
| D13 | Split: content + captions in the white pane, lifted off its edge; full hair line | SK §Look, §Captions (split mode); ref/SCENE_LIBRARY S4 |
| D14 | Organic shape, not a circle, many orbit words | SK §Look; ref/SCENE_LIBRARY S5 |
| D15 | Behind-head uses real person matte; no gap/oval | SK §Depth |
| D16 | Wall: white slop tiles, one-word black Playfair below face | SK §Captions (wall mode); ref/SCENE_LIBRARY S7 |
| D17 | PiP rounded, headspace cropped, one card stays + contents swap, return after the line | SK §Scenes, §Motion; ref/SCENE_LIBRARY S8 |
| D18 | CTA comments sheet + keyboard, blurred face, one-word captions, tap + green tick, held to last frame | SK §Scenes, §Captions; ref/SCENE_LIBRARY S9 |
| D19 | Sound dense-quiet, long smooth swooshes, SFX-only + voice-only on request | SK §Sound, §W6 |
| D20 | Each draft in a new folder | SK §W3 |
| D21 | Timebox 2–3 min; structural changes need feasibility + approval | SK §Working rules |
| D22 | Browser GUI editor parked (needs Brave FSA flag or Chrome) | ref/TESSERACT_NOTES "Browser editor"; SK §Engine (GUI → edit .tsrct in place) |
| D23 | Every export 1080p incl. check renders; never `--resolution 720p` | SK §QC |
| D24 | Re-offer every liked option, best-liked first | SK §W1 |
| D25 | v2.1 adds R26–R50 + upgrades R01/R02/R03/R05/R16 + soft caption exits | SK §Motion, §Engine; ref/MOTION_LIBRARY |
| D26 | Accent chosen per video from five tokens; default `accent.duo` | SK §Look |
| D27 | Digits in Inter (or Playfair roman), never Playfair italic | SK §Look |
| D28 | Behind-head words/orbits only with room to read | SK §Depth |
| Rejected (v3) | Paper Stage look; "nope."; blue/white-on-white captions; fade/scale pops; snappy sheet/keyboard; sudden orbit words; blank white > ~1 s; separate behind-head scene for lists when PiP is up; big tile corners; circles; face too low in split; over-correcting | SK §Scenes (rejected line), §Captions, §Motion, §Look, §Working rules ("a little" ≈30 px) |
| Rejected (Style Lab) | blurred own frame as ground; chapter marker; strike-then-replace; window zoom-through motion | SK §Look, §Scenes |

## C. learnings.md (hist/learnings)
| § | Item | Now in |
|---|---|---|
| 1.1.1 | Rough cut + SRT from Rishi; remap by spectral audio matching (raw waveform failed) | SK §W0; engine/tools/srt_remap.py docstring; ref/PRODUCTION_WORKFLOW |
| 1.1.2 | Options board: 5 options per frame type, phone-frame mock-ups, Keep/Maybe/No, notes, Copy my picks | SK §W1; ref/REVIEW_FORMATS |
| 1.1.3–5 | Storyboard before building; Tesseract; feedback F-list → storyboard → build | SK §W2–W4 |
| 1.1.6 | Sound included once visuals are close (with draft 2) | SK §W5 |
| 1.1.7 | Deliverables MP4 + .tsrct + filmstrip + cue sheet; SFX-only/voice-only MP3 on request | SK §W6 |
| 1.2 | No artifacts; visual over text + PNG; ≥5 options, build exact mix; 5-frame strips (0/0.15/0.30/0.50/0.72 s); storyboard approval rule; ask but don't stall; each draft own folder; timebox; approval gates; report honestly | SK §W1–W6, §Working rules |
| 1.3 | Voice-transcribed notes → numbered items; vocabulary (smooth, snappy, pop, premium, subtle, a little, decent); notices every glitch | SK §W4, §Working rules |
| 2 | Format 9:16 1080×1920 30 fps ≈30–35 s Hinglish, lav, marble wall, green jacket; topic; structure hook → … → CTA; CTA keyword → DM | SK intro, §QC; structure as beat map in ref/EDITING_PSYCHOLOGY §2 |
| 3.1 | Premium minimal, one idea per screen, smooth even if longer; face is the spine; real things beat stand-ins | SK §Look, §Motion |
| 3.2 | Palette (ice, ink, accent, card white→grey, muted, green, Claude orange); grain 0.6–1.0; grey-scale white gradients | SK §Look; ref/DESIGN_SYSTEM §2, §4 |
| 3.3 | Inter + Playfair Display Bold Italic | SK §Look |
| 3.4 | Card reveal line → rect; exits; word-by-word lists (26 px, 0.12–0.15 s); big moves 0.8–1.45 s; subtle life (±6°/3 s logo, drifting gradients, orbit fast→slow); corners | SK §Motion, §Look; ref/MOTION_LIBRARY R01–R03, R07, R11, R25 (stagger superseded by R03+ 0.20→0.08 s) |
| 3.5.1–9 | Approved scenes (shrink into chat, twin slide-out, B&W nose-track, split pane, doc + blob, behind-head card, wall zoom-out, PiP + swap, comments-sheet CTA) | ref/SCENE_LIBRARY S1–S9; key lessons in SK §Scenes, §Look |
| 3.6 | Rejected list | SK §Scenes (rejected), see B |
| 4 | Captions: romanised, hero 132 px ≤740, support 48 px 85 % centred, ≤22 chars ≤5 words, reveals, gradient 0→45 % bottom 40 %, no blue, context modes, blur layerSize glitch | SK §Captions, §Engine; ref/CAPTION_SYSTEM |
| 5 | Sound: Minimal SFX dense-quiet; hero −17, flick −27…−30; highlighter, pops, techpop, key clicks, risertick; full-length swooshes peak on midpoint; first 5 s +3 dB; ≈ −15.5 LUFS, TP ≤ −1 (achieved −7.2); voice −13.9 LUFS → 75 Hz HPF, −1.5 dB; effects-only ±60 ms; cue sheet; MP3s | SK §Sound, §QC; ref/SOUND_DESIGN |
| 6 | Assets/folders (logos, face sticker, matte, storyboards, edits paths) | SK §W0–W3, §Look, §Depth (matte path updated: old `Rishi's Editing Style/pilot/...` → `02. Shared Core/engine/matte/matte.py`) |
| 7 | Tesseract lessons (parent clock; rect top-left; wrap Video in Group; blur layerSize; fill opacity 0..1; cropRect → punched framing + mask; Bézier corners; lumaInverted matte mirroring JS; missing ✓↑●; one regenerable script from clean base; GUI → edit in place) | SK §Engine (key musts), §Look (glyphs), §Depth; ref/TESSERACT_NOTES (all) |
| 8.1 | Paper Stage skill to be replaced | Done (archived at `09. Archive/Unused Styles/Azma Paper Stage/`); obsolete |
| 8.2 | Browser editor parked | ref/TESSERACT_NOTES (D22) |
| 8.3 | Confirm per video what the hook "result" shows | SK §Scenes |

## D. LESSONS_LEARNED.md (hist/LESSONS_LEARNED)
| Entry | Lesson | Now in |
|---|---|---|
| v3 draft 1 | Paper Stage too generic → options board mixing several style books | SK §W1 (options from all sources); ref/SCENE_LIBRARY pools |
| v3 process | No artifacts; Tesseract | SK §Working rules |
| v3 process | Storyboards/questions as HTML | SK §W1–W2; ref/REVIEW_FORMATS |
| v3 board | Mixes; 5 options; build exact mix | SK §W1 |
| v3 captions | Romanised as spoken; serif hero + gradient, no blue | SK §Captions |
| v3 assets | Download real logos to assets/logos; face sticker avatar | SK §W0, §Look |
| v3 draft 2→3 (28 points) | Smoothness; no pops; Playfair glyph glitch; line → rect; B&W from the cut; split captions in white; white slop tiles; PiP headspace crop; green tick; longer swooshes → R01–R25 | SK §Motion/§Captions/§Sound; F-list in E; ref/MOTION_LIBRARY |
| v3 storyboard 3 | Face too low → hair line just below pane; organic blob + more orbit words; drawn oval read as real → label mock-ups as sketches | SK §Look, §W2 |
| v3 draft 3→4 | Logo + video slide out from behind head (lower, white disc, shadow); slow spin; captions slightly higher; wall one-word black Playfair; rounded PiP; same card contents swap; return after "intervention"; one-word CTA; keyboard held to end | SK §Captions, §Scenes, §Motion; ref/SCENE_LIBRARY S1, S7–S9 |
| v3 | "a little" ≈30 px not 120 | SK §Working rules |
| v3 deliverables | SFX-only + voice-only via `fx_check.py --mp3` | SK §W6, §Engine |
| v3 export | Always 1080p, even checks | SK §QC |
| process | GUI feasibility phase by phase; drop if >2–3 min | SK §Working rules |
| vid2 board | Don't ask about silence/unclear trims; cut and report | SK §W0 (C7) |
| vid2 board | SRT is a draft; flag meaning-changing words | SK §W0; ref/CAPTION_SYSTEM §1 |
| vid2 board | Reel timer element (12 px corners, behind head → corner, ring + countdown, label words rise + fade) | SK §Scenes (named); details in ref/SCENE_LIBRARY "Approved on vid2/vid5" |
| vid2 board | Real past drafts + skill-file cards with GitHub mark for effort beats | SK §Look; ref/SCENE_LIBRARY |
| vid2 captions | Repeated phrase, one changed word → keep support, swap hero | SK §Captions; ref/CAPTION_SYSTEM §2 |
| vid2 CTA | DM resource card on the tick, mid, left → right, above caption | SK §Scenes (C6); ref/SCENE_LIBRARY S9 |
| vid2 build | NFD matching for nukta letters; mode boundaries a little before word starts | SK §Captions; ref/CAPTION_SYSTEM |
| Style Lab | Animated looping tiles; re-offer every liked option (D24) | SK §W1 |
| Style Lab | Lower support line tight (+0.55 × size) | SK §Captions (C1) |
| Style Lab | Graphics on A-roll go low; blur only bottom half; face sharp, hair line visible | SK §Look |
| Style Lab | Labels never on lines/dots → above | SK §Look |
| Style Lab | Deck: anchor bottom-centre, fan wide → still-visible fan; fan-out screens appear together, then split | SK §Depth (pointer); ref/DEPTH_AND_MATTE §5; ref/MOTION_LIBRARY R29, R39 |
| Style Lab | Outro = calm move (parallax), not intro reversed | SK §Motion |
| Style Lab | Watch for accidental textures he likes (coarse grain) | SK §Working rules, §Look |
| Style Lab | Voice-note mishearings glossary | SK §Working rules |
| vid5 intake | Keep pauses carrying a joke/beat; say which | SK §W0 (C7) |
| vid5 board | Fan tops ≈ y 180, ±255 px / ±12°, rise 0.7 + split 1.1 s | ref/DEPTH_AND_MATTE §5, ref/MOTION_LIBRARY R39 (C4); SK §Depth pointer |
| vid5 board | Mixes (arc + timeline card; split + dock/liquid glass with real icons; PiP card + GitHub doc cards; progress bar below card) → build exact mix, list as F-list | SK §W1; ref/SCENE_LIBRARY "Approved on vid2/vid5" |
| vid5 board | CTA DM as notification "rishi sent you a file"; keyword in CAPITALS | SK §Scenes |
| vid5 build | One `setFxPropertyKeyframes` call per property; `t-(-0.05)`; unique mask ids | SK §Engine; ref/TESSERACT_NOTES |
| vid5 build | Giant word baseline ≈ y 445 at 360 px, rise ≤0.7 s | ref/DEPTH_AND_MATTE §5, ref/MOTION_LIBRARY R41; SK §Depth pointer |

## E. roughcut_v3 F-list (draft 3 storyboard, F1–F28)
| F | Note | Now |
|---|---|---|
| F1 | Hook shrink ~0.7 → 2.0 s, slow ease, no pause/snap | ref/MOTION_LIBRARY R05; SK §Motion (big moves) |
| F2 | Logo rises from behind head into chat header | superseded by draft 4 (C9): ref/SCENE_LIBRARY S1, R06 |
| F3 | Playfair glyph glitch fixed | SK §Engine (blur layerSize), §QC |
| F4 | Result card line → rect, his clip with premium grade | SK §Motion R01, §Scenes |
| F5 | B&W + nose-track from the return to face; pane drops while still B&W | ref/SCENE_LIBRARY S3; ref/MOTION_LIBRARY R13 |
| F6 | "nope." removed | SK §Scenes (reaction beats carry no words) |
| F7 | Split: whole head incl. hair visible | SK §Look |
| F8 | Split captions in the white area | SK §Captions (split mode) |
| F9 | Pane lands first, then cards one by one, slower | ref/MOTION_LIBRARY R09 |
| F10 | Skill-card padding consistent; small GitHub mark on all | ref/SCENE_LIBRARY S4; SK §Working rules (uneven padding is a glitch) |
| F11 | Smoothness everywhere; longer eases fine | SK §Working rules |
| F12 | No long empty white; exits overlap entrances | SK §Motion |
| F13 | design-skill.md line → rect, no pop, slower | SK §Motion R01 |
| F14 | Blob and doc close together; orbit fades in; fast → slow | ref/SCENE_LIBRARY S5; ref/MOTION_LIBRARY R11 |
| F15 | Jump cut hidden in a zoom | SK §Motion; R14 |
| F16 | Timeline card softer corners, gradient bars, grey gradient + vignette | ref/SCENE_LIBRARY S6; SK §Look |
| F17 | Wall zoom-out exactly on "why", slow, holds | SK §Motion (cut on trigger word); R15 |
| F18 | White tiles, moving grey gradient, "slop" Inter Bold | ref/SCENE_LIBRARY S7, DESIGN_SYSTEM; R24 |
| F19 | Smooth PiP move, headspace cropped | ref/SCENE_LIBRARY S8; R16 |
| F20 | Claude card line → rect, white/grey (no blue) | SK §Motion, §Look |
| F21 | Progress fills slower, holds longer | ref/MOTION_LIBRARY R18 |
| F22 | Iterations stay in PiP layout, card swap | SK §Scenes; R17 (draft 4: same card, contents swap) |
| F23 | Grow back to full screen slowly before the next line | SK §Motion (return after the line); R16 |
| F24 | Comment sheet + keyboard smoother, stay longer | SK §Scenes; R19 |
| F25 | Soft tap dot, blue → green tick | ref/MOTION_LIBRARY R20 |
| F26 | CTA captions one Playfair line | superseded by draft 4: one word at a time (C9); SK §Captions |
| F27 | Centre-aligned, ≈22 chars per line | SK §Captions |
| F28 | Swooshes longer, smoother, fade-in, peak on midpoint | SK §Sound |

## F. Motion IDs (ref/MOTION_LIBRARY, all retained there)
| IDs | In SKILL.md | Reference |
|---|---|---|
| E1, ES, EX, hold; no linear/overshoot | SK §Motion (values) | ref/MOTION_LIBRARY Easing |
| R01 (+R01+ shadow grows) | SK §Motion (values) | full |
| R02 (+R02+ directional continuity) | SK §Motion | full |
| R03 (+R03+ eased stagger 0.20/0.15/0.12/0.10/0.08) | SK §Motion | full |
| R04 hero letter build | SK §Captions | ref/CAPTION_SYSTEM §3 |
| R05/R16 (+ motion blur 0 → 6 → 0 at 50 %) | SK §Motion (big moves, motion blur) | full |
| R06, R07, R08 (+R08+), R09, R10, R11 (+R11+), R12, R13, R15, R17–R24 | via SK §Scenes / read-when trigger | ref/MOTION_LIBRARY |
| R14 cut-hiding zoom | SK §Motion | full |
| R25 A-roll push +1.2 %/s | SK §Motion | full |
| C-out soft caption exit (0.18 s EX, blur 6, up 10) | SK §Captions | full |
| Soft landing (Maybe) | — | ref/MOTION_LIBRARY (option only) |
| R26–R30 entrances (R26/R27/R28 top-3; R28 placed low; R29 bottom-centre anchor) | SK §Look (low placement), §Depth (deck) | full; pools in ref/SCENE_LIBRARY |
| R31 parallax lift, R32 blob wipe (outro = R31), R33 light sweep, R34 rack focus (Maybe) | SK §Motion (outro rule), §Look (bottom-half blur) | full |
| R35–R38b emphasis (R35/R44 digits Inter) | SK §Look (digits) | full |
| R39–R41, R11+ behind head | SK §Depth | full + ref/DEPTH_AND_MATTE §5 |
| R42–R50 proof/chrome/ambient (R42 label above line end) | SK §Look (labels above) | full |

## G. Scenes and pools (ref/SCENE_LIBRARY, ref/EDITING_PSYCHOLOGY)
S1–S9, A-roll-between-scenes, option pools (v2.0 and v2.1), beat → scene table, pacing (first graphic ~0.7 s, 45–55 % graphics, ≤ ~8 s plain A-roll, cut on trigger, return after line, no empty white, hide jump cuts, hold ≥0.5 s, CTA to the end), captions-as-psychology, anti-patterns (decorative graphics, >2 focal points, cutting away for the verdict, generic AI mock-ups): pacing, anti-patterns and core ideas are in SK §Motion/§Look/§Scenes; recipes and pools stay in reference (read for every options board and scene build).

## H. Other reference docs
| Doc | Hard rules surfaced in SKILL.md | Detail kept in reference |
|---|---|---|
| CAPTION_SYSTEM | text rules, grouping, A-roll spec, 5 modes, highlighter underline, don'ts, NFD, mode boundaries, repeated-phrase rule | exact mode geometry (baselines 372/330/922/935, sizes 100–110/54/78, auto-fit widths), reveal timings, not-adopted list |
| DESIGN_SYSTEM | palette, card gradient, accent default, grounds, type roles, corners, digits, missing glyphs | safe zone x 120–960, y 250–1600, icon column clear below y 1130; tokens board/wall/slop/teal/row.highlight/blob; type sizes; shadows; PiP/logo disc/video card; layout grids; coarse grain calibration (size ≈5.3); B&W −100 sat eased back ≈0.45 s |
| DEPTH_AND_MATTE | 1–3 per reel, no gap, new matte per cut, command, polarity check, mirrored JS, lumaInverted, non-matted hand-off, D28 | wiring steps, card high y 250–710, labels left/ticks right, failure modes, §5 tuned layouts; built-in `personMatte` gave empty matte |
| SOUND_DESIGN | cue levels (hero, flick, swoosh, pops, ticks), first 5 s +3 dB, voice chain, LUFS/TP, no music without licence | full cue map (highlighter −20…−23, risertick −20, flicker −21…−24, click −20…−24, typing −25), flick ±1 dB / 110 ms skip, peak alignment, raw-voice chain (HPF → 2.5:1 @ −24 → limiter −1.5), music ≈20 dB under voice, MP3 320 kbps |
| QUALITY_CONTROL | condensed checklist | full checkbox list |
| TESSERACT_NOTES | key musts | full pipeline, gotcha table (now + vid5 rows), review commands, browser editor |
| PRODUCTION_WORKFLOW | all stages | inputs list, build review loop, deliverables, "rules for every stage" (+ raw-footage, no-SRT, close-out added) |
| REVIEW_FORMATS | board/storyboard essentials, node --check, PNG, looping tiles, re-offer liked | fonts via Google Fonts, cqw units, sticky Copy-my-picks + Download .txt, localStorage in try/catch, picks text format, A/B layout questions, chat-report format |
| VISUAL_REFERENCE_LIBRARY | — (trigger only) | still index (paths updated) |

## I. Old SKILL.md v2.1
Load order → replaced by "Read only when…" table. Gates 1–7 → SK §W0–W6 (+ W7 close-out). Working rules (local HTML only, smoothness, "a little" ≈30 px, timebox, ask before installs, keep drafts) → SK §Working rules, §W3. "Defaults, not rules" → SK intro precedence.
