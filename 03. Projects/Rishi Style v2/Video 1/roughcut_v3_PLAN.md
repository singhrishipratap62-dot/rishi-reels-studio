# roughcut_v3 — Paper Stage planning doc (Gate 2)

**Source:** `roughcut_v3.mp4` · 1080×1920 · 30 fps · 33.5 s
**Intake files:** `roughcut_v3.face.json` (face found in 67/67 samples, chin_y median 0.644, so captions go at about y = 0.66 × 1920 ≈ 1270 px) · `roughcut_v3.srt` (the `Vid_1_hin.srt` timings mapped onto the rough cut)
**Silences > 0.6 s:** none.

### How the SRT was mapped
`Vid_1_hin.srt` is timed against `Vid 1.mp4` (51.7 s). I matched the rough-cut audio to the original and found 7 kept segments:

| rough cut | original | offset |
|---|---|---|
| 0.00–12.52 | 1.29–13.81 | +1.29 |
| 12.52–14.35 | 14.47–16.30 | +1.95 |
| 14.35–17.45 | 16.78–19.88 | +2.43 |
| 17.45–18.50 | 20.50–21.55 | +3.05 |
| 18.50–22.00 | 29.04–32.54 | +10.54 |
| 22.00–26.75 | 38.11–42.86 | +16.11 |
| 26.75–33.50 | 43.35–50.10 | +16.60 |

Two SRT chunks span a cut: "है। पहली" (18.50, only "पहली" survives) and "गया। कुछ" / "get-- कुछ" (21.7–22.3, the audio says "गया। कुछ"). I'll fix this caption text by ear at build time.

---

## Script → scenes
Recommended pick is marked ★. A-roll = plain A-roll + K01 caption (+ K02 focus-return after a graphic).

| # | time (rc) | line | trigger | suggested keys | ★ pick |
|---|---|---|---|---|---|
| 1 | 0.21–2.87 | Claude में video डाल के ये prompt डाल दोगे तो ऐसा कुछ बन जाएगा। | tool (Claude) · hook | **K17** Claude chat box: a video chip drops in on "video", the prompt types on "prompt", K09 cursor clicks send, a polished output thumb appears on "ऐसा कुछ बन जाएगा" · **K06** Claude logo as hero prop + K04 "video + prompt =" · **K10** video → prompt → result cards stack · **K04** alone | A-roll 0.21–0.55 → **K17 + K09** 0.55–2.87 |
| 2 | 2.87–4.27 | ऐसा कुछ नहीं होता है। | reaction | **A-roll** · **K03** mono-beat (dry "nope" beat) · K04 "NOPE." full-screen | **A-roll** (K03 if you want it, see Q3) |
| 3 | 4.27–5.59 | This doesn't work like that. | opinion | **A-roll** · K04 on white "doesn't work like that." | **A-roll** |
| 4 | 5.59–8.49 | आप दुनिया भर की skills इकट्ठा कर लो, GitHub repos इकट्ठा कर लो। | list (2) · tool (GitHub) | **K10** SKILL.md cards pile in on "skills", then GitHub repo cards on "GitHub repos" (K04 lead "collect all the" + big word) · **K11** a growing pile of skill files · **K17** GitHub repo page + cursor starring · **K06** folder pile on a teal floor | **K10** 5.93–8.10 |
| 5 | 8.49–12.51 | जब तक आप Claude को अपना taste या design skill नहीं समझा पाओगे, वो आपके लिए कुछ घंटा अच्छा edit नहीं करने वाला है। | thesis | **K06** Claude prop on a yellow floor + K04 lead "until you teach it your", big "*taste*" (Playfair italic) then "design skill", inking on the spoken word · **K07** Rishi cut-out explaining to a Claude prop (needs a photo) · **K18** quote card · **K04** alone | A-roll → **K06 + K04** 9.15–10.75 → A-roll from "वो आपके लिए…" |
| 6 | 12.53–14.35 | And ये पूरी video भी end-to-end Claude से edited है। | product · claim about this video | **K19** Claude logo on a base plate + pill "EDITED BY CLAUDE" over A-roll · **K17** Motion timeline mock · **K04** "end-to-end" full-screen | **K19** 13.39–14.71 (on A-roll, so his face stays up for "this video") |
| 7 | 14.35–17.43 | Why does this look better than all the Claude slop which you see out there? | question · picture-able ("slop") | **K06** a pile of identical generic "AI slop" cards (purple gradients, 🚀) on red felt + K04 lead "than all the", big "Claude slop" with "slop" in red · **K10** slop cards stacking · **A-roll** | A-roll 14.35–15.81 → **K06** 15.81–17.45 |
| 8 | 17.51–18.50 | Because मैंने उसको समझाया है। | "I" moment · bridge | **A-roll** · K07 Rishi cut-out (photo) | **A-roll** |
| 9 | 18.50–22.00 | पहली बार में आपको उसको मेहनत से समझाना है कि क्या करना है, कैसे करना है और एक बार वो समझ गया, | process · list (what / how) | **K17** the real skill folder: SKILL.md, RULEBOOK.md, LOOKBOOK.md rows reveal; cursor clicks RULEBOOK on "क्या करना है" and LOOKBOOK on "कैसे करना है" · **K10** two cards "what to do" / "how to do it" · **K07** Rishi teaching · **K20** first time → iterations | A-roll 18.50–19.60 → **K17 + K09** 19.60–21.70 |
| 10 | 22.00–26.75 | कुछ iterations के बाद it will get so better that it can do the whole thing autonomously without your intervention. | iterations · chronology | **K20** rail on A-roll, pill rolls v1 → v2 → v3 (the real version of this cut) · **K11** iteration counter with draft cards improving · **K06** K04 big "autonomously", lead "the whole thing,", sub "without you" · K16 quality chart (no real data, so not recommended) | **K20** on A-roll 22.27–24.29 → A-roll (K06 "autonomously" 25.19–26.75 as the alternative) |
| 11 | 26.75–33.50 | And if you want to learn how I did this, comment "edit" and I will send you a step-by-step breakdown of how you can achieve these kind of results. | CTA · outro | **K18** CTA card on A-roll: tab "comment", big word "EDIT" lights on "edit" · **K17** Instagram comment box with "edit" typing · **A-roll** only | A-roll → **K18** 29.10–31.06 → plain A-roll to the end |

## Density check (recommended picks)
| | value | target |
|---|---|---|
| graphic share | 15.1 s / 33.5 s = **45 %** | 40–45 % ✓ (with the alt "autonomously" scene added: 50 %) |
| first graphic | **0.55 s** | ≤ 2 s ✓ |
| longest A-roll stretch | **4.8 s** (24.29–29.10) | ≤ 8 s ✓ |
| hook coverage 0–8 s | **55 %** (K17 + K10) | ≥ 60 % ✗ slightly short. Fix options: K03 on line 2, or K04 on line 3 (→ ~70 %) |
| outro (last ~10 s) | 1 graphic (K18), then A-roll | ✓ |
| repeats | no key twice in a row; full-screen and on-A-roll alternate | ✓ |

## Assets (Gate 3 preview)
Everything above can be drawn in code: Claude logo/UI, GitHub mark and repo cards, generic slop cards, file rows, cursor, floors, cards. The skill folder rows use the real filenames from `skill/`. **I need nothing from you** unless you pick K07 (Rishi cut-out photo).

## Questions for Rishi
1. **K19 + K18 brand colour:** I recommend Claude's own clay orange **#D97757** (dark → light gradient). OK?
2. **Line 1 output thumb** ("ऐसा कुछ बन जाएगा"): a generic polished reel thumbnail, or a still from one of the reference edits?
3. **K03 / K14:** do you want the mono-beat on "ऐसा कुछ नहीं होता है" (it also fixes the hook density)? No b-roll planned.
4. **Line 10:** K20 version rail (v1 → v3) or the K06 "autonomously" scene, or both?
5. **Line 9:** the real skill folder (K17), or simpler "what / how" cards (K10)?

**Plan format:** edit the ★ column, or reply like "1 ok, 4 K11, 7 A-roll…".
