"""№86 · Обработка исключений: try/except/else/finally и кастомные ошибки.

Источник: ``HSEtasks/basics/try_except.py``. Тема: исключения.
"""


class ValidationError(Exception):
    """Ошибка валидации входных данных."""


def parse_range(value: str, low: int = 5, high: int = 9) -> int:
    """Превратить строку в число из [low; high] или поднять ``ValidationError``."""
    try:
        number = int(value)
    except ValueError as exc:
        raise ValidationError(f"Не целое число: {value!r}") from exc
    if not low <= number <= high:
        raise ValidationError(f"Число должно быть в диапазоне {low}..{high}")
    return number


def safe_div(a: float, b: float, default: float | None = None) -> float | None:
    """Деление без ZeroDivisionError: при делении на 0 — ``default``."""
    try:
        return a / b
    except ZeroDivisionError:
        return default


def main() -> None:
    print(safe_div(1, 0, default=None))
    try:
        print(parse_range("12"))
    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
