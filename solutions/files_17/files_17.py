"""№17 · Безопасное чтение файла: список строк без переводов строк.

Источник: ``FilesTrain/Train17.py``. Тема: файлы.
"""

from pathlib import Path


def read_lines_safe(filename: str | Path) -> list[str]:
    """Прочитать файл построчно (без \\n). Если файла нет — вернуть []."""
    try:
        with Path(filename).open("r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def main() -> None:
    print(read_lines_safe("test17.txt"))


if __name__ == "__main__":
    main()
