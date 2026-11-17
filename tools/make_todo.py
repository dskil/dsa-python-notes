"""Превратить готовые решения в заготовки: `python tools/make_todo.py --all`.

Что делает: для выбранной задачи находит папку ``solutions/<slug>/``,
делает резервную копию ``<slug>.py.bak`` и переписывает тела функций на
``raise NotImplementedError`` — оставляя сигнатуры, докстринги и ``main()``.

Резервная копия — единственный способ вернуть решение, поэтому ``*.bak``
попадает в ``.gitignore``. Запускай осознанно. Полезные флаги:
``--dry-run`` (ничего не пишет) и ``--all``.
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "src" / "dsa_trainer" / "catalog.json"
SOLUTIONS = ROOT / "solutions"

KEEP_BODY = {"main"}


def stubify(source: str) -> str:
    """Заменить тела функций на ``raise NotImplementedError``.

    Сигнатуры, докстринги, ``main()`` и код на уровне модуля сохраняются.
    Работает по AST: каждому ``def`` соответствует диапазон строк, поэтому
    многострочные сигнатуры и вложенные функции не ломают результат.
    """
    tree = ast.parse(source)
    lines = source.splitlines()

    replacements: list[tuple[int, int, int, str]] = []  # (начало 1-based, конец, отступ, имя)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name in KEEP_BODY or node.name.startswith("__"):
            continue
        if (
            node.body
            and isinstance(node.body[0], ast.Expr)
            and isinstance(node.body[0].value, ast.Constant)
            and isinstance(node.body[0].value.value, str)
        ):
            body_start = node.body[1].lineno if len(node.body) > 1 else node.body[0].end_lineno + 1
        else:
            body_start = node.body[0].lineno
        if body_start > node.end_lineno:
            body_start = node.end_lineno + 1
        replacements.append((body_start, node.end_lineno, node.col_offset, node.name))

    # Если тело уже заглушка — не трогаем.
    filtered = [item for item in replacements if not _already_stub(lines, item)]
    # Заменяем сверху вниз с конца, чтобы индексы не съезжали.
    for start, end, column, _name in sorted(filtered, key=lambda item: item[0], reverse=True):
        stub = f"{' ' * (column + 4)}raise NotImplementedError"
        lines[start - 1 : end] = [stub]

    return "\n".join(lines).rstrip() + "\n"


def _already_stub(lines: list[str], item: tuple[int, int, int, str]) -> bool:
    start, end, _, _ = item
    body = "\n".join(lines[start - 1 : end])
    return "NotImplementedError" in body


def task_slugs(selection: list[str], everything: bool) -> list[str]:
    tasks = json.loads(CATALOG.read_text(encoding="utf-8"))["tasks"]
    if everything:
        return [task["slug"] for task in tasks]
    by_id = {str(task["id"]): task["slug"] for task in tasks}
    slugs = []
    for raw in selection:
        if raw in by_id:
            slugs.append(by_id[raw])
        elif raw:
            slugs.append(raw)
    return slugs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("tasks", nargs="*", help="номера задач или slug")
    parser.add_argument("--all", action="store_true", help="обработать все задачи")
    parser.add_argument("--dry-run", action="store_true", help="ничего не записывать")
    args = parser.parse_args(argv)

    slugs = task_slugs(list(args.tasks), args.all)
    if not slugs:
        parser.print_help(sys.stderr)
        return 2

    changed = 0
    for slug in slugs:
        path = SOLUTIONS / slug / f"{slug}.py"
        if not path.exists():
            print(f"пропуск: нет файла {path.relative_to(ROOT)}", file=sys.stderr)
            continue
        source = path.read_text(encoding="utf-8")
        stubbed = stubify(source)
        if stubbed == source:
            print(f"без изменений: {path.relative_to(ROOT)}")
            continue
        if args.dry_run:
            print(f"было бы изменено: {path.relative_to(ROOT)}")
            continue
        backup = path.with_suffix(".py.bak")
        backup.write_text(source, encoding="utf-8")
        path.write_text(stubbed, encoding="utf-8")
        changed += 1
        print(f"заготовка: {path.relative_to(ROOT)} (копия: {backup.name})")

    if not args.dry_run:
        print(f"\nГотово, изменено файлов: {changed}.")
        print("Вернуть решение: переименуй <slug>.py.bak обратно в <slug>.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
