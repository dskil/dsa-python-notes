"""Тест tools/start.py: стартовый экран для новичка."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import start  # noqa: E402


def test_list_shows_all_tasks(capsys):
    assert start.main(["--list"]) == 0
    output = capsys.readouterr().out
    assert output.count("\n") >= 86
    assert "01  Удалить цифры" in output
    assert "[x] — ты уже решил" in output


def test_show_task_for_known_number(capsys, tmp_path, monkeypatch):
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(tmp_path / "p.json"))
    assert start.main(["33", "--only-show"]) == 0
    output = capsys.readouterr().out
    assert "ЗАДАЧА №33" in output
    assert (
        "solutions\\recursion_33\\recursion_33.py" in output or "solutions/recursion_33" in output
    )
    assert "digit_sum" in output
    assert "python -m pytest tests/test_recursion_33.py -v" in output


def test_unknown_task(capsys, tmp_path, monkeypatch):
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(tmp_path / "p.json"))
    assert start.main(["999"]) == 2
    assert "Нет задачи №999" in capsys.readouterr().out


def test_first_unsolved_task_is_picked(capsys, tmp_path, monkeypatch):
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(tmp_path / "p.json"))
    assert start.main(["--only-show"]) == 0
    output = capsys.readouterr().out
    assert re.search(r"ЗАДАЧА №01", output), "без прогресса берётся первая задача"
