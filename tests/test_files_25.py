"""Тесты задачи №25."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


@pytest.mark.parametrize(
    "data,count,expected",
    [(b"abcdef", 2, b"ef"), (b"abc", 10, b"abc"), (b"abc", 0, b""), (b"", 5, b"")],
)
def test_read_tail_bytes(solution, tmp_path: Path, data, count, expected):
    path = tmp_path / "f.bin"
    path.write_bytes(data)
    assert solution.read_tail_bytes(path, count) == expected


def test_negative_count(solution, tmp_path: Path):
    path = tmp_path / "f.bin"
    path.write_bytes(b"abc")
    with pytest.raises(ValueError):
        solution.read_tail_bytes(path, -1)
