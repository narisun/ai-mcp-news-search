# Build context: monorepo root (docker build -f tools/news-search-mcp/Dockerfile .)
# After Phase 5 carve-out, build context is the MCP's own repo root.
ARG BASE_TAG=3.11-sdk0.4.0
FROM ghcr.io/narisun/ai-python-base:${BASE_TAG}

WORKDIR /app

COPY tools/news-search-mcp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tools/news-search-mcp/src/ /app/src/

USER appuser
EXPOSE 8083
CMD ["python", "-m", "src.server"]
