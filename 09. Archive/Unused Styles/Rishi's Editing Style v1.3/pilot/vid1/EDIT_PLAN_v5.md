# Vid 1 — EDIT PLAN v5 (pack v1.3: Ink blue + Editorial serif) — Gate 3: waiting for Rishi's approval

Replaces the copy-folder `EDIT_PLAN_v4.md` (written for v1.1 reference blue/cream). Beats, cut and cue words carry over from v4; the look is rebuilt on v1.3.

**Input:** `Video Projects/roughcut_v3.mp4` (1080x1920, 30 fps, 33.5 s; identical to the pilot's rough cut, md5 checked). Cut list = copy-folder `pilot/vid1/cutlist_v3.csv` (7 segments from `Vid 1.mp4`, retakes at 21.6-29.1 s and 32.5-38.0 s removed). Script = `Video Projects/Vid_1_hin.srt`, shown in Roman Hinglish only.
**Build:** Remotion (`tools/remotion/engine`), 1080x1920, 30 fps, ≈ 1005 frames. Fonts already in `assets/fonts/` (Inter-Variable, PlayfairDisplay-Italic-Variable). Sound after visual approval.
**Genre:** AI / tool workflow. Claim: "this whole video was edited end-to-end by Claude."

## A. What v1.3 changes vs v4
| v4 (v1.1 reference look) | v5 (v1.3) |
|---|---|
| blue `#4279BB→#205AA4` ground + streaks | **ink `#0B1224`** for heavy beats (verdict, question, autonomy) · **ice `#EAF0F8`** for proof/UI beats; grain + soft vignette, no grid/streaks |
| Inter captions, grey → white, one Playfair italic word | **Editorial serif**: hero word Playfair Bold Italic lowercase ≈ 132px, Inter Medium 48px support; support rises word by word, hero builds char by char with blur |
| red strike on "nahi" | red `#E5484D` kept only for that one negation strike |
| no depth move | **one signature depth move** (≤ 1 per reel): Style Pack files fan out *behind Rishi's head* on "samjhaya" (person matte, `engine/matte/`) |
| blue send button / badges `#2F80FF` | accent `#3E7BFA` (the only accent) |

## B. Caption placement (measured from the rough cut)
Face y ≈ 470-1200 (24-62% H); mic + hand y ≈ 1300-1540; gesturing hand on frame right. → A-roll captions: support line y ≈ 1270, **hero baseline y ≈ 1420**, centred, inside x 64-920; 0 → 45% black gradient over the bottom 40% so white type reads over the green jacket/mic. Graphic scenes: top band y 260-420.

## C. Beats (rough-cut time, s)
| # | time | script (Roman) | idea · function | scene (moves) | hero word | options (A = recommended) | why |
|---|---|---|---|---|---|---|---|
| 1 | 0.00-2.83 | Claude mein video daal ke yeh prompt daal doge toh aisa kuch ban jaayega. | naive belief · hook | face 0-0.5 → **ice**: recreated Claude chat card (white, orange asterisk) `hero-settle`; prompt types from "prompt daal" (1.11); a glossy "result" card `spring-pop` on "aisa kuch" (1.73) | *prompt* | A · B footage→card opener (A-roll shrinks into the chat card) · C face + prompt pill only | viewer sees their own shortcut; 4 changes in 2.8 s |
| 2 | 2.83-5.27 | Aisa kuch nahi hota hai. This doesn't work like that. | reject + verdict · turn | red strike (8 f) across the result card on "nahi" (3.0); cut to **ink** type beat: "this doesn't work" (Inter) → verdict hero *like that.* 200px `hero-char-blur` from 4.10 | *nahi* / *like that* | A · B red ellipse on the prompt · C giant *nahi* on ink | the "no" is drawn, then gets its own frame |
| 3 | 5.27-8.17 | Aap duniya bhar ki skills ikattha kar lo, GitHub repos ikattha kar lo. | hoarding tools · claim | `pane-drop` (ice pane top 48%, face below): skill cards `wall-build` on "skills" (5.89); dark repo cards slide over on "repos" (7.01); `wall-zoom-out` on the last "kar lo" | *skills* → *repos* | A · B full-frame wall · C cylinder carousel of cards (uses the one depth move here instead of beat 7) | quantity → wall; face stays |
| 4 | 8.17-12.46 | Jab tak aap Claude ko apna taste ya design skill nahi samjha paoge, woh aapke liye kuch ghanta achha edit nahi karne wala hai. | missing taste · thesis | pane keeps; wall blurs; one card "design-skill" `card→doc morph` on "design skill" (9.47); `pane-lift` on "ghanta" (11.07) → full face, `hold-push` | *taste* · *ghanta* | A · B full-frame doc · C face only | thesis lands on the face |
| 5 | 12.46-14.42 | And yeh poori video bhi end-to-end Claude se edited hai. | this video = proof | **ice**: real session card ("Read plan.md and continue…"), pill "end-to-end" (13.35, blue), `SKILL.md` file card `card-snap` on "edited" (14.01) | *end-to-end* | A · B Remotion timeline recreation · C split pane | real artifact, no invented numbers |
| 6 | 14.42-17.43 | Why does this look better than all the Claude slop which you see out there? | contrast · question | **ink**: two cards side by side: "this edit" (our ink/ice look) lights blue on "better" (15.28); generic "AI slop" parody card (gradients, emoji, no real creator's work) on "slop" (16.38) → greys + red ✗ | *better* · *slop* | A · B type beat only · C face only | makes "better" visible |
| 7 | 17.43-20.91 | Because maine usko samjhaya hai. Pehli baar mein aapko usko mehnat se samjhana hai ki kya karna hai, kaise karna hai, | I taught it · answer | **signature depth**: face full frame, ink-tinted wall; real Style Pack file cards (DESIGN_SYSTEM · SCENE_PRINCIPLES · MOTION_LIBRARY · EDITING_PSYCHOLOGY · SOUND_DESIGN) fan out **behind the head** on "samjhaya" (17.96), one per 4 f; chip "15 reels studied"; "kya" (19.93) and "kaise" (20.49) as hero words | *samjhaya* · *mehnat* · *kya* · *kaise* | A behind-head fan · B split pane with files · C ice full-graphic stack | "samjhaya" made literal; keeps the face during the core idea |
| 8 | 20.91-23.04 | aur ek baar woh samajh gaya, kuch iterations ke baad, | iteration · bridge | face, captions only, `hold-push` 1.0 → 1.04 | *iterations* | A · B version chips v1.0 → v1.3 (real) | breather |
| 9 | 23.04-26.82 | it will get so better that it can do the whole thing autonomously without your intervention. | autonomy · climax | **ink**: pipeline card (`card.dark`) ticks the real gates Analyse ✓ Plan ✓ Build ✓ Captions ✓ Export ✓ (≈ 0.45 s each from 23.3, ticks in blue), last tick on "autonomously" (25.14); `hold-push` | *autonomously* | A · B split · C giant word on ink | calmest move on the biggest claim |
| 10 | 26.82-33.50 | And if you want to learn how I did this, comment EDIT and I will send you a step-by-step breakdown of how you can achieve these kind of results. | offer · CTA | face 26.82-29.03; **Comments sheet** (`card.dark`) `comment-sheet-rise` on "comment" (29.03), "EDIT" types ≈ 8 f/char from 29.41, blue `#3E7BFA` send button press on "send you" (30.05); holds to end | *EDIT* · *step-by-step* | fixed (CTA = EDIT, from the earlier brief) | one literal action; ends on the face |

## D. Pacing / face check (approx.)
0-10 s ≈ 13 changes (target 10-14) · 10-20 s ≈ 9 (7-9) · 20-30 s ≈ 8 · 30-33.5 s ≈ 3 (CTA holds on purpose). Face visible: 0-0.5, 5.3-12.5 (lower pane), 17.4-23.0, 26.8-end. Longest face-free run: beat 1-2 (0.5-5.3 s) and beat 9 (3.8 s).

## E. Assets
Recreated UI only: Claude chat/session cards (neutral asterisk glyph in `#D97757`, no logo file), skill/repo cards (made-up names), "AI slop" parody card. Real: Style Pack file names, the "Read plan.md…" session line, "15 reels studied", the five gates. Person matte for beat 7: run `engine/matte/matte.py` on the rough cut (≈ 1 min at 720p).

## F. Decisions for Rishi (default if no answer)
1. Approve the beat table as-is? (default: A options throughout)
2. Signature depth move: beat 7 behind-head file fan (A) or beat 3 cylinder carousel? → beat 7.
3. CTA keyword still **EDIT**? → yes.
4. Keep the "AI slop" parody card (beat 6)? → keep.
5. Renders: Remotion needs headless Chrome outside the sandbox (LESSONS G1) — approve the out-of-sandbox render, or run `npx remotion render` yourself.
