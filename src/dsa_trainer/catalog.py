"""Каталог задач.

Единственный источник правды — файл ``catalog.json`` рядом с этим модулем.
Он генерируется скриптом ``tools/build_catalog.py`` из исходных файлов
``Train*.py`` и ``HSEtasks/*`` и хранит для каждой задачи:

- ``id``    — стабильный номер (совпадает с номером исходного Train-файла);
- ``slug``  — человекочитаемое имя папки в ``tasks/`` и ``solutions/``;
- ``topic`` — тема;
- ``title`` / ``description`` — условие задачи;
- ``status`` — ``solved`` (есть рабочее решение) или ``todo`` (заготовка).

Что возвращать и как считать граничные случаи — задаёт ``tests/conftest.py``
(файл ``cases.json`` в папке задачи).
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from dataclasses import dataclass
from importlib import resources


@dataclass(frozen=True)
class Task:
    id: int
    slug: str
    topic: str
    title: str
    description: str
    status: str
    source: str = ""

    @property
    def solved(self) -> bool:
        return self.status == "solved"

    @property
    def display_id(self) -> str:
        """Номер с ведущим нулём: 1 -> '01'."""
        return f"{self.id:02d}"


def _load() -> list[Task]:
    raw = resources.files(__package__).joinpath("catalog.json").read_text(encoding="utf-8")
    data = json.loads(raw)
    return [
        Task(
            id=int(item["id"]),
            slug=item["slug"],
            topic=item["topic"],
            title=item["title"],
            description=item["description"],
            status=item.get("status", "todo"),
            source=item.get("source", ""),
        )
        for item in data["tasks"]
    ]


_CATALOG: list[Task] | None = None


def all_tasks() -> list[Task]:
    """Все задачи каталога, отсортированные по номеру."""
    global _CATALOG
    if _CATALOG is None:
        _CATALOG = sorted(_load(), key=lambda task: task.id)
    return list(_CATALOG)


def resolve_task_id(raw: str | int) -> int:
    """Принять '7', '07' или '007' и вернуть 7."""
    try:
        task_id = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Номер задачи должен быть числом, получено: {raw!r}") from exc
    if task_id <= 0:
        raise ValueError(f"Номер задачи должен быть > 0, получено: {task_id}")
    return task_id


def get_task(task_id: str | int) -> Task | None:
    """Задача по номеру или ``None``, если такого номера нет."""
    try:
        wanted = resolve_task_id(task_id)
    except ValueError:
        return None
    for task in all_tasks():
        if task.id == wanted:
            return task
    return None


def by_topic() -> dict[str, list[Task]]:
    """Задачи, сгруппированные по теме (порядок тем — по первой задаче)."""
    grouped: dict[str, list[Task]] = {}
    for task in all_tasks():
        grouped.setdefault(task.topic, []).append(task)
    return grouped


def tasks_iter() -> Iterator[Task]:
    return iter(all_tasks())
