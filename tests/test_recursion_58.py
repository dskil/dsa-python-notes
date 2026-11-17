"""Тесты задачи №58."""

import pytest
from conftest import assert_case, case_ids

DEPTH = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, [2, [3, [4]]]]}, "output": 4},
        {"input": {"items": []}, "output": 1},
        {"input": {"items": [1, 2]}, "output": 1},
        {"input": {"items": [[], []]}, "output": 2},
    ],
}

FLAT = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, [2, [3, [4]]], 5]}, "output": [1, 2, 3, 4, 5]},
        {"input": {"items": []}, "output": []},
        {"input": {"items": [[[1]], []]}, "output": [1]},
    ],
}


@pytest.mark.parametrize("case", DEPTH["cases"], ids=case_ids(DEPTH["cases"]))
def test_max_depth(solution, case):
    assert_case(solution, "max_depth", DEPTH, case)


@pytest.mark.parametrize("case", FLAT["cases"], ids=case_ids(FLAT["cases"]))
def test_flatten(solution, case):
    assert_case(solution, "flatten", FLAT, case)


def test_roundtrip(solution):
    items = [1, [2, [3]], 4]
    assert solution.flatten(items) == [1, 2, 3, 4]
    assert solution.max_depth(items) == 3
