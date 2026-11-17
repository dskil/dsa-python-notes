"""№50 · Все подмножества (power set).

Источник: ``Recursion/Train50.py``. Тема: рекурсия.

Порядок подмножеств зафиксирован и проверяется тестами.
"""


def power_set(items: list[int]) -> list[list[int]]:
    """Все подмножества, включая пустое и исходное.

    Порядок: сначала подмножества без первого элемента, затем с ним.
    """
    if not items:
        return [[]]
    head, rest = items[0], items[1:]
    without: list[list[int]] = []
    with_head: list[list[int]] = []
    for subset in power_set(rest):
        without.append(subset)
        with_head.append([head, *subset])
    return without + with_head


def main() -> None:
    print(power_set([1, 2, 3]))


if __name__ == "__main__":
    main()
