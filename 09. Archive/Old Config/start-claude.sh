#!/bin/zsh
# Launch Claude Code fully isolated inside this folder.
DIR="${0:A:h}"
export CLAUDE_CONFIG_DIR="$DIR/.claude-home"
cd "$DIR" || exit 1
exec claude "$@"
