# QUALITY_NOTES — V01/V02 check (Opus, 2026-11-06)
Scope: read BRIEF + V01/V02 BREAKDOWN.md + animations.json; spot-checked 2 V01 CSVs (d_orbit_ang, t_typeon) and 2 V02 CSVs (sw_black, icon_shrink_b). No videos/strips re-viewed.
Sonnet: apply §2 "forward" rules to every remaining reel, tick §3 before marking a reel done, and do the "now" fixes when budget allows (cheapest first).

## 1. Verdicts
**V01 — PARTIALLY meets the bar.**
- Strong: all 12 sections; 14 curves measured with bezier + rmse; timeline gap-free with WHY on every row; catalogue frame-exact.
- Weak: §5/§6/§10 thin (glow radii/corner radii EST, no orbit radius or perspective, pacing curve not quantified); sound named as fact ("whoosh", "hit"); coordinates mostly src px only; ~half the entries lack a trigger offset.
- Errors: A19 mis-described (not centred, see §4); json conflicts with text on A05/A07/A22.

**V02 — PARTIALLY meets the bar (weaker on process).**
- Strong: 10 measured curves, measured hexes, honest gaps section, good editing-psychology logic.
- Weak: only 3/25 strips viewed, yet sheet-based timings are written at frame precision (A02 "8-10 f", A17 "0.4-0.5 s"); noisy spring fits (rmse .17-.20) promoted into signature move 5; existing CSVs (eye, a_script, split_in2/3, icon_in) never cited.
- Errors: timeline gap #198-199 + overlaps; json dur_ms uses an inclusive (+1 frame) convention unlike V01.

Both clearly beat a "normal" reverse-engineering. They are not at "10x" yet because about a third of the numbers a rebuilder needs are EST, and some EST numbers read like MEAS.

## 2. Corrections
Tag key: **forward** = apply to: V03-V15 going forward · **now** = fix in V01/V02 now. Cost: C cheap · M medium · E expensive.

- **Q1** [forward + now, C] `dur_ms = (end_f − start_f) × 1000/30`, where end_f = first frame at rest. Why: V01 and V02 disagree; V02 json is +33 ms on every entry. Recompute V02 json.
- **Q2** [forward + now, C] One json entry = one motion phase. Split enter/hold/exit into `-a/-b` ids (or a `phases` array); bezier + evidence describe only the measured phase. Caption *styles* (V01-A14, V02-A20) → `category:"style"`, `dur_ms:null`. Why: V01-A22 json spans 2200 ms "MEAS" but the bezier is only the 467 ms entrance.
- **Q3** [forward + now, C] Fit-quality gate. Always print rmse next to the bezier. rmse ≤ .05 → bezier [MEAS]. .05-.12 → named easing [MEAS], bezier marked "≈". > .12 → easing family only, json `bezier:null`, evidence EST. Net change < 40 src px or < 15% → no overshoot % claim. Why: V02 A10/A16/A18 overshoots come from rmse .17-.23 fits.
- **Q4** [forward, C] Report overshoot as a peak/final ratio ("peak 1.24× final"). Add the % of net change only when the start value is a real rest value, not the first frame where the tracker detects the element. Why: V02 sw_black starts at 96 px only because detection begins there.
- **Q5** [forward + now, C] Precision follows the source. From 2 fps sheets write "~0.5 s [EST]", never frame counts. Frame counts come only from strips or CSVs.
- **Q6** [forward, M] View every strip that contains an events.md burst or a catalogued animation; static strips may be skipped. §12 must state `Strips viewed: N/M; skipped = static: [list]`. Worth it: this is the BRIEF's frame-by-frame pass.
- **Q7** [forward + now, C] Run `ls work/` (and subfolders) before writing. Cite every CSV (number + file name) or list it in §12 as discarded, with the reason.
- **Q8** [forward + now, C] Every catalogue entry carries a trigger offset: `trigger: "<word>" @#F (words.json) → start #S, Δ = S−F f`. Non-speech triggers: `trigger: cut #N`. Cheap: read from words.json.
- **Q9** [forward, C] Every position is given as x%, y% AND 1080-px (src × 1.5). Applies to cx/left/right values in §3, not just §2.
- **Q10** [forward + now, C] Hard rule (Claude cannot hear): never write whoosh/riser/hit/pop/impact as fact, including in the timeline SFX column. Format: `onset 2.86 s (attack 350 ms, centroid 2.1 kHz) [MEAS]; whoosh-like [INF]`.
- **Q11** [forward + now, C] The timeline tiles frame 0 to the last frame exactly: each row starts at the previous end + 1. Check before saving: `awk -F'|' '/^\| [0-9]/{split($2,a,"-"); print a[1], a[2]}' BREAKDOWN.md` and eyeball the continuity.
- **Q12** [forward, C] Every hex carries [MEAS f#] or [EST]; no bare "-ish". For the 1-2 dominant glows, measure the radius once (numpy luma profile across one edge, distance from 90% to 10% of peak).
- **Q13** [forward, C] Corner radius always as % of card width (one unit). §6 must give, per 3D/orbit element: radius (px + %W), deg/s from a CSV, tilt, perspective/rotateY estimate, or "flat [OBS f#]".
- **Q14** [forward, C] §10 must include (a) a selection table condition → action → reason with ≥ 4 rows, and (b) a pacing curve: visual changes per 10 s for hook/body/CTA, counted from timeline rows.
- **Q15** [forward, C] §11 recipes are self-contained: duration ms, easing/bezier, size %, hex, so they can be copied without opening §3.
- **Q16** [forward + now, C] json `evidence` matches the BREAKDOWN tags for the same numbers. Mixed evidence → e.g. `"MEAS(scale),EST(rotation)"`.
- **Q17** [forward, C] Every catalogue entry ends with `Rebuild:` (a CSS or Remotion one-liner), including micro-animations.
- **Q18** [forward, C] On-screen text beats ASR. Quote the ASR word once as `[ASR: x]`, then use the on-screen spelling everywhere, consistently.
- **Q19** [now, M — worth it] V02: view the strips for A02 (0-2 s), A12 meter (22-26 s), A15 panels (~28 s), A16/A17 swatches + logos (34-40 s) and the CTA (~44 s), about 8 of the 22 unviewed strips. Replace the sheet-based timings. Viewing all 22 is E and not worth it.
- **Q20** [now, C — worth it] V01-A04 push-in scale: pull #92 and #93 with frame.sh, measure the height of one shared element (card edge or numeral) in both, and report the ratio as the scale [MEAS]. This replaces the timed-out zoom solver; the move is signature-level.
- **Q21** [now, C] V01 mic-boom occlusion: keep it as [OBS caps2] and add `[INF] static roto / track matte (camera locked)` plus `Rebuild: caption layer between footage and a static boom mask`. Further investigation is not worth it.

## 3. Minimum bar checklist (tick all before marking a reel done)
1. 12 sections present; timeline tiles every frame (Q11).
2. Every timeline row has WHY = job + mechanism.
3. ≥ 8 curves measured; each cites CSV + rmse; Q3 gate applied.
4. Every catalogue entry: start/end f, ms, from→to, easing, trigger Δf (Q8), exit, Rebuild (Q17).
5. No frame-precision number taken from sheets; "Strips viewed N/M" in §12 (Q5, Q6).
6. Every work/ CSV cited or listed as discarded (Q7).
7. Coordinates in % + 1080 px (Q9).
8. Every hex tagged; radius in % width; main glow radius measured (Q12, Q13).
9. No sound named as fact; onsets with attack/centroid (Q10).
10. §10 selection table + pacing per 10 s; §11 recipes self-contained (Q14, Q15).
11. json: Q1 duration, one phase per entry, evidence matches text (Q2, Q16).
12. Hard rules: "gradnext" lowercase, Hinglish in Roman script, no asset reuse outside work folders.

## 4. Wrong or overstated (line → fix)
### V01 BREAKDOWN.md
- **L77 A19** "text block centred while growing (left edge 632→22 px)" is wrong. t_typeon.csv shows the right edge pinned at 719 (frame edge) for #489-510 while the left edge goes 490→0. Fix: "grows leftward from the right frame edge (right edge pinned at x100%), overflows the left edge by #504; then the line scrolls left 9.7 px src/f (14.6 px @1080), measured on the right edge 719→545 over #510-528 [MEAS t_typeon.csv]".
- **L85 A23** "easing to ~0 by #1084" is overstated. d_orbit_ang.csv still shows 144.8°→151.4° over #1070-1084 (~14°/s). Fix to that. (The 160°/s figure checks out: 36.4→123.3° over #1036-1052 = 163°/s.)
- **L73 A17** "2D rot ≈ −40° at #427" has no tag → add [EST].
- **L41 vs L104** glow colour "#2F7BFF-ish" vs "#2E7CF6": pick one and tag it. **L41 vs L105** corner radius "≈4% of card W" vs "~6% of height": unify to % of width.
- **L16, L22, L149** "whoosh", "hit", "Whoosh-type cues" → Q10 format.
- **json vs text**: A05 text 400 ms (#103-115) vs json 94-115 = 700 ms; A07 text 233 ms fade (#146-153) vs json 146-157 = 367 ms "MEAS linear"; A22 json 857-923 = 2200 ms "MEAS" carrying the entrance-only bezier → split phases (Q2).
- **json A14** 531-1238 = 23 567 ms → turn into a style entry (Q2).

### V02 BREAKDOWN.md
- **L145 signature move 5** "45-60% overshoot, bezier ≈ (0,1.4,0,1.05)" is overstated. Fix: "spring pop, peak ≈ 1.24× final (sw_black bw 96→193→156) [MEAS]; curve shape EST (fits rmse .17-.20)".
- **L54 A10, L66 A16** overshoot % and bezier are tagged MEAS but the fits have rmse .17-.20 → EST per Q3/Q4. (A09 at L52, 21% undershoot 225→157→169, checks out but has rmse .128 → bezier "≈".)
- **L70 A18** already flagged noisy (rmse .205-.226) → json `bezier:null`, evidence EST.
- **L38 A02** "≈8-10 f [EST from sheets]" → measure from the existing work/tr/a_script.csv, or write "~0.3 s [EST]".
- **L60 A13** eye "not tracked" is false: work/tr/eye.csv exists → run ease_fit on it and cite.
- **L48 A07** reuse at #712/#990 "[OBS]" → cite durations from split_in2.csv / split_in3.csv.
- **L50 A08** → cite icon_in.csv / icon_in_b.csv (and cardexp.csv for A05) or list them as discarded.
- **L68 A17** "staggered ≈0.4-0.5 s apart" comes from 2 fps sheets → "~0.5 s [EST]" until the strips are viewed (Q19).
- **L15** "risers" and **L131** "soft whoosh/pop texture" → Q10 format.
- **L17-18 timeline**: gap #198-199 (row ends 197, next starts 200); overlaps at #125, #536-540, #714-719 → retile (Q11).
- **L29** "jargiest" vs **L154** "jergiest" → `[ASR: jargiest]` → on-screen "Luxurious brands" (Q18).
- **json**: every dur_ms is +33 ms (Q1); A21 start = end = 920 → dur_ms 0, category "cut".
