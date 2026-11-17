"""Тесты задачи №08."""

import pytest
from conftest import assert_case, case_ids

SECOND = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [5, 3, 9, 1]}, "output": 5},
        {"input": {"numbers": [1, 1, 2, 2]}, "output": 1},
        {"input": {"numbers": [-5, -1, -10]}, "output": -5},
        {"input": {"numbers": [5]}, "raises": "ValueError"},
        {"input": {"numbers": []}, "raises": "ValueError"},
        {"input": {"numbers": [7, 7, 7]}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", SECOND["cases"], ids=case_ids(SECOND["cases"]))
def test_second_largest(solution, case):
    assert_case(solution, "second_largest", SECOND, case)


def test_not_max_and_must_exist(solution):
    numbers = [10, 4, 10, 8]
    assert solution.second_largest(numbers) == 8
    assert solution.second_largest(numbers) < max(numbers)
