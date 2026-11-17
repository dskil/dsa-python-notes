"""Тесты задачи №47."""

from collections.abc import Iterator

import pytest


def _is_valid_solution(
    moves: list[tuple[str, str]],
    pegs: tuple[str, str, str] = ("A", "B", "C"),
    source: str = "A",
    target: str = "C",
) -> bool:
    """Проверить легальность последовательности ходов.

    Количество дисков восстанавливается из длины ходов: ``2**n - 1``.
    """
    n = (len(moves) + 1).bit_length() - 1
    if 2**n - 1 != len(moves):
        return False

    if source not in pegs or target not in pegs or source == target:
        return False
    towers: dict[str, list[int]] = {peg: [] for peg in pegs}
    towers[source] = list(range(n, 0, -1))
    for from_peg, to_peg in moves:
        if from_peg not in towers or to_peg not in towers:
            return False
        if not towers[from_peg]:
            return False
        disc = towers[from_peg].pop()
        if towers[to_peg] and towers[to_peg][-1] < disc:
            return False
        towers[to_peg].append(disc)
    return towers[target] == list(range(n, 0, -1))


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 8])
def test_hanoi_solution_is_valid(solution, n):
    moves = solution.hanoi(n)
    assert len(moves) == 2**n - 1
    assert _is_valid_solution(moves)


def test_hanoi_uses_given_peg_names(solution):
    moves = solution.hanoi(3, "X", "Y", "Z")
    assert len(moves) == 7
    assert {from_peg for move in moves for from_peg in move} == {"X", "Y", "Z"}
    assert _is_valid_solution(moves, ("X", "Y", "Z"), "X", "Y")


def test_hanoi_iter_is_lazy(solution):
    result = solution.hanoi_iter(3)
    assert isinstance(result, Iterator)
    assert len(list(result)) == 7


@pytest.mark.parametrize("n", [1, 4, 10])
def test_hanoi_and_hanoi_iter_agree(solution, n):
    assert list(solution.hanoi_iter(n)) == solution.hanoi(n)


def test_hanoi_iter_is_valid(solution):
    moves = list(solution.hanoi_iter(10))
    assert len(moves) == 2**10 - 1
    assert _is_valid_solution(moves)


@pytest.mark.parametrize("n", [-1])
def test_hanoi_negative(solution, n):
    with pytest.raises(ValueError):
        solution.hanoi(n)
    with pytest.raises(ValueError):
        list(solution.hanoi_iter(n))


def test_hanoi_rejects_huge_n(solution):
    with pytest.raises(ValueError):
        solution.hanoi(31)
