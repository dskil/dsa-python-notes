"""№02 · Двоичная запись числа: количество единиц и нулей.

Источник: ``Train2.py``. Тема: битовые операции.
"""


def to_binary(n: int) -> str:
    """Двоичная запись ``n`` без префикса ``0b``."""
    return bin(n)[2:]


def count_ones(n: int) -> int:
    """Сколько единиц в двоичной записи числа."""
    return bin(n).count("1")


def count_zeros(n: int) -> int:
    """Сколько нулей в двоичной записи числа (без префикса 0b и ведущих нулей)."""
    return bin(n)[2:].count("0")


def main() -> None:
    number = 2534
    binary = to_binary(number)
    print(binary)
    print(count_ones(number))
    print(count_zeros(number))


if __name__ == "__main__":
    main()
