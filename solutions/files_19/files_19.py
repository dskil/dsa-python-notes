"""№19 · Подсчёт строк в файле.

Источник: ``FilesTrain/Train19.py``. Тема: файлы.
"""

from pathlib import Path


def count_lines(filename: str | Path) -> int:
    """Количество строк в файле."""
    with Path(filename).open("r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def main() -> None:
    print(count_lines("numbers.txt"))


if __name__ == "__main__":
    main()
