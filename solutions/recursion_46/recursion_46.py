"""№46 · Бинарный поиск (рекурсивный и итеративный).

Источник: ``Recursion/Train46.py``. Тема: рекурсия/поиск.
"""

from collections.abc import Sequence


def binary_search_recursive(items: Sequence[int], target: int) -> bool:
    if not items:
        return False
    middle = len(items) // 2
    if items[middle] == target:
        return True
    if items[middle] > target:
        return binary_search_recursive(items[:middle], target)
    return binary_search_recursive(items[middle + 1 :], target)


def binary_search_index(items: Sequence[int], target: int) -> int:
    """Индекс ``target`` в отсортированном списке или -1."""
    left, right = 0, len(items) - 1
    while left <= right:
        middle = (left + right) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search_recursive(numbers, 2))
    print(binary_search_index(numbers, 2))


if __name__ == "__main__":
    main()
