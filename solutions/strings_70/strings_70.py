"""№70 · Уникальные ли все символы строки.

Источник: ``HSEtasks/strings/all_unique.py``. Тема: строки.
"""


def all_unique(text: str) -> bool:
    """Все символы различны (однострочный вариант через set)."""
    return len(text) == len(set(text))


def first_duplicate(text: str) -> str | None:
    """Первый повторяющийся символ или None."""
    seen: set[str] = set()
    for symbol in text:
        if symbol in seen:
            return symbol
        seen.add(symbol)
    return None


def main() -> None:
    print(all_unique("dgvca"))
    print(first_duplicate("abcda"))


if __name__ == "__main__":
    main()
