import os
import sys
from pathlib import Path

# 1. Local src/ package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

# 2. Set env-var defaults BEFORE src.server is imported (module-level MCPConfig.load())
_defaults = {
    "ENVIRONMENT": "dev",
    "CONFIG_DIR": str(Path(__file__).resolve().parent / "config"),
    "INTERNAL_API_KEY": "test-key",
    "REDIS_PASSWORD": "test-redis-password",
    "MCP_TRANSPORT": "sse",
}
for k, v in _defaults.items():
    os.environ.setdefault(k, v)

# 3. Pre-import so patch("src.server._opa") can resolve the module
import src.server  # noqa: E402, F401
