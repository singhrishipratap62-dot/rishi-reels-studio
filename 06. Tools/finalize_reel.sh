#!/bin/bash
# Close out a finished reel (dry run unless --yes). See finalize_reel.py for what is kept and deleted.
# usage: finalize_reel.sh "<project folder>" [--export <final.mp4>] [--yes]
exec python3 "$(cd "$(dirname "$0")" && pwd)/finalize_reel.py" "$@"
