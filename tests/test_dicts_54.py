"""Тесты задачи №54."""

import pytest
from conftest import assert_case, case_ids

FREQ = {
    "module": "solution",
    "cases": [
        {"input": {"word": "абракадабра"}, "output": {"а": 5, "б": 2, "р": 2, "к": 1, "д": 1}},
        {"input": {"word": ""}, "output": {}},
    ],
}

MOST = {
    "module": "solution",
    "cases": [
        {"input": {"word": "абракадабра"}, "output": ["а", 5], "invalid": True},
        {"input": {"word": "bbaa"}, "output": ["a", 2], "invalid": True},
        {"input": {"word": ""}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", FREQ["cases"], ids=case_ids(FREQ["cases"]))
def test_letter_frequencies(solution, case):
    assert_case(solution, "letter_frequencies", FREQ, case)


@pytest.mark.parametrize("case", MOST["cases"], ids=case_ids(MOST["cases"]))
def test_most_frequent_letter(solution, case):
    expected = tuple(case["output"]) if "output" in case else None
    assert_case(solution, "most_frequent_letter", MOST, {**case, "output": expected})
