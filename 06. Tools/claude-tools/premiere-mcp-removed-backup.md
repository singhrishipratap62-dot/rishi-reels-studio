# Removed Premiere MCP entries (2026-11-05)
Removed at the user's request. To restore either one:

User scope (was `premiere-pro`):
    claude mcp add premiere-pro -s user -e PREMIERE_MCP_TELEMETRY=0 -e PREMIERE_MCP_UPDATE_CHECK=0 -- premiere-pro-mcp

Project scope (was in `.mcp.json`):
```json
{
  "mcpServers": {
    "premiere-pro": {
      "command": "/Users/rishi/.nvm/versions/node/v24.19.0/bin/node",
      "args": ["/Users/rishi/.nvm/versions/node/v24.19.0/lib/node_modules/adobe-premiere-pro-mcp/dist/index.js"],
      "env": { "PREMIERE_TEMP_DIR": "/Users/rishi/Documents/Teaching Claude/.premiere-bridge" }
    }
  }
}
```
