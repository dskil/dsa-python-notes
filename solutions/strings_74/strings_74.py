"""№74 · Самый частый символ: количество вхождений.

Источник: ``HSEtasks/strings/most_frequent_count.py``. Тема: строки.
"""

from collections import Counter


def most_frequent_count(text: str) -> int:
    """Сколько раз встречается самый частый символ; пустая строка — 0."""
    if not text:
        return 0
    counts: dict[str, int] = {}
    for symbol in text:
        counts[symbol] = counts.get(symbol, 0) + 1
    return max(counts.values())


def most_frequent_count_counter(text: str) -> int:
    return max(Counter(text).values(), default=0)


def main() -> None:
    print(most_frequent_count("aabbbc"))


if __name__ == "__main__":
    main()
