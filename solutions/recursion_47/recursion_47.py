"""№47 · Ханойские башни.

Источник: ``Recursion/Train47.py``. Тема: рекурсия.

Возвращаем список ходов, а не печатаем — так его можно проверить тестами.
Верхняя граница — 30 дисков (2**30 - 1 ходов, порядка гигабайта списка),
для больших n — ленивый ``hanoi_iter``.
"""

from collections.abc import Iterator


def hanoi_iter(
    n: int, source: str = "A", target: str = "C", aux: str = "B"
) -> Iterator[tuple[str, str]]:
    """Ленивый генератор ходов: память O(n), а не O(2**n).

    Идея та же, что у рекурсивной версии, но вместо сборки списков ``yield``:
    первый элемент пары — откуда, второй — куда.
    """
    if n < 0:
        raise ValueError("Количество дисков должно быть неотрицательным")
    if n == 0:
        return
    yield from hanoi_iter(n - 1, source, aux, target)
    yield source, target
    yield from hanoi_iter(n - 1, aux, target, source)


def hanoi(n: int, source: str = "A", target: str = "C", aux: str = "B") -> list[tuple[str, str]]:
    """Список ходов (откуда, куда) для переноса ``n`` дисков; 2**n - 1 ход."""
    if n > 30:
        raise ValueError("Для n > 30 используй hanoi_iter(): иначе получится слишком много ходов")
    return list(hanoi_iter(n, source, target, aux))


def main() -> None:
    for source, target in hanoi(3):
        print(f"перенести диск с {source} на {target}")


if __name__ == "__main__":
    main()
