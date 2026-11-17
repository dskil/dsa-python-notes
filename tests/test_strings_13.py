"""Тесты задачи №13."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "Hello, world! 42"}, "output": [2, 2], "invalid": True},
        {"input": {"text": ""}, "output": [0, 0], "invalid": True},
        {"input": {"text": "----"}, "output": [0, 4], "invalid": True},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_count_digits_and_punctuation(solution, case):
    case = {**case, "output": tuple(case["output"])}
    assert_case(solution, "count_digits_and_punctuation", CASES, case)


def test_counts_are_independent(solution):
    digits, punctuation = solution.count_digits_and_punctuation("a1!b2?")
    assert (digits, punctuation) == (2, 2)
