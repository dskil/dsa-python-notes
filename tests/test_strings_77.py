"""Тесты задачи №77."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"text": "привет!!!!! как дела? норм."}, "output": 3},
        {"input": {"text": ""}, "output": 0},
        {"input": {"text": "."}, "output": 1},
        {"input": {"text": "?!."}, "output": 1},
        {"input": {"text": "а. б. в"}, "output": 2},
        {"input": {"text": "без точки"}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_count_sentences(solution, case):
    assert_case(solution, "count_sentences", CASES, case)
