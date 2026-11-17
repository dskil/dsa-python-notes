"""№48 · Слияние двух отсортированных списков.

Источник: ``Recursion/Train48.py``. Тема: рекурсия/сортировка.
"""

from collections.abc import Sequence


def merge(left: Sequence[int], right: Sequence[int]) -> list[int]:
    """Рекурсивное слияние двух отсортированных последовательностей."""
    if not left:
        return list(right)
    if not right:
        return list(left)
    if left[0] <= right[0]:
        return [left[0], *merge(left[1:], right)]
    return [right[0], *merge(left, right[1:])]


def main() -> None:
    print(merge([1, 2, 4], [3, 5, 6]))


if __name__ == "__main__":
    main()
