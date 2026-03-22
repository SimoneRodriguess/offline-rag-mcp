# offline-rag-mcp

Offline RAG pipeline over local PDFs, exposed as an MCP server. No cloud APIs.

## Stack
- LLM + embeddings: Ollama (llama3.2, nomic-embed-text)
- Vector DB: ChromaDB
- MCP: Python SDK

## Usage
```bash
pip install -r requirements.txt
python ingest.py --all        # index docs/
python mcp_server.py          # start server
```

Register in Claude Desktop config:
```json
{
  "mcpServers": {
    "offline-rag": {
      "command": "python",
      "args": ["/path/to/mcp_server.py"]
    }
  }
}
```

## Status
- [x] MCP tool stubs
- [ ] ingest.py
- [ ] retriever.py
- [ ] mcp_server.py implementation
