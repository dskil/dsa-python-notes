"""№84 · Словари: обновление и ``get``.

Источник: ``HSEtasks/basics/list_dict_set_tuple/dictionary.py``. Тема: словари.
"""


def merge_dicts(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    """Новый словарь; при совпадении ключей побеждает ``second``."""
    return first | second


def increment(data: dict[str, int], key: str, delta: int = 1) -> int:
    """Прибавить ``delta`` к значению и вернуть новое значение."""
    data[key] = data.get(key, 0) + delta
    return data[key]


def key_with_max_value(data: dict[str, int]) -> str | None:
    """Ключ с максимальным значением; ничья решается по имени ключа."""
    if not data:
        return None
    return max(data, key=lambda key: (data[key], key))


def main() -> None:
    info = {"name": "John", "age": 21}
    print(merge_dicts(info, {"age": 26, "city": "NY"}))
    print(increment(info, "age", 5))


if __name__ == "__main__":
    main()
