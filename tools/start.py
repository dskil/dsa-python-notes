"""Старт для новичка: выбрать задачу и проверить её одной командой.

    python tools/start.py            # первая нерешённая задача: условие + тест
    python tools/start.py 33         # конкретная задача
    python tools/start.py --list     # что есть и что решено

Скрипт ничего не делает за тебя: показывает условие, показывает, какие
функции надо дописать, и запускает тесты. Дальше — правь файл в solutions/
и запускай ту же команду снова.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dsa_trainer.catalog import Task, all_tasks, get_task  # noqa: E402
from dsa_trainer.progress import completed_ids  # noqa: E402

BAR = "=" * 70


def _functions_in(solution_path: Path) -> list[str]:
    """Имена функций решения (кроме main и приватных)."""
    import ast

    try:
        tree = ast.parse(solution_path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return []
    names = []
    for node in tree.body:
        if (
            isinstance(node, ast.FunctionDef)
            and not node.name.startswith("_")
            and node.name != "main"
        ):
            names.append(f"{node.name}({', '.join(arg.arg for arg in node.args.args)})")
    return names


def _show_task(task: Task) -> None:
    solution = ROOT / "solutions" / task.slug / f"{task.slug}.py"

    print(BAR)
    print(f"  ЗАДАЧА №{task.display_id} — {task.title}")
    print(f"  тема: {task.topic}   |   решена в репозитории: {'да' if task.solved else 'нет'}")
    print(BAR)
    print()
    print(task.description.strip())
    print()
    print(BAR)
    print("  ГДЕ ПИСАТЬ КОД")
    print(f"    {solution.relative_to(ROOT)}")
    if task.solved:
        print("    (сейчас там эталонное решение — замени тело функции своим кодом)")
    print()
    print("  ФУНКЦИИ, КОТОРЫЕ ДОЛЖНЫ БЫТЬ В ФАЙЛЕ")
    for signature in _functions_in(solution) or ["(файл пока не читается — но тесты его ждут)"]:
        print(f"    def {signature}:")
    print()
    print("  КАК ПРОВЕРИТЬ")
    print(f"    python -m pytest tests/test_{task.slug}.py -v")
    print()
    print(BAR)


def _run_tests(slug: str) -> int:
    print("  ЗАПУСКАЮ ТЕСТЫ...")
    print()
    command = [
        sys.executable,
        "-m",
        "pytest",
        f"tests/test_{slug}.py",
        "-v",
        "--no-header",
        "-p",
        "no:warnings",
    ]
    return subprocess.run(command, cwd=ROOT).returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", nargs="?", help="номер задачи; без аргумента — первая нерешённая")
    parser.add_argument("--list", action="store_true", help="показать все задачи")
    parser.add_argument("--only-show", action="store_true", help="не запускать тесты")
    args = parser.parse_args(argv)

    done = completed_ids()

    if args.list:
        for task in all_tasks():
            mark = "x" if task.id in done else ("." if task.solved else " ")
            print(f"[{mark}] {task.display_id}  {task.title}")
        print()
        print(
            "  [x] — ты уже решил (dsa-trainer run), [.] — эталон есть в репозитории, [ ] — пусто"
        )
        return 0

    if args.task:
        task = get_task(args.task)
        if task is None:
            print(f"Нет задачи №{args.task}. Посмотри список: python tools/start.py --list")
            return 2
    else:
        remaining = [task for task in all_tasks() if task.id not in done]
        if not remaining:
            print(
                "Поздравляю: все задачи отмечены как решённые! "
                "Сброс: python -m dsa_trainer reset -y"
            )
            return 0
        task = remaining[0]

    _show_task(task)
    if args.only_show:
        return 0

    code = _run_tests(task.slug)
    print()
    if code == 0:
        print(BAR)
        print("  ВСЁ ЗЕЛЁНОЕ — тесты прошли. Задача решена.")
        print("  Следующая: python tools/start.py")
        print(BAR)
    else:
        print(BAR)
        print("  КРАСНЫЙ — где-то не так. Открой файл из блока «ГДЕ ПИСАТЬ КОД»,")
        print("  поправь функцию и запусти ту же команду снова.")
        print("  Если непонятен текст ошибки — смотри docs/HOW_TO_PLAY.md, шаг 5.")
        print(BAR)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
