"""№41 · НОД (алгоритм Евклида, рекурсия).

Источник: ``Recursion/Train41.py``. Тема: рекурсия.
"""


def gcd(a: int, b: int) -> int:
    """Наибольший общий делитель, всегда неотрицательный."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)


def main() -> None:
    print(gcd(56, 16))


if __name__ == "__main__":
    main()
