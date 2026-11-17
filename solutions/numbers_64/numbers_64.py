"""№64 · Разложение на простые множители.

Источник: ``HSEtasks/numbers/factorization.py``. Тема: числа.
"""


def factorize(n: int) -> list[int]:
    """Простые множители по возрастанию; для n <= 1 — пустой список."""
    if n < 1:
        raise ValueError("n должно быть не меньше 1")
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2
    if n > 1:
        factors.append(n)
    return factors


def main() -> None:
    print(factorize(360))


if __name__ == "__main__":
    main()
