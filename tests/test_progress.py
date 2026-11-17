"""Тесты журнала прогресса: пути, битые файлы, отметки."""

from __future__ import annotations

import json

from dsa_trainer import progress


def test_progress_path_from_env(tmp_path, monkeypatch):
    target = tmp_path / "p.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(target))
    assert progress.attempts_path() == target


def test_progress_path_default(monkeypatch):
    monkeypatch.delenv("DSA_PROGRESS_FILE", raising=False)
    path = progress.attempts_path()
    assert path.name == ".dsa_progress.json"
    assert path.parent == progress.repo_root()


def test_load_progress_missing_file(tmp_path, monkeypatch):
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(tmp_path / "nope.json"))
    assert progress.load_progress() == {}


def test_load_progress_broken_json(tmp_path, monkeypatch):
    path = tmp_path / "p.json"
    path.write_text("{not json", encoding="utf-8")
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(path))
    assert progress.load_progress() == {}


def test_load_progress_not_a_dict(tmp_path, monkeypatch):
    path = tmp_path / "p.json"
    path.write_text("[1, 2, 3]", encoding="utf-8")
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(path))
    assert progress.load_progress() == {}


def test_mark_solved_then_completed(tmp_path, monkeypatch):
    path = tmp_path / "nested" / "p.json"
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(path))
    progress.mark_solved(47, "recursion_47")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["47"]["slug"] == "recursion_47"
    assert data["47"]["solved_at"]
    assert progress.completed_ids() == {47}


def test_completed_ids_ignores_garbage_keys(tmp_path, monkeypatch):
    path = tmp_path / "p.json"
    path.write_text(json.dumps({"1": {}, "abc": {}}), encoding="utf-8")
    monkeypatch.setenv("DSA_PROGRESS_FILE", str(path))
    assert progress.completed_ids() == {1}
