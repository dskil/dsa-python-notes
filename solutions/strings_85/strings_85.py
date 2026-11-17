"""№85 · Идиомы Python по умолчанию.

Источник: ``HSEtasks``. Тема: строки.

Здесь собраны привычки «питоновского» кода: срезы, распаковка, list
comprehension, ``enumerate``/``zip``, ``any``/``all``.
"""


def chunks(items: list[int], size: int) -> list[list[int]]:
    """Разбить список на порции ``size`` (последняя может быть короче)."""
    if size <= 0:
        raise ValueError("size должен быть положительным")
    return [items[index : index + size] for index in range(0, len(items), size)]


def enumerate_pairs(items: list[str]) -> list[str]:
    """``['0:a', '1:b']`` через enumerate."""
    return [f"{index}:{value}" for index, value in enumerate(items)]


def is_all_even(numbers: list[int]) -> bool:
    return all(number % 2 == 0 for number in numbers)


def any_negative(numbers: list[int]) -> bool:
    return any(number < 0 for number in numbers)


def main() -> None:
    print(chunks([1, 2, 3, 4, 5], 2))
    print(enumerate_pairs(["a", "b"]))


if __name__ == "__main__":
    main()
