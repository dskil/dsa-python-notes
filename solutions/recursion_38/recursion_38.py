"""№38 · Разворот строки рекурсией.

Источник: ``Recursion/Train38.py``. Тема: рекурсия.
"""


def reverse_string(text: str) -> str:
    """Строка в обратном порядке без использования срезов."""
    if not text:
        return ""
    return reverse_string(text[1:]) + text[0]


def main() -> None:
    print(reverse_string("hello"))


if __name__ == "__main__":
    main()
