"""№39 · Сумма цифр числа (вариант 2, рекурсия).

Источник: ``Recursion/Train39.py``. Тема: рекурсия.

По сути дублирует №33 — это нормально: на повторах закрепляется шаблон.
"""


def digit_sum(n: int) -> int:
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    return n if n < 10 else n % 10 + digit_sum(n // 10)


def main() -> None:
    print(digit_sum(94732))


if __name__ == "__main__":
    main()
