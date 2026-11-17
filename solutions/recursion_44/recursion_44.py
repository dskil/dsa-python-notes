"""№44 · Числа Фибоначчи с кэшем.

Источник: ``Recursion/Train44.py``. Тема: рекурсия.

``functools.lru_cache`` превращает экспоненциальную рекурсию из №32 в O(n).
"""

from functools import cache


@cache
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    print(fib(6))
    print(fib(200))


if __name__ == "__main__":
    main()
