"""Тесты задачи №48."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"left": [1, 2, 4], "right": [3, 5, 6]}, "output": [1, 2, 3, 4, 5, 6]},
        {"input": {"left": [], "right": [1, 2]}, "output": [1, 2]},
        {"input": {"left": [1, 2], "right": []}, "output": [1, 2]},
        {"input": {"left": [], "right": []}, "output": []},
        {"input": {"left": [1, 1], "right": [1]}, "output": [1, 1, 1]},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_merge(solution, case):
    assert_case(solution, "merge", CASES, case)


def test_merge_does_not_mutate(solution):
    left, right = [1, 3], [2, 4]
    solution.merge(left, right)
    assert (left, right) == ([1, 3], [2, 4])


def test_merge_is_sorted_result(solution):
    merged = solution.merge([-3, 0, 9], [-5, 4])
    assert merged == sorted([-3, 0, 9, -5, 4])
