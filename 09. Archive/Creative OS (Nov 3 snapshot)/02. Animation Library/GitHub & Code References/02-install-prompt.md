# Install Prompt: Video and Motion Graphics Toolkit

Paste everything inside the block below into Claude Code, run on the machine where you want the tools.

````
You are setting up a video editing and motion graphics toolkit on this machine. Work step by step, run the commands yourself, and verify each step before moving on. Be token-efficient: do not echo long outputs, only report pass or fail and any error.

RULES
- Do not invent commands. If a step says "look up the README", fetch the README and use only the commands it gives. If it gives none, say so and skip that item.
- Install each thing once. Several items appear in more than one list.
- If a command fails, show the exact error, try one reasonable fix, then continue and flag it in the final report.
- Never use sudo without telling me first.
- Do not delete or overwrite anything that already exists. If something is already installed, mark it "already present".

STEP 0: CHECK WHAT EXISTS
Check for: node, npm, npx, python3, pip, uv, brew, ffmpeg (and libass support), git, claude. Print a one-line status for each. Install missing basics with brew (macOS) before continuing.

STEP 1: SYSTEM DEPENDENCIES
1. brew install cairo pkg-config ffmpeg
2. Confirm ffmpeg has libass: run `ffmpeg -filters | grep -i subtitles`. If missing, reinstall ffmpeg with libass support.
3. pip install yt-dlp pysrt
4. Install uv if missing.

STEP 2: ENGINES
1. Manim Community Edition: `uv tool install manim`. Verify with `manim --version`.
2. Check the Manim docs to see whether LaTeX is required for math text. If it is, tell me and ask before installing it (it is large).
3. 3b1b/manim (ManimGL): look up https://github.com/3b1b/manim README and follow its install steps in an isolated environment so it does not conflict with Manim Community Edition.
4. Remotion: no global install needed. Confirm Node is 18 or newer. Do not create a project yet.
5. Motion Canvas: do not create a project yet. Confirm Node and npm work. The quickstart is https://motion-canvas.io/docs/quickstart.

STEP 3: SKILLS AND PLUGINS
Install in this order. After each one, confirm it appears in the list of installed skills or plugins.
1. `npx skills add remotion-dev/skills`
2. `/plugin marketplace add Yusuke710/manim-skill` then `/plugin install manim-skill/manim-skill`
3. `npx skills add adithya-s-k/manim_skill/skills/manimce-best-practices`
4. manimgl-best-practices: look up https://github.com/adithya-s-k/manim_skill, find the manimgl-best-practices skill, and install it the same way as item 3 if the path follows the same pattern. If unclear, tell me.
5. `npx skills add https://github.com/op7418/Youtube-clipper-skill`
6. Math-To-Manim: clone https://github.com/HarleyCoops/Math-To-Manim into ~/claude-tools/, then note that it loads with `claude --plugin-dir ./Math-To-Manim/skill`. Do not change my default launch command. Just tell me how to use it.
7. digitalsamba toolkit: clone https://github.com/digitalsamba/claude-code-video-toolkit into ~/claude-tools/. Read its README and report how its skills and slash commands are meant to be installed or loaded. Install them if the README gives clear steps. Otherwise report only.
8. Motion Canvas community skill: compare https://vibeindex.ai/skills/apoorvlathey/motion-canvas-skills/motion-canvas and https://smithery.ai/skills/davila7/motion-canvas. Pick the better-documented one, follow its own install instructions, and tell me which you chose and why in one line.

Note: some of these commands (/plugin ...) are Claude Code slash commands. If you cannot run them from here, print them clearly for me to paste into Claude Code.

STEP 4: MCP SERVERS
1. Playwright with video: `claude mcp add playwright -s user -- npx @playwright/mcp@latest --save-video=1920x1080`
2. Manim MCP Server: SKIP. No install command is documented. Only mention it in the report.

STEP 5: SMOKE TESTS
1. Create a throwaway folder ~/claude-tools/smoke-test/.
2. Manim: render a 3-second scene with a circle and a square, low quality (`manim -ql`). Confirm an MP4 is produced.
3. ffmpeg: run `ffmpeg -version | head -1`.
4. Remotion: do NOT scaffold a full project. Just confirm `npx remotion --help` runs.
5. Delete the smoke-test folder when done.

STEP 6: FINAL REPORT
Print one table with these columns: Item, Type (skill, plugin, engine, MCP, dependency), Status (installed, already present, failed, skipped), Notes.
Then list:
- anything that needs me to do something manually,
- anything that was skipped and why,
- the exact commands to start using each skill.
Keep the report under 40 lines.
````

---

## Before you run it

- Run it on your own machine's Claude Code, not a cloud session, so skills land where you will actually use them.
- Items marked "not verified" in `01-video-motion-toolkit-list.md` (manimgl skill path, Motion Canvas community skill, Math-To-Manim, digitalsamba toolkit) are handled by the prompt looking up the README instead of guessing.
- The LaTeX question for Manim is left for you to approve, because that install is large.
