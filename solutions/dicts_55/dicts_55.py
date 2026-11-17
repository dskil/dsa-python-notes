"""№55 · Анаграммы через словари.

Источник: ``Train55.py``. Тема: словари.
"""

from collections import Counter


def are_anagrams(word1: str, word2: str) -> bool:
    """Одна и та же мультимножественная раскладка букв."""
    return Counter(word1) == Counter(word2)


def main() -> None:
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("", ""))


if __name__ == "__main__":
    main()
