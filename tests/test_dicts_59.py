"""Тесты задачи №59."""

import pytest
from conftest import assert_case, case_ids

CASES = {
    "module": "solution",
    "cases": [
        {
            "input": {"words": ["мышь", "слон", "кот", "ёж"]},
            "output": {"4": ["мышь", "слон"], "3": ["кот"], "2": ["ёж"]},
            "invalid": True,
        },
        {"input": {"words": []}, "output": {}, "invalid": True},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
def test_group_lengths(solution, case):
    expected = {int(key): value for key, value in case["output"].items()}
    assert_case(solution, "group_lengths", CASES, {**case, "output": expected})


def test_groups_keep_order(solution):
    groups = solution.group_lengths(["bb", "a", "cc"])
    assert groups == {2: ["bb", "cc"], 1: ["a"]}
