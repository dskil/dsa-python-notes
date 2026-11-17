"""№34 · Количество путей: +1 и ×2 (динамическое программирование).

Источник: ``Recursion/Train34.py``. Тема: рекурсия.
"""


def count_paths(start: int, end: int) -> int:
    """Сколько способов дойти от ``start`` до ``end`` шагами +1 и ×2."""
    if start <= 0 or end < start:
        raise ValueError("Нужно 1 <= start <= end")
    dp = [0] * (end + 1)
    dp[start] = 1
    for value in range(start + 1, end + 1):
        total = dp[value - 1]
        # Шаг ×2 возможен только из уже достижимой клетки value // 2.
        if value % 2 == 0 and value // 2 >= start:
            total += dp[value // 2]
        dp[value] = total
    return dp[end]


def main() -> None:
    print(count_paths(3, 25))


if __name__ == "__main__":
    main()
