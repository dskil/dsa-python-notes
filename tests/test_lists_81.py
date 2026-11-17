"""Тесты задачи №81."""

import pytest


def test_sorted_desc_does_not_mutate(solution):
    source = ["apple", "banana"]
    assert solution.sorted_desc(source) == ["banana", "apple"]
    assert source == ["apple", "banana"]


@pytest.mark.parametrize("index", [0, 1, -1])
def test_insert_at_returns_new_list(solution, index):
    items = ["a", "c"]
    result = solution.insert_at(items, index, "b")
    assert len(result) == len(items) + 1
    assert result.count("b") == 1
    assert items == ["a", "c"], "исходный список не должен меняться"


def test_insert_at_keeps_neighbours(solution):
    assert solution.insert_at(["a", "c"], 1, "b") == ["a", "b", "c"]


def test_merge_lists_returns_new(solution):
    first, second = ["a"], ["b"]
    merged = solution.merge_lists(first, second)
    assert merged == ["a", "b"]
    assert first == ["a"] and second == ["b"]
