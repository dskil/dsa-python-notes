"""Тесты задачи №66."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 4}, "output": True},
        {"input": {"n": 7}, "output": False},
        {"input": {"n": 0}, "output": True},
        {"input": {"n": -3}, "output": False},
        {"input": {"n": -2}, "output": True},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_is_even(solution, case):
    assert_case(solution, "is_even", CASES, case)


def test_matches_modulo(solution):
    for n in range(-20, 21):
        assert solution.is_even(n) == (n % 2 == 0)
