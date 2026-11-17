"""Тесты задачи №36.

Задача на +1/+2 шаги: пути нужно считать ЗАКАНЧИВАЮЩИМИСЯ ровно в target.
"""

from functools import cache

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"current": 1, "target": 3}, "output": 2},
        {"input": {"current": 1, "target": 1}, "output": 1},
        {"input": {"current": 3, "target": 1}, "output": 0},
        {"input": {"current": 1, "target": 5}, "output": 5},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_count_ways(solution, case):
    assert_case(solution, "count_ways", CASES, case)


@cache
def _reference(current: int, target: int) -> int:
    if current > target:
        return 0
    if current == target:
        return 1
    return _reference(current + 1, target) + _reference(current + 2, target)


@pytest.mark.parametrize("target", [2, 4, 6, 9])
def test_matches_reference(solution, target):
    assert solution.count_ways(1, target) == _reference(1, target)
