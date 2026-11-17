"""№23 · Случайный выбор и перемешивание.

Источник: ``StringRandomTrain`` (тренировка на ``random``).
Тема: строки.
"""

import random


def pick_random(sequence: list, rng: random.Random | None = None):
    """Один случайный элемент."""
    if not sequence:
        raise ValueError("Пустая последовательность")
    return (rng or random).choice(sequence)


def shuffle_copy(sequence: list, rng: random.Random | None = None) -> list:
    """Перемешанная копия без изменения исходного списка."""
    copy = list(sequence)
    (rng or random).shuffle(copy)
    return copy


def generated_numbers(
    count: int, low: int, high: int, rng: random.Random | None = None
) -> list[int]:
    """``count`` случайных чисел из [low; high]."""
    if count < 0:
        raise ValueError("count не может быть отрицательным")
    if low > high:
        raise ValueError("low должен быть не больше high")
    source = rng or random
    return [source.randint(low, high) for _ in range(count)]


def main() -> None:
    print(shuffle_copy([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
