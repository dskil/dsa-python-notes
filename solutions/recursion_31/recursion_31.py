"""№31 · Факториал рекурсией.

Источник: ``Recursion/Train31.py``. Тема: рекурсия.
"""


def factorial(n: int) -> int:
    """n! для n >= 0."""
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    return 1 if n == 0 else n * factorial(n - 1)


def main() -> None:
    print(factorial(10))


if __name__ == "__main__":
    main()
