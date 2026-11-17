"""№51 · Подсчёт частоты букв в слове.

Источник: ``Train51.py``. Тема: словари.
"""

from collections import Counter


def letter_counts(word: str) -> dict[str, int]:
    """Сколько раз встречается каждая буква (порядок — по первому появлению)."""
    counts: dict[str, int] = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def letter_counts_counter(word: str) -> dict[str, int]:
    """То же самое, но одной строкой через ``collections.Counter``."""
    return dict(Counter(word))


def main() -> None:
    print(letter_counts("asdaaassdf"))
    print(letter_counts_counter("asdaaassdf"))


if __name__ == "__main__":
    main()
