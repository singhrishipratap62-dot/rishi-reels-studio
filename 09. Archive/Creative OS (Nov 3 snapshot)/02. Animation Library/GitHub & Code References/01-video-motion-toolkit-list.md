# Video Editing and Motion Graphics Toolkit: Full List

Last checked: 3 Nov 2026. Star counts come from each repo's GitHub page and will drift.

## How to read this

There are three kinds of things here, and they are not interchangeable:

- **Skill / plugin:** instructions that teach Claude Code how to use a tool correctly. It does not render anything by itself.
- **Library / engine:** the real software that produces the video. Skills drive these.
- **MCP server:** a tool Claude can call directly.

A skill without its engine installed will write code that can't render.

---

## 1. Skills and plugins (install in Claude Code)

| # | Name | Type | Stars | Purpose | Install |
|---|------|------|-------|---------|---------|
| 1 | [remotion-dev/skills](https://github.com/remotion-dev/skills) | Skill (official) | 5.5k | Best practices for building Remotion (React) videos | `npx skills add remotion-dev/skills` |
| 2 | [Yusuke710/manim-skill](https://github.com/Yusuke710/manim-skill) | Plugin | 145 | Plan, write and render Manim scenes | `/plugin marketplace add Yusuke710/manim-skill` then `/plugin install manim-skill/manim-skill` |
| 3 | manimce-best-practices (from [adithya-s-k/manim_skill](https://github.com/adithya-s-k/manim_skill)) | Skill | not checked | Manim **Community Edition** best practices | `npx skills add adithya-s-k/manim_skill/skills/manimce-best-practices` |
| 4 | manimgl-best-practices (same repo) | Skill | not checked | Best practices for **3b1b/manim (ManimGL)**, the 3Blue1Brown version | Install command not verified. Check the repo README. |
| 5 | [op7418/Youtube-clipper-skill](https://github.com/op7418/Youtube-clipper-skill) | Skill | README claims 633, unverified | Download, chapter, clip, translate subtitles, burn them in | `npx skills add https://github.com/op7418/Youtube-clipper-skill` |
| 6 | [HarleyCoops/Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) | Plugin | not checked | Generates Manim from prompts via Claude, Gemini or Kimi pipelines (55+ examples) | Clone it, then `claude --plugin-dir ./Math-To-Manim/skill` |
| 7 | [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) | Project template | not checked | Skills, slash commands, components, transitions and brand profiles. Includes an FFmpeg skill for Remotion workflows. | Clone the repo. The README gives no exact command. |
| 8 | Motion Canvas community skills: [apoorvlathey/motion-canvas-skills](https://vibeindex.ai/skills/apoorvlathey/motion-canvas-skills/motion-canvas), [davila7/motion-canvas](https://smithery.ai/skills/davila7/motion-canvas) | Skill (community) | not checked | Teaches Claude Motion Canvas. There is no official skill. | Not verified. Pick one and follow its page. |

Notes:
- #1 is the same skill the toolkit README lists as `npx skills add remotion`. Install it once.
- #2 is also listed in the toolkit README. Install it once.
- #3 and #4 cover different engines. Install both if you want both Manim flavours.

## 2. Engines and libraries (needed to actually render)

| Name | Stars | Purpose | Install |
|------|-------|---------|---------|
| [Remotion](https://github.com/remotion-dev/remotion) | 70.2k | Videos from React code | Needs Node.js. Created per project. |
| [3b1b/manim](https://github.com/3b1b/manim) | 93.9k | Explanatory math animation (3Blue1Brown) | See its README. |
| Manim Community Edition | n/a | Community fork of Manim, used by skills #2, #3 and #6 | `uv tool install manim` |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 19.5k | Vector animation in TypeScript with voiceover sync | `npm`, via the quickstart at motion-canvas.io/docs/quickstart |
| FFmpeg (with libass) | n/a | Encoding, clipping, burning subtitles | `brew install ffmpeg` |

## 3. System dependencies

- macOS: `brew install cairo pkg-config ffmpeg`
- Python packages for the clipper: `pip install yt-dlp pysrt`
- Python tool installer: `uv`
- Node.js and npm (Remotion, Motion Canvas, `npx skills`)
- **Unverified:** whether Manim needs LaTeX for math text. Check the Manim docs before your first render.

## 4. MCP servers (optional)

| Name | Purpose | Install |
|------|---------|---------|
| Playwright MCP with video | Records browser sessions to MP4 | `claude mcp add playwright -s user -- npx @playwright/mcp@latest --save-video=1920x1080` |
| Manim MCP Server | Renders Manim scenes to MP4 | The toolkit README gives no install command. Skip unless needed. |

---

## 5. What is inside claude-code-video-toolkit (wilwaldon)

[wilwaldon/Claude-Code-Video-Toolkit](https://github.com/wilwaldon/Claude-Code-Video-Toolkit) has 101 stars. It contains only a README that links to the tools below. It is a curated list, not a bundle.

- Programmatic video: Remotion Agent Skills (#1), digitalsamba toolkit (#7)
- Math animation: Manim Skill (#2), Math-To-Manim (#6), Manim MCP Server
- Screen recording: Playwright MCP with `--save-video`
- YouTube clipping: Youtube Clipper Skill (#5)
- FFmpeg: FFmpeg skill inside the digitalsamba toolkit (#7)

---

## 6. Quick answer: which of these are skills?

| Item | Skill? |
|------|--------|
| Remotion skills | Yes |
| Yusuke710 manim-skill | Yes, as a plugin |
| manimce / manimgl best practices | Yes |
| Youtube Clipper | Yes |
| Math-To-Manim | Plugin |
| digitalsamba toolkit | Template containing skills |
| Motion Canvas community entries | Yes (community) |
| Remotion, 3b1b/manim, Motion Canvas, FFmpeg | No, they are engines |
| Playwright MCP, Manim MCP | No, they are MCP servers |
| wilwaldon toolkit | No, it is a list |
