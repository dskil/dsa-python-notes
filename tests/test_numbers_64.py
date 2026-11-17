"""Тесты задачи №64."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 360}, "output": [2, 2, 2, 3, 3, 5]},
        {"input": {"n": 1}, "output": []},
        {"input": {"n": 2}, "output": [2]},
        {"input": {"n": 97}, "output": [97]},
        {"input": {"n": 0}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_factorize(solution, case):
    assert_case(solution, "factorize", CASES, case)


@pytest.mark.parametrize("n", [1, 2, 12, 12345, 99991])
def test_product_restores_number(solution, n):
    import math

    factors = solution.factorize(n)
    assert math.prod(factors) == n
