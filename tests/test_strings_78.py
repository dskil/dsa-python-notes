"""Тесты задачи №78."""

import pytest
from conftest import assert_case, case_ids

NORMALIZE = {
    "module": "solution",
    "cases": [
        {"input": {"text": "  Привет, Мир!  "}, "output": "Привет, Мир!"},
        {"input": {"text": "abc"}, "output": "abc"},
        {"input": {"text": "   "}, "output": ""},
    ],
}

FIRST_WORD = {
    "module": "solution",
    "cases": [
        {"input": {"text": "  Привет, Мир!  "}, "output": "Привет"},
        {"input": {"text": "one"}, "output": "one"},
        {"input": {"text": ""}, "raises": "ValueError"},
    ],
}

JOIN = {
    "module": "solution",
    "cases": [
        {"input": {"words": ["a", "b"]}, "output": "a1b"},
        {"input": {"words": [], "separator": "-"}, "output": ""},
        {"input": {"words": ["x"], "separator": " "}, "output": "x"},
    ],
}


@pytest.mark.parametrize("case", NORMALIZE["cases"], ids=case_ids(NORMALIZE["cases"]))
def test_normalize(solution, case):
    assert_case(solution, "normalize", NORMALIZE, case)


@pytest.mark.parametrize("case", FIRST_WORD["cases"], ids=case_ids(FIRST_WORD["cases"]))
def test_first_word(solution, case):
    assert_case(solution, "first_word", FIRST_WORD, case)


@pytest.mark.parametrize("case", JOIN["cases"], ids=case_ids(JOIN["cases"]))
def test_join_with(solution, case):
    assert_case(solution, "join_with", JOIN, case)
