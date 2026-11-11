#!/bin/bash
# Snapshot the studio's knowledge to git (dry run unless --yes). Media is excluded by .gitignore.
# usage: backup.sh [--yes] ["commit message"]
ROOT="$(d="$(cd "$(dirname "$0")" && pwd)"; while [ ! -e "$d/.studio-root" ] && [ "$d" != / ]; do d="$(dirname "$d")"; done; echo "$d")"
cd "$ROOT" || exit 1
YES=0; MSG=""
for a in "$@"; do [ "$a" = "--yes" ] && YES=1 || MSG="$a"; done
[ -z "$MSG" ] && MSG="studio snapshot $(date +%F)"
python3 "$ROOT/06. Tools/build_vault_index.py" >/dev/null 2>&1
git add -A
echo "Staged changes:"; git status --short | head -40
[ "$YES" = 1 ] || { echo; echo "Dry run. Re-run with --yes to commit and push."; git reset -q; exit 0; }
git diff --cached --quiet && { echo "Nothing to commit."; exit 0; }
git commit -q -m "$MSG" && echo "Committed: $MSG"
if git remote | grep -q .; then git push && echo "Pushed."; else echo "No remote yet: see 00. START HERE/README.md (Backing up) to add GitHub."; fi
