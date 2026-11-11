# Sound Design for AI Edits
### How Claude does sound when it can't hear

*by @rishi.docx*

Sound is where most AI edits fall apart, and it's what made mine feel premium. The catch: **Claude can't listen.** So the whole system is built on rules and measurement, with your ears as the final check.

---

## The one rule: lots of sound, each one quiet
My first attempt had about 27 sound effects in a 30-second edit. It felt thin. The version I approved had over 100, and a later reel had about 170 in 33 seconds. It still doesn't feel busy, because **the more often a sound plays, the quieter it is.**

## The cue map (what gets a sound)
| On screen | Sound | Level in the mix |
|---|---|---|
| Key caption word appears | short hi-tech click | the loudest small sound |
| Every other caption word, list row, line of text | very soft flick | very quiet (10+ dB under the click) |
| Big transition (scene change, zoom, panel sliding in) | long, smooth swoosh | medium |
| Card or block lands | small pop | quiet |
| Tick, checkmark, dot | tech pop | quiet |
| Highlight or line drawing | highlighter / marker swipe | quiet |
| Progress hits 100% | riser + tick | medium |
| Button press, keyboard | click / key sounds | quiet |

Skip a flick if a bigger sound is playing within about a tenth of a second. Stacked sounds turn to mush.

## Timing tricks that matter
- **Line up the sound's loudest moment, not its start**, with the visual. A whoosh file often peaks half a second in; if you start it on the move, it lands late.
- **Swooshes peak in the middle of the movement**, with a soft fade in. I asked for "longer and smoother" swooshes, and short sharp ones felt cheap.
- **First 5 seconds slightly louder** (about +3 dB on effects), easing back by 6 seconds. The hook needs energy.
- **Nothing on exits.** Sound on things arriving, silence on things leaving.

## Levels
- Voice is king. Effects sit under it.
- If you add music, keep it well under the voice. One of my series uses about 13 dB under; I tried 21 dB and it vanished on a phone.
- Final loudness for Instagram: around **−14 to −16 LUFS**, true peak at or below −1 dB. Measure the **final exported video**, not the separate tracks. Trimming pauses alone changed my loudness by 3 dB.
- Clean voice chain if your audio is raw: cut the low rumble (high-pass around 75 Hz), gentle compression, then a limiter.

## How to check when Claude can't hear
1. **Effects-only export:** mute the voice and export just the sound effects. Claude checks each sound happens within about 60 ms of when it should.
2. **Cue sheet:** time · sound · level · reason. You can scan it and spot "why is there a pop here?"
3. **Separate files:** SFX-only and voice-only MP3s make it easy to hear problems.
4. **Your phone.** Always listen on a phone speaker and on earphones. That's the real test, and it's yours, not Claude's.

## Build a small library
You don't need thousands of sounds. About 15–20 good ones cover everything: 2 clicks, 2 flicks, 3 swooshes/whooshes, 2–3 pops, a highlighter, a riser, a few UI clicks and key presses. Name them clearly, and ask Claude to measure each file's peak once so levels are right every time.

---

## Prompt
> Do the sound design for this approved edit. Rule: lots of sound, each one quiet; the more frequent a sound, the lower its level. Use my library: [list files]. Map: click on key caption words, soft flick on other words, long smooth swoosh peaking mid-move on big transitions, pop when cards land, tech pop on ticks, nothing on exits. First 5 seconds +3 dB. Align each sound's peak to the visual moment, not its file start. Final mix −15 LUFS, true peak ≤ −1 dB, measured on the export. Give me a cue sheet (time · sound · level · reason), an effects-only check, and tell me exactly what to listen for on my phone.

*@rishi.docx*
