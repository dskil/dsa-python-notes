"""№06 · Самая длинная подстрока из цифр.

Источник: ``Train6.py``. Тема: строки.
"""


def longest_digit_run(text: str) -> str:
    """Самая длинная непрерывная подстрока, состоящая только из цифр."""
    best = ""
    current = ""
    for symbol in text:
        if symbol.isdigit():
            current += symbol
            if len(current) > len(best):
                best = current
        else:
            current = ""
    return best


def longest_digit_run_length(text: str) -> int:
    return len(longest_digit_run(text))


def main() -> None:
    text = "a1b23c456de7f8901g45h6"
    print(longest_digit_run_length(text))
    print(longest_digit_run(text))


if __name__ == "__main__":
    main()
