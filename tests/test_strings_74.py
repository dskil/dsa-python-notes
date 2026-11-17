"""Тесты задачи №74."""

import pytest
from conftest import assert_case, case_ids

BASIC = {
    "module": "solution",
    "cases": [
        {"input": {"text": "aabbbc"}, "output": 3},
        {"input": {"text": ""}, "output": 0},
        {"input": {"text": "abc"}, "output": 1},
        {"input": {"text": "aaaa"}, "output": 4},
    ],
}


@pytest.mark.parametrize("case", BASIC["cases"], ids=case_ids(BASIC["cases"]))
def test_most_frequent_count(solution, case):
    assert_case(solution, "most_frequent_count", BASIC, case)


@pytest.mark.parametrize("case", BASIC["cases"], ids=case_ids(BASIC["cases"]))
def test_counter_variant(solution, case):
    assert_case(solution, "most_frequent_count_counter", BASIC, case)
