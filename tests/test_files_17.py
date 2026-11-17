"""Тесты задачи №17."""

from pathlib import Path

CASES = {"module": "solution", "cases": []}


def test_reads_lines(solution, tmp_path: Path):
    path = tmp_path / "f.txt"
    path.write_text("1\n2\ntext\n", encoding="utf-8")
    assert solution.read_lines_safe(path) == ["1", "2", "text"]


def test_missing_file_returns_empty(solution, tmp_path: Path):
    assert solution.read_lines_safe(tmp_path / "nope.txt") == []


def test_unicode(solution, tmp_path: Path):
    path = tmp_path / "u.txt"
    path.write_text("привет\nмир\n", encoding="utf-8")
    assert solution.read_lines_safe(path) == ["привет", "мир"]
