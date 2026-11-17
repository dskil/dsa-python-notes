"""№13 · Количество цифр и знаков пунктуации в строке.

Источник: ``StringRandomTrain/Train13.py``. Тема: строки.
"""

import string


def count_digits_and_punctuation(text: str) -> tuple[int, int]:
    """Кортеж (цифры, знаки пунктуации)."""
    digits = sum(1 for symbol in text if symbol.isdigit())
    punctuation = sum(1 for symbol in text if symbol in string.punctuation)
    return digits, punctuation


def main() -> None:
    digits, punctuation = count_digits_and_punctuation(input())
    print("Цифр: ", digits)
    print("Символы: ", punctuation)


if __name__ == "__main__":
    main()
