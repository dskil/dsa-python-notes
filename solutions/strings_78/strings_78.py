"""№78 · Базовая работа со строками (методы и join).

Источник: ``HSEtasks/basics/strings.py``. Тема: строки.
"""


def normalize(text: str) -> str:
    """Убрать пробелы по краям."""
    return text.strip()


def first_word(text: str) -> str:
    """Первое слово (по запятым и пробелам); пустая строка — ValueError."""
    words = text.replace(",", " ").split()
    if not words:
        raise ValueError("Нет слов")
    return words[0]


def join_with(words: list[str], separator: str = "1") -> str:
    return separator.join(words)


def main() -> None:
    text = "  Привет, Мир!  "
    print(repr(normalize(text)))
    print(text.find("Мир"))
    print(join_with(text.split(",")))


if __name__ == "__main__":
    main()
