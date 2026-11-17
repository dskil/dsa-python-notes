"""Тесты задачи №73."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "asa"}, "output": True},
        {"input": {"text": "abc"}, "output": False},
        {"input": {"text": ""}, "output": True},
        {"input": {"text": "Aba"}, "output": False},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_is_palindrome(solution, case):
    assert_case(solution, "is_palindrome", CASES, case)
