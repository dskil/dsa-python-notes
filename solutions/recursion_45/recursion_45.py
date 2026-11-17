"""№45 · Сумма элементов вложенных списков.

Источник: ``Recursion/Train45.py``. Тема: рекурсия.

Для простых ``int`` внутри списков работает ``sum()``; для произвольной
вложенности нужна рекурсия.
"""

from collections.abc import Iterable


def deep_sum(items: Iterable) -> int:
    total = 0
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            total += deep_sum(item)
        elif isinstance(item, int) and not isinstance(item, bool):
            total += item
    return total


def main() -> None:
    print(deep_sum([1, [2, 3], 4, [5, [6, 7]]]))


if __name__ == "__main__":
    main()
