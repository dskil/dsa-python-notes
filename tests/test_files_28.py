"""Тесты задачи №28."""

import pytest
from conftest import assert_case, case_ids

FILTER = {
    "module": "solution",
    "cases": [
        {
            "input": {
                "lines": [
                    "2024-01-01 10:00:00 [INFO] Started",
                    "2024-01-01 10:00:01 [ERROR] Boom",
                    "garbage",
                    "2024-01-01 10:00:02 [error] lower",
                ]
            },
            "output": ["2024-01-01 10:00:01 [ERROR] Boom"],
        },
        {"input": {"lines": []}, "output": []},
        {
            "input": {"lines": ["2024-01-01 10:00:01 [ERROR] x"], "level": "INFO"},
            "output": [],
        },
    ],
}


@pytest.mark.parametrize("case", FILTER["cases"], ids=case_ids(FILTER["cases"]))
def test_filter_level(solution, case):
    assert_case(solution, "filter_level", FILTER, case)


def test_broken_lines_do_not_crash(solution):
    assert solution.filter_level(["", "only one"]) == []
