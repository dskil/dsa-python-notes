"""Тесты задачи №43."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, 2, 3, 4]}, "output": 4},
        {"input": {"items": []}, "output": 0},
        {"input": {"items": [None]}, "output": 1},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_count_items(solution, case):
    assert_case(solution, "count_items", CASES, case)


def test_recursion_limit_safe(solution):
    assert solution.count_items(list(range(400))) == 400
