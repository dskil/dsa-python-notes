"""Тест CLI: команды не падают и печатают ожидаемые блоки."""

from __future__ import annotations

import json

import pytest

import dsa_trainer.cli as cli
from dsa_trainer.catalog import all_tasks, get_task, resolve_task_id
from dsa_trainer.cli import main


def test_catalog_has_every_task_once():
    tasks = all_tasks()
    assert len(tasks) == 86
    assert [task.id for task in tasks] == list(range(1, 87))


def test_get_task_accepts_padded_numbers():
    assert get_task("07") is not None
    assert get_task(7) is not None
    assert get_task("007") is not None
    assert get_task(999) is None


def test_resolve_task_id_rejects_garbage():
    with pytest.raises(ValueError):
        resolve_task_id("abc")
    with pytest.raises(ValueError):
        resolve_task_id(0)


def test_cli_list(capsys):
    assert main(["list"]) == 0
    output = capsys.readouterr().out
    assert "Рекурсия" in output
    assert "Ханойские башни" in output


def test_cli_list_topic(capsys):
    assert main(["list", "--topic", "Числа"]) == 0
    output = capsys.readouterr().out
    assert "Банкомат" in output
    assert "Ханойские башни" not in output


def test_cli_show(capsys):
    assert main(["show", "47"]) == 0
    output = capsys.readouterr().out
    assert "hanoi(" in output
    assert "solutions/recursion_47/recursion_47.py" in output


def test_cli_show_unknown_task(capsys):
    assert main(["show", "999"]) == 2
    assert capsys.readouterr().err


def test_cli_stats_and_progress(capsys, tmp_path, monkeypatch):
    progress = tmp_path / "progress.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(progress))
    solved = {"1": {"slug": "strings_01", "solved_at": "x"}}
    progress.write_text(json.dumps(solved), encoding="utf-8")

    assert main(["stats"]) == 0
    output = capsys.readouterr().out
    assert "1/86" in output
    assert "Строки" in output
    assert str(progress) in output


def test_cli_run_marks_task_solved(tmp_path, monkeypatch):
    """Фейковый ``pytest.main`` — тест не запускает вложенный pytest."""
    progress = tmp_path / "progress.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(progress))
    calls: list[list[str]] = []

    def fake_pytest_main(args):
        calls.append(list(args))
        return 0

    monkeypatch.setattr(cli.pytest, "main", fake_pytest_main)

    assert main(["run", "2", "-q"]) == 0
    assert calls, "pytest.main не вызван"
    assert calls[0][0].replace("\\", "/") == "tests/test_bitops_02.py"
    assert "-q" in calls[0]
    data = json.loads(progress.read_text(encoding="utf-8"))
    assert data["2"]["slug"] == "bitops_02"


def test_cli_run_failure_does_not_mark(tmp_path, monkeypatch):
    progress = tmp_path / "progress.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(progress))
    monkeypatch.setattr(cli.pytest, "main", lambda args: 1)

    assert main(["run", "2"]) == 1
    assert not progress.exists()


def test_cli_run_unknown_task(capsys):
    assert main(["run", "999"]) == 2


def test_cli_reset(capsys, tmp_path, monkeypatch):
    progress = tmp_path / "progress.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(progress))
    progress.write_text("{}", encoding="utf-8")
    assert main(["reset", "-y"]) == 0
    assert not progress.exists()
    assert "Удалено" in capsys.readouterr().out
