"""Тесты задачи №60."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"amount": 7800}, "output": {"5000": 1, "2000": 1, "500": 1, "200": 1, "100": 1}},
        {"input": {"amount": 100}, "output": {"100": 1}},
        {"input": {"amount": 0}, "raises": "ValueError"},
        {"input": {"amount": 150}, "raises": "ValueError"},
        {"input": {"amount": -100}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_withdraw(solution, case):
    expected = None
    if "output" in case:
        expected = {int(key): value for key, value in case["output"].items()}
    assert_case(solution, "withdraw", CASES, {**case, "output": expected})


@pytest.mark.parametrize("amount", [100, 600, 12300, 25000])
def test_withdraw_sum_matches(solution, amount):
    bills = solution.withdraw(amount)
    assert sum(denomination * count for denomination, count in bills.items()) == amount
