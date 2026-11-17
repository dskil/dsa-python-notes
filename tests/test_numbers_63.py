"""Тесты задачи №63."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"base": 2, "exponent": 10}, "output": 1024},
        {"input": {"base": 2, "exponent": 0}, "output": 1},
        {"input": {"base": 2, "exponent": 5, "modulus": 15}, "output": 2},
        {"input": {"base": 3, "exponent": 0, "modulus": 7}, "output": 1},
        {"input": {"base": 2, "exponent": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_binpow(solution, case):
    assert_case(solution, "binpow", CASES, case)


@pytest.mark.parametrize("exponent", [0, 1, 7, 64, 1000])
def test_matches_builtin_pow(solution, exponent):
    assert solution.binpow(13, exponent) == pow(13, exponent)
    assert solution.binpow(13, exponent, 97) == pow(13, exponent, 97)
