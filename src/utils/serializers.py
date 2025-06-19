import json
from typing import Any

def save_to_file(data: Any, path: str) -> None:
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def load_from_file(path: str) -> Any:
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

