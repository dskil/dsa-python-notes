"""Тесты задачи №67."""

import pytest
from conftest import assert_case, case_ids

UP_TO = {
    "module": "solution",
    "cases": [
        {"input": {"year": 0}, "output": 0},
        {"input": {"year": 4}, "output": 1},
        {"input": {"year": 100}, "output": 24},
        {"input": {"year": 2000}, "output": 485},
    ],
}

RANGE = {
    "module": "solution",
    "cases": [
        {"input": {"left": 1, "right": 4}, "output": 1},
        {"input": {"left": 1900, "right": 2000}, "output": 25},
        {"input": {"left": 5, "right": 4}, "raises": "ValueError"},
        {"input": {"left": 2000, "right": 2000}, "output": 1},
        {"input": {"left": 1999, "right": 1999}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", UP_TO["cases"], ids=case_ids(UP_TO["cases"]))
def test_leap_years_up_to(solution, case):
    assert_case(solution, "leap_years_up_to", UP_TO, case)


@pytest.mark.parametrize("case", RANGE["cases"], ids=case_ids(RANGE["cases"]))
def test_count_leap_years(solution, case):
    assert_case(solution, "count_leap_years", RANGE, case)


def test_against_calendar(solution):
    import calendar

    left, right = 1800, 2400
    expected = sum(1 for year in range(left, right + 1) if calendar.isleap(year))
    assert solution.count_leap_years(left, right) == expected
