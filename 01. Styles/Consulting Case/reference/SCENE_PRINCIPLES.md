# SCENE_PRINCIPLES (v1.5)
Reference only: SKILL.md wins on any conflict.
Only four scene types exist in the references. Don't invent more.

## S1 Hook (0 → end of hook question, ~2.5–3.0 s) [OBS R1 0:00–3.0, R2 0:00–2.47]
Top white panel: header, case photo, the question in text, MBB logo strip. Bottom: full-bleed raw face, caption word-by-word.
The spoken hook = "How do you price X?" — the panel question is that sentence verbatim.
Mistakes: card/glow on face in the hook; missing logos; photo that doesn't show the object literally.

## S2 Punch-in (credibility line, ~1.8–2.0 s) [OBS R1 3.0–4.84, R2 2.47–4.30] [R1.0]
Full-screen raw at a tighter crop (~1.25–1.35x, mic visible at bottom-right, hands in frame). No graphics, NO caption. Hard cut in and out. [R1.13, R1.14] Inside S2 the frame settles from 110% to 100% over the whole span: centred, sine ease-in-out, sub-pixel (engine/s2zoom.py; R1.14 replaced R1.13's cubic ease).
Only on "This is a real BCG/McKinsey/Bain case (interview)". Exactly once.

## S3 Board scene (main body, ~85–90% of runtime)
Background = gradnext loop video [R1.17], board card top, caption middle, face card bottom. Board builds per beat (see DESIGN_SYSTEM Board grammar). Hard cut from S2 into S3 with the board EMPTY (white card + header only) for ~0.3 s, then content starts building with the next words. [OBS R1 4.84]
Phase switch to SOLVE on "So how do we price it?" — board clears (fade out ~0.3 s), question box re-centres, tabs appear on "I'd price it in N ways", one tab per method.

## S4 End card (last ~3 s, on "This is part NN of solving real consulting cases. Follow for part NN+1.") [OBS R1 1:41–1:44]
Board content replaced by the end card (no "gradnext", no header; see DESIGN_SYSTEM) [R1.9, R1.17]. "Follow for Part NN+1" pill pops in on the word "Follow". Video ends ~0.3–0.5 s after the last word. No black.

## Share of runtime [EST R1]
S1 2.6% · S2 1.7% · S3 ~93% · S4 ~3%.
