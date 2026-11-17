"""№62 · Проверка простоты числа.

Источник: ``HSEtasks/numbers/is_prime.py``. Тема: числа.

Исходник был O(sqrt(n)) с шагом 1; здесь — шаг 6k±1, что в 3 раза быстрее
на больших числах.
"""


def is_prime(n: int) -> bool:
    """Простое ли число (перебор делителей 6k ± 1)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


def main() -> None:
    print(is_prime(1_000_000_000_039))


if __name__ == "__main__":
    main()
