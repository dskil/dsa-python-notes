"""Тесты задачи №42."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"base": 2, "exponent": 10}, "output": 1024},
        {"input": {"base": 2, "exponent": 0}, "output": 1},
        {"input": {"base": 0, "exponent": 0}, "output": 1},
        {"input": {"base": -2, "exponent": 3}, "output": -8},
        {"input": {"base": 2, "exponent": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_power(solution, case):
    assert_case(solution, "power", CASES, case)
