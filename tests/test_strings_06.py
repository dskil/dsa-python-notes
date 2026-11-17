"""Тесты задачи №06."""

import pytest
from conftest import assert_case, case_ids

RUNS = {
    "module": "solution",
    "cases": [
        {"input": {"text": "a1b23c456de7f8901g45h6"}, "output": "8901"},
        {"input": {"text": "abc"}, "output": ""},
        {"input": {"text": "12345"}, "output": "12345"},
        {"input": {"text": "12a34"}, "output": "12"},
        {"input": {"text": ""}, "output": ""},
    ],
}

LENGTHS = {
    "module": "solution",
    "cases": [
        {"input": {"text": "a1b23c456de7f8901g45h6"}, "output": 4},
        {"input": {"text": "abc"}, "output": 0},
        {"input": {"text": "999"}, "output": 3},
    ],
}


@pytest.mark.parametrize("case", RUNS["cases"], ids=case_ids(RUNS["cases"]))
def test_longest_digit_run(solution, case):
    assert_case(solution, "longest_digit_run", RUNS, case)


@pytest.mark.parametrize("case", LENGTHS["cases"], ids=case_ids(LENGTHS["cases"]))
def test_longest_digit_run_length(solution, case):
    assert_case(solution, "longest_digit_run_length", LENGTHS, case)


def test_returns_substring_of_input(solution):
    text = "a1b23c456de7f8901g45h6"
    run = solution.longest_digit_run(text)
    assert run in text
    assert run == "8901"
