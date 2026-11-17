"""№71 · Длина последнего слова.

Источник: ``HSEtasks/strings/length_of_last_word.py``. Тема: строки.
"""


def length_of_last_word(text: str) -> int:
    """Длина последнего слова; пустая строка — 0."""
    words = text.split()
    return len(words[-1]) if words else 0


def main() -> None:
    print(length_of_last_word("python is"))


if __name__ == "__main__":
    main()
