"""№25 · Чтение последних байт файла.

Источник: ``Train25.py``. Тема: файлы.
"""

from pathlib import Path


def read_tail_bytes(filename: str | Path, count: int) -> bytes:
    """Последние ``count`` байт файла (меньше, если файл короче)."""
    if count < 0:
        raise ValueError("count не может быть отрицательным")
    with Path(filename).open("rb") as file:
        file.seek(0, 2)
        size = file.tell()
        file.seek(max(size - count, 0))
        return file.read()


def main() -> None:
    path = Path("text.txt")
    path.write_text("abcdefghijklm", encoding="utf-8")
    tail = read_tail_bytes(path, 10)
    print(tail)
    print(tail.decode("utf-8"))
    print(tail.hex())


if __name__ == "__main__":
    main()
