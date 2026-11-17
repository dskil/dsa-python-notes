"""Тесты задачи №02."""

import pytest
from conftest import assert_case

CASES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 2534}, "output": "100111100110"},
        {"input": {"n": 0}, "output": "0"},
        {"input": {"n": 1}, "output": "1"},
        {"input": {"n": 7}, "output": "111"},
    ],
}

ONES = {
    "module": "solution",
    "cases": [
        {"input": {"n": 2534}, "output": 7},
        {"input": {"n": 0}, "output": 0},
        {"input": {"n": 7}, "output": 3},
        {"input": {"n": 8}, "output": 1},
    ],
}

ZEROS = {
    "module": "solution",
    "cases": [
        {"input": {"n": 2534}, "output": 5},
        {"input": {"n": 0}, "output": 1},
        {"input": {"n": 7}, "output": 0},
    ],
}


@pytest.mark.parametrize("case", CASES["cases"], ids=[c["input"]["n"] for c in CASES["cases"]])
def test_to_binary(solution, case):
    assert_case(solution, "to_binary", CASES, case)


@pytest.mark.parametrize("case", ONES["cases"], ids=[c["input"]["n"] for c in ONES["cases"]])
def test_count_ones(solution, case):
    assert_case(solution, "count_ones", ONES, case)


@pytest.mark.parametrize("case", ZEROS["cases"], ids=[c["input"]["n"] for c in ZEROS["cases"]])
def test_count_zeros(solution, case):
    assert_case(solution, "count_zeros", ZEROS, case)


def test_ones_and_zeros_cover_bits(solution):
    for n in (0, 1, 2, 5, 63, 64, 1023, 4096):
        bits = len(solution.to_binary(n))
        assert solution.count_ones(n) + solution.count_zeros(n) == bits
