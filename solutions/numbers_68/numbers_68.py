"""№68 · Положительные чётные целые числа.

Источник: ``HSEtasks/numbers/count_positive_even_ints.py``. Тема: числа.

Ловушка: ``float`` вида ``2.0`` — тоже целое; ``bool`` — нет, хотя
``True == 1``.
"""


def is_positive_even_int(value: object) -> bool:
    """True, если значение — положительное чётное целое."""
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return value > 0 and value % 2 == 0
    if isinstance(value, float):
        return value.is_integer() and value > 0 and int(value) % 2 == 0
    return False


def count_positive_even_ints(values: list) -> int:
    return sum(1 for value in values if is_positive_even_int(value))


def main() -> None:
    print(count_positive_even_ints([2.0, 3.5, -4.0, 6.0, 7, 0.0]))


if __name__ == "__main__":
    main()
