"""Тесты задачи №40."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"word": "шалаш"}, "output": True},
        {"input": {"word": "abba"}, "output": True},
        {"input": {"word": "abc"}, "output": False},
        {"input": {"word": ""}, "output": True},
        {"input": {"word": "x"}, "output": True},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_is_palindrome(solution, case):
    assert_case(solution, "is_palindrome", CASES, case)
