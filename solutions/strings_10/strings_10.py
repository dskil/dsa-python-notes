"""№10 · Генератор паролей с гарантированными категориями символов.

Источник: ``Train10.py``. Тема: строки.
"""

import secrets
import string

DEFAULT_ALPHABET = string.ascii_letters + string.digits + string.punctuation


def has_all_categories(password: str) -> bool:
    """В пароле есть строчная, заглавная буква, цифра и спецсимвол."""
    return (
        any(ch.islower() for ch in password)
        and any(ch.isupper() for ch in password)
        and any(ch.isdigit() for ch in password)
        and any(ch in string.punctuation for ch in password)
    )


def generate_password(length: int = 12, alphabet: str = DEFAULT_ALPHABET) -> str:
    """Пароль длины ``length``, где есть хотя бы по одному символу каждой категории.

    Используется ``secrets`` — криптостойкий источник случайности.
    ``ValueError`` — если ``length < 4`` или в ``alphabet`` нет всех категорий.
    """
    if length < 4:
        raise ValueError("Длина пароля должна быть не меньше 4 символов")
    if not {"lower", "upper", "digit", "punct"} <= _categories(alphabet):
        raise ValueError("В alphabet должны быть строчные/заглавные буквы, цифры и спецсимволы")

    categories = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    ]
    required = [secrets.choice(category) for category in categories]
    required.extend(secrets.choice(alphabet) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(required)
    return "".join(required)


def _categories(alphabet: str) -> set[str]:
    found: set[str] = set()
    if any(ch.islower() for ch in alphabet):
        found.add("lower")
    if any(ch.isupper() for ch in alphabet):
        found.add("upper")
    if any(ch.isdigit() for ch in alphabet):
        found.add("digit")
    if any(ch in string.punctuation for ch in alphabet):
        found.add("punct")
    return found


def main() -> None:
    print(generate_password(int(input("Длина пароля (минимум 4): ") or 12)))


if __name__ == "__main__":
    main()
