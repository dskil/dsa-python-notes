"""№81 · Списки: сортировка, вставка, объединение.

Источник: ``HSEtasks/basics/list_dict_set_tuple/lists.py``. Тема: списки.
"""


def sorted_desc(items: list[str]) -> list[str]:
    """Новая копия, отсортированная по убыванию (исходный не меняется)."""
    return sorted(items, reverse=True)


def insert_at(items: list[str], index: int, value: str) -> list[str]:
    """Новая копия с ``value`` на позиции ``index``; соседи не затираются.

    Возвращаем копию, а не меняем аргумент: мутировать вход — частый баг.
    """
    updated = list(items)
    updated.insert(index, value)
    return updated


def merge_lists(items: list[str], others: list[str]) -> list[str]:
    """Новый список из обоих (== ``+``), без изменения аргументов."""
    return [*items, *others]


def main() -> None:
    fruits = ["apple", "banana", "orange"]
    print(sorted_desc(fruits))
    print(merge_lists(fruits, ["tomato"]))


if __name__ == "__main__":
    main()
