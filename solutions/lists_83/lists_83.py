"""№83 · Кортежи.

Источник: ``HSEtasks/basics/list_dict_set_tuple/tuple.py``. Тема: списки.
"""


def add_to_tuple(items: tuple[str, ...], value: str) -> tuple[str, ...]:
    """Кортеж + новый элемент (без изменения исходного)."""
    return (*items, value)


def safe_index(items: tuple, value: object) -> int:
    """Индекс элемента или -1, если его нет."""
    try:
        return items.index(value)
    except ValueError:
        return -1


def main() -> None:
    fruits = ("Apple", "Banana", "Kiwi")
    print(add_to_tuple(fruits, "Pineapple"))
    print(safe_index(fruits, "Kiwi"))


if __name__ == "__main__":
    main()
