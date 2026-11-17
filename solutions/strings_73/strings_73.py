"""№73 · Палиндром (простой).

Источник: ``HSEtasks/strings/is_palindrome.py``. Тема: строки.
"""


def is_palindrome(text: str) -> bool:
    """True, если строка читается одинаково в обе стороны (без нормализации)."""
    return text == text[::-1]


def main() -> None:
    print(is_palindrome("asa"))


if __name__ == "__main__":
    main()
