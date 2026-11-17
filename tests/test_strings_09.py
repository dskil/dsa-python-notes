"""Тесты задачи №09."""

import pytest
from conftest import assert_case, case_ids

NORMALIZE = {
    "module": "solution",
    "cases": [
        {"input": {"text": "А роза упала на лапу Азора"}, "output": "арозаупаланалапуазора"},
        {"input": {"text": "No, ...'lemon'!"}, "output": "nolemon"},
        {"input": {"text": ""}, "output": ""},
    ],
}

PALINDROME = {
    "module": "solution",
    "cases": [
        {"input": {"text": "А роза упала на лапу Азора"}, "output": True},
        {"input": {"text": "No lemon, no melon"}, "output": True},
        {"input": {"text": "Hello"}, "output": False},
        {"input": {"text": "   "}, "output": False},
        {"input": {"text": ""}, "output": False},
        {"input": {"text": "1"}, "output": True},
    ],
}


@pytest.mark.parametrize("case", NORMALIZE["cases"], ids=case_ids(NORMALIZE["cases"]))
def test_normalize(solution, case):
    assert_case(solution, "normalize", NORMALIZE, case)


@pytest.mark.parametrize("case", PALINDROME["cases"], ids=case_ids(PALINDROME["cases"]))
def test_is_palindrome_loose(solution, case):
    assert_case(solution, "is_palindrome_loose", PALINDROME, case)
