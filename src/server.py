from fastmcp import FastMCP

mcp = FastMCP("MCP Demo Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Return the sum of two integers"""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Return a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport='http')