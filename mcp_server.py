from mcp.server.fastmcp import FastMCP

mcp = FastMCP("offline-rag")


@mcp.tool()
def search_docs(query: str, n_results: int = 5) -> str:
    raise NotImplementedError


@mcp.tool()
def ask_with_context(question: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    mcp.run(transport="stdio")