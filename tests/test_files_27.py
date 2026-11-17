"""Тесты задачи №27."""

from pathlib import Path

CASES = {"module": "solution", "cases": []}


def test_write_and_read_temp(solution):
    name, content, hex_view = solution.write_and_read_temp(b"temp data")
    assert Path(name).exists() is False
    assert content == b"temp data"
    assert hex_view == b"temp data".hex()


def test_empty_payload(solution):
    _, content, hex_view = solution.write_and_read_temp(b"")
    assert content == b""
    assert hex_view == ""
