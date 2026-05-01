"""News-search MCP service-specific configuration.

Extends the SDK's MCPConfig with fields that are only relevant to this
service (Tavily API key for live news search, etc.). Following the
canonical pattern: vendor-specific fields stay in the service repo,
the SDK MCPConfig stays generic.
"""
from __future__ import annotations

from pydantic import ConfigDict

from platform_sdk import MCPConfig


class NewsSearchMCPConfig(MCPConfig):
    """MCPConfig + news-search-specific fields."""

    model_config = ConfigDict(extra="forbid")

    # Tavily Search API key. Empty string => news-search uses mock data.
    tavily_api_key: str = ""

    @classmethod
    def load(cls, *, config_dir: str | None = None, env: str | None = None) -> "NewsSearchMCPConfig":
        from platform_sdk.config.loader import load_config
        return load_config(cls, config_dir=config_dir, env=env)
