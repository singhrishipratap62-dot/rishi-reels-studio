---
name: premiere-handoff
description: Send a rough cut and its transcript markers into Adobe Premiere Pro via the premiere-pro MCP server. Use when the user wants to finish an edit in Premiere.
---
1. Call `verify_premiere_connection`. If it returns userActionRequired, relay the nextStep and stop.
2. Use `search_tools` to find import/sequence/marker tools, then `invoke_tool`:
   import `projects/$REEL_ID/roughcut.mp4`, create a 1080x1920 30fps sequence named $REEL_ID, place the clip.
3. Add a marker per transcript sentence (from transcript.srt) so the editor can navigate by line.
4. Save the project as `projects/$REEL_ID/$REEL_ID.prproj`. Report what was created; never claim success without tool confirmation.
