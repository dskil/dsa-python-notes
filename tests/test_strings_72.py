"""Тесты задачи №72."""

import pytest
from conftest import assert_case, case_ids

NAIVE = {
    "module": "solution",
    "cases": [
        {"input": {"text": "абакадабра", "pattern": "кад"}, "output": 3},
        {"input": {"text": "abc", "pattern": "z"}, "output": -1},
        {"input": {"text": "abc", "pattern": ""}, "output": 0},
        {"input": {"text": "", "pattern": "a"}, "output": -1},
        {"input": {"text": "aaa", "pattern": "aa"}, "output": 0},
    ],
}

FAST = {
    "module": "solution",
    "cases": [
        {"input": {"text": "абакадабра", "pattern": "кад"}, "output": 3},
        {"input": {"text": "abc", "pattern": "c"}, "output": 2},
        {"input": {"text": "abc", "pattern": ""}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", NAIVE["cases"], ids=case_ids(NAIVE["cases"]))
def test_naive(solution, case):
    assert_case(solution, "find_substring_naive", NAIVE, case)


@pytest.mark.parametrize("case", FAST["cases"], ids=case_ids(FAST["cases"]))
def test_fast(solution, case):
    assert_case(solution, "find_substring", FAST, case)


def test_variants_agree(solution):
    for text, pattern in (("abracadabra", "cad"), ("hello", "ll"), ("abc", "d")):
        naive = solution.find_substring_naive(text, pattern)
        assert naive == solution.find_substring(text, pattern)
