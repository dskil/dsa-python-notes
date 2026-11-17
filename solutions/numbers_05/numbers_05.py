"""№05 · Числа на отрезке ровно с 6 делителями.

Источник: ``Train5.py``. Тема: числа.
"""

import math


def count_divisors(n: int) -> int:
    """Количество делителей числа (включая 1 и само число)."""
    if n < 1:
        return 0
    count = 0
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            count += 1 if d == n // d else 2
    return count


def numbers_with_divisor_count(start: int, end: int, divisors: int = 6) -> list[int]:
    """Все числа из [start; end] у которых ровно ``divisors`` делителей."""
    return [n for n in range(start, end + 1) if count_divisors(n) == divisors]


def main() -> None:
    found = numbers_with_divisor_count(100, 200)
    print(len(found))
    print(found)


if __name__ == "__main__":
    main()
