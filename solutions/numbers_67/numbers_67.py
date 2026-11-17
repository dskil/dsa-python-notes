"""№67 · Сколько високосных лет на отрезке [left; right].

Источник: ``HSEtasks/numbers/visokosniy_god.py``. Тема: числа.

Через префиксные функции: ``f(r) - f(l - 1)`` — O(1).
"""


def leap_years_up_to(year: int) -> int:
    """Количество високосных лет в диапазоне 1..year."""
    return year // 4 - year // 100 + year // 400


def count_leap_years(left: int, right: int) -> int:
    """Количество високосных лет на отрезке [left; right]."""
    if left > right:
        raise ValueError("left должно быть не больше right")
    return leap_years_up_to(right) - leap_years_up_to(left - 1)


def main() -> None:
    left, right = 1900, 2000
    print(count_leap_years(left, right))


if __name__ == "__main__":
    main()
