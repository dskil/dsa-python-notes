"""№65 · НОД и НОК.

Источник: ``HSEtasks/numbers/gcd_and_lcm.py``. Тема: числа.
"""

import math


def gcd(a: int, b: int) -> int:
    """НОД через ``math.gcd`` (быстро и корректно для отрицательных)."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """НОК; для нуля — 0."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def main() -> None:
    print(lcm(12, 8))


if __name__ == "__main__":
    main()
