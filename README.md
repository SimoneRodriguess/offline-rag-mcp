# offline-rag-mcp

> **Status: WIP** — Offline RAG system exposed as an MCP server for Claude Desktop.  
> No cloud APIs. Everything runs locally.

---

## What this is

A fully offline Retrieval-Augmented Generation (RAG) pipeline wired up as an [MCP](https://modelcontextprotocol.io/) server, so Claude Desktop can call it as a tool. Drop PDFs into `docs/`, ingest them once, then ask Claude questions grounded in your documents — all on-device.

---

## Stack

| Layer | Tool |
|---|---|
| Local LLM | [Ollama](https://ollama.com) + `llama3.2` |
| Embeddings | `nomic-embed-text` via Ollama |
| Vector DB | [ChromaDB](https://www.trychroma.com/) (persistent, local) |
| MCP server | [`mcp`](https://github.com/modelcontextprotocol/python-sdk) Python SDK |
| Doc parsing | `pypdf` + `langchain-text-splitters` |

---

## Architecture
```
docs/
 └─ your PDFs/txts
       │
       ▼
  ingest.py
 (chunk → embed → store)
       │
       ▼
  ChromaDB  ◄──── retriever.py ◄──── mcp_server.py
 (local disk)     (top-k query)       (MCP tools)
                                           │
                                           ▼
                                    Claude Desktop
```

---

## MCP Tools exposed

| Tool | Description |
|---|---|
| `search_docs(query)` | Returns top-k relevant chunks from ingested docs |
| `ask_with_context(question)` | Retrieves context + answers via local Ollama LLM |

---

## Setup

**1. Install Ollama and pull models**
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
ollama pull nomic-embed-text
```

**2. Install Python deps**
```bash
pip install -r requirements.txt
```

**3. Ingest your documents**
```bash
python ingest.py --path docs/paper.pdf
python ingest.py --all
```

**4. Register with Claude Desktop**

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "offline-rag": {
      "command": "python",
      "args": ["/absolute/path/to/offline-rag-mcp/mcp_server.py"]
    }
  }
}
```

Restart Claude Desktop. The tools `search_docs` and `ask_with_context` will appear.

---

## Roadmap

- [x] Project scaffold + MCP tool stubs
- [ ] `ingest.py` — chunking + embedding + ChromaDB storage
- [ ] `retriever.py` — dense retrieval from ChromaDB
- [ ] `mcp_server.py` — wire tools to retriever + Ollama
- [ ] Benchmark retrieval quality on test queries
- [ ] Hybrid search (dense + BM25)
- [ ] Reranking pass (cross-encoder)
