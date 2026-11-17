"""№21 · Побайтовое копирование файла.

Источник: ``Train21.py``. Тема: файлы.
"""

from pathlib import Path


def copy_binary(source: str | Path, target: str | Path, block_size: int = 4096) -> int:
    """Скопировать файл порциями по ``block_size`` байт, вернуть число байт."""
    if block_size <= 0:
        raise ValueError("block_size должен быть положительным")
    copied = 0
    with Path(source).open("rb") as source_file, Path(target).open("wb") as target_file:
        while block := source_file.read(block_size):
            target_file.write(block)
            copied += len(block)
    return copied


def main() -> None:
    print(copy_binary("image.jpg", "image_copy.jpg"))


if __name__ == "__main__":
    main()
