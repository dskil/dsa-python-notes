"""Тесты задачи №32."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 1}, "output": 1},
        {"input": {"n": 10}, "output": 55},
        {"input": {"n": 20}, "output": 6765},
        {"input": {"n": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_fib(solution, case):
    assert_case(solution, "fib", CASES, case)


def test_first_values(solution):
    assert [solution.fib(n) for n in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]
