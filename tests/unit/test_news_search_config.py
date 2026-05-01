"""NewsSearchMCPConfig holds tavily_api_key separate from base MCPConfig."""
from __future__ import annotations

import pytest
from pydantic import ValidationError

pytestmark = pytest.mark.unit


def test_subclass_has_tavily_field():
    from src.news_search_config import NewsSearchMCPConfig

    cfg = NewsSearchMCPConfig(environment="dev", tavily_api_key="secret")
    assert cfg.tavily_api_key == "secret"


def test_subclass_default_empty():
    from src.news_search_config import NewsSearchMCPConfig

    cfg = NewsSearchMCPConfig(environment="dev")
    assert cfg.tavily_api_key == ""


def test_subclass_inherits_mcpconfig():
    from platform_sdk import MCPConfig
    from src.news_search_config import NewsSearchMCPConfig

    assert issubclass(NewsSearchMCPConfig, MCPConfig)


def test_subclass_load_reads_yaml(tmp_path, monkeypatch):
    from src.news_search_config import NewsSearchMCPConfig

    monkeypatch.setenv("TAVILY_API_KEY", "from-env")
    (tmp_path / "default.yaml").write_text(
        "environment: dev\ntavily_api_key: ${TAVILY_API_KEY}\n"
    )
    cfg = NewsSearchMCPConfig.load(config_dir=str(tmp_path), env="dev")
    assert cfg.tavily_api_key == "from-env"
