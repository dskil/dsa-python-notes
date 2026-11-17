"""Индекс задач: имя файла в tests/ строится по номеру и теме.

``dsa-trainer list``/``run`` берут данные из ``src/dsa_trainer/catalog.json``,
а здесь проверяется, что каталог, решения и тесты не разъехались:

- у каждой задачи есть папка ``solutions/<slug>/<slug>.py``;
- у каждой задачи есть ``tests/test_<slug>.py``;
- имена уникальны, номера идут как числа, статуса — только solved/todo;
- темы из каталога отображаются на префиксы slug.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "src" / "dsa_trainer" / "catalog.json"

TOPIC_PREFIX = {
    "Строки": "strings",
    "Битовые операции": "bitops",
    "Числа": "numbers",
    "Списки": "lists",
    "Файлы": "files",
    "Рекурсия": "recursion",
    "Словари": "dicts",
    "Множества": "sets",
    "Исключения": "errors",
}


def _load() -> list[dict]:
    return json.loads(CATALOG.read_text(encoding="utf-8"))["tasks"]


def test_all_fields_present():
    tasks = _load()
    assert 86 <= len(tasks) <= 99
    registered = set()
    for task in tasks:
        for field in ("id", "slug", "topic", "title", "description", "status"):
            assert task.get(field), f"Задача {task.get('id')}: пустое поле {field}"
        assert task["status"] in {"solved", "todo"}
        assert task["id"] not in registered, f"Повтор номера: {task['id']}"
        registered.add(task["id"])
        assert task["id"] >= 1
        assert task["slug"].startswith(TOPIC_PREFIX[task["topic"]])
        number = task["slug"].rsplit("_", 1)[1]
        assert number == f"{task['id']:02d}", f"slug {task['slug']} не совпадает с id {task['id']}"


def test_every_task_has_solution_and_test():
    for task in _load():
        slug = task["slug"]
        solution = ROOT / "solutions" / slug / f"{slug}.py"
        test = ROOT / "tests" / f"test_{slug}.py"
        assert solution.exists(), f"Нет решения: {solution}"
        assert test.exists(), f"Нет тестов: {test}"


def test_task_folders_have_no_extras():
    known = {task["slug"] for task in _load()}
    for folder in (ROOT / "solutions").iterdir():
        if folder.is_dir() and not folder.name.startswith("__"):
            assert folder.name in known, f"Лишняя папка решения: {folder.name}"


def test_no_empty_tests_specs():
    """Техническая проверка: ``tests/cases.json`` — коллекция или отсутствует."""
    cases_path = ROOT / "tests" / "cases.json"
    if not cases_path.exists():
        return
    data = json.loads(cases_path.read_text(encoding="utf-8"))
    assert isinstance(data, (dict, list))
