"""Тесты задачи №62."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 2}, "output": True},
        {"input": {"n": 3}, "output": True},
        {"input": {"n": 4}, "output": False},
        {"input": {"n": 1}, "output": False},
        {"input": {"n": 0}, "output": False},
        {"input": {"n": -7}, "output": False},
        {"input": {"n": 97}, "output": True},
        {"input": {"n": 91}, "output": False},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_is_prime(solution, case):
    assert_case(solution, "is_prime", CASES, case)


def test_matches_sieve(solution):
    primes = set(solution.sieve(1000)) if hasattr(solution, "sieve") else None
    assert primes is None or all(solution.is_prime(n) == (n in primes) for n in range(-5, 1000))
