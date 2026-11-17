"""№37 · Сумма 1..n рекурсией.

Источник: ``Recursion/Train37.py``. Тема: рекурсия.
"""


def sum_to_n(n: int) -> int:
    """1 + 2 + ... + n; для n = 0 вернуть 0."""
    if n < 0:
        raise ValueError("Число должно быть положительным")
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)


def main() -> None:
    print(sum_to_n(5))


if __name__ == "__main__":
    main()
