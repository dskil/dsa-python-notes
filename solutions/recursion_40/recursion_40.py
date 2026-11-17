"""№40 · Палиндром рекурсией (через срезы).

Источник: ``Recursion/Train40.py``. Тема: рекурсия.

Для палиндрома с игнорированием регистра и пунктуации см. №09.
"""


def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


def main() -> None:
    print(is_palindrome("шалаш"))


if __name__ == "__main__":
    main()
