"""Тесты задачи №46."""

import pytest
from conftest import assert_case, case_ids

RECURSIVE = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, 2, 3, 4, 5, 6, 7], "target": 2}, "output": True},
        {"input": {"items": [1, 2, 3], "target": 9}, "output": False},
        {"input": {"items": [], "target": 1}, "output": False},
    ],
}

INDEX = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, 2, 3, 4, 5, 6, 7], "target": 2}, "output": 1},
        {"input": {"items": [1, 2, 3], "target": 9}, "output": -1},
        {"input": {"items": [], "target": 1}, "output": -1},
        {"input": {"items": [5], "target": 5}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", RECURSIVE["cases"], ids=case_ids(RECURSIVE["cases"]))
def test_binary_search_recursive(solution, case):
    assert_case(solution, "binary_search_recursive", RECURSIVE, case)


@pytest.mark.parametrize("case", INDEX["cases"], ids=case_ids(INDEX["cases"]))
def test_binary_search_index(solution, case):
    assert_case(solution, "binary_search_index", INDEX, case)


def test_index_matches_list_index(solution):
    items = list(range(0, 100, 3))
    for value in items:
        assert solution.binary_search_index(items, value) == items.index(value)
