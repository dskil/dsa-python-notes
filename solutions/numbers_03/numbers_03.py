"""№03 · Все делители числа, кроме 1 и самого числа.

Источник: ``Train3.py``. Тема: числа.
"""

import math


def proper_divisors(n: int) -> list[int]:
    """Делители ``n``, кроме 1 и самого числа, по возрастанию."""
    if n < 4:
        return []

    divisors: list[int] = []
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            divisors.append(d)
            pair = n // d
            if pair != d and pair != n:
                divisors.append(pair)

    return sorted(divisors)


def count_proper_divisors(n: int) -> int:
    return len(proper_divisors(n))


def main() -> None:
    print(proper_divisors(36))
    print(count_proper_divisors(36))


if __name__ == "__main__":
    main()
