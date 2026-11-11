# Scene library: Rishi v2

> Recipes Rishi approved on roughcut_v3. They are starting points; recombine them, and invent new ones in the same language (white cards, smooth reveals, the face kept in the frame). Each recipe: trigger → layout → motion (MOTION_LIBRARY IDs) → assets → engine block. Reference frames: `../references/stills/`.

## S1 · Opening twin slide-out (0–0.7 s) · `01_opening-twin-slide-out.jpg`
- **Trigger:** first words of the hook, naming a tool plus "video" or "me".
- **Layout:**
  - the Claude logo on a white disc goes upper-left (250, 610);
  - a framed card of the live video goes upper-right (830, 620);
  - both sit low enough to stay clearly in frame.
- **Motion:** R06 from behind the head (track matte), R07 spin on the logo. Afterwards the logo flies to the next scene's header and the video card drifts off with R02.
- **Assets:** logo PNG, live clip, person matte.
- **Engine:** `logo_disc()`, `logoA` / `vidA` / `logoB` / `vidB` in `# B1`.

## S2 · Hook: shrink into the chat (0.7–2.9 s) · `12_hook-shrink.jpg`, `02_hook-chat-result.jpg`
- **Trigger:** "put X into Claude/tool + prompt → result".
- **Layout:** ice ground, white chat card with the real logo in the header, the face as a video attachment, the prompt in the input, a send button, and a result card top-right.
- **Motion:**
  - R05 shrink;
  - R22 typing;
  - R23 highlighter;
  - send press;
  - result via R01 showing **his own clip, graded warmer (+14 saturation), dark bottom gradient, a serif word**.
- **Don't:** a "wow" gradient mock-up or a pop entrance.
- **Captions:** light-ground mode, just above the card.

## S3 · B&W nose-tracked beat (≈2.9–5.3 s) · `03_bw-nose-track.jpg`
- **Trigger:** a reaction or verdict ("aisa kuch nahi hota", "doesn't work like that").
- **Start:** the instant the previous scene returns to the face; hold through the verdict.
- **Motion:** R13. Colour can carry over into the next scene's entrance (the pane dropped while still B&W).
- **Don't:** a word overlay ("nope." was removed).

## S4 · Split pane: list or collection (≈5.3–8.4 s) · `04_split-skills-repos.jpg`
- **Trigger:** "collect all the X, Y" (lists of things).
- **Layout:**
  - ice pane on the top 940 px, captions at the top of the pane, then a 3×2 grid of white skill cards (small GitHub mark, even padding, auto-fit font);
  - dark repo cards below it;
  - the face in the lower half with the full hair line visible.
- **Motion:**
  - R08 drop;
  - then R09 cards one by one (only after the pane lands);
  - R10 repo cards;
  - R02 exit up while the next set arrives, with no empty white beat.

## S5 · Split pane: doc + organic figure (≈8.5–11.5 s) · `05_split-doc-orbit.jpg`
- **Trigger:** a thesis about taste, skill or knowledge.
- **Layout:**
  - left of centre: a `design-skill.md` card with headings and lines;
  - right: the organic painted blob with a halo;
  - ~8 orbiting words (palette, practice, rhythm, sound design, pacing, texture, timing, typography).
- **Motion:**
  - R12 blob, then the doc R01 ≈0.15 s later (close together);
  - doc lines R03 at 0.12 s;
  - R11 orbit;
  - R08 lift on the next beat.
- **Don't:** a plain circle, or words popping in suddenly.

## S6 · Behind-the-head card (≈12.7–14.6 s) · `06_behind-head-timeline.jpg`
- **Trigger:** proof or meta ("this video was edited by Claude").
- **Layout:**
  - a white card (x 90–990, y 250–710, radius 14), white → grey gradient + vignette;
  - a Claude name pill;
  - timeline lanes (A-roll, captions, graphics, sfx) with gradient blue bars;
  - a red playhead;
  - all behind the head via the matte.
- **Motion:** R01, lanes R10-style from the left, playhead linear; R14 zoom hides the jump cut before it.
- **Depth:** `DEPTH_AND_MATTE.md`. No visible gap around the head.

## S7 · Wall zoom-out (≈14.6–17.5 s) · `07_slop-wall-one-word.jpg`
- **Trigger:** contrast with "all the other X" ("all the Claude slop out there").
- **Layout:**
  - a 3×4 wall of white grey-gradient tiles, each labelled "slop" in grey Inter Bold;
  - the face is tile 2 from the top (centre column), with a soft white glow;
  - subtle 8 px corners.
- **Motion:** R15 starting exactly on the trigger word (e.g. "why"); R24 breathing tiles.
- **Captions:** wall one-word mode in the tile below the face (black Playfair).

## S8 · PiP + card (≈18.5–27.5 s) · `08_pip-card-files.jpg`, `09_pip-card-pipeline.jpg`
- **Trigger:** an explanation with steps ("I taught it what to do, how to do it" → "after iterations it runs autonomously").
- **Layout:**
  - the face in a rounded, glowing PiP (headspace cropped, scale 32 %, centre (540, 1270));
  - one white card above with a "Claude · ● awake" header that **stays**;
  - contents A: a file list (`paper-stage-edit/`, SKILL.md, RULEBOOK.md → "what to do" ✓, LOOKBOOK.md → "how to do it" ✓, progress bar → 100 %);
  - contents B: Analyse · Plan · Build · Captions · Export with dividers, pending rings and ticks (the last tick lands on the key word).
- **Motion:**
  - R16 in;
  - card R01;
  - R03 rows;
  - R18 progress (≈1 s, slow);
  - R17 swap;
  - card R02 out and R16 back to full screen **after** the line ends.
- **Captions:** PiP single-line mode.

## S9 · Comments-sheet CTA (≈29.1 s → end) · `11_cta-comments-sheet.jpg`
- **Trigger:** "comment X and I'll send you…".
- **Layout:**
  - the face moved up, blurred and dimmed;
  - a dark sheet (#1C1C1E) with a handle and "Comments";
  - Rishi's sticker avatar, then the field, then the send button;
  - a suggestion bar (left, typed word in quotes, right);
  - a full iOS-style dark keyboard.
- **Motion:**
  - R19 rise;
  - R21 typing E · D · I · T;
  - R20 tap + green tick on "send";
  - held until the final 0.35 s.
- **Captions:** CTA one-word mode.
- **Keyword** typed in CAPITALS (vid5).
- **DM follow-up (vid2 → vid5, current):** on the green tick, a message notification ("rishi sent you a file") slides in left → right, mid-screen, just above the one-word caption. (vid2 used a DM "resource" card in the same place; vid5 refined it into the notification.)

## A-roll between scenes · `10_aroll-caption.jpg`
- Plain face + caption system + R25 push. Use R14 to hide jump cuts.
- Return to the face between graphic scenes, but the face may stay *inside* graphics (S2, S7, S8, S9).

---

## Option pools for future options boards (5+ per frame type)
| Frame type | Pool (mix freely) |
|---|---|
| Hook (tool + result) | S2 shrink-into-chat · footage → card opener · framed screen + highlighter `[DP]` · face + floating prompt pill · twin slide-out S1 + chat |
| Reaction / "no" | S3 B&W track · face punch-in · circled serif word `[DP]` · drum-roll words on ink `[RES]` · red strike on the previous card `[RES]` |
| List / collection | S4 split pane grid · full-frame card wall + zoom-out `[RES]` · chip row `[DP]` · file stack on paper `[ME]` · cylinder carousel behind the head `[RES]` |
| Thesis | S5 doc + organic figure · quote card with blue nouns `[DP]` · text-centric with quote marks `[ME]` · face-only serif hero · card → doc morph `[RES]` |
| Proof / meta | S6 behind-head card · name pill on the face `[DP]` · real session card + pill `[RES]` · highlight-box caption `[ME]` · timeline recreation full frame |
| Contrast | S7 wall zoom-out · two cards side by side `[RES]` · struck word vs serif word `[DP]` · graph of two lines `[ME]` · tile pile |
| Explanation / steps | S8 PiP + card · whiteboard + PiP `[DP]` · split checklist `[RES]` · line + zigzag `[ME]` · files fanning behind the head `[RES]` |
| Iteration / autonomy | S8 contents swap · version rail v1 → vN `[PS]` · staircase graph `[ME]` · pipeline card behind the head `[RES]` · chapter card `[DP]` |
| CTA | S9 comments sheet · comment bar from the right edge · text-centric "edit" `[ME]` · face + highlight box + DM arrow `[ME]` · brand-colour card `[PS]` |

## v2.1 option pools (Style Lab v1, 2026-11-09)
**Rule from Rishi:** on every future options board, show **every option he has already liked** for that frame type (Keeps first, then Maybes), even if that goes past 5. New ideas come after.
| Frame type | Liked options to always offer (IDs in MOTION_LIBRARY) |
|---|---|
| Card entrance | R01 · R26 · R27 (top 3) · R28 (low) · R29 · R30 |
| Face ↔ graphic | R08 · R31 · R32 · R33 · maybe R34, window zoom |
| Emphasis | R23 highlighter · R35 number roll · R36 circle · R37 echo · R38 / R38b spotlight · caption highlighter underline |
| Grounds | mesh (favourite) · ice · paper.warm · dots+mesh · ink.spot (dark or white card) |
| Behind the head | S6 card · R39 fan · R40 arc · maybe R41 giant word, orbit (only with headroom) |
| Proof / data | S6 timeline (gradient bars) · R42 graph · R43 before/after · R44 stats · R45 comments (+ phone mock-up variant) |
| Chrome | reel timer ring · R46 cursor guide |
| Ambient | R07 · R47 · R48 · R49 · R48+R49 combo · R50 |
| Accent | duo · blue · clay · mono · jacket |

## Approved on vid2 / vid5 (2026-11-09/10) `[R]`
- **Reel timer** (chrome): subtle 12 px corners, comes from behind the head → corner, ring + countdown held for the whole reel, label words rise + fade on the move.
- **Show the real work** for effort beats ("hafte ya mahine"): real past drafts as proof + real skill-file cards with a small GitHub mark.
- vid5 picked mixes (build exactly such mixes, listed as an F-list): horizon arc + a smaller timeline card inside it; split pane + macOS dock / liquid glass with big real icons; PiP card + 2–3 GitHub doc cards under it; progress bar *below* the card, after the rows.
