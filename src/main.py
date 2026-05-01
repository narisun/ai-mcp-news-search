"""Main entry point for the news-search-mcp server."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from platform_sdk import MCPConfig, configure_logging, get_logger

from .news_search_mcp_service import NewsSearchMcpService

configure_logging()
log = get_logger(__name__)

config = MCPConfig.load()
service = NewsSearchMcpService(config=config)

mcp = FastMCP(
    "news-search-mcp",
    lifespan=service.lifespan,
    host="0.0.0.0",
    port=config.port,
)

service.register_tools(mcp)


if __name__ == "__main__":
    log.info("mcp_server_starting", transport=config.transport)
    service.run_with_registration(mcp, config.transport)
