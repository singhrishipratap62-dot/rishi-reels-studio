# RULE_AUDIT — pack v1.4 → v1.5 restructure (2026-11-11)
Proof that no rule was lost when SKILL.md became the only mandatory read. Every rule/ID from the old docs → where it lives now. "SKILL §X" = section of ../SKILL.md; "ref/" = ../reference/. Conflicts: the later rule (by R/E number, CHANGELOG version and date) wins.

## Conflicts resolved
| Topic | Old rule(s) | Current truth | Why |
|---|---|---|---|
| Sound | R1.0 voice only, no SFX/music, loudness as recorded | SFX on animations, −15 LUFS / ≤ −1 dBTP, music bed | R1.10, R1.15 (v1.3) override |
| Header | R1.0 refs had header; R1.9 removed it everywhere | Header on hook panel + board card; none on end card; no "gradnext" on end card | R1.17 reversed R1.9's header part only; R1.9's end-card part stands |
| End card "gradnext" | DESIGN_SYSTEM END (centred "gradnext") | No "gradnext" on end card | R1.9 (not reversed by R1.17) |
| Blur-in | R1.7 whole frame, σ 40 → 0, ~1 s; old SKILL "~1 s blur-in" | Panel only (y 0–750), σ 12 → 0, by 0.8 s (max 1 s), face never | R1.11 |
| Hook caption | DESIGN_SYSTEM [OBS] top-left ~y 800 x≈160; R1.4 y≈590 | Centred inside panel, y≈625 | R1.4 + R1.14 |
| Caption words | M02 original 2–7 words | 2–4 words, ≤680 px (x 200–880) | R1.5 |
| MBB strip | E1.10 typeset wordmarks | Real logos, mbb_logos_trim.png | R1.8 |
| Punch-in motion | R1.0 static ~1.25–1.35x; R1.13 cubic ease 110→100 % | 110→100 %, centred, sine ease-in-out, sub-pixel (s2zoom.py) | R1.14 |
| Music level | R1.15 ~21 dB under voice (Minimal Edit 18–24); E1.19 GAP 21; speed_music.sh header comment "~18 dB" | 13 dB under voice, 2 dB steps on request | R1.16 (comment in speed_music.sh corrected; code already GAP=13) |
| `_raw` export | R1.1 source resolution via cut.py --native | cut.mp4 scaled to 1080x1920 | R1.18 |
| Board background | DESIGN_SYSTEM CSS lavender gradient | gradnext loop video; gradient = fallback only | R1.17 |
| Premiere | R1.0 / old SKILL "never Premiere" | Build never in Premiere; Rishi's Premiere sequence may be the cut source; no hand-off back | E1.26 (R011) |
| Re-transcribing the cut | E1.2 re-transcribe every cut segment | Map island words; re-transcribe only non-whole-island segments | E1.20 |
| Paths | Video Projects/, projects/, exports/, assets/, DIff Acc | 03. Projects/Consulting Case/…, 04. Exports/Consulting Case/, 05. Asset Library/ | studio reorganisation |
| E1.24 duplicate | E1.24 (R008) and E1.24 (R009) | Merged into one entry (union of both) | same lesson, two reels |
| Gate count | R1.0 "one approval stop only" vs new Model gate | Still one approval STOP (plan); the model gate is a model check, not an approval | both kept |

## DECISIONS.md [R1.0] lines
| Rule | Now lives |
|---|---|
| R1.0 style name / pack location | SKILL title + paths |
| R1.0 references R1 (27 oct, Part 40) / R2 (28 oct, Part 39) | ref/VISUAL_REFERENCE_LIBRARY.md; SKILL intro ("R1/R2") |
| R1.0 exact clone | SKILL intro |
| R1.0 brand gradnext lowercase, IG 9:16 1080x1920 | SKILL intro, §The look |
| R1.0 input one-camera talking head, normal bg, English | SKILL intro ("one-camera talking head"); ref/DESIGN_SYSTEM |
| R1.0 goal raw in → MP4 out on laptop | SKILL intro |
| R1.0 build engine Playwright + ffmpeg; Tesseract OCR only | SKILL intro |
| R1.0 keep LAST complete take, drop flubs, tighten pauses | SKILL §Workflow 3 |
| R1.0 board planned from transcript | SKILL §Workflow 5 |
| R1.0 one approval stop (plan) | SKILL §Workflow 5 |
| R1.0 hook image sourced/generated licence-safe, flagged in plan | SKILL §Workflow 5, 6 |
| R1.0 MBB strip every video | SKILL §The look S1 |
| R1.0 exactly one punch-in on the credibility line | SKILL §The look S2 |
| R1.0 part number from speech; end card Part N / Follow for Part N+1 | SKILL §The look S4 |
| R1.0 no black after speech | SKILL §The look S4 |
| R1.0 sound voice only | superseded by R1.10/R1.15 |
| R1.0 font Avenir Next Demi Bold/Medium/Regular | SKILL §Captions; ref/DESIGN_SYSTEM Type |

## Rishi corrections R1.1–R1.19
| ID | Now lives |
|---|---|
| R1.1 three exports + placement guide | SKILL §Deliverables (resolution part superseded by R1.18) |
| R1.2 never overwrite a watched file; temp name + move | SKILL §Deliverables |
| R1.3 revisions final only | SKILL §Deliverables, §Workflow 9 |
| R1.4 hook caption centred inside panel | SKILL §The look S1 |
| R1.5 max 4 words / 680 px | SKILL §Captions |
| R1.6 hook question grey → dark as spoken | SKILL §The look S1 |
| R1.7 whole-frame σ 40 blur | superseded by R1.11 |
| R1.8 real MBB logos | SKILL §The look S1 |
| R1.9 no header anywhere | header part superseded by R1.17; end-card part ("no gradnext", end-card text) in SKILL §S4 |
| R1.10 SFX wanted, Minimal Edit sound rules, cue sheet | SKILL §Sound; ref/SOUND_DESIGN.md |
| R1.11 blur panel only σ 12, by 0.8 s | SKILL §The look S1 |
| R1.12 no SFX on captions/hook darkening | SKILL §Sound |
| R1.13 110→100 % settle (cubic) | settle in SKILL §S2; easing superseded by R1.14 |
| R1.14 sine, sub-pixel, centred; hook caption y≈625 | SKILL §S1, §S2 |
| R1.15 1.2x, music not sped, fades, skip intro, keep `_1x`, QC with 1.2 | SKILL §Sound, §Deliverables, §Workflow 8; level superseded by R1.16 |
| R1.16 music 13 dB under voice, 2 dB steps | SKILL §Sound |
| R1.17 header back; bg loop video | SKILL §The look Header, S3 |
| R1.18 all exports 1080x1920, decode 4K once | SKILL §Deliverables |
| R1.19 pack = the workflow; newest Video N input | SKILL intro, paths, §Workflow 1 |

## Engine / process E1.1–E1.27
| ID | Now lives |
|---|---|
| E1.1 4K raw, no 4K intermediates, 1440x2560, 3 GB | SKILL §Workflow 0; ref/ENGINE_NOTES.md |
| E1.2 islands + per-segment whisper, drift, parallel retry | SKILL §Workflow 2; ref/ENGINE_NOTES.md |
| E1.3 multiple raw files, later wins | SKILL §Workflow 1 |
| E1.4 no piped board render; chunks; QC catches truncation | SKILL §Workflow 8; ref/ENGINE_NOTES.md (built into compose.sh) |
| E1.5 caption splitting | SKILL §Captions |
| E1.6 number-line tiers, y≈375, axis y 508 | SKILL §Board grammar (tiers); ref/DESIGN_SYSTEM.md (y values) |
| E1.7 strike-through + small ✗ | SKILL §Board grammar; ref/DESIGN_SYSTEM.md |
| E1.8 face crops | SKILL §Workflow 6; ref/PRODUCTION_WORKFLOW.md §5 (exact values) |
| E1.9 hook photo logo check + CREDITS | SKILL §Workflow 6; ref/ENGINE_NOTES.md |
| E1.10 typeset wordmarks | superseded by R1.8 |
| E1.11 screenshot hang, 4 s timeout, 6 retries | ref/ENGINE_NOTES.md (built into render.js) |
| E1.12 video/audio length pad; QC stream durations | SKILL §Workflow 8; ref/ENGINE_NOTES.md |
| E1.13 gblur sigma + sigmaV; sharpness QC | SKILL §Workflow 8; ref/ENGINE_NOTES.md |
| E1.14 AAC +0.3–0.5 dB TP, limit −1.6 dBFS | SKILL §Sound (target); ref/SOUND_DESIGN.md |
| E1.15 keep Mac awake | SKILL §Workflow 0; ref/ENGINE_NOTES.md |
| E1.16 chat images don't reach disk | SKILL §Workflow 6; ref/ENGINE_NOTES.md |
| E1.17 sub-pixel zoom (PIL) | SKILL §S2 ("sub-pixel"); ref/ENGINE_NOTES.md |
| E1.18 4x oversampled limiter | SKILL §Sound (target); ref/SOUND_DESIGN.md |
| E1.19 light duck threshold 0.1 ratio 2 | SKILL §Sound; GAP 21 superseded by R1.16 |
| E1.20 islands.py; map island words | SKILL §Workflow 2, 3 |
| E1.21 qc.py reads crops.env; tail from word END | ref/QUALITY_CONTROL.md, ref/ENGINE_NOTES.md (SKILL §S4 tail value) |
| E1.22 compose_green.sh needs BGVIDEO | ref/PRODUCTION_WORKFLOW.md §6, ref/ENGINE_NOTES.md (R011 run_build.sh passes it) |
| E1.23 disk ~1.7 GB/project, clear board chunks | SKILL §Workflow 0, 10 (finalize_reel.sh); ref/ENGINE_NOTES.md |
| E1.24 (R008) sandbox: WHISPER_NG=1, VideoToolbox outside sandbox, parallel terminals own R### | SKILL §Workflow 0, 2, 7; ref/ENGINE_NOTES.md (merged) |
| E1.24 (R009, duplicate ID) same + render.js needs ~/.npm and ms-playwright | merged into the above; ref/ENGINE_NOTES.md, ref/PRODUCTION_WORKFLOW.md |
| E1.25 OCR heuristic caveat; sizing board variant | SKILL §Workflow 8; ref/QUALITY_CONTROL.md; sizing variant SKILL §Board grammar + ref/DESIGN_SYSTEM.md |
| E1.26 Premiere sequence as EDL | SKILL §Workflow 3; ref/PRODUCTION_WORKFLOW.md §2 |
| E1.27 sfx48/info.json preflight | SKILL §Workflow 6; ref/ENGINE_NOTES.md |

## MOTION_LIBRARY M01–M12 (file kept whole in ref/MOTION_LIBRARY.md)
| ID | Now lives |
|---|---|
| M01 caption word rise-in | SKILL §Captions (named); full spec ref/MOTION_LIBRARY.md |
| M02 hard phrase change, 2–4 words | SKILL §Captions |
| M03 board fade/rise 200–250 ms | ref/MOTION_LIBRARY.md (implemented in board.html/beats.js) |
| M04 icon draw-on | ref/MOTION_LIBRARY.md |
| M05 count-up | ref/MOTION_LIBRARY.md; SKILL Flexible (ranges) |
| M06 bar grow | ref/MOTION_LIBRARY.md |
| M07 unit grid | ref/MOTION_LIBRARY.md |
| M08 board clear ~250–300 ms, root to top-centre | SKILL §Board grammar; ref/MOTION_LIBRARY.md |
| M09 number-line marker | ref/MOTION_LIBRARY.md |
| M10 tab activate | ref/MOTION_LIBRARY.md |
| M11 hard cuts only at S1→S2, S2→S3 | SKILL §Canvas |
| M12 no zoom/move on face card | SKILL §Canvas |

## Other old docs (non-ID rules)
| Source → rule | Now lives |
|---|---|
| Old SKILL: 1080x1920 29.97, four scenes, scene contents | SKILL §The look |
| Old SKILL: board card / caption / face card px | SKILL §S3 |
| Old SKILL: element ±2 frames; cut no pause > 0.3 s; 8–12 ms crossfades | SKILL §Board grammar, §Workflow 3 (cut.py uses 10 ms fades, within 8–12) |
| Old SKILL: Gates 1–8, plan contents, revisions table | SKILL §Workflow 1–9 |
| Old SKILL: Flexible list | SKILL §Never/Flexible |
| Old SKILL: Evolve the system (LESSONS + CHANGELOG versioning) | replaced by SKILL §Learning loop |
| DESIGN_SYSTEM: philosophy, colour tokens, type sizes, glow, highlight strip, core/optional, low-evidence list | ref/DESIGN_SYSTEM.md (navy #2C3552 and caption size also in SKILL) |
| DESIGN_SYSTEM: text safe zone y 140–830, Reels UI | SKILL §Captions |
| DESIGN_SYSTEM: board grammar FACTS / SOLVE / END | SKILL §Board grammar, §S4; detail ref/DESIGN_SYSTEM.md |
| DESIGN_SYSTEM: canvas H.264 ~17–19 Mb/s, AAC 48 kHz | SKILL §Canvas (codec); bitrate ref/DESIGN_SYSTEM.md |
| SCENE_PRINCIPLES: S1 ~2.5–3.0 s, S2 ~1.8–2.0 s, mic visible, board empty ~0.3 s, tabs on "N ways", S4 ~3 s, share of runtime | SKILL §The look (empty board, tabs, S4); rest ref/SCENE_PRINCIPLES.md |
| SCENE_PRINCIPLES: don't invent scene types; photo literal; no card/glow in hook | SKILL §Canvas, S1, §Workflow 6 |
| EDITING_PSYCHOLOGY: script template 1–10, selection framework | ref/EDITING_PSYCHOLOGY.md (trigger: writing the beat table) |
| EDITING_PSYCHOLOGY: anti-patterns | SKILL §Never |
| EDITING_PSYCHOLOGY: captions use corrected script, confirm in plan | SKILL §Captions, §Workflow 4–5 |
| SOUND_DESIGN: trigger map + target peaks | ref/SOUND_DESIGN.md (implemented in sfx.py) |
| SOUND_DESIGN: 110 ms louder wins; +3 dB first 5 s → 0 by 6 s | SKILL §Sound |
| SOUND_DESIGN: voice chain (75 Hz HPF, 2.5:1 @ −24 dB 15/180 ms, +4 dB, limiter −1.5 dBFS, voice −15 LUFS) | ref/SOUND_DESIGN.md (implemented in sfx.py) |
| SOUND_DESIGN: music offset 0:15, duck 60/450 ms, fades | SKILL §Sound; attack/release ref/SOUND_DESIGN.md |
| SOUND_DESIGN: cue sheet; phone listening | SKILL §Sound |
| PRODUCTION_WORKFLOW: tool paths, step commands | ref/PRODUCTION_WORKFLOW.md (paths updated); SKILL §Workflow |
| PRODUCTION_WORKFLOW: edl handles 40/60 ms, tail 0.4 s | SKILL §Workflow 3 |
| PRODUCTION_WORKFLOW: hook photo 4:3, Wikimedia/Unsplash/Pexels | SKILL §Workflow 6; sources ref/PRODUCTION_WORKFLOW.md |
| QUALITY_CONTROL: all 17 checks | SKILL §Workflow 8 (summary); full list ref/QUALITY_CONTROL.md |
| VISUAL_REFERENCE_LIBRARY: private study only, never publish; capture notes | ref/VISUAL_REFERENCE_LIBRARY.md |
| README read order | obsolete (history/README.md); replaced by SKILL "Read only when…" |
| CHANGELOG v1.0–v1.4.2 | history/CHANGELOG.md (+ v1.5 entry) |
