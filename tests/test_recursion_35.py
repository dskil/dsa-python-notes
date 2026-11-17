"""Тесты задачи №35."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"start": 1, "end": 5}, "output": 5},
        {"input": {"start": 0, "end": 4}, "output": 5},
        {"input": {"start": 3, "end": 3}, "output": 1},
        {"input": {"start": 3, "end": 4}, "output": 1},
        {"input": {"start": 5, "end": 1}, "raises": "ValueError"},
        {"input": {"start": -1, "end": 2}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_kuznechik(solution, case):
    assert_case(solution, "kuznechik", CASES, case)


@pytest.mark.parametrize("end", [1, 2, 3, 6, 9, 12])
def test_matches_fibonacci(solution, end):
    assert solution.kuznechik(0, end) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233][end]
