"""Тесты задачи №86."""

import pytest
from conftest import assert_case, case_ids

PARSE = {
    "module": "solution",
    "cases": [
        {"input": {"value": "9"}, "output": 9},
        {"input": {"value": "abc"}, "raises": "solution.ValidationError"},
        {"input": {"value": "3"}, "raises": "solution.ValidationError"},
        {"input": {"value": "10"}, "raises": "solution.ValidationError"},
        {"input": {"value": "5", "low": 1, "high": 5}, "output": 5},
    ],
}

DIV = {
    "module": "solution",
    "cases": [
        {"input": {"a": 6, "b": 3}, "output": 2.0},
        {"input": {"a": 1, "b": 0}, "output": None, "invalid": True},
        {"input": {"a": 1, "b": 0, "default": 0}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", PARSE["cases"], ids=case_ids(PARSE["cases"]))
def test_parse_range(solution, case):
    assert_case(solution, "parse_range", PARSE, case)


@pytest.mark.parametrize("case", DIV["cases"], ids=case_ids(DIV["cases"]))
def test_safe_div(solution, case):
    assert_case(solution, "safe_div", DIV, case)


def test_validation_error_is_exception(solution):
    assert issubclass(solution.ValidationError, Exception)
