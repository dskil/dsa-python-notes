"""Тесты задачи №16."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


@pytest.mark.parametrize("start,stop", [(1, 10), (0, 0), (-3, 3), (100, 110)])
def test_write_sum_append(solution, tmp_path: Path, start, stop):
    path = tmp_path / "numbers.txt"
    solution.write_range(path, start, stop)
    expected = sum(range(start, stop + 1))
    assert solution.sum_linked_file(path) == expected

    solution.append_range(path, 11, 13)
    assert solution.sum_linked_file(path) == expected + sum(range(11, 14))


def test_write_overwrites(solution, tmp_path: Path):
    path = tmp_path / "n.txt"
    path.write_text("9\n9\n9\n", encoding="utf-8")
    solution.write_range(path, 1, 2)
    assert path.read_text(encoding="utf-8") == "1\n2\n"
