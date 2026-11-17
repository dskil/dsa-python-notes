"""Тесты задачи №39."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 94732}, "output": 25},
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 9}, "output": 9},
        {"input": {"n": -5}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_digit_sum(solution, case):
    assert_case(solution, "digit_sum", CASES, case)
