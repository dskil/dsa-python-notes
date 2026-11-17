"""Тесты задачи №21."""

from pathlib import Path

import pytest

CASES = {"module": "solution", "cases": []}


@pytest.mark.parametrize("payload", [b"", b"abc", b"\x00\xff" * 3000, bytes(range(256))])
@pytest.mark.parametrize("block", [1, 7, 4096])
def test_copy_binary(solution, tmp_path: Path, payload, block):
    source = tmp_path / "src.bin"
    target = tmp_path / "dst.bin"
    source.write_bytes(payload)
    copied = solution.copy_binary(source, target, block)
    assert copied == len(payload)
    assert target.read_bytes() == payload


def test_copy_overwrites_target(solution, tmp_path: Path):
    source = tmp_path / "s.bin"
    target = tmp_path / "t.bin"
    source.write_bytes(b"new")
    target.write_bytes(b"old-old-old")
    solution.copy_binary(source, target)
    assert target.read_bytes() == b"new"
