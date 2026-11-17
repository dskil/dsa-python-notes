"""№60 · Итоговая тренировка: банкомат (жадный алгоритм).

Источник: пустой ``Train60.py`` — финальный файл серии. Тема: числа.
"""

DENOMINATIONS = (5000, 2000, 1000, 500, 200, 100)


def withdraw(amount: int) -> dict[int, int]:
    """Сколько купюр каждого номинала отдаст банкомат.

    Сумма должна делиться на 100, иначе ``ValueError``.
    """
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    if amount % 100 != 0:
        raise ValueError("Сумма должна быть кратна 100")

    bill_count: dict[int, int] = {}
    remaining = amount
    for denomination in DENOMINATIONS:
        count, remaining = divmod(remaining, denomination)
        if count:
            bill_count[denomination] = count
    return bill_count


def main() -> None:
    print(withdraw(7800))


if __name__ == "__main__":
    main()
