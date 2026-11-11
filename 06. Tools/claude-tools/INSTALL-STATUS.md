# Video & Motion Toolkit: Install Status
Last updated: 2026-11-04. Source prompt: `Creative OS/02. Animation Library/GitHub & Code References/02-install-prompt.md`

## Installed

| Item | Type | Where / how |
|---|---|---|
| cairo, pkg-config | dependency | brew |
| ffmpeg-full (has libass) | dependency | brew, keg-only. Use `/opt/homebrew/opt/ffmpeg-full/bin/ffmpeg` for captions. Plain `ffmpeg` has no `subtitles`/`drawtext` filter |
| pysrt | dependency | venv at `06. Tools/claude-tools/venv` (pip is blocked by PEP 668) |
| Manim Community 0.22.1 | engine | `uv tool`, `~/.local/bin/manim` |
| ManimGL 1.7.2 | engine | isolated `uv tool` with `setuptools<81`, `~/.local/bin/manimgl` |
| Remotion CLI | engine | no global install; run `npx -p @remotion/cli remotion` |
| remotion-dev/skills (11 skills) | skill | `~/.claude/skills` |
| manimce-best-practices | skill | `~/.claude/skills` |
| manimgl-best-practices | skill | `~/.claude/skills` |
| manim-skill (Yusuke710) | skill | `~/.claude/skills`, installed via `npx skills add Yusuke710/manim-skill` |
| math-to-manim | skill | copied from the cloned repo's `legacy/` plugin folder into `~/.claude/skills` |
| youtube-clipper | skill | `~/.claude/skills` |
| motion-canvas (apoorvlathey) | skill | `~/.claude/skills`. Chosen because the Smithery page returned a 404 |
| Playwright MCP | MCP | user scope, connected, **without** video (see below) |
| Math-To-Manim repo | reference clone | `~/claude-tools/Math-To-Manim` |
| claude-code-video-toolkit repo | reference clone | `~/claude-tools/claude-code-video-toolkit` |

Add to your shell profile: `export PATH="$HOME/.local/bin:$PATH"`. Restart Claude Code to load new skills.

## Not installed

| Item | Reason | Workaround |
|---|---|---|
| LaTeX | Large download; skipped on request | Manim `Text` works without it; `MathTex`/`Tex` need it. Ask to install a minimal distribution later |
| Manim MCP server | No install command documented | None needed; the Manim skills plus the `manim` CLI cover it. Ask to search for a maintained one |
| Motion Canvas engine | No project created, as instructed | Follow https://motion-canvas.io/docs/quickstart when needed. The skill is installed |
| digitalsamba video toolkit (skills/commands) | No global install. Its skills load only inside its own folder, and `/setup` needs a cloud GPU account (Modal or RunPod) | `cd ~/claude-tools/claude-code-video-toolkit && claude`, then `/setup` and `/video` |
| Playwright video recording | Prompt's `--save-video=1920x1080` flag is invalid in the current version | Use a Playwright config file; needs checking in the Playwright MCP docs |
| Math-To-Manim as a full plugin | Only its skill was installed. The `plugin.json` plugin form is not loaded globally | `claude --plugin-dir ~/claude-tools/Math-To-Manim/legacy/Math-To-Manim/.claude/plugins/math-to-manim` (untested) |
