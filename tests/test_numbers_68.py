"""Тесты задачи №68."""

import pytest
from conftest import assert_case, case_ids

CHECK = {
    "module": "solution",
    "cases": [
        {"input": {"value": 4}, "output": True},
        {"input": {"value": 2.0}, "output": True},
        {"input": {"value": 3.5}, "output": False},
        {"input": {"value": -4}, "output": False},
        {"input": {"value": True}, "output": False},
        {"input": {"value": 0}, "output": False},
        {"input": {"value": "4"}, "output": False},
        {"input": {"value": "abc"}, "output": False},
    ],
}

COUNT = {
    "module": "solution",
    "cases": [
        {"input": {"values": [2.0, 3.5, -4.0, 6.0, 7.0, 0.0]}, "output": 2},
        {"input": {"values": []}, "output": 0},
        {"input": {"values": [True, 2, "2"]}, "output": 1},
    ],
}


@pytest.mark.parametrize("case", CHECK["cases"], ids=case_ids(CHECK["cases"]))
def test_is_positive_even_int(solution, case):
    assert_case(solution, "is_positive_even_int", CHECK, case)


@pytest.mark.parametrize("case", COUNT["cases"], ids=case_ids(COUNT["cases"]))
def test_count_positive_even_ints(solution, case):
    assert_case(solution, "count_positive_even_ints", COUNT, case)
