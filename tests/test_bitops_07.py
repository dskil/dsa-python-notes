"""Тесты задачи №07."""

import pytest
from conftest import assert_case, case_ids

NUMBERS = {
    "module": "solution",
    "cases": [
        {"input": {"start": 1, "end": 7}, "output": [7]},
        {"input": {"start": 7, "end": 8}, "output": [7]},
        {"input": {"start": 9, "end": 14}, "output": [11, 13, 14]},
        {"input": {"start": 10, "end": 10}, "output": []},
        {"input": {"start": 11, "end": 30}, "output": [11, 13, 14, 19, 21, 22, 25, 26, 28]},
    ],
}

COUNT = {
    "module": "solution",
    "cases": [
        {"input": {"start": 1, "end": 10}, "output": 1},
        {"input": {"start": 7, "end": 7}, "output": 1},
        {"input": {"start": 8, "end": 10}, "output": 0},
        {"input": {"start": 9, "end": 14}, "output": 3},
    ],
}


@pytest.mark.parametrize("case", NUMBERS["cases"], ids=case_ids(NUMBERS["cases"]))
def test_numbers_with_ones(solution, case):
    assert_case(solution, "numbers_with_ones", NUMBERS, case)


@pytest.mark.parametrize("case", COUNT["cases"], ids=case_ids(COUNT["cases"]))
def test_count_numbers_with_ones(solution, case):
    assert_case(solution, "count_numbers_with_ones", COUNT, case)


def test_matches_manual_counting(solution):
    for n in range(1, 300):
        assert solution.count_numbers_with_ones(n, n) == (bin(n).count("1") == 3)
