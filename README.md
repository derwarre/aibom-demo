# aibom-demo — AcmeSupport AI

A deliberately AI-asset-rich demo application for showcasing **Cisco AI Defense AI BOM** scanning
([cisco-ai-defense/aibom](https://github.com/cisco-ai-defense/aibom)).

It is a fake customer-support AI service ("AcmeSupport AI") packed with assets across the AI BOM
detection categories:

| BOM category | Where |
|---|---|
| Models / LLM endpoints | `gpt-4o`, `gpt-4o-mini`, `claude-sonnet-4-5` literals in `app/agent.py`, `config/settings.py`, `prompts/prompt_templates.yaml` |
| Model artifact | Trained scikit-learn classifier `models/ticket_classifier.joblib` (+ `models/model_card.md`) |
| Agent + tools | LangChain tool-calling agent in `app/agent.py` |
| MCP server / client | `app/mcp_server.py` (FastMCP) + `mcp/config.json` |
| Embeddings / vector store / retriever | Chroma + `text-embedding-3-small` in `app/rag.py` |
| Prompts | `prompts/` |
| Dataset | `data/support_tickets.jsonl` |
| Guardrails | `app/guardrails.py`, `guardrails/config.yaml` (tagged `# aibom: concept=guardrail`) |
| Secrets (fake, planted) | `config/settings.py` — demo values only, incl. AWS's documented example credentials |
| Dependencies | `requirements.txt` (12 pinned AI packages) |

> **Note:** every credential in this repository is intentionally fake, planted so AI BOM secret
> scanning has something to find. Nothing here is a real secret.

## Build and run the container

```bash
docker build -t acmesupport-ai:1.0.0 .
docker run -p 8000:8000 acmesupport-ai:1.0.0   # GET /healthz -> {"status":"ok"}
```

## Scan

Scan the repo or the container image with the `cisco-aibom` CLI (LLM key required for the
agentic classifier), optionally uploading straight to Cisco AI Defense:

```bash
LLM_MODEL=gpt-5.4 OPENAI_API_KEY=... AI_DEFENSE_API_KEY=... ./run-aibom-scan.sh
```

See `run-aibom-scan.sh` for the scan-only and region-override options. Git repository scans and
container image scans auto-project into AI Defense's AI Inventory.
