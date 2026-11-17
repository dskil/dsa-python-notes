"""№24 · tell() и seek(): перечитывание строки.

Источник: ``Train24.py``. Тема: файлы.
"""

from pathlib import Path


def reread_line(filename: str | Path, position: int = 0) -> tuple[str, str]:
    """Прочитать строки ``position + 1`` и ``position + 2`` без \\n."""
    with Path(filename).open("r", encoding="utf-8") as file:
        for _ in range(position):
            if not file.readline():
                raise IndexError(f"В файле нет строки №{position + 1}")
        first = file.readline().rstrip("\n")
        second = file.readline().rstrip("\n")
    return first, second


def main() -> None:
    first, second = reread_line("text.txt", 1)
    print(first)
    print(second)


if __name__ == "__main__":
    main()
