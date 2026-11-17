"""№09 · Палиндром без учёта пробелов, регистра и пунктуации.

Источник: ``Train9.py``. Тема: строки.
"""


def normalize(text: str) -> str:
    """Оставить только буквы и цифры, привести к нижнему регистру."""
    return "".join(symbol for symbol in text if symbol.isalnum()).lower()


def is_palindrome_loose(text: str) -> bool:
    """True, если нормализованная строка — палиндром и она не пустая."""
    clean = normalize(text)
    return bool(clean) and clean == clean[::-1]


def main() -> None:
    print("yes" if is_palindrome_loose("А роза упала на лапу Азора") else "no")


if __name__ == "__main__":
    main()
