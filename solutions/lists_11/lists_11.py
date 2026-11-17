"""№11 · Пересечение двух списков в порядке возрастания.

Источник: ``StringRandomTrain/Train11.py``. Тема: списки.
"""


def intersection(numbers1: list[int], numbers2: list[int]) -> list[int]:
    """Общие элементы (без повторов) по возрастанию."""
    return sorted(set(numbers1) & set(numbers2))


def format_intersection(numbers1: list[int], numbers2: list[int]) -> str:
    """Строка для вывода: числа через пробел или "Пусто"."""
    common = intersection(numbers1, numbers2)
    return " ".join(map(str, common)) if common else "Пусто"


def main() -> None:
    print(format_intersection([1, 5, 9], [5, 2, 1]))


if __name__ == "__main__":
    main()
