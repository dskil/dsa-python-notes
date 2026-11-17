"""Тесты задачи №50."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"items": []}, "output": [[]]},
        {"input": {"items": [1]}, "output": [[], [1]]},
        {
            "input": {"items": [1, 2]},
            "output": [[], [2], [1], [1, 2]],
        },
        {
            "input": {"items": [1, 2, 3]},
            "output": [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]],
        },
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_power_set(solution, case):
    assert_case(solution, "power_set", CASES, case)


def test_subset_count(solution):
    for size in range(7):
        assert len(solution.power_set(list(range(size)))) == 2**size
