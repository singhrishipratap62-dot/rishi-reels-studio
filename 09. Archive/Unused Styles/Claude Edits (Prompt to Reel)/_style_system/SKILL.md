---
name: prompt-to-reel-style
description: Build 9:16 reels in the "Prompt-to-Reel" style — dark Claude-like app UI showing a slash command typed, then the generated visual, view counters, and a Comment-WORD CTA; or talking-head effects reels with a numbered effects list.
version: 1.1
---
# Prompt-to-Reel Style — operating instructions

**Brand: @rishi.docx. Always apply BRAND_SKIN_RISHI_DOCX.md — it overrides the reference colours/fonts in DESIGN_SYSTEM.md.** Never use this skin for gradnext reels (those use the gradnext design system).

Read first: BRAND_SKIN_RISHI_DOCX.md → DESIGN_PHILOSOPHY.md → DESIGN_SYSTEM.md (tokens) → COMPONENT_LIBRARY.md / LAYOUT_LIBRARY.md / MOTION_LIBRARY.md. Check with QUALITY_CONTROL.md before delivering. References: VISUAL_REFERENCE_LIBRARY.md (+ contact_sheets/).

## 1. Interpret the brief
- What is being shown off? A set of N outputs (prompts, skills, effects, explainers). N drives the counter and the CTA grid.
- Is there talking-head footage? Yes + many quick effects → **Family B (T-B)**. Outputs/demos with no face, or a clip being transformed → **Family A (T-A)**.
- CTA keyword (single UPPERCASE word) and what they get ("the link", "all 6", "every prompt").

## 2. Plan (before building)
Write a beat sheet: per demo → slash name, one-line description (for C04), label stack text, the number that animates, and whether it breaks out full-bleed (max 1 per 2 demos). Target length: A = 4–5 s × N + 3.5 s CTA; B = ~1 s × N + 2 s hook + 3 s CTA. Get approval if the user is present.

## 3. Build
- Canvas 1080×1920, 30 fps. Use rishi.docx skin tokens verbatim; never invent new chrome colours. Start from mockups/rishidocx_prompt-to-reel_frame.html.
- A: L01 compose (M01, M02) → M03 send → L02 (M04, M05) → L03 payoff (M07 caption, M08 count, M09 tick) → optional L04 breakout → next demo. End L08 (M12/M13).
- B: L05/L06 with persistent C13 list + C14 badge; hard cut each effect (M14); caption = effect name or keyword in yellow; mid-video pull-back (M15); end with CTA.
- Outputs inside cards can be any style — make them rich; chrome stays quiet.
- Build in HTML/CSS/JS (Motion artifact / Remotion / HyperFrames) — implementation method is free; the look is not.

## 4. Verify
Render stills at 0.5 s, each demo payoff, and CTA; compare against R01-3.2, R05-7.5, R06-20.5 boards; run QUALITY_CONTROL; list deviations and fixes.

## 5. Updating the system
New refs → add as R07+, extract 1 fps sheets, compare to DNA, add components only if seen ≥ 2× (else mark experimental), bump version in CHANGELOG. Never change core DNA (quiet chrome, single signal accent, prompt-first hook, counters, Comment-WORD CTA) without the user's decision.

## Decisions
1. Brand: rishi.docx skin (decided 2026-11-02).
2. Fonts: rishi.docx fonts — Bricolage / General Sans / Gambetta italic (decided).
3. Light mode: undecided — ink and paper mockups made for comparison.
4. Open: keep Gambetta italic sub-line or swap to General Sans?
