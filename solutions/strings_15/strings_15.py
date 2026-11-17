"""№15 · Пароль ровно из 10 символов, где есть цифра и спецсимвол.

Источник: ``StringRandomTrain/Train15.py``. Тема: строки.
"""

import secrets
import string

ALL_CHARS = string.ascii_letters + string.digits + string.punctuation


def generate_password() -> str:
    """10 символов: минимум одна цифра и минимум один спецсимвол."""
    symbols = [
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    symbols.extend(secrets.choice(ALL_CHARS) for _ in range(8))
    secrets.SystemRandom().shuffle(symbols)
    return "".join(symbols)


def main() -> None:
    print(generate_password())


if __name__ == "__main__":
    main()
