"""№14 · Оставить только латиницу и цифры.

Источник: ``StringRandomTrain/Train14.py``. Тема: строки.
"""

import string

_ASCII_KEEP = set(string.ascii_letters + string.digits)


def keep_ascii_alnum(text: str) -> str:
    """Убрать всё, кроме латинских букв и ASCII-цифр (кириллица тоже уходит)."""
    return "".join(symbol for symbol in text if symbol in _ASCII_KEEP)


def main() -> None:
    print(keep_ascii_alnum("Привет! Как дела? Python3.0"))


if __name__ == "__main__":
    main()
