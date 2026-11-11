# DECISIONS: Rishi v2

> **History (v2.2, 2026-11-11):** fully compiled into `../SKILL.md` and `../reference/`; where each item now lives is in `RULE_AUDIT.md`. Kept for the why, not as a mandatory read.

> Defaults, not rules: a newer verdict from Rishi on a specific video beats anything here.

## Precedence (highest first)
1. Rishi's notes on the current video.
2. `[R]` verdicts below (and `LESSONS_LEARNED.md`).
3. This pack's tokens and recipes (`[S]`).
4. Source books: Minimal Edit Style → Rishi's Editing Style v1.3 → Daniel Presley → Paper Stage.

## Verdicts (roughcut_v3, 2026-11-08/09)
| # | Decision | Tag |
|---|---|---|
| D1 | Never create Claude artifacts. Review pages are local HTML (+ PNG). Builds are Tesseract | [R] |
| D2 | Options board before anything: ≥5 options per frame type; Rishi mixes them | [R] |
| D3 | Storyboard before every build and before every revision. Silence after a storyboard = approved, unless he said "storyboard only" | [R] |
| D4 | Captions: romanised Hinglish exactly as spoken, Inter only for Latin text, no Devanagari font | [R] |
| D5 | Caption style = Minimal serif hero (Playfair Bold Italic) + Inter support, white hero, bottom gradient kept, **no blue hero** | [R] |
| D6 | Captions centre-aligned, ≈22 characters per line max | [R] |
| D7 | Smoothness above all; slow eases are fine; pops/snaps are defects | [R] |
| D8 | Every card enters with the "line → rectangle + blur + small slide" reveal | [R] |
| D9 | White cards/screens use white → light-grey gradients + vignette, never blue tints | [R] |
| D10 | Subtle corners (tiles ≈8 px, cards 14–36 px) | [R] |
| D11 | Real logos (Claude, GitHub, Instagram), stored in `assets/logos/` for reuse | [R] |
| D12 | Rishi's face sticker is the avatar wherever a profile picture appears | [R] |
| D13 | Split screen: content + captions in the white pane, lifted off its edge; face shows the full hair line | [R] |
| D14 | Organic painted shape, not a circle ("a circle has no personality"), with many orbiting words | [R] |
| D15 | Behind-the-head graphics use the real person matte; no visible gap/oval | [R] |
| D16 | Wall scene: white "slop" tiles, one-word black Playfair captions inside the tile below the face | [R] |
| D17 | PiP: rounded corners, headspace cropped; one card stays, contents swap; return to full screen only after the line ends | [R] |
| D18 | CTA: comments sheet + full keyboard, face blurred above, one-word Playfair captions above "Comments", tap dot + green tick, sheet held to the last frame | [R] |
| D19 | Sound: dense but quiet (Minimal SFX), long smooth swooshes; deliver SFX-only + voice-only on request | [R] |
| D20 | Each draft in a new folder; previous drafts untouched | [R] |
| D21 | Investigations timeboxed to 2–3 min; structural changes need a feasibility report + approval | [R] |
| D22 | Browser GUI editor (official tesseract-editor) parked: needs Brave's File System Access flag or Chrome | [R] |
| D23 | **Every export is 1080p (1080×1920, 30 fps)**, including internal check renders. Never pass `--resolution 720p` | [R] |

## Rejected (don't bring back unless asked)
- Paper Stage as the main look (coloured floors, ink headlines everywhere, K-key menus).
- Text words on reaction beats ("nope.").
- Blue captions over light scenes; white captions on white tiles.
- Fade-pop / scale-pop entrances; snappy sheet/keyboard; sudden orbit words.
- A blank white beat of more than ~1 s between graphics.
- A separate behind-head scene for list beats when a PiP layout is already up (swap the card contents instead).
- Big rounded corners on tiles; circles as "illustrations".
- Face pushed too low in the split (a black bar, or cut off).
- Over-correcting small asks.

## Verdicts (Style Lab v1, 2026-11-09)
| # | Decision | Tag |
|---|---|---|
| D24 | Options boards always re-offer every previously liked option for a frame type (even beyond 5); best-liked first | [R] |
| D25 | Pack v2.1 adds R26–R50 + upgrades to R01/R02/R03/R05/R16 and soft caption exits (see MOTION_LIBRARY) | [R] |
| D26 | Accent colour is chosen per video from five tokens; default to `accent.duo` if unstated | [R] |
| D27 | Digits in Inter (or Playfair roman), never Playfair italic | [R] |
| D28 | Behind-the-head words/orbits only when the framing leaves room to read them | [R] |
- Rejected in Style Lab v1: blurred own frame as a ground, chapter marker, strike-then-replace, the window zoom-through motion.
