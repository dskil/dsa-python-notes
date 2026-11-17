"""№32 · Числа Фибоначчи (наивная рекурсия).

Источник: ``Recursion/Train32.py``. Тема: рекурсия.

Наивная реализация — O(φ^n). Для больших n используй итерации или кэш
(см. задачу №44).
"""


def fib(n: int) -> int:
    """n-е число Фибоначчи: F(0) = 0, F(1) = 1."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    print(fib(10))


if __name__ == "__main__":
    main()
