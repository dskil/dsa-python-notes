"""Тесты задачи №70."""

import pytest
from conftest import assert_case, case_ids

UNIQUE = {
    "module": "solution",
    "cases": [
        {"input": {"text": "dgvca"}, "output": True},
        {"input": {"text": "abcda"}, "output": False},
        {"input": {"text": ""}, "output": True},
        {"input": {"text": "   "}, "output": False},
    ],
}

FIRST_DUP = {
    "module": "solution",
    "cases": [
        {"input": {"text": "abcda"}, "output": "a"},
        {"input": {"text": "aab"}, "output": "a"},
        {"input": {"text": "abca"}, "output": "a"},
        {"input": {"text": "abc"}, "output": None, "invalid": True},
    ],
}


@pytest.mark.parametrize("case", UNIQUE["cases"], ids=case_ids(UNIQUE["cases"]))
def test_all_unique(solution, case):
    assert_case(solution, "all_unique", UNIQUE, case)


@pytest.mark.parametrize("case", FIRST_DUP["cases"], ids=case_ids(FIRST_DUP["cases"]))
def test_first_duplicate(solution, case):
    assert_case(solution, "first_duplicate", FIRST_DUP, case)
