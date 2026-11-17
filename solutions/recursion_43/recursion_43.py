"""№43 · Количество элементов списка рекурсией.

Источник: ``Recursion/Train43.py``. Тема: рекурсия.
"""


def count_items(items: list) -> int:
    if not items:
        return 0
    return 1 + count_items(items[1:])


def main() -> None:
    print(count_items([1, 2, 3, 4]))
    print(count_items([]))


if __name__ == "__main__":
    main()
