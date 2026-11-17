"""№04 · Соседние пары: оба числа нечётные, сумма кратна 5.

Источник: ``Train4.py``. Тема: списки.
"""


def count_special_pairs(numbers: list[int]) -> int:
    """Количество пар соседних элементов: оба нечётные, сумма кратна 5."""
    count = 0
    for index in range(len(numbers) - 1):
        left, right = numbers[index], numbers[index + 1]
        if left % 2 == 1 and right % 2 == 1 and (left + right) % 5 == 0:
            count += 1
    return count


def max_special_pair_sum(numbers: list[int]) -> int:
    """Максимальная сумма среди подходящих пар или 0, если пар нет."""
    best = 0
    for index in range(len(numbers) - 1):
        left, right = numbers[index], numbers[index + 1]
        if left % 2 == 1 and right % 2 == 1 and (left + right) % 5 == 0:
            best = max(best, left + right)
    return best


def main() -> None:
    numbers = [15, 20, 25, 30, 35, 45]
    print(count_special_pairs(numbers))
    print(max_special_pair_sum(numbers))


if __name__ == "__main__":
    main()
