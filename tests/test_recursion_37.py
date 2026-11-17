"""Тесты задачи №37."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 5}, "output": 15},
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 1}, "output": 1},
        {"input": {"n": -2}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_sum_to_n(solution, case):
    assert_case(solution, "sum_to_n", CASES, case)
