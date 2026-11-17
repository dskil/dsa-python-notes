"""Тесты задачи №18."""

from pathlib import Path
from unittest import mock

import pytest

CASES = {"module": "solution", "cases": []}


def test_reads_ok(solution, tmp_path: Path):
    path = tmp_path / "a.txt"
    path.write_text("hello", encoding="utf-8")
    assert solution.read_text_checked(path) == "hello"


def test_missing_file(solution, tmp_path: Path):
    with pytest.raises(solution.FileNotFoundReadError):
        solution.read_text_checked(tmp_path / "missing.txt")


def test_permission_error(solution, tmp_path: Path):
    path = tmp_path / "p.txt"
    path.write_text("x", encoding="utf-8")
    with mock.patch.object(Path, "read_text", side_effect=PermissionError("denied")):
        with pytest.raises(solution.PermissionReadError):
            solution.read_text_checked(path)


def test_error_is_catchable_as_base(solution, tmp_path: Path):
    with pytest.raises(solution.ReadError):
        solution.read_text_checked(tmp_path / "missing.txt")
