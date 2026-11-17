"""№16 · Запись чисел в файл, подсчёт суммы и дозапись.

Источник: ``FilesTrain/Train16.py``. Тема: файлы.
"""

from pathlib import Path


def write_range(path: Path, start: int, stop: int) -> None:
    """Перезаписать файл числами ``start..stop`` (по одному в строке)."""
    path.write_text("\n".join(str(n) for n in range(start, stop + 1)) + "\n", encoding="utf-8")


def sum_linked_file(path: Path) -> int:
    """Сумма чисел из файла (по одному числу в строке)."""
    return sum(int(line) for line in path.read_text(encoding="utf-8").split())


def append_range(path: Path, start: int, stop: int) -> None:
    """Дописать в файл числа ``start..stop``."""
    with path.open("a", encoding="utf-8") as file:
        for n in range(start, stop + 1):
            file.write(f"{n}\n")


def main() -> None:
    path = Path("numbers.txt")
    write_range(path, 1, 10)
    print(sum_linked_file(path))
    append_range(path, 11, 13)


if __name__ == "__main__":
    main()
