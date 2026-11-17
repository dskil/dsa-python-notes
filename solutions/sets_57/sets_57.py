"""№57 · Уникальные элементы: preserve order и множества.

Источник: пустой ``Train57.py`` — задача придумана как продолжение тренировок
на множества. Тема: словари.
"""


def unique_in_order(items: list[int]) -> list[int]:
    """Убрать повторы, сохранив порядок первого появления."""
    seen: set[int] = set()
    result: list[int] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def train56_noisy_letters_count(text: str) -> int:
    """Сколько различных символов в строке."""
    return len(set(text))


def main() -> None:
    print(unique_in_order([3, 1, 3, 2, 1]))


if __name__ == "__main__":
    main()
