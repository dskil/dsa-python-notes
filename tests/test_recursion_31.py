"""Тесты задачи №31."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 0}, "output": 1},
        {"input": {"n": 1}, "output": 1},
        {"input": {"n": 5}, "output": 120},
        {"input": {"n": 10}, "output": 3628800},
        {"input": {"n": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_factorial(solution, case):
    assert_case(solution, "factorial", CASES, case)


def test_big_factorial(solution):
    assert solution.factorial(100) == __import__("math").factorial(100)
