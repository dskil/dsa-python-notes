"""Прогресс: простое хранилище решённых задач в JSON.

Файл лежит рядом с репозиторием, а не внутри ``solutions/`` — так личные
результаты не попадают в git (см. ``.gitignore``).

Переопределить путь можно переменной окружения ``DSA_PROGRESS_FILE``
(полезно для тестов и CI).
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path


def attempts_path() -> Path:
    override = os.environ.get("DSA_PROGRESS_FILE")
    if override:
        return Path(override).expanduser()
    return repo_root() / ".dsa_progress.json"


def repo_root() -> Path:
    """Корень репозитория: папка с ``pyproject.toml`` над ``src/``."""
    return Path(__file__).resolve().parents[2]


def load_progress() -> dict[str, dict[str, str]]:
    path = attempts_path()
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    if not isinstance(data, dict):
        return {}
    return data


def mark_solved(task_id: int, slug: str) -> None:
    data = load_progress()
    data[str(task_id)] = {
        "slug": slug,
        "solved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    path = attempts_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def completed_ids() -> set[int]:
    ids: set[int] = set()
    for key in load_progress():
        try:
            ids.add(int(key))
        except ValueError:
            continue
    return ids
