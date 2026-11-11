# Reverse-Engineer Any Editing Style with Claude
### The method I use to turn reference reels into a style Claude can follow

*by @rishi.docx*

I've broken down seven editing styles this way. Here's the method, without the shortcuts that waste your usage.

**Before you start:** a style you study is a starting point, not a destination. The first full style I built copied one creator closely, and my first edit with it looked generic. Use this to learn *how* a style works, then make it yours (see "Teach Claude Your Taste").

**And:** other creators' frames are for your private study. Don't post their footage, faces or graphics.

---

## Step 0: Decide before you analyse
Answer these first and write them down (Claude should ask you):
- What exactly do you want to copy? The whole look, or just captions / motion / sound / pacing?
- How strictly? Exact clone, core fixed with room to vary, or loose inspiration?
- Your brand: your own colours and fonts instead of theirs?
- What kind of video is it for? Talking head, AI voiceover, split screen, podcast?
- Language? (Hinglish: Roman script only.)
- What will you build with? Your editor (CapCut/Premiere), or Claude building it directly?

## Step 1: Collect 7–20 references
The best reels from one creator, in one style. More isn't better past ~20. Include any tutorial where they explain their own process.

## Step 2: Turn video into something Claude can read cheaply
Claude reads images, not motion, and video eats usage. So:
- **Contact sheets:** one image with 12–30 small frames in order (one frame every 1–2 seconds, or one per scene change). This is what Claude studies.
- **Motion strips:** for an animation you love, take 1–2 seconds at full frame rate and tile those frames into one image. Claude can measure the timing from that. Only 1–2 examples per animation type.
- **Transcripts** with timestamps for each reel, so Claude can see *which words* trigger *which visuals*.

Tip: do the frame extraction on your computer (free tools like ffmpeg do it in one line; Claude can write the command for you). On one style, 2,222 frames became 82 contact sheets.

## Step 3: Analyse in layers
Ask Claude for one layer at a time, and to mark guesses as guesses:
1. **Captions:** fonts (closest free match), sizes, position, words at a time, emphasis, how words appear.
2. **Colours and look:** palette, backgrounds, textures, corners, shadows.
3. **Scene types:** discover them from the reels, don't start from a preset list. Name each one, describe it, note when it's used and how often.
4. **Motion:** each animation with start, end, duration and feel. Measured from strips where possible.
5. **Placement:** which kind of line gets which scene (numbers → counters, names → name tags, lists → stacked cards, opinions → just the face).
6. **Pacing:** how much of the video is graphics, how soon the first one appears, the longest stretch of plain face, cuts per minute.
7. **Sound:** Claude can't hear, so measure: when sounds happen relative to visuals, how loud, how often. Then you listen and correct.

Example numbers from one style I studied: about half the runtime was graphics, ~11 cuts per minute, graphics lasted ~2 seconds, the first one appeared within 3 seconds in 12 of 15 reels.

## Step 4: Sort what's core from what's occasional
- **Core:** appears in most reels. This defines the style.
- **Optional:** appears sometimes; use when it fits.
- **Experimental:** seen once. Don't let one reel rewrite the style.

## Step 5: Write it up as a small pack
- **Rule book:** the numbers: sizes, spacing, timing, pacing, when to use what.
- **Look book:** what it looks like: colours, shapes, scene examples.
- **Scene menu:** each named scene, when to use it, how it moves.
- **Lessons:** empty at first. Every correction you make goes here and outranks everything else.
Keep a short index Claude reads every time; open the detailed parts only for the scenes you're using.

## Step 6: Test it on a real video
Edit one short clip with it. Expect 60–70% right. Your corrections are where the style becomes usable, and where it starts becoming yours.

---

## Save your usage
- Contact sheets, never full videos or hundreds of single frames.
- New chat for each step, with a plan file Claude updates ("continue from the next unchecked step").
- Use a stronger model for the analysis and style decisions, a faster one for sorting and repetitive work.
- Do heavy file work on your computer, not in the chat.

## Prompt to kick it off
> I want to reverse-engineer an editing style from reference reels. Before analysing anything, ask me: what to copy, how strictly, my brand colours/fonts, the video type, the language and how I'll build it. Then, one layer at a time from my contact sheets, strips and transcripts, work out: captions, look, scene types (discovered, not preset), motion, which lines trigger which visuals, pacing, and sound by measurement. Mark every claim as seen, measured or guessed. Separate core from optional. Finish with a rule book, a look book, a scene menu and an empty lessons file.

*@rishi.docx*
