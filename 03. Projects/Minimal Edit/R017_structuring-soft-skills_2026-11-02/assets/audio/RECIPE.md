# voice_clean_v1.wav
Source: `assets/source_clip.mov` audio (episode 00:38:20.330 onward, 49.0 s, PCM 48 kHz), same clock as the footage.
1. highpass=f=75:p=2 (rumble)
2. acompressor threshold=0.063 (≈ -24 dBFS), ratio 2.5, attack 15 ms, release 180 ms, knee 4
3. volume=+13 dB, alimiter limit=0.84 (≈ -1.5 dBFS), attack 5 ms, release 60 ms
Output 48 kHz 24-bit mono. No noise reduction (pause floor measured at -61.6 dB RMS); no de-reverb.

# music_bed_v1.wav
Original composition, generated locally by `.tesseract-work/music.py` (no samples, no third-party audio). It's the user's own; there's no licence restriction.
- Style: documentary / Johnny Harris-style explainer score. 96 BPM, D minor, Dm–Bb–F–C one chord per bar, resolving to F major at "not work out".
- Layers:
  - Detuned additive pad.
  - Pluck arpeggio with ping-pong delay: 8ths in the intro, 16ths from the white scene on.
  - Sub on the chord roots and ticking 16th hats, in the graph and stages scenes only.
  - Noise and sine riser into the 30% reveal, with a low hit on it.
  - Synthetic 2.2 s hall.
- Pre-ducked up to −5 dB under the edited voice (50 ms RMS sidechain, 40 ms attack / 350 ms release).
- Then a 40 Hz 24 dB/oct high-pass. 48 kHz stereo, on the edit clock (0 = first frame).
