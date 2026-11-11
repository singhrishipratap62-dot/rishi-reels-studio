# SOUND DESIGN: Rishi's Editing Style (v1.0)

Hard rule: Claude cannot hear. Every number below was **measured** from the reference reels' audio (onset detection on the full mix). **What the sounds are (whoosh, click, pop, riser) was never verified** and is never claimed. Sound is built only after Rishi approves the visuals `[R1.0]`.

## 1. What was measured and how
Per reel (`audio.json`): strong onsets in the full mix (time, duration, attack, spectral centroid, peak), cut↔onset alignment (±100 ms), rms percentiles. Music cannot be separated from SFX in a full mix, so "music bed" is an estimate from the rms floor. Source: `SYNTHESIS.md` §7 (15 reels).

## 2. Results (medians across 15 reels)
| metric | median | range | tag |
|---|---|---|---|
| strong onsets per second | ≈ 0.42 | 0.29 (V10) - 0.58 (V06) | [MEAS] |
| cut↔onset hit rate (≤ 100 ms) | ≈ 0.18 | 0.0 (V04, V08, V14) - 0.33 (V15) | [MEAS] |
| cue length | ≈ 590 ms | 571-604 ms | [MEAS] |
| cue attack | ≈ 226 ms | 104 ms (V02) - 447 ms (V13) | [MEAS] |
| spectral centroid | ≈ 2.4 kHz | 2.2-2.7 kHz | [MEAS] |
| cue peak | ≈ −3 dBFS | −2.1 to −4.1 | [MEAS] |
| mix rms p10 / p50 / p90 | −30.4 / −19.6 / −13.2 dB | ±1.5 dB between reels | [MEAS]; bed = "music" [EST] |

## 3. Where cues sit (patterns)
| event | pattern | evidence |
|---|---|---|
| hard cuts | mostly **dry**; about 1 in 5 carries an onset within ±3 f; chapter-opening cuts are the likelier ones | [MEAS] V15 3/10 (Second / Finally / deadline cuts), V09 2/10, V10 2/9 |
| split-pane moves | onset at or just before the move start in about half the cases | [MEAS] V14 3/6 within ±3 f |
| card / panel entrances | onsets within ±15 f of the entrance | [MEAS] V04 9/21 |
| counters / counts | onset at the count start (±4 f) | [MEAS] V07, V09, V15 |
| keyword typing + send | cluster of onsets in the last 2.5 s | [MEAS] V13 (5 onsets) |
| long-attack onsets (≥ 400 ms) | often begin before a move; swell-like [INF] | [MEAS] |
Principle: sound marks **new information** (a card, a number, a keyword), not **new shot**.

## 4. Rules for the edit skill
1. Build sound last, after the visual approval.
2. Target ≈ 0.4 cues per second over the whole reel (e.g. 22-30 cues in 60 s); denser in the hook and chapter openings, sparse in calm stretches.
3. Cues attach to: split-pane drops/expands/lifts, hero-card settles, counter starts, price/strike moves, keyword typing and the send click. A cue on a chapter-opening hard cut is allowed. Ordinary jump cuts stay dry.
4. Two cue families, defined by **function** (not by what a reference used):
   - *move cue*: soft, long attack (≈ 200-450 ms), ≈ 0.6 s long, centroid ≈ 2-3 kHz: pane and hero-card moves, counters.
   - *entry cue*: short attack (≤ 60 ms), ≈ 0.3-0.6 s: toasts, small cards, typing/click.
5. Start the cue at the move start, or up to ≈ 3 f earlier for long-attack cues. Never after the move has finished.
6. Music: one quiet bed under the whole reel, ducked further under speech; no beat-synced cutting (the references do not cut to a beat).
7. Speech first: the voice stays the loudest element. Final integrated loudness −14 LUFS (`CLAUDE.md` export spec); true peak ≤ −1 dBTP *proposed*.
8. Never write "whoosh/pop/click" as a fact about a reference. Name library files by function (`move_soft_01`, `entry_short_01`, `type_tick_01`, `send_click_01`).

## 5. Asset state at v1.0
| item | state |
|---|---|
| `assets/sfx/` | empty |
| `assets/music/` | 1 file: `Background music.mp3` (≈ 25 min); suitability not assessed |
| cue library | none yet; Rishi supplies or approves files |
Until files exist, the plan's sound column lists cue positions only (time + family) and the build leaves them silent.

## 6. Listening step (Rishi, optional but recommended once)
Claude cannot hear, so to label the cue types Rishi can listen to these reference moments and tell Claude what each sounds like; the answers go into `LESSONS_LEARNED.md` as `[R1.x]` sound notes:
| reel | time (s) | what is on screen |
|---|---|---|
| V14 | 14.8 | split pane expands (onset ±1 f) |
| V14 | 48.8 | split pane enters (onset ±1 f) |
| V15 | 23.85 | hard cut into "Second," (onset −2 f) |
| V15 | 44.3 | hard cut into "Finally," (onset +2 f) |
| V13 | 46.6 | hard cut into the payoff line (onset +1.5 f) |
| V13 | 56.4-58.5 | comment sheet typing and send (5 onsets) |

## 7. Measuring your own mix (QC)
`ffmpeg -i exports/<id>.mp4 -af ebur128=peak=true -f null -` → integrated loudness ≈ −14 LUFS, peak ≤ −1 dBTP. Compare cue count per second to §2 (0.29-0.58 is the reference range).
