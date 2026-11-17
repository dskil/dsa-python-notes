"""Тесты задачи №53."""

import pytest
from conftest import assert_case, case_ids

FREQ = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [1, 2, 2, 3]}, "output": {"1": 1, "2": 2, "3": 1}, "invalid": True},
        {"input": {"numbers": []}, "output": {}, "invalid": True},
    ],
}

MOST = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [1, 2, 2, 3, 3, 3]}, "output": 3},
        {"input": {"numbers": [5, 5, 1, 1]}, "output": 1},
        {"input": {"numbers": [7]}, "output": 7},
        {"input": {"numbers": []}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", FREQ["cases"], ids=case_ids(FREQ["cases"]))
def test_frequency(solution, case):
    expected = {int(key): value for key, value in case["output"].items()}
    assert_case(solution, "frequency", FREQ, {**case, "output": expected})


@pytest.mark.parametrize("case", MOST["cases"], ids=case_ids(MOST["cases"]))
def test_most_common(solution, case):
    assert_case(solution, "most_common", MOST, case)


def test_tie_goes_to_smaller_value(solution):
    assert solution.most_common([3, 3, 1, 1]) == 1


def test_counter_variant(solution):
    assert solution.most_common_counter([1, 2, 2]) == 2
