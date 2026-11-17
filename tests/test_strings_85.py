"""Тесты задачи №85."""

import pytest
from conftest import assert_case, case_ids

CHUNKS = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, 2, 3, 4, 5], "size": 2}, "output": [[1, 2], [3, 4], [5]]},
        {"input": {"items": [], "size": 3}, "output": []},
        {"input": {"items": [1], "size": 3}, "output": [[1]]},
        {"input": {"items": [1], "size": 0}, "raises": "ValueError"},
    ],
}

PAIRS = {
    "module": "solution",
    "cases": [
        {"input": {"items": ["a", "b"]}, "output": ["0:a", "1:b"]},
        {"input": {"items": []}, "output": []},
    ],
}

ALL_EVEN = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [2, 4]}, "output": True},
        {"input": {"numbers": [2, 3]}, "output": False},
        {"input": {"numbers": []}, "output": True},
    ],
}

ANY_NEGATIVE = {
    "module": "solution",
    "cases": [
        {"input": {"numbers": [1, -1]}, "output": True},
        {"input": {"numbers": []}, "output": False},
        {"input": {"numbers": [0]}, "output": False},
    ],
}


@pytest.mark.parametrize("case", CHUNKS["cases"], ids=case_ids(CHUNKS["cases"]))
def test_chunks(solution, case):
    assert_case(solution, "chunks", CHUNKS, case)


@pytest.mark.parametrize("case", PAIRS["cases"], ids=case_ids(PAIRS["cases"]))
def test_enumerate_pairs(solution, case):
    assert_case(solution, "enumerate_pairs", PAIRS, case)


@pytest.mark.parametrize("case", ALL_EVEN["cases"], ids=case_ids(ALL_EVEN["cases"]))
def test_is_all_even(solution, case):
    assert_case(solution, "is_all_even", ALL_EVEN, case)


@pytest.mark.parametrize("case", ANY_NEGATIVE["cases"], ids=case_ids(ANY_NEGATIVE["cases"]))
def test_any_negative(solution, case):
    assert_case(solution, "any_negative", ANY_NEGATIVE, case)
