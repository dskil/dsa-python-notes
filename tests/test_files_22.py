"""Тесты задачи №22."""

from pathlib import Path


def test_to_hex(solution):
    assert solution.to_hex(b"\x00\x01\x02\x03\xff") == "00010203ff"
    assert solution.to_hex(b"\xde\xad\xbe\xef") == "deadbeef"
    assert solution.to_hex(b"") == ""


def test_roundtrip(solution):
    raw = bytes(range(256))
    assert bytes.fromhex(solution.to_hex(raw)) == raw


def test_read_hex(solution, tmp_path: Path):
    path = tmp_path / "data.bin"
    path.write_bytes(bytes(range(5)))
    assert solution.read_hex(path) == "0001020304"
