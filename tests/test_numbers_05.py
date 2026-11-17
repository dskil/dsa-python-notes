"""Тесты задачи №05."""

import pytest
from conftest import assert_case, case_ids

COUNT = {
    "module": "solution",
    "cases": [
        {"input": {"n": 1}, "output": 1},
        {"input": {"n": 2}, "output": 2},
        {"input": {"n": 12}, "output": 6},
        {"input": {"n": 36}, "output": 9},
        {"input": {"n": 0}, "output": 0},
    ],
}

FOUND = {
    "module": "solution",
    "cases": [
        {"input": {"start": 1, "end": 5, "divisors": 2}, "output": [2, 3, 5]},
        {"input": {"start": 10, "end": 10}, "output": []},
        {"input": {"start": 27, "end": 30, "divisors": 2}, "output": [29]},
        {"input": {"start": 1, "end": 3, "divisors": 1}, "output": [1]},
        {"input": {"start": 4, "end": 9, "divisors": 3}, "output": [4, 9]},
    ],
}


@pytest.mark.parametrize("case", COUNT["cases"], ids=case_ids(COUNT["cases"]))
def test_count_divisors(solution, case):
    assert_case(solution, "count_divisors", COUNT, case)


@pytest.mark.parametrize("case", FOUND["cases"], ids=case_ids(FOUND["cases"]))
def test_numbers_with_divisor_count(solution, case):
    assert_case(solution, "numbers_with_divisor_count", FOUND, case)


def test_answer_for_100_200(solution):
    found = solution.numbers_with_divisor_count(100, 200)
    # Ровно 6 делителей дают p²·q и p⁵ (p ≠ q простые).
    assert found == [116, 117, 124, 147, 148, 153, 164, 171, 172, 175, 188]
    assert 123 not in found  # 1, 3, 41, 123 — всего 4 делителя
    assert all(solution.count_divisors(n) == 6 for n in found)
