"""Тесты задачи №38."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "hello"}, "output": "olleh"},
        {"input": {"text": ""}, "output": ""},
        {"input": {"text": "ab"}, "output": "ba"},
        {"input": {"text": "привет"}, "output": "тевирп"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_reverse_string(solution, case):
    assert_case(solution, "reverse_string", CASES, case)


def test_is_palindrome_check(solution):
    for word in ("шалаш", "abba", "x"):
        assert solution.reverse_string(word) == word
