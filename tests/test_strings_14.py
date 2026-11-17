"""Тесты задачи №14."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "Привет! Как дела? Python3.0"}, "output": "Python30"},
        {"input": {"text": ""}, "output": ""},
        {"input": {"text": "abcДЕФ123"}, "output": "abc123"},
        {"input": {"text": "!!!__"}, "output": ""},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_keep_ascii_alnum(solution, case):
    assert_case(solution, "keep_ascii_alnum", CASES, case)
