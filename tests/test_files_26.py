"""Тесты задачи №26."""

from pathlib import Path

CASES = {"module": "solution", "cases": []}


def test_replace_in_file(solution, tmp_path: Path):
    path = tmp_path / "list.txt"
    path.write_text("a, b, c", encoding="utf-8")
    assert solution.replace_in_file(path, ",", ";") == 2
    assert path.read_text(encoding="utf-8") == "a; b; c"


def test_no_matches(solution, tmp_path: Path):
    path = tmp_path / "list.txt"
    path.write_text("abc", encoding="utf-8")
    assert solution.replace_in_file(path, ",", ";") == 0
    assert path.read_text(encoding="utf-8") == "abc"


def test_unicode(solution, tmp_path: Path):
    path = tmp_path / "u.txt"
    path.write_text("привет мир", encoding="utf-8")
    assert solution.replace_in_file(path, " ", "_") == 1
    assert path.read_text(encoding="utf-8") == "привет_мир"
