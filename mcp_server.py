import requests
from mcp.server import Server
from fastmcp import FastMCP
# --- Define MCP server ---
server = FastMCP("local-greeting-mcp")

@server.tool(
    name="get_local_greeting",
    description="testing 101"
)
def get_local_greeting(name: str) -> dict:
    return "testing 101"


if __name__ == "__main__":
    print("🚀 MCP server started (local-greeting-mcp)")
    server.run()
