"""№33 · Сумма цифр числа рекурсией.

Источник: ``Recursion/Train33.py``. Тема: рекурсия.
"""


def digit_sum(n: int) -> int:
    """Сумма цифр неотрицательного целого числа."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def main() -> None:
    print(digit_sum(123))


if __name__ == "__main__":
    main()
