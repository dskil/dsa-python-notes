"""№01 · Удалить цифры из строки и посчитать длину.

Источник: ``Train1.py``. Тема: строки.
"""


def strip_digits(text: str) -> str:
    """Вернуть строку без цифр (порядок остальных символов сохраняется)."""
    return "".join(symbol for symbol in text if not symbol.isdigit())


def digits_free_length(text: str) -> int:
    """Длина строки после удаления всех цифр."""
    return len(strip_digits(text))


def main() -> None:
    text = "23ffskl1321dfldasdf"
    print(strip_digits(text))
    print(digits_free_length(text))


if __name__ == "__main__":
    main()
