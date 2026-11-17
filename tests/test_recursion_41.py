"""Тесты задачи №41."""

import math

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"a": 56, "b": 16}, "output": 8},
        {"input": {"a": 0, "b": 5}, "output": 5},
        {"input": {"a": 5, "b": 0}, "output": 5},
        {"input": {"a": -12, "b": 8}, "output": 4},
        {"input": {"a": 17, "b": 13}, "output": 1},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_gcd(solution, case):
    assert_case(solution, "gcd", CASES, case)


def test_matches_math_gcd(solution):
    for a, b in ((12, 18), (100, 75), (7, 7), (0, 0)):
        assert solution.gcd(a, b) == math.gcd(a, b)
