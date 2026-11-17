"""№36 · Способы дойти на +1 и +2 (рекурсия).

Источник: ``Recursion/Train36.py``. Тема: рекурсия.
"""


def count_ways(current: int, target: int) -> int:
    """Число путей от ``current`` до ``target`` шагами +1 и +2."""
    if current > target:
        return 0
    if current == target:
        return 1
    return count_ways(current + 1, target) + count_ways(current + 2, target)


def main() -> None:
    print(count_ways(1, 3))


if __name__ == "__main__":
    main()
