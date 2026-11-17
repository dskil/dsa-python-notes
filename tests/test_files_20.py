"""Тесты задачи №20."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


def test_chunks_concatenate_to_file(solution, tmp_path: Path):
    path = tmp_path / "f.txt"
    path.write_text("abcdefghij", encoding="utf-8")
    assert "".join(solution.read_chunks(path, 3)) == "abcdefghij"
    assert solution.read_chunks(path, 3) == ["abc", "def", "ghi", "j"]


def test_empty_file(solution, tmp_path: Path):
    path = tmp_path / "e.txt"
    path.write_text("", encoding="utf-8")
    assert solution.read_chunks(path, 5) == []


def test_unicode_not_split_into_bytes(solution, tmp_path: Path):
    path = tmp_path / "u.txt"
    path.write_text("привет", encoding="utf-8")
    chunks = solution.read_chunks(path, 2)
    assert "".join(chunks) == "привет"


@pytest.mark.parametrize("size", [0, -1])
def test_bad_chunk_size(solution, tmp_path: Path, size):
    path = tmp_path / "f.txt"
    path.write_text("abc", encoding="utf-8")
    with pytest.raises(ValueError):
        solution.read_chunks(path, size)
