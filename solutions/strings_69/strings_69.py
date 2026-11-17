"""№69 · Наибольший общий префикс-суффикс (бордер) строки.

Источник: ``HSEtasks/strings/longest_prefix_suffix.py``. Тема: строки.

Наивное решение — O(n²); именно так работает функция префиксов в KMP,
и её принято называть ``pi``-функцией.
"""


def longest_prefix_suffix_naive(word: str) -> int:
    """O(n²) — понятно, но для длинных строк медленно."""
    for length in range(len(word) - 1, 0, -1):
        if word[:length] == word[-length:]:
            return length
    return 0


def prefix_function(word: str) -> list[int]:
    """pi[i] = длина наибольшего бордера префикса ``word[:i+1]``."""
    pi = [0] * len(word)
    for index in range(1, len(word)):
        border = pi[index - 1]
        while border and word[index] != word[border]:
            border = pi[border - 1]
        if word[index] == word[border]:
            border += 1
        pi[index] = border
    return pi


def longest_prefix_suffix(word: str) -> int:
    """O(n) через префикс-функцию."""
    return prefix_function(word)[-1] if word else 0


def main() -> None:
    print(longest_prefix_suffix("aabaa"))


if __name__ == "__main__":
    main()
