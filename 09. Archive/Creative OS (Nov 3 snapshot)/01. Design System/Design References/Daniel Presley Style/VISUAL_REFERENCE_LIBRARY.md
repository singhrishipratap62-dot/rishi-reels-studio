# VISUAL REFERENCE LIBRARY — Daniel Priestley Editing Style (v1.0)

Private study material. Third-party frames — **never publish or put in outputs**.

## 1. How frames were captured (and limits)
- `tools/style_extract.sh`: one decode pass per video, 480×270 analysis; saves a frame at every scene change (ffmpeg scene score > 0.3) **and** at least every 4 s → `.work/R##/frames/` + `frames.log`.
- `tools/style_sheets.py`: cut stats (`cuts.json`); removes near-duplicate frames by perceptual hash (threshold 12 bits) so repeated talking-head angles collapse; tiles survivors 6×5 at 320×180 with mm:ss labels → `.work/R##/sheets/` + `index.csv`. 87 sheets in total.
- `tools/style_strip.py`: native-fps frame strips of 12 moments → `.work/strips/S01–S12` (timings in MOTION_LIBRARY).
- Four review agents read every sheet (R01–07, R08–15, R16–23, R24–28) and pulled ~40 full-res frames to read small text.
- **Limits**: sheets over-represent graphics and under-represent talking head; things that happen between 4 s samples without a cut (e.g. overlay entrances) may be missed; scene detection treats whiteboard+PiP as one long shot (inflates ASL in R26/R28); hex values from compressed YouTube video ±3–5 per channel; font names unconfirmed; only R22 has a transcript (whisper failed elsewhere: Metal/OpenMP blocked in sandbox; CPU retry took 19 min for one video).
- **Not viewed**: audio of any video (cannot hear); full motion of the 4-s-sampled stretches; YouTube end-screen overlays (not in the files).

## 2. Stills index (`stills/`)
| File | What |
|---|---|
| P01_R22-0006 | Serif title "Obsessed" behind subject, cooled background |
| P02_R01-0100 | Name sting black diagonal band |
| P03_R24-0046 | Name card on cream, crimson/blue letter tint |
| P04_R24-0048 | Chapter card "1 / Product with Proof", title mid-reveal |
| P05_R22-0050 | Quote panel wiped up over whiteboard PiP |
| P06_R22-0053 | Whiteboard + PiP with blue glow |
| P07_R18-0003 | White name pill on guest clip |
| P08_R24-0100 | Blue chip row "You did something:" |
| P09_R16-0359 | Red pill stack "Product Ecosystem" |
| P10_R24-0144 | Iris spotlight + neon "-$500,000" |
| P11_R18-0089 | B-roll card + PiP with "Example 1" pill |
| P12_R20-0225 | Principle (book-page) card |
| P13_R05-0905 | Quote card full-screen |
| P14_R22-0254 | Light-leak transition |
| P15_R16-0047 | Chapter card sliding up over A-roll |
| P16_R05-0901 | List + PiP with word-building bullets |

## 3. Animation strips (`.work/strips/`)
S01 name sting (R01) · S02 name sting + arc wipe (R24) · S03 behind-subject title (R22) · S04 bullets → quote card (R05) · S05 chips (R24) · S06 kinetic title + name-pill montage (R18) · S07 B-roll card + PiP (R18) · S08 light leak (R22) · S09 bullets (R01) · S10 iris + neon stat (R24) · S11 pill stack + whiteboard draw-on (R16) · S12 glitch (R22).

## 4. Transcript
`.work/tx/R22.json` (whisper base, word-level JSON). Beat map in EDITING_PSYCHOLOGY §1. Base-model errors likely (e.g. "Emigried" for a name at 00:06) — never quote as fact.

## 5. Reference stats (from `cuts.json`)
| ID | Title | Dur | Cuts | ASL s | Median shot s | Cuts in first 30 s |
|---|---|---|---|---|---|---|
| R01 | The 5 Laws of Microeconomics To Make Your First $1 Million | 33:25 | 210 | 9.5 | 5.87 | 6 |
| R02 | Sell a Business Someone Will Fight to Buy - My Playbook in | 22:11 | 213 | 6.22 | 4.96 | 11 |
| R03 | What I Learned From Being Around The Top 0.01% | 22:15 | 345 | 3.86 | 2.72 | 16 |
| R04 | 7 Unsexy Habits That Build a $1 Million Business | 21:39 | 258 | 5.02 | 3.36 | 17 |
| R05 | Why You Must Stop Selling Your Time for Money | 16:24 | 152 | 6.43 | 4.04 | 12 |
| R06 | Why You Must Master Hiring in the Age of AI | 15:50 | 80 | 11.73 | 7.44 | 7 |
| R07 | Why You Must Build a YouTube Channel | 21:29 | 176 | 7.28 | 4.6 | 7 |
| R08 | 25 Years of Money Advice in 31 Minutes | 31:43 | 360 | 5.27 | 3.88 | 14 |
| R09 | Why You Must Build a Personal Brand | 17:57 | 146 | 7.33 | 5.2 | 12 |
| R10 | The New Rules of Business (AI Changes Everything) | 18:38 | 183 | 6.08 | 3.88 | 11 |
| R11 | Business Advice You Must Know at Every Level | 18:12 | 159 | 6.83 | 4.28 | 12 |
| R12 | The $1 Million Opportunity Hidden in ChatGPT | 9:24 | 82 | 6.81 | 4.96 | 9 |
| R13 | Business Is Easy After You Achieve Product Market Fit | 15:42 | 122 | 7.66 | 5.16 | 5 |
| R14 | The Marketing Strategy for $1 Million in 2026 | 9:56 | 76 | 7.75 | 5.6 | 8 |
| R15 | Don't Set a Business Goal For 2026 (Until You Watch This) | 18:21 | 100 | 10.9 | 8.12 | 12 |
| R16 | Exactly How to Build a Highly Profitable Lifestyle Busines | 17:19 | 184 | 5.62 | 3.4 | 9 |
| R17 | 25 Years of Sales Knowledge in 34 Minutes | 34:01 | 198 | 10.26 | 6.24 | 12 |
| R18 | How to Get Attention from Rich People | 19:21 | 124 | 9.29 | 5.4 | 9 |
| R19 | How to Become Famous in Your Industry (and Make $1 Million | 15:46 | 127 | 7.4 | 4.2 | 12 |
| R20 | How to Generate So Many Leads, You Can Double Your Prices | 20:55 | 188 | 6.64 | 5.64 | 10 |
| R21 | Trust Me, You Want a Highly Profitable Lifestyle Business | 11:41 | 85 | 8.16 | 6.2 | 9 |
| R22 | The Entrepreneur Mindset： How to Become Obsessed | 8:09 | 100 | 4.84 | 3.56 | 9 |
| R23 | The $1 Million Landing Page (Works For Normal People) | 11:59 | 76 | 9.35 | 5.16 | 10 |
| R24 | Everyone Who Uses This Playbook Makes $1 Million | 22:02 | 203 | 6.48 | 4.76 | 12 |
| R25 | Winners Move Fast - Here's How to Stop Overthinking | 10:41 | 79 | 8.02 | 3.96 | 10 |
| R26 | Why You Must Become an Entrepreneur | 14:08 | 37 | 22.32 | 2.72 | 7 |
| R27 | AI Will Make You a Millionaire - Here's How | 9:25 | 67 | 8.32 | 6.34 | 8 |
| R28 | Give Me 29 Minutes and I’ll Teach You to Make $1 Million | 29:40 | 85 | 20.71 | 7.77 | 9 |

Median ASL across 28: 7.4 s; range 3.86–22.32 s
