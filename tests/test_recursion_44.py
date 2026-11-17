"""Тесты задачи №44."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 1}, "output": 1},
        {"input": {"n": 50}, "output": 12586269025},
        {"input": {"n": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_fib(solution, case):
    assert_case(solution, "fib", CASES, case)


def test_large_n_is_fast(solution):
    value = solution.fib(500)
    assert len(str(value)) == 105
