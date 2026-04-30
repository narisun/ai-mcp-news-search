# ai-mcp-news-search

News search MCP server (Tavily).

## Quick start

```bash
pip install -r requirements.txt
python -m src.server
```

## Build the container

```bash
docker build -t ai-mcp-news-search:dev .
docker run --rm -p 8083:8083 ai-mcp-news-search:dev
```

The Dockerfile inherits from `ghcr.io/narisun/ai-python-base:3.11-sdk0.4.0`,
which has the platform SDK pre-installed.

## Requirements files

- **`requirements.txt`** — full deps including the SDK (git+ssh pin) and tavily. Used for local dev and CI.
- **`requirements-runtime.txt`** — only server-specific runtime extras (tavily). Used by the Dockerfile because the base image already provides the SDK.

## Local SDK development

```bash
pip install -e ../ai-platform-sdk
```
