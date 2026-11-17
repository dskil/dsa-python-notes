"""Тесты задачи №71."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "python is"}, "output": 2},
        {"input": {"text": "   hello world   "}, "output": 5},
        {"input": {"text": ""}, "output": 0},
        {"input": {"text": "   "}, "output": 0},
        {"input": {"text": "one"}, "output": 3},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_length_of_last_word(solution, case):
    assert_case(solution, "length_of_last_word", CASES, case)
