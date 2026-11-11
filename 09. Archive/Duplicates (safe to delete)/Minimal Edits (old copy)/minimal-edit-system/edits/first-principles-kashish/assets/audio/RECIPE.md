# voice_clean_v1.wav
Source: riverside_first_principles thinking in consulting_kashish_malhotra's .mp4, audio stream 0 (AAC mono 44.1 kHz), full length, starting at source 0 ms (same clock as the footage).
1. highpass=f=75:p=2 (rumble)
2. acompressor threshold=0.063 (≈ -24 dBFS), ratio 2.5, attack 15 ms, release 180 ms, knee 4
3. volume=+15.5 dB, alimiter limit=0.84 (≈ -1.5 dBFS), attack 5 ms, release 60 ms
Output 48 kHz 24-bit mono. No noise reduction (pause noise floor measured at -59 dB, clean); no de-reverb.
