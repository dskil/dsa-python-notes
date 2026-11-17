"""№22 · Hex-представление байтов.

Источник: ``Train23.py`` (в исходнике номер файла не совпадает с номером задачи).
Тема: файлы.
"""

from pathlib import Path

PAYLOAD = b"\x00\x01\x02\x03\xff"


def to_hex(raw: bytes) -> str:
    """Байты в hex-строке в нижнем регистре."""
    return raw.hex()


def read_hex(filename: str | Path) -> str:
    """Hex-представление содержимого файла."""
    return Path(filename).read_bytes().hex()


def main() -> None:
    path = Path("data.bin")
    path.write_bytes(PAYLOAD)
    print(read_hex(path))


if __name__ == "__main__":
    main()
