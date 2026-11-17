"""№52 · Базовые операции со словарём.

Источник: ``Train52.py``. Тема: словари.
"""


def update_and_check(data: dict[str, int], key: str, delta: int) -> dict[str, int]:
    """Прибавить ``delta`` к ``data[key]`` (ключа нет — начать с 0)."""
    data[key] = data.get(key, 0) + delta
    return data


def safe_get(data: dict[str, int], key: str, default: int = 0) -> int:
    return data.get(key, default)


def invert(data: dict[str, int]) -> dict[int, str]:
    """Словарь ключ->значение, который работает и в обратную сторону."""
    return {value: key for key, value in data.items()}


def main() -> None:
    data = {"x": 10, "y": 40}
    print(update_and_check(data, "x", -20))
    print(safe_get(data, "q", 0))
    print(invert(data))


if __name__ == "__main__":
    main()
