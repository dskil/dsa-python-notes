"""Тесты задачи №24."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


def test_reread_line(solution, tmp_path: Path):
    path = tmp_path / "t.txt"
    path.write_text("one\ntwo\nthree\n", encoding="utf-8")
    assert solution.reread_line(path, 1) == ("two", "three")
    assert solution.reread_line(path, 0) == ("one", "two")


def test_out_of_range(solution, tmp_path: Path):
    path = tmp_path / "t.txt"
    path.write_text("one\n", encoding="utf-8")
    with pytest.raises(IndexError):
        solution.reread_line(path, 5)
