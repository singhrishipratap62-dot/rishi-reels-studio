# QUALITY_CONTROL (v1.5) — all must pass before export is reported
Reference only: SKILL.md step 8 is the mandatory summary. OCR caveat [E1.25]: qc.py counts reads shorter than 4 characters as unreadable and the S1 caption (y≈625) is outside its OCR band, so a reel can fail at ~83 % with every caption correct — read `qc_ocr.txt`; if every line is a correct script word, it passes. Tail check = last word END + 0.2–0.6 s; S1_END/S2_END read from crops.env [E1.21].
Automated by `engine/qc.py <proj> <final.mp4> <part> 1.2`; the rest is a look.
- [ ] 1080x1920, 29.97 fps, H.264 High, audio present. Every file in `04. Exports/Consulting Case/` for this reel is 1080x1920 [R1.18].
- [ ] Video and audio streams the same length (±2 frames); duration = speech + ≤0.5 s (÷1.2 on the final).
- [ ] `blackdetect=d=0.2` finds no black anywhere (esp. tail).
- [ ] `silencedetect=n=-45dB:d=0.35` finds no gaps inside speech.
- [ ] No retake/duplicate sentence survives (diff final transcript vs plan).
- [ ] Hook: header, question text == spoken hook, words darken as spoken, photo + real MBB logos, face full-bleed, caption centred in the white panel.
- [ ] Blur-in: hook panel blurred at 0 s, sharp by ≤1 s, face never blurred.
- [ ] Exactly one punch-in, on the credibility line, no caption, smooth 110 → 100 % settle.
- [ ] Scene cuts only at S1→S2 and S2→S3; board background = the gradnext loop video.
- [ ] Every board element appears within ±2 frames of its word.
- [ ] Caption one line, max 4 words / 680 px, centred; corrected words.
- [ ] Tesseract OCR every 2 s: captions readable and match words.json.
- [ ] Numbers on board add up (re-check arithmetic).
- [ ] End card shows Part NN and "Follow for Part NN+1"; no "gradnext" on the end card.
- [ ] Sound: SFX on animations only (none on captions); program −15 LUFS ±1, true peak ≤ −1 dBTP; music audible ~13 dB under the voice.
- [ ] Final is 1.2x; `_1x`, `_green`, `_raw` same frame count as each other.
- [ ] Contact sheet of the export reviewed.
