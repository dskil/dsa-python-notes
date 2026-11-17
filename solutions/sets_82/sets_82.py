"""№82 · Множества: объединение, пересечение, разность.

Источник: ``HSEtasks/basics/list_dict_set_tuple/sets.py``. Тема: множества.
"""


def union(first: set, second: set) -> set:
    """Элементы, которые есть хотя бы где-то."""
    return first | second


def intersection(first: set, second: set) -> set:
    """Элементы в обоих множествах."""
    return first & second


def symmetric_difference(first: set, second: set) -> set:
    """Элементы, которые есть ровно в одном из множеств."""
    return first ^ second


def difference(first: set, second: set) -> set:
    """Элементы ``first``, которых нет в ``second``."""
    return first - second


def main() -> None:
    cities1 = {"Tokyo", "Toronto", "Moscow", "London"}
    cities2 = {"Tokyo", "Warsaw", "London", "Canberra"}
    print(union(cities1, cities2))
    print(intersection(cities1, cities2))
    print(symmetric_difference(cities1, cities2))


if __name__ == "__main__":
    main()
