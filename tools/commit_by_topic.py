"""Создать коммиты по темам: python tools/commit_by_topic.py.

Скрипт не стыдится быть маленьким: `git add` в PowerShell с не-ASCII
аргументами ведёт себя странно, поэтому добавляем пути через окружение.

Запуск: python tools/commit_by_topic.py [--dry-run]
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GROUPS = [
    (
        "Строки",
        "strings_12 strings_13 strings_14 strings_15 strings_23 strings_69 strings_70 "
        "strings_71 strings_72 strings_73 strings_74 strings_75 strings_76 strings_77 "
        "strings_78 strings_79 strings_80 strings_85",
    ),
    ("Битовые операции", "bitops_02 bitops_07 bitops_66"),
    (
        "Числа",
        "numbers_03 numbers_05 numbers_60 numbers_61 numbers_62 numbers_63 "
        "numbers_64 numbers_65 numbers_67 numbers_68",
    ),
    ("Списки", "lists_04 lists_08 lists_11 lists_81 lists_83"),
    ("Множества", "sets_56 sets_57 sets_82"),
    ("Словари", "dicts_51 dicts_52 dicts_53 dicts_54 dicts_55 dicts_59 dicts_84"),
    (
        "Файлы",
        "files_16 files_17 files_18 files_19 files_20 files_21 files_22 files_24 "
        "files_25 files_26 files_27 files_28 files_29 files_30",
    ),
    ("Исключения", "errors_86"),
    (
        "Рекурсия",
        "recursion_31 recursion_32 recursion_33 recursion_34 recursion_35 "
        "recursion_36 recursion_37 recursion_38 recursion_39 recursion_40 "
        "recursion_41 recursion_42 recursion_43 recursion_44 recursion_45 "
        "recursion_46 recursion_47 recursion_48 recursion_49 recursion_50 "
        "recursion_58",
    ),
]


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    if result.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    for topic, slugs in GROUPS:
        paths = []
        for slug in slugs.split():
            paths += [f"solutions/{slug}", f"tests/test_{slug}.py"]
        missing = [p for p in paths if not (ROOT / p).exists()]
        if missing:
            raise SystemExit(f"Нет файлов: {missing}")

        if dry_run:
            print(f"[{topic}] {len(paths)} путей")
            continue

        git("add", "--", *paths)
        staged = git("diff", "--cached", "--name-only").splitlines()
        message = f"feat(solutions): тема «{topic}» — задачи и тесты"
        git("commit", "-m", message)
        print(f"[{topic}] {len(staged)} файлов -> {message}")

    # make_todo.py — отдельным коммитом: это инструмент, а не задачи.
    if not dry_run and (ROOT / "tools/make_todo.py").exists():
        git("add", "--", "tools/make_todo.py")
        git("commit", "-m", "feat(tools): make_todo — превращает решения в заготовки")
        print("[tools] make_todo.py")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
