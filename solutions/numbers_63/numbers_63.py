"""№63 · Бинарное возведение в степень.

Источник: ``HSEtasks/numbers/binpow.py``. Тема: числа.

В Python есть встроенный ``pow(a, n, mod)`` — правильное решение — но
написать свой цикл полезно, чтобы понять алгоритм за O(log n).
"""


def binpow(base: int, exponent: int, modulus: int | None = None) -> int:
    """``base ** exponent`` (mod ``modulus``) за O(log exponent)."""
    if exponent < 0:
        raise ValueError("Ожидался неотрицательный показатель степени")
    result = 1
    if modulus:
        base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus if modulus else result * base
        base = base * base % modulus if modulus else base * base
        exponent >>= 1
    return result


def main() -> None:
    print(binpow(2, 100, 1_000_000_007))
    print(pow(2, 100, 1_000_000_007))


if __name__ == "__main__":
    main()
