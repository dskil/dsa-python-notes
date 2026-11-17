"""Тесты задачи №45."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, [2, 3], 4]}, "output": 10},
        {"input": {"items": [1, [2, [3, [4]]]]}, "output": 10},
        {"input": {"items": []}, "output": 0},
        {"input": {"items": [10]}, "output": 10},
        {"input": {"items": [[], [[]]]}, "output": 0},
        {"input": {"items": [True, 2]}, "output": 2},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_deep_sum(solution, case):
    assert_case(solution, "deep_sum", CASES, case)


def test_strings_are_not_iterated(solution):
    assert solution.deep_sum([[1], [2, [3]]]) == 6
