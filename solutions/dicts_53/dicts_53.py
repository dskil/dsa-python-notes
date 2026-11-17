"""№53 · Частоты элементов списка.

Источник: ``Train53.py``. Тема: словари.
"""

from collections import Counter


def frequency(numbers: list[int]) -> dict[int, int]:
    """Сколько раз встречается каждое число."""
    counts: dict[int, int] = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts


def most_common(numbers: list[int]) -> int:
    """Самое частое число (при равенстве — меньшее)."""
    if not numbers:
        raise ValueError("Пустой список")
    counts = frequency(numbers)
    return min(counts, key=lambda value: (-counts[value], value))


def most_common_counter(numbers: list[int]) -> int:
    """То же через ``Counter.most_common`` — компактнее, но порядок ничьих другой."""
    if not numbers:
        raise ValueError("Пустой список")
    return Counter(numbers).most_common(1)[0][0]


def main() -> None:
    print(frequency([1, 2, 2, 3, 3, 3, 4, 1, 2]))
    print(most_common([1, 2, 2, 3, 3, 3, 4, 1, 2]))


if __name__ == "__main__":
    main()
