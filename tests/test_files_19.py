"""Тесты задачи №19."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


@pytest.mark.parametrize(
    "content,expected",
    [("", 0), ("a", 1), ("a\n", 1), ("a\nb", 2), ("a\nb\nc\n", 3), ("\n\n", 2)],
)
def test_count_lines(solution, tmp_path: Path, content, expected):
    path = tmp_path / "f.txt"
    path.write_text(content, encoding="utf-8")
    assert solution.count_lines(path) == expected
