# PLACEMENT.md — when she uses a graphic vs plain A-roll (A8)

> **A10 adaptation for Rishi's edits:** no memes (K12/K13), no today-card (K22), no b-roll unless asked (K14). Where she cuts to a meme, Rishi stays on A-roll (or K03 only if he asks). Expect a little less graphic coverage than her ~50 %; aim for ~40–45 % unless the plan says otherwise. Captions sit below his chin.

Data: INDEX.md segments joined to `work/transcripts/vid-N.srt` (`work/a7/place.py`). SRT lines are sentence-level, so word timing is approximate (±1 s).

## Numbers
| | value (15 videos) |
|---|---|
| non-A-roll share of runtime | **~50 %** (range 39–57 %) |
| cutaways per minute | **~11** (7–13) |
| graphic length | median **2.0 s**, middle half 1.5–3.3 s; long ones (6–15 s) only for article reads, lists and counters |
| A-roll stretch between cutaways | median **~2.8 s**; longest usually **6–9 s** (v1 intro 17 s is the only exception) |
| first graphic | ≤ 3 s in 12/15 videos (median 1.1 s); v1 and v8 hold A-roll for ~5.8 s |
| 0–5 s covered by graphics | median **~66 %** (0–90 %) |
| outro | last graphic ends 1–10 s before the end; video always ends on plain A-roll (no end card except series → K18 end-card) |

## Structure of every video
1. **Hook (0–~8 s):** 0.5–1 s of A-roll + K01 caption on the first words, then the hook claim visualised full-screen (K04 + K06/K16/K11), usually the key number as the big word ("Billions of Dollars", "$14,000 → $200,000", "Lewis HAMILTON"). Often a K12 meme or K03 mono-beat right after the hook line as a reaction.
2. **Intro (≈"Hi, I'm Asma, and I research/talk about things I find fascinating…"):** plain A-roll with K01, **no graphic** (3–6 s).
3. ~~"And today…" K22 today-card~~ (dropped in A10; the topic line stays on A-roll).
4. **Body:** repeating cell of ~6–8 s: fact graphic (2–4 s) → A-roll 2–3 s (K02 return) → meme / beat (1–2 s) → A-roll. Graphic types rotate; no type repeats more than twice in a row.
5. **Thesis / outro (last 10–25 s):** fewer graphics; one closing K06 that restates the thesis literally (stairs "the tech is really moving", keyboard "Ctrl + d"), optionally K18 quote-card with the key line, then plain A-roll to the end.

## What triggers what (SRT line → key)
| line contains | she uses | example |
|---|---|---|
| a number, money, %, date, stat | K04 with the number as the big word, inside K06/K11/K16 | v15 "60 trillion won" → map with cash towers |
| a person or brand named for the first time | K07/K08 cut-out or face-sticker + name (K05 gold tag or pennant name); products → K19 if she keeps talking | v7 "Mark did something very interesting" → Zuck sticker + gold tag "Very" |
| "according to / reported / announced / said in an interview" | K15 article, highlight = the exact sentence she reads | v7 49–59 s Business Insider |
| a list ("send emails, fill forms, book trips") | K10 stack-in / K09 cursor, one item per spoken word | v7 32–36 s Muse Features cards |
| punchline, sarcasm, Hinglish aside, "imagine…", reaction | *(Rishi: plain A-roll)* · her: K12 mono-meme 1–2 s, often a Hinglish caps caption that *adds* a joke, not repeats the line | v15 "thanks to people investing…" → hamster "KYA BAAT KAR RAHAY HO" |
| her own sarcastic self-comment ("Congratulations", "Great decision") | K03 mono-beat with that one word | v4 11.5 s |
| a metaphor or "imagine" picture | literal illustration in K06 with K07 avatar | v7 "fat person floating on a device" |
| years in a story | K20 timeline-rail on A-roll (she stays on camera) | v13/v14 |
| a real-world place/product/event she describes visually | K14 colour b-roll, rapid cuts | v5 car, v9 anime |
| the thesis/quote of the video | K18 quote-card (last 15 s) | v2 133 s |

## What stays plain A-roll
- The "Hi, I'm Asma…" intro and the closing question.
- Opinion / bridge sentences that set up the next fact ("Considering all of this is coming from Meta, it sounds a bit terrifying.", "Very useful, but also very scary.").
- The sentence just **after** a graphic, so the viewer sees her react (A-roll returns with K02).
- Rule of thumb: if a line has no number, name, quote, list or joke, it is A-roll.
- Never more than ~8 s of A-roll in the body.

## Graphic timing relative to speech
- Graphics cut in **on the trigger word** (or 2–3 frames before it) and cut out on the first word of the next sentence; they rarely span more than one SRT sentence unless it is a list/article.
- Memes cut in **right after** the punchline word, last ~1–1.5 s, and the next A-roll sentence starts over/after them.
- Text inside a graphic follows the VO word-by-word (A2); the big word turns ink exactly when it is spoken.
- K01 captions are only on A-roll. During graphics the caption is replaced by the graphic's own headline; during memes by the meme caption; during K03 by nothing or one word.

## Hook vs body density
- Hook (0–8 s): ~1 cut every 1–1.5 s, ≥ 60 % covered, most graphic-dense part of the video.
- Body: ~1 cut every 5–6 s, ~50 % covered.
- Outro (last 10–20 s): ≤ 1 graphic, mostly A-roll.
