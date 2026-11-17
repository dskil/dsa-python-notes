"""Тесты задачи №57."""

import pytest
from conftest import assert_case, case_ids

UNIQUE = {
    "module": "solution",
    "cases": [
        {"input": {"items": [3, 1, 3, 2, 1]}, "output": [3, 1, 2]},
        {"input": {"items": []}, "output": []},
        {"input": {"items": [1, 1, 1]}, "output": [1]},
    ],
}

LETTERS = {
    "module": "solution",
    "cases": [
        {"input": {"text": "hello"}, "output": 4},
        {"input": {"text": ""}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", UNIQUE["cases"], ids=case_ids(UNIQUE["cases"]))
def test_unique_in_order(solution, case):
    assert_case(solution, "unique_in_order", UNIQUE, case)


@pytest.mark.parametrize("case", LETTERS["cases"], ids=case_ids(LETTERS["cases"]))
def test_train56_noisy_letters_count(solution, case):
    assert_case(solution, "train56_noisy_letters_count", LETTERS, case)


def test_equals_set_size(solution):
    items = [4, 4, 2, 9, 2]
    assert len(solution.unique_in_order(items)) == len(set(items))
