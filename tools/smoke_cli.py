"""Запуск: python tools/smoke_cli.py [--full]

Проверяет, что примеры из README работают на живом CLI:

- коротко: ``list``, ``list --todo``, ``show``, ``stats``;
- ``--full``: плюс ``run 2`` и полный прогон ``pytest`` (медленнее).

Скрипт кроссплатформенный: его запускает CI, поэтому никаких оболочек.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(arguments: list[str], env: dict[str, str]) -> int:
    print("$ python", " ".join(arguments), flush=True)
    return subprocess.run([sys.executable, *arguments], cwd=ROOT, env=env).returncode


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    full = "--full" in args

    env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), PYTHONUTF8="1")
    progress = Path(tempfile.mkdtemp()) / "progress.json"
    env["DSA_PROGRESS_FILE"] = str(progress)

    commands = [
        ["-m", "dsa_trainer", "--version"],
        ["-m", "dsa_trainer", "list"],
        ["-m", "dsa_trainer", "list", "--todo"],
        ["-m", "dsa_trainer", "list", "--solved"],
        ["-m", "dsa_trainer", "show", "47"],
        ["-m", "dsa_trainer", "stats"],
    ]
    if full:
        commands.append(["-m", "pytest", "-q"])
        commands.append(["-m", "dsa_trainer", "run", "2", "-q", "-p", "no:warnings"])

    for command in commands:
        code = run(command, env)
        if code != 0:
            print(f"Команда {command} упала с кодом {code}", file=sys.stderr)
            return code

    print("\nВсе проверки прошли.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
