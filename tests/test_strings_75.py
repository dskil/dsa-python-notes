"""Тесты задачи №75."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "aeifkd"}, "output": "fkd"},
        {"input": {"text": ""}, "output": ""},
        {"input": {"text": "AEIOU"}, "output": ""},
        {"input": {"text": "hello world"}, "output": "hll wrld"},
        {"input": {"text": "школа"}, "output": "школа"},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_remove_vowels(solution, case):
    assert_case(solution, "remove_vowels", CASES, case)
