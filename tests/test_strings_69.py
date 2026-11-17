"""Тесты задачи №69."""

import pytest
from conftest import assert_case, case_ids

NAIVE = {
    "module": "solution",
    "cases": [
        {"input": {"word": "aabaa"}, "output": 2},
        {"input": {"word": "abc"}, "output": 0},
        {"input": {"word": ""}, "output": 0},
        {"input": {"word": "a"}, "output": 0},
        {"input": {"word": "aaaa"}, "output": 3},
    ],
}

FAST = {
    "module": "solution",
    "cases": [
        {"input": {"word": "aabaa"}, "output": 2},
        {"input": {"word": "abacaba"}, "output": 3},
        {"input": {"word": "xyz"}, "output": 0},
        {"input": {"word": ""}, "output": 0},
    ],
}

PREFIX = {
    "module": "solution",
    "cases": [
        {"input": {"word": "aabaa"}, "output": [0, 1, 0, 1, 2]},
        {"input": {"word": "abc"}, "output": [0, 0, 0]},
        {"input": {"word": ""}, "output": []},
    ],
}


@pytest.mark.parametrize("case", NAIVE["cases"], ids=case_ids(NAIVE["cases"]))
def test_naive(solution, case):
    assert_case(solution, "longest_prefix_suffix_naive", NAIVE, case)


@pytest.mark.parametrize("case", FAST["cases"], ids=case_ids(FAST["cases"]))
def test_fast(solution, case):
    assert_case(solution, "longest_prefix_suffix", FAST, case)


@pytest.mark.parametrize("case", PREFIX["cases"], ids=case_ids(PREFIX["cases"]))
def test_prefix_function(solution, case):
    assert_case(solution, "prefix_function", PREFIX, case)


@pytest.mark.parametrize("word", ["aab", "abab", "abcabcab", "aaaaa"])
def test_variants_agree(solution, word):
    assert solution.longest_prefix_suffix_naive(word) == solution.longest_prefix_suffix(word)
