"""№58 · Вложенный подсчёт: деревья списков.

Источник: пустой ``Train58.py`` — задача-продолжение на рекурсию по
вложенным структурам. Тема: рекурсия.
"""


def max_depth(items: list) -> int:
    """Глубина вложенности списка: ``[1, [2]]`` -> 2, ``[]`` -> 1."""
    if not isinstance(items, list):
        return 0
    if not items:
        return 1
    return 1 + max((max_depth(item) for item in items if isinstance(item, list)), default=0)


def flatten(items: list) -> list:
    """Развернуть произвольную вложенность списков в плоский список (порядок сохраняется)."""
    result: list = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def main() -> None:
    print(max_depth([1, [2, [3, [4]]]]))
    print(flatten([1, [2, [3, [4]]], 5]))


if __name__ == "__main__":
    main()
