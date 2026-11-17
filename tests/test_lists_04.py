"""Тесты задачи №04."""

import pytest
from conftest import assert_case, case_ids

PAIRS = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [15, 20, 25, 30, 35, 45]}, "output": 1},
        {"input": {"numbers": []}, "output": 0},
        {"input": {"numbers": [5]}, "output": 0},
        {"input": {"numbers": [5, 5]}, "output": 1},
        {"input": {"numbers": [1, 2, 3]}, "output": 0},
    ],
}

MAX_SUM = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [15, 20, 25, 30, 35, 45]}, "output": 80},
        {"input": {"numbers": []}, "output": 0},
        {"input": {"numbers": [1, 2, 3]}, "output": 0},
        {"input": {"numbers": [3, 7]}, "output": 10},
        {"input": {"numbers": [9, 21]}, "output": 30},
    ],
}


@pytest.mark.parametrize("case", PAIRS["cases"], ids=case_ids(PAIRS["cases"]))
def test_count_special_pairs(solution, case):
    assert_case(solution, "count_special_pairs", PAIRS, case)


@pytest.mark.parametrize("case", MAX_SUM["cases"], ids=case_ids(MAX_SUM["cases"]))
def test_max_special_pair_sum(solution, case):
    assert_case(solution, "max_special_pair_sum", MAX_SUM, case)


@pytest.mark.parametrize(
    "numbers",
    [
        [15, 20, 25, 30, 35, 45],  # пара (35, 45) на стыке двойки и тройки
        [1, 3, 5, 7, 9],
        [10, 25, 30, 35],
    ],
)
def test_pairs_count_and_sum_are_consistent(solution, numbers):
    count = solution.count_special_pairs(numbers)
    best = solution.max_special_pair_sum(numbers)
    if count == 0:
        assert best == 0
    else:
        assert best > 0
