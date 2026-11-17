"""Сгенерировать docs/tasks.md из каталога и проверить консистентность.

Запуск::

    python tools/build_catalog.py          # печатает таблицу в stdout
    python tools/build_catalog.py --write  # перезаписывает docs/tasks.md

Скрипт намеренно кроссплатформенный (не PowerShell): его запускает CI.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "src" / "dsa_trainer" / "catalog.json"
DOCS = ROOT / "docs" / "tasks.md"

TOPIC_ORDER = [
    "Строки",
    "Битовые операции",
    "Числа",
    "Списки",
    "Файлы",
    "Рекурсия",
    "Словари",
    "Множества",
    "Исключения",
]

STATUS_MARK = {"solved": "✅", "todo": "⬜"}


def render(tasks: list[dict]) -> str:
    by_topic: dict[str, list[dict]] = {topic: [] for topic in TOPIC_ORDER}
    for task in tasks:
        by_topic.setdefault(task["topic"], []).append(task)

    lines = [
        "# Каталог задач",
        "",
        "> Файл сгенерирован `tools/build_catalog.py` из `src/dsa_trainer/catalog.json`.",
        "> Не редактируй вручную — правь каталог.",
        "",
        f"Всего задач: **{len(tasks)}**.",
        "",
    ]

    for topic in TOPIC_ORDER:
        topic_tasks = by_topic.get(topic) or []
        if not topic_tasks:
            continue
        lines.append(f"## {topic}")
        lines.append("")
        lines.append("| № | Задача | Статус | Источник |")
        lines.append("|---:|---|:---:|---|")
        for task in topic_tasks:
            source = task.get("source") or "—"
            lines.append(
                f"| {task['id']:02d} | {task['title']} | "
                f"{STATUS_MARK.get(task['status'], '?')} | `{source}` |"
            )
        lines.append("")

    lines.append("## Журнал")
    lines.append("")
    for task in tasks:
        lines.append(f"{task['id']:02d}. **{task['title']}**")
        lines.append("")
        for raw_line in task["description"].splitlines():
            lines.append(f"   {raw_line}".rstrip())
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="записать docs/tasks.md")
    parser.add_argument("--check", action="store_true", help="упасть, если docs устарел")
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    args = parser.parse_args(argv)

    tasks = json.loads(args.catalog.read_text(encoding="utf-8"))["tasks"]
    ids = [task["id"] for task in tasks]
    duplicates = {i for i in ids if ids.count(i) > 1}
    if duplicates:
        print(f"Повторяющиеся номера задач: {sorted(duplicates)}", file=sys.stderr)
        return 1

    rendered = render(tasks)

    if args.check:
        if not DOCS.exists() or DOCS.read_text(encoding="utf-8") != rendered:
            message = "docs/tasks.md устарел: запусти `python tools/build_catalog.py --write`"
            print(message, file=sys.stderr)
            return 1
        print("docs/tasks.md в порядке.")
        return 0

    if args.write:
        DOCS.parent.mkdir(parents=True, exist_ok=True)
        with DOCS.open("w", encoding="utf-8", newline="\n") as file:
            file.write(rendered)
        print(f"Записано {DOCS} ({len(tasks)} задач).")
        return 0

    sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
