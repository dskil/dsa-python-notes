"""Тесты задачи №34."""

from functools import cache

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"start": 3, "end": 25}, "output": 28},
        {"input": {"start": 1, "end": 1}, "output": 1},
        {"input": {"start": 1, "end": 5}, "output": 4},
        {"input": {"start": 5, "end": 3}, "raises": "ValueError"},
        {"input": {"start": 0, "end": 5}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_count_paths(solution, case):
    assert_case(solution, "count_paths", CASES, case)


@cache
def _brute(value: int, start: int) -> int:
    """Пути «снизу вверх»: из value назад до start шагами -1 и /2."""
    if value == start:
        return 1
    if value < start:
        return 0
    total = _brute(value - 1, start)
    if value % 2 == 0 and value // 2 >= start:
        total += _brute(value // 2, start)
    return total


@pytest.mark.parametrize("start", [1, 2, 3, 7])
@pytest.mark.parametrize("end", [5, 8, 12, 25])
def test_matches_bruteforce(solution, start, end):
    if end < start:
        pytest.skip("start > end")
    assert solution.count_paths(start, end) == _brute(end, start)
