"""№35 · Кузнечик: прыжки на 1 и на 2 клетки.

Источник: ``Recursion/Train35.py``. Тема: рекурсия.
"""


def kuznechik(start: int, end: int) -> int:
    """Способы дойти от ``start`` до ``end`` прыжками +1 и +2."""
    if start < 0 or end < start:
        raise ValueError("Нужно 0 <= start <= end")
    if end - start <= 1:
        return 1
    dp = [0] * (end - start + 1)
    dp[0] = dp[1] = 1
    for index in range(2, len(dp)):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[-1]


def main() -> None:
    print(kuznechik(1, 5))


if __name__ == "__main__":
    main()
