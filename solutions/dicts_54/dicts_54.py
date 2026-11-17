"""№54 · Самая частая буква.

Источник: ``Train54.py``. Тема: словари.
"""


def letter_frequencies(word: str) -> dict[str, int]:
    letters: dict[str, int] = {}
    for letter in word:
        letters[letter] = letters.get(letter, 0) + 1
    return letters


def most_frequent_letter(word: str) -> tuple[str, int]:
    """(буква, частота); при ничьей — первая по алфавиту."""
    if not word:
        raise ValueError("Пустая строка")
    counts = letter_frequencies(word)
    best = min(counts, key=lambda letter: (-counts[letter], letter))
    return best, counts[best]


def main() -> None:
    print(letter_frequencies("абракадабра"))
    print(most_frequent_letter("абракадабра"))


if __name__ == "__main__":
    main()
