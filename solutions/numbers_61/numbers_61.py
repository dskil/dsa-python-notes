"""№61 · Простые числа до N (решето Эратосфена).

Источник: ``HSEtasks/numbers/sieve_of_eratosthenes.py``. Тема: числа.
"""


def sieve(limit: int) -> list[int]:
    """Все простые числа p <= limit."""
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, int(limit**0.5) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                is_prime[multiple] = False
    return [number for number, flag in enumerate(is_prime) if flag]


def main() -> None:
    print(sieve(30))


if __name__ == "__main__":
    main()
