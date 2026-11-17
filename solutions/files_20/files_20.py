"""№20 · Чтение файла порциями (генератор).

Источник: ``FilesTrain/Train20.py``. Тема: файлы.
"""

from pathlib import Path


def read_chunks(filename: str | Path, chunk_size: int = 1024) -> list[str]:
    """Содержимое файла кусками по ``chunk_size`` символов."""
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть положительным")

    chunks: list[str] = []
    with Path(filename).open("r", encoding="utf-8") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            chunks.append(chunk)
    return chunks


def main() -> None:
    for index, chunk in enumerate(read_chunks(input("Файл: "), 256), start=1):
        print(f"===---==={index} порция===---===")
        print(chunk)


if __name__ == "__main__":
    main()
