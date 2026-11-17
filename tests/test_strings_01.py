"""Тесты задачи №01."""

import itertools

import pytest
from conftest import assert_case, case_ids

STRIP_CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "23ffskl1321dfldasdf"}, "output": "ffskldfldasdf"},
        {"input": {"text": "a1b2c3"}, "output": "abc"},
        {"input": {"text": "123"}, "output": ""},
        {"input": {"text": ""}, "output": ""},
        {"input": {"text": "без цифр"}, "output": "без цифр"},
    ],
}

LEN_CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "23ffskl1321dfldasdf"}, "output": 13},
        {"input": {"text": "123"}, "output": 0},
        {"input": {"text": "a1"}, "output": 1},
    ],
}


@pytest.mark.parametrize("case", STRIP_CASES["cases"], ids=case_ids(STRIP_CASES["cases"]))
def test_strip_digits(solution, case):
    assert_case(solution, "strip_digits", STRIP_CASES, case)


@pytest.mark.parametrize("case", LEN_CASES["cases"], ids=case_ids(LEN_CASES["cases"]))
def test_digits_free_length(solution, case):
    assert_case(solution, "digits_free_length", LEN_CASES, case)


def test_matches_reference(solution):
    for length in range(6):
        for combo in itertools.product("ab1", repeat=length):
            text = "".join(combo)
            expected = "".join(ch for ch in text if ch not in "0123456789")
            assert solution.strip_digits(text) == expected
