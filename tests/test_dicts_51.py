"""Тесты задачи №51."""

import pytest
from conftest import assert_case, case_ids

COUNTS = {
    "module": "solution",
    "cases": [
        {"input": {"word": "asdaaassdf"}, "output": {"a": 4, "s": 3, "d": 2, "f": 1}},
        {"input": {"word": ""}, "output": {}},
        {"input": {"word": "ab"}, "output": {"a": 1, "b": 1}},
    ],
}

COUNTER = {
    "module": "solution",
    "cases": [
        {"input": {"word": "asdaaassdf"}, "output": {"a": 4, "s": 3, "d": 2, "f": 1}},
        {"input": {"word": ""}, "output": {}},
    ],
}


@pytest.mark.parametrize("case", COUNTS["cases"], ids=case_ids(COUNTS["cases"]))
def test_letter_counts(solution, case):
    assert_case(solution, "letter_counts", COUNTS, case)


@pytest.mark.parametrize("case", COUNTER["cases"], ids=case_ids(COUNTER["cases"]))
def test_letter_counts_counter(solution, case):
    assert_case(solution, "letter_counts_counter", COUNTER, case)


def test_variants_agree(solution):
    text = "abracadabra"
    assert solution.letter_counts(text) == solution.letter_counts_counter(text)
