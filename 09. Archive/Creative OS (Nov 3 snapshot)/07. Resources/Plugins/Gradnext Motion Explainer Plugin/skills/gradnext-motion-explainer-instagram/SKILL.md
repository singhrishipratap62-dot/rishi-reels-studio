---
name: "gradnext-motion-explainer-instagram"
description: "Turn any topic, image or Instagram post into a gradnext motion-graphic reel package: voiceover script, figure check and visual cue doc. Learns from the user's edits when asked to update."
---

# gradnext motion explainer (Instagram)

When the user gives a topic, an image, a post link, a PDF or any source and wants it turned into an explainer reel, produce the whole package below on your own. Do not ask clarifying questions first. State any assumption in one line at the top of your reply. Ask only if the source is unreadable or has no usable facts.

The package is ONE Claude doc (use the docs skill; create the title, a date-chip byline and one pending block per section BEFORE any research, open it, then fill one section per call). Title: "Reel: <topic> script and motion graphic cues". Byline is the date chip only, no author mention. End with up to three anchored comments (with suggested replies) only where a real choice or guess is open, then a one-line hand-off.

## Doc sections, in order
1. **Voiceover script** (final, TTS-ready), then one line: word count, runtime at 2.6 words a second, and what was fixed.
2. **Figures check**: a short lead, then a table with columns Figure | In the source | In this script | How it is worked out. List every derived or refreshed number with its arithmetic and source links. Say which source figures were not refreshed and why that is safe.
3. **Scene-by-scene visual cues**: table with columns # | Start | VO cue (first words) | Visuals and motion | On-screen text. One scene per beat, start times estimated from cumulative words at 2.6 words a second. Note that the final edit is keyed to the SRT.
4. **Look and motion notes**: canvas, type, chart behaviour, easing, numbers, captions, sound.

## Reading the source
- Instagram posts are behind a login wall. Open the post in the browser pane, read the meta description and image alt text with JavaScript, take the image URLs (naturalWidth 1000 or more), open each image URL directly and screenshot it to read the slide. Never log in or create an account. Say which slides you could and could not see.
- Take the look (palette, type, layout, footer style) from the supplied image or post. gradnext design system only; never use another brand's or a personal account's styling and never mention the user's personal accounts.

## Script rules
- Length: about one minute, roughly 140 to 165 words. Put detail figures on screen, not in the voice. The voice carries the hook, the key numbers, the reveal and the takeaway.
- Open on the shock stat in a conversational line (for example "Do you know ... ?" then the twist "Or does it?").
- Set up before payoff. Establish the baseline before showing a change (for example show where a country ranks before saying it moved). Every claim in the voice must already be shown or stated earlier.
- Go straight to the end point the viewer cares about (for example year-ten pay or the ten-year total). Skip step-by-step breakdowns of how you get there (career levels, promotion timings, sub-steps) in the voice; they can sit on screen if needed.
- Do not name a specific institution, firm or person in the voice when a generic label works (for example say "a tier one MBA in India", not the campus name). Keep the exact name in the figures check.
- No analogies of any kind. Define terms directly and plainly.
- Never use the "don't just look at X, look at Y as well" construction (or close variants such as "don't just compare X, compare Y"). The user rejected it; state the point directly instead.
- Writing style (borrowed from the gradnext primer scripts, style only): reads as human-written, flowing medium-length sentences, very short sentences only occasionally. No AI giveaways such as "Here's the thing", "Let that sink in", "It's not X, it's Y", constant triplets, em dashes or dramatic one-line paragraphs. Do not open sentences with "Most" often and do not repeat the same transition word.
- Audio-ready: numbers, money and percentages in words (years may stay digits), no symbols or brackets except audio tags, British spelling, "per cent", gradnext in lower case. Spell acronyms letter by letter for speech ("M B B", "D M") and write an unfamiliar acronym out in full on first use.
- Add one to three ElevenLabs audio tags in square brackets at turning points, for example [thoughtful]. Nothing else in brackets.
- Deliver the voiceover as one continuous block with no headings or stage directions.
- Call to action: every script ends with the spoken line "Follow for more consulting insights." The closing card shows the same words. No other spoken call to action.
- Caveats are not spoken. They go on screen as small chips such as Self-reported, Before tax, Snapshot date.

## Figures rules
- Any time-sensitive figure (exchange rates, prices, rankings, headcounts) must be searched and checked on at least two live sources before use. Recompute everything that depends on it and say which figures do not change and why.
- Keep the source's caveats (self-reported, estimated, illustrative, small sample) and carry them to the on-screen chips.
- Flag inconsistencies inside the source (for example a slide and caption that disagree) instead of silently choosing.
- When the voice states a derived figure that the source does not (for example a year-ten value), show the arithmetic in the table.

## Visual cue rules
- Format 1080 by 1920, 30 fps. Background is the supplied loop `assets/gradnext-background-loop-9-16.mp4`; navy text and gradient bars, periwinkle as the single highlight per scene, pale lavender plates with a very subtle corner radius (no pills). gradnext wordmark top right; **no topic tag** (it reads as AI design). Headline in bold sans with one italic serif phrase per scene at most.
- Use one persistent chart whose bars change length and order; never cut between separate chart screens.
- Every element enters with motion: text word by word (slide up out of a blur), headlines line by line, bars with ease in-out, colour changes as right-to-left gradient wipes, hero numbers dropping in and counting up, key figures under a bold half-height highlighter. Key numbers hold at least 0.4 seconds.
- Captions word by word from about 1.0 s in the lower safe-zone band, clear of the chips. Hook, first bars and wordmark sit inside the centred 4:5 crop.
- Sound: every on-screen event except captions gets a quiet, peak-aligned cue from the Minimal Edit Style library (see MOTION_PRODUCTION.md).
- Closing card text: "Follow for more consulting insights", with *consulting insights* highlighted.

## Building the video
When the user supplies the voiceover and asks for the video, follow `MOTION_PRODUCTION.md` (Tesseract pipeline, look, motion vocabulary, sound design, known pitfalls, review checklist). Start from `templates/build_reel.py` and the assets in `assets/`. After each review round, add the user's notes to `FEEDBACK_LOG.md` and fold lasting rules into `MOTION_PRODUCTION.md`.

## Reference example (user-approved, October 2026)
Hook and flow: "Do you know McKinsey India pays under a fifth of the United States. Or does it? ..." then the pay in both countries, India last of six at market rates, purchasing power defined directly, India climbing from sixth to fourth, and the closing takeaway "So before comparing a salary in dollars, compare what it can buy." The user added a [thoughtful] tag before the reveal.

## Self-learning (when the user says to update the skill)
After you deliver a package the user may edit the doc or reply with changes, then say "update the skill" (or similar). Then:
1. Re-read the latest version of the doc and the whole conversation.
2. Compare what this skill produced with the user's final version and requests: wording they replaced, lines they cut or added, structure and length changes, new tags, corrected facts, rejected ideas.
3. Turn each repeated or clearly stated preference into a short, general rule. Do not store one-off topic facts.
4. Call propose_skills with kind "improvement", target "gradnext-motion-explainer-instagram", carrying the COMPLETE updated SKILL.md. Merge new rules into the right section, resolve contradictions in favour of the newest instruction, keep everything still valid, and add a dated line under "Learned changes" below.
5. Tell the user in one line what changed.

## Learned changes
- 2026-10-28: first version, built from the PPP pay reel (script cut from 285 to about 165 words, analogies banned, baseline-before-change rule, refreshed exchange rate, audio tag added).
- 2026-10-28: from the 2.8 crore reel feedback: every script ends with the spoken CTA "Follow for more consulting insights." (replaces the earlier on-screen-only DM MBB card); use generic labels instead of institution names; skip career-level or step breakdowns and go straight to the end-point figures.
- 2026-10-28: the "don't just look at X, look at Y" speech pattern was tried and rejected; never use it.
- 2026-11-03: from the R003 video rounds: added MOTION_PRODUCTION.md, FEEDBACK_LOG.md, templates and assets. The topic tag was removed; the supplied background loop, word-by-word blur reveals, ease in-out gradient bars, right-to-left colour wipes, bold half-height highlighters, subtle corner radii and Minimal Edit Style sound design are now standard.