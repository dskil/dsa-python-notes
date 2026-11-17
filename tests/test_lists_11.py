"""Тесты задачи №11."""

import pytest
from conftest import assert_case, case_ids

INTERSECTION = {
    "module": "solution",
    "cases": [
        {"input": {"numbers1": [3, 1, 2], "numbers2": [2, 3, 4]}, "output": [2, 3]},
        {"input": {"numbers1": [1, 2], "numbers2": [3, 4]}, "output": []},
        {"input": {"numbers1": [], "numbers2": [1]}, "output": []},
        {"input": {"numbers1": [2, 2, 2], "numbers2": [2]}, "output": [2]},
    ],
}

FORMAT = {
    "module": "solution",
    "cases": [
        {"input": {"numbers1": [3, 1, 2], "numbers2": [2, 3, 4]}, "output": "2 3"},
        {"input": {"numbers1": [1], "numbers2": [9]}, "output": "Пусто"},
    ],
}


@pytest.mark.parametrize("case", INTERSECTION["cases"], ids=case_ids(INTERSECTION["cases"]))
def test_intersection(solution, case):
    assert_case(solution, "intersection", INTERSECTION, case)


@pytest.mark.parametrize("case", FORMAT["cases"], ids=case_ids(FORMAT["cases"]))
def test_format_intersection(solution, case):
    assert_case(solution, "format_intersection", FORMAT, case)
