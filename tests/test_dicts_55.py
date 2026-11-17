"""Тесты задачи №55."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"word1": "listen", "word2": "silent"}, "output": True},
        {"input": {"word1": "abcd", "word2": "abc"}, "output": False},
        {"input": {"word1": "", "word2": ""}, "output": True},
        {"input": {"word1": "aab", "word2": "abb"}, "output": False},
        {"input": {"word1": "расстояние", "word2": "нерассотояние"}, "output": False},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_are_anagrams(solution, case):
    assert_case(solution, "are_anagrams", CASES, case)


def test_anagrams_are_symmetric(solution):
    cases = [("listen", "silent"), ("abc", "cba"), ("ab", "ab")]
    for first, second in cases:
        assert solution.are_anagrams(first, second) == solution.are_anagrams(second, first)
