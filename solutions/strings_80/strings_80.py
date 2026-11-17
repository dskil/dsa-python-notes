"""№80 · Докстринги: ``__doc__``.

Источник: ``HSEtasks/basics/dogstring.py``. Тема: строки.
"""


def double(n: int) -> int:
    """This Func doubles arg"""
    return n * 2


def docstring_of(function: object) -> str:
    """Докстринг функции или пустая строка, если его нет."""
    return function.__doc__ or ""


def describe(function: object) -> str:
    """Как ``help()``, но в одну строку: что делает функция."""
    return f"{function.__name__}: {docstring_of(function)}"


def main() -> None:
    print(double.__doc__)
    print(describe(double))


if __name__ == "__main__":
    main()
