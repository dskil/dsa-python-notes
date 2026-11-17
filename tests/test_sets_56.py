"""Тесты задачи №56."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text1": "abc", "text2": "cba"}, "output": "abc"},
        {"input": {"text1": "abc", "text2": "xyz"}, "output": ""},
        {"input": {"text1": "", "text2": "abc"}, "output": ""},
        {"input": {"text1": "aab", "text2": "ab"}, "output": "ab"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_common_letters(solution, case):
    assert_case(solution, "common_letters", CASES, case)


def test_is_intersection(solution):
    text1, text2 = "программирование", "разработка"
    assert set(solution.common_letters(text1, text2)) == set(text1) & set(text2)
