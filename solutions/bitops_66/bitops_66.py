"""№66 · Чётность через бит.

Источник: ``HSEtasks/numbers/is_even.py``. Тема: битовые операции.
"""


def is_even(n: int) -> bool:
    """Последний бит 0 — число чётное (работает и для отрицательных)."""
    return n & 1 == 0


def main() -> None:
    print(is_even(4), is_even(7), is_even(-3))


if __name__ == "__main__":
    main()
