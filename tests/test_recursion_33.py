"""Тесты задачи №33 и №39 (одинаковые сигнатуры, разные варианты)."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 123}, "output": 6},
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 94732}, "output": 25},
        {"input": {"n": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_digit_sum(solution, case):
    assert_case(solution, "digit_sum", CASES, case)


def test_matches_reference(solution):
    for n in (5, 99, 1000, 123456789):
        assert solution.digit_sum(n) == sum(int(digit) for digit in str(n))
