# Teach Claude Your Taste
### How I edit my reels with Claude, step by step

*by @rishi.docx*

You saw the reel: the whole thing was edited with Claude. Here's the honest version of how. It took me weeks, a lot of rejected drafts, and one complete editing system I built and then threw away.

The short version: **Claude doesn't edit well out of the box. It edits well once you teach it your taste.** Without that, you get the same generic "AI slop" edit everyone else gets. This guide is the method I use to teach it.

---

## First, what's Claude and what's me

| I do | Claude does |
|---|---|
| Record the video | Cleans up the transcript |
| Make the rough cut (remove mistakes) | Plans what goes on screen, line by line |
| Pick from the options it gives me | Designs every graphic, caption and animation |
| Give feedback on each draft | Times captions and graphics to my words |
| Listen on my phone at the end | Places and levels the sound effects |
| | Checks the export and keeps notes on what I liked |

AI is not making the creative calls alone. **It proposes, I choose, it builds, I correct.** Every correction makes the next edit better.

---

## What you need

- A Claude plan (Pro or above). Projects or Cowork help a lot because Claude keeps your files and notes between chats.
- 5–10 reels whose editing style you love.
- One short video of your own to practise on (15–30 seconds is perfect).
- Optional, for the full setup: Claude Code (or Cowork linked to your computer) plus free tools like ffmpeg. Not needed to start.

**Two ways to use this:**
- **Path A, no code:** Claude studies, plans and designs; you put it together in your usual editor (CapCut, Premiere, Final Cut). Start here.
- **Path B, full automation:** Claude also cuts, builds the graphics, mixes the sound and renders the video on your computer. This is what I use now, but it takes setup. Get Path A working first.

---

## Step 1: Collect references and say why you like them

Pick 5–10 reels in one style. Not five different styles. One look.

For each one, write one line: *what exactly do you like?* "The captions feel calm." "Graphics appear exactly when he says the word." "The sound is busy but never loud."

These lines matter more than the videos. They're the start of your taste written down.

---

## Step 2: Let Claude study them (the cheap way)

Don't upload full videos and ask "copy this". Claude reads images, not motion, and long videos burn your usage fast.

Instead, give it **contact sheets**: one image with 12–30 small frames from a reel, in order. (Screenshot every 1–2 seconds and tile them, or use any "video to contact sheet" tool.) Add the transcript of each reel if you have it.

**Starter prompt:**
> I'm attaching contact sheets and transcripts from [N] reels in one editing style. Study them like a senior editor. Tell me:
> 1. The caption system: fonts (guess the closest Google Fonts), size, position, how many words at a time, which words get emphasis and how.
> 2. Every type of scene or graphic you see, with a name, what it looks like and when it's used.
> 3. How text and graphics enter and leave (fast/slow, blur, slide, pop).
> 4. Pacing: roughly how often something changes on screen, how soon the first graphic appears.
> 5. Which line of the script triggers which kind of visual.
> Mark anything you're guessing as a guess. Don't invent details you can't see.

Expect it to be roughly right, not perfect. That's fine. You'll correct it.

---

## Step 3: Turn it into a one-page Style Card

This is the most important file you'll make. Ask Claude to write it from Step 2 plus your notes from Step 1, then **you edit it until it sounds like you**.

**The Style Card has these sections:**
1. **Feel in one sentence** (e.g. "premium, calm, smooth; the face is always the centre").
2. **Captions:** fonts, size, position, words per line, how the key word is shown, how words appear.
3. **Colours:** 3–6 colours and what each is for.
4. **Scene menu:** 6–10 named scene types and when to use each ("a list → cards appear one by one"; "a number → big number counts up").
5. **Motion rules:** how things enter and leave, how long, what's banned (for me: anything that "pops").
6. **Pacing:** first graphic within X seconds; never more than X seconds of just the face.
7. **Sound:** what gets a sound and how loud.
8. **Never do:** your list of things you hate.

Keep it to one page. Claude reads it before every edit.

**My lesson here:** the first full style system I built copied one creator very closely. It was detailed, measured and technically correct, and when I used it on my own video it looked generic. Copying one person doesn't give you *your* style. Use references as a starting point, then let your picks and corrections reshape it.

---

## Step 4: Use the gated edit loop

This is where most people go wrong: they paste a transcript and say "edit this". Claude improvises, you get slop, you start over.

Instead, work in stages and **never let Claude build before you approve the plan**:

1. **Plan.** Give Claude your transcript (with timestamps) and the Style Card. It makes a table: one row per line → what goes on screen → why.
2. **Options.** For the important moments (hook, key point, call to action), ask for **3–5 different options** each. You pick, or mix ("option B, but with A's colours").
3. **Build.** Only now does Claude design the graphics and captions.
4. **Feedback.** Write your notes with timestamps. Claude turns them into a numbered list and fixes them all in one go.
5. **Sound.** Only after the visuals are approved.
6. **Check.** Safe zones (nothing under Instagram's buttons), captions readable, export size right (1080×1920).

**Prompt for the plan:**
> Here's my transcript with timestamps and my Style Card. Make an edit plan: one row per line with the time, the exact words, what this line is doing (hook, claim, example, list, number, call to action), and 3 visual options from my scene menu with one line each. Recommend one. Mark lines that should stay as just my face with captions. Don't design or build anything yet. Wait for my picks.

---

## Step 5: Start with one short clip

Your first edit: 15–20 seconds, only 2–3 scene types plus captions. My first draft of a 33-second reel was maybe 60–70% right. It took **four drafts** and one round of 28 notes before it felt like mine. That's normal. The goal of the first edit isn't a perfect video. It's to discover what Claude gets wrong about your taste.

---

## Step 6: Keep a lessons log (this is the secret)

After every round of feedback, ask Claude to add your corrections as rules to a **LESSONS** file, and to read it before every new edit. Real lines from mine:

- "Smooth beats fast. Anything that pops or snaps is a mistake."
- "'A little higher' means about 30 pixels, not 120."
- "Never white captions on a white background."
- "Return to my face only after the sentence finishes."

These rules **outrank** the Style Card. That's how Claude's edits get closer to yours every time instead of starting from zero.

**Prompt after feedback:**
> Turn my notes into a numbered fix list and fix them all. Then add every note that reflects my general taste (not just this video) to LESSONS as a short rule. Read LESSONS before every future edit.

---

## Step 7: Your second edit should be faster

By edit two or three, the Style Card plus LESSONS do most of the work. You spend your time on choices, not explaining. That's when it starts to feel like having an editor who knows you.

---

## Things Claude still can't do (be ready for these)

- **It can't hear.** It places sound by timing and measured levels. Always listen on your phone yourself.
- **It can't judge "feel" from a description alone.** Show it options and pick; don't try to describe taste in paragraphs.
- **It doesn't plan creatively enough on its own.** Its first plan is safe and generic. Your picks are where the good ideas come from.
- **It reads your sketches literally.** If something in a mock-up is a placeholder, say so.
- **It's not a rough-cut machine for messy footage.** I still make the rough cut myself (or with a simple auto-cut tool).

---

## Small habits that save a lot of time and usage

- **One project per style.** Keep the Style Card, LESSONS and references in one place.
- **New chat for each stage**, with a short plan file Claude updates ("continue from the next unchecked step").
- **Images, not videos,** for studying references.
- **Ask for numbered fixes in one pass,** not one change per message.
- **Keep every draft.** Never let Claude overwrite the last one. You'll want to compare.

---

## Sound in one rule

What made my edits feel premium: **lots of sound effects, each one very quiet.** A soft click when a key word appears, a light flick for each caption word, a smooth long swoosh for big transitions, louder in the first 5 seconds. Then listen on your phone and adjust.

---

## What's next

This is the method. Over the next videos I'll break down individual pieces: captions, sound, reverse-engineering a style, and how I run a whole series with one template.

Try Steps 1–3 this week with one clip. Reply to the email and tell me where you got stuck. I read them, and the next resource gets built from your answers.

*@rishi.docx*
