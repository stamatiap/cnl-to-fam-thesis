import sys
import json
from datetime import datetime
from dataclasses import is_dataclass, fields
from enum import Enum
from pathlib import Path
from loguru import logger
from antlr4.error.ErrorListener import ErrorListener


def setup_logging(log_dir: Path = Path("logs")) -> Path:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"run-{datetime.now():%Y%m%d-%H%M%S}.log"
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add(log_file, level="DEBUG", backtrace=True, diagnose=True)
    return log_file

# Serialize artifact
def serialize(obj):
    if isinstance(obj, Enum):
        return obj.value
    if is_dataclass(obj):
        return {"__class__": obj.__class__.__name__,
                **{f.name: serialize(getattr(obj, f.name)) for f in fields(obj)}}
    if isinstance(obj, list):
        return [serialize(x) for x in obj]
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    return obj

# Store artifact
def write_artifact(obj, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(obj, str):
        path.write_text(obj, encoding="utf-8")
    else:
        path.write_text(json.dumps(serialize(obj), indent=4), encoding="utf-8")
    logger.debug("artifact written: {}", path)
    return path

# ANTLR error capture
class LoguruErrorListener(ErrorListener):
    def __init__(self, source: str):
        super().__init__()
        self.source = source
        self.errors: list[dict] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({"line": line, "column": column, "message": msg})
        logger.warning("Syntax error {}:{}:{} — {}", self.source, line, column, msg)
