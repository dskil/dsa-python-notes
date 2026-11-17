"""CLI тренажёра.

Примеры::

    dsa-trainer list                # все задачи + статус
    dsa-trainer list --solved       # только решённые
    dsa-trainer show 7              # условие задачи №7
    dsa-trainer run 7               # запустить тесты задачи №7
    dsa-trainer run 7 -- -x         # передать флаги в pytest
    dsa-trainer stats               # прогресс по темам
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .catalog import Task, all_tasks, by_topic, get_task
from .progress import attempts_path, completed_ids, load_progress, mark_solved

try:  # pragma: no cover - импорт обязателен для `run`, но пусть падает мягко
    import pytest
except ImportError:  # pragma: no cover
    pytest = None  # type: ignore[assignment]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _status_mark(task: Task, solved_local: set[int]) -> str:
    if task.id in solved_local:
        return "[✓]"
    return "[ ]" if task.solved else "[.]"


def _print_task(task: Task, solved_local: set[int], show_desc: bool = False) -> None:
    print(f"{_status_mark(task, solved_local)} {task.display_id}  {task.title}")
    print(f"       тема: {task.topic}")
    if show_desc:
        print()
        for line in task.description.strip().splitlines() or [""]:
            print(f"       {line}")
        print()
        print(f"       решение: solutions/{task.slug}/{task.slug}.py")
        print(f"       тесты:   tests/test_{task.slug}.py")
        print(f"       запуск:  dsa-trainer run {task.id}")


def _cmd_list(args: argparse.Namespace) -> int:
    solved_local = completed_ids()
    tasks = all_tasks()
    if args.solved:
        tasks = [task for task in tasks if task.id in solved_local]
    elif args.todo:
        tasks = [task for task in tasks if task.id not in solved_local]
    if args.topic:
        tasks = [task for task in tasks if task.topic.lower() == args.topic.lower()]

    if not tasks:
        print("Задачи не найдены.")
        return 0

    current = None
    for task in tasks:
        if task.topic != current:
            current = task.topic
            print(f"\n{current}")
            print("-" * len(current))
        print(f"  {_status_mark(task, solved_local)} {task.display_id:<3} {task.title}")
    print()
    return 0


def _cmd_show(args: argparse.Namespace) -> int:
    task = get_task(args.task_id)
    if task is None:
        print(f"Задачи №{args.task_id} нет в каталоге.", file=sys.stderr)
        return 2
    _print_task(task, completed_ids(), show_desc=True)
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    task = get_task(args.task_id)
    if task is None:
        print(f"Задачи №{args.task_id} нет в каталоге.", file=sys.stderr)
        return 2
    relative = Path("tests") / f"test_{task.slug}.py"
    target = _repo_root() / relative
    if not target.exists():
        print(f"Файл тестов не найден: {target}", file=sys.stderr)
        return 2

    pytest_args = list(args.pytest_args)
    # argparse.REMAINDER оставляет разделитель '--' в начале, pytest его не любит.
    if pytest_args and pytest_args[0] == "--":
        pytest_args = pytest_args[1:]

    if pytest is None:
        print("pytest не установлен: pip install -r requirements-dev.txt", file=sys.stderr)
        return 2

    # Запускаем pytest в этом процессе: так результат известен без разбора
    # кода возврата дочернего процесса, а прогресс задачи пишется в журнал.
    pytest_main = pytest.main
    exit_code = int(pytest_main([str(relative), "-v", *pytest_args]))
    if exit_code == 0:
        mark_solved(task.id, task.slug)
        print(f"\nЗадача №{task.display_id} решена ✓ ({task.title})")
    return exit_code


def _cmd_stats(args: argparse.Namespace) -> int:
    solved_local = completed_ids()
    total = 0
    done = 0
    for topic, tasks in by_topic().items():
        topic_done = sum(1 for task in tasks if task.id in solved_local)
        total += len(tasks)
        done += topic_done
        bar_len = 20
        filled = round(bar_len * topic_done / len(tasks)) if tasks else 0
        bar = "#" * filled + "." * (bar_len - filled)
        print(f"  {topic:<28} [{bar}] {topic_done:>2}/{len(tasks)}")
    percent = round(100 * done / total) if total else 0
    print()
    print(f"  Итого: {done}/{total} ({percent}%)")
    print(f"  Журнал попыток: {attempts_path()}")
    if not load_progress():
        print("  Пока пусто — начни с `dsa-trainer list --todo`.")
    return 0


def _cmd_reset(args: argparse.Namespace) -> int:
    path = attempts_path()
    if not path.exists():
        print("Журнал попыток пуст.")
        return 0
    if not args.yes:
        answer = input(f"Удалить {path}? [y/N] ").strip().lower()
        if answer not in {"y", "yes", "д", "да"}:
            print("Отменено.")
            return 1
    path.unlink()
    print(f"Удалено: {path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dsa-trainer",
        description="Алгоритмический тренажёр на Python: каталог задач + pytest-автопроверка.",
    )
    parser.add_argument("--version", action="version", version="dsa-trainer 0.1.0")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="показать каталог задач")
    group = p_list.add_mutually_exclusive_group()
    group.add_argument("--solved", action="store_true", help="только решённые")
    group.add_argument("--todo", action="store_true", help="только нерешённые")
    p_list.add_argument("--topic", help="фильтр по теме")
    p_list.set_defaults(func=_cmd_list)

    p_show = sub.add_parser("show", help="показать условие задачи")
    p_show.add_argument("task_id")
    p_show.set_defaults(func=_cmd_show)

    p_run = sub.add_parser("run", help="запустить тесты задачи")
    p_run.add_argument("task_id")
    p_run.add_argument(
        "pytest_args",
        nargs=argparse.REMAINDER,
        help="доп. аргументы pytest (после --)",
    )
    p_run.set_defaults(func=_cmd_run)

    p_stats = sub.add_parser("stats", help="прогресс по темам")
    p_stats.set_defaults(func=_cmd_stats)

    p_reset = sub.add_parser("reset", help="очистить журнал попыток")
    p_reset.add_argument("-y", "--yes", action="store_true", help="без подтверждения")
    p_reset.set_defaults(func=_cmd_reset)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
