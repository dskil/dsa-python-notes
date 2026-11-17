"""№26 · Замена разделителя в файле на месте.

Источник: ``Train26.py``. Тема: файлы.
"""

from pathlib import Path


def replace_in_file(filename: str | Path, old: str, new: str) -> int:
    """Заменить ``old`` на ``new`` во всём файле, вернуть число замен."""
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    updated = text.replace(old, new)
    path.write_text(updated, encoding="utf-8")
    return text.count(old)


def main() -> None:
    path = Path("list.txt")
    path.write_text(
        "Анна, Иван, Мария, Петр, Ольга, Сергей, Елена, Дмитрий, Татьяна, Андрей",
        encoding="utf-8",
    )
    print(replace_in_file(path, ",", ";"))


if __name__ == "__main__":
    main()
