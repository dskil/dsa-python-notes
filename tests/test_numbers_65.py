"""Тесты задачи №65."""

import math

import pytest
from conftest import assert_case, case_ids

GCD = {
    "module": "solution",
    "cases": [
        {"input": {"a": 12, "b": 8}, "output": 4},
        {"input": {"a": 0, "b": 0}, "output": 0},
        {"input": {"a": -6, "b": 9}, "output": 3},
    ],
}

LCM = {
    "module": "solution",
    "cases": [
        {"input": {"a": 12, "b": 8}, "output": 24},
        {"input": {"a": 0, "b": 5}, "output": 0},
        {"input": {"a": -4, "b": 6}, "output": 12},
    ],
}


@pytest.mark.parametrize("case", GCD["cases"], ids=case_ids(GCD["cases"]))
def test_gcd(solution, case):
    assert_case(solution, "gcd", GCD, case)


@pytest.mark.parametrize("case", LCM["cases"], ids=case_ids(LCM["cases"]))
def test_lcm(solution, case):
    assert_case(solution, "lcm", LCM, case)


def test_lcm_gcd_relation(solution):
    for a, b in ((12, 18), (7, 5), (100, 75)):
        assert solution.gcd(a, b) * solution.lcm(a, b) == abs(a * b) or a * b == 0
        assert solution.gcd(a, b) == math.gcd(a, b)
