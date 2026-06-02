import json
import datetime
from pathlib import Path


LOG_DIR = Path(__file__).parent.parent / "logs"


def log_interaction(role: str, model: str, input_tokens: int, output_tokens: int) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "role": role,
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
    }
    log_file = LOG_DIR / "interactions.jsonl"
    with log_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def count_words(text: str) -> int:
    return len(text.split())


def truncate(text: str, max_chars: int = 200) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
