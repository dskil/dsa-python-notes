"""Тесты задачи №61."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"limit": 1}, "output": []},
        {"input": {"limit": 2}, "output": [2]},
        {"input": {"limit": 30}, "output": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]},
        {"input": {"limit": 0}, "output": []},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_sieve(solution, case):
    assert_case(solution, "sieve", CASES, case)


def test_matches_trial_division(solution):
    expected = [n for n in range(2, 200) if all(n % d for d in range(2, int(n**0.5) + 1))]
    assert solution.sieve(200) == expected
