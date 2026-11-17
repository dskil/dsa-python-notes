"""Тесты задачи №30."""

from pathlib import Path

import pytest

pytest.importorskip("PIL")


@pytest.fixture()
def png(tmp_path: Path) -> Path:
    from PIL import Image

    path = tmp_path / "img.png"
    Image.new("RGB", (12, 7), "red").save(path)
    return path


def test_image_info(solution, png):
    assert solution.get_image_info(png) == (12, 7, "RGB")


def test_not_an_image(solution, tmp_path: Path):
    broken = tmp_path / "broken.png"
    broken.write_bytes(b"not a png")
    with pytest.raises(ValueError):
        solution.get_image_info(broken)


def test_missing_image(solution, tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        solution.get_image_info(tmp_path / "nope.png")
