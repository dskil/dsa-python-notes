"""№42 · Возведение в степень рекурсией (линейное).

Источник: ``Recursion/Train42.py``. Тема: рекурсия.

Для бинарного возведения в степень см. задачу №46.
"""


def power(base: int, exponent: int) -> int:
    """``base ** exponent`` для exponent >= 0."""
    if exponent < 0:
        raise ValueError("Ожидался неотрицательный показатель степени")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def main() -> None:
    print(power(2, 10))


if __name__ == "__main__":
    main()
