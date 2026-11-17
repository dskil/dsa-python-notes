"""№49 · Сортировка слиянием.

Источник: ``Recursion/Train49.py``. Тема: рекурсия/сортировка.
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    """Слить два отсортированных списка (итеративно, O(n))."""
    result: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return list(items)
    middle = len(items) // 2
    return merge(merge_sort(items[:middle]), merge_sort(items[middle:]))


def main() -> None:
    print(merge_sort([1, 2, 3, 7, 8, 4]))


if __name__ == "__main__":
    main()
