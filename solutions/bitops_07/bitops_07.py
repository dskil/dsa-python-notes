"""№07 · Числа на отрезке с ровно 3 единицами в двоичной записи.

Источник: ``Train7.py``. Тема: битовые операции.
"""


def numbers_with_ones(start: int, end: int, ones: int = 3) -> list[int]:
    """Числа из [start; end], в двоичной записи которых ровно ``ones`` единиц."""
    return [n for n in range(start, end + 1) if bin(n).count("1") == ones]


def count_numbers_with_ones(start: int, end: int, ones: int = 3) -> int:
    return len(numbers_with_ones(start, end, ones))


def main() -> None:
    print(count_numbers_with_ones(50, 150))


if __name__ == "__main__":
    main()
