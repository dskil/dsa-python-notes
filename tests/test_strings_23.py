"""Тесты задачи №23."""

import random

import pytest
from conftest import assert_case, case_ids

PICK = {
    "module": "solution",
    "cases": [
        {"input": {"sequence": []}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", PICK["cases"], ids=case_ids(PICK["cases"]))
def test_pick_random_rejects_empty(solution, case):
    assert_case(solution, "pick_random", PICK, case)


def test_pick_random_is_deterministic_with_seed(solution):
    rng = random.Random(42)
    assert solution.pick_random([1, 2, 3], rng=rng) in {1, 2, 3}
    assert solution.pick_random(["x"], rng=rng) == "x"


def test_shuffle_copy_does_not_mutate(solution):
    source = [1, 2, 3, 4, 5]
    result = solution.shuffle_copy(source, rng=random.Random(1))
    assert source == [1, 2, 3, 4, 5]
    assert sorted(result) == source


def test_generated_numbers_bounds_and_errors(solution):
    rng = random.Random(7)
    numbers = solution.generated_numbers(100, 1, 3, rng=rng)
    assert len(numbers) == 100
    assert all(1 <= n <= 3 for n in numbers)
    with pytest.raises(ValueError):
        solution.generated_numbers(1, 5, 1)
    with pytest.raises(ValueError):
        solution.generated_numbers(-1, 1, 5)
