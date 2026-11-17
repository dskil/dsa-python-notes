"""№12 · Случайный логин из строчных букв и цифр.

Источник: ``StringRandomTrain/Train12.py``. Тема: строки.
"""

import secrets
import string

LOGIN_ALPHABET = string.ascii_lowercase + string.digits


def make_login(length: int = 8, alphabet: str = LOGIN_ALPHABET) -> str:
    """Случайный логин длины ``length`` из ``alphabet``."""
    if length <= 0:
        raise ValueError("Длина логина должна быть положительной")
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    print(make_login())


if __name__ == "__main__":
    main()
