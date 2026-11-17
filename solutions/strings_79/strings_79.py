"""№79 · Форматирование строк (format и f-string).

Источник: ``HSEtasks/basics/format.py``. Тема: строки.
"""


def email_greeting(first: str, second: str) -> str:
    """``Hello {1}, {0}`` — позиционные аргументы ``format``."""
    return f"Hello {second}, {first}"


def price_line(name: str, price: float) -> str:
    """Два знака после запятой."""
    return f"Привет {name}, вам необходимо заплатить {price:.2f}"


def align(text: str, width: int, align: str = "left") -> str:
    """Выравнивание: left, right, center (нужная ширина)."""
    symbols = {"left": "<", "right": ">", "center": "^"}
    if align not in symbols:
        raise ValueError(f"align должен быть одним из {sorted(symbols)}")
    return f"{text:{symbols[align]}{width}}"


def main() -> None:
    print(email_greeting("Genry", "Harry"))
    print(price_line("Alex", 49))
    print(align("Python", 12, "center"))


if __name__ == "__main__":
    main()
