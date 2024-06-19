from __future__ import annotations

from typing import Any

# from uvicorn.workers import UvicornWorker
from uvicorn_worker import UvicornWorker


class OliveUvicornWorker(UvicornWorker):
    CONFIG_KWARGS: dict[str, Any] = {'loop': 'uvloop', 'http': 'httptools'}
