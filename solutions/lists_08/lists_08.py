"""№08 · Второе по величине число в списке.

Источник: ``Train8.py``. Тема: списки.
"""


def second_largest(numbers: list[int]) -> int:
    """Второе по величине (различное) значение; ValueError, если его нет."""
    unique = sorted(set(numbers), reverse=True)
    if len(unique) < 2:
        raise ValueError("Нужно минимум два различных значения")
    return unique[1]


def main() -> None:
    print(second_largest([5, 3, 9, 1]))


if __name__ == "__main__":
    main()
