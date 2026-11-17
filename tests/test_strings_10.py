"""Тесты задачи №10."""

import pytest
from conftest import assert_case, case_ids

HAS_CATEGORIES = {
    "module": "solution",
    "cases": [
        {"input": {"password": "aA1!"}, "output": True},
        {"input": {"password": "aA1"}, "output": False},
        {"input": {"password": "aa1!"}, "output": False},
        {"input": {"password": ""}, "output": False},
    ],
}


@pytest.mark.parametrize("case", HAS_CATEGORIES["cases"], ids=case_ids(HAS_CATEGORIES["cases"]))
def test_has_all_categories(solution, case):
    assert_case(solution, "has_all_categories", HAS_CATEGORIES, case)


@pytest.mark.parametrize("length", [4, 5, 12, 40])
def test_generate_password_length_and_categories(solution, length):
    for _ in range(200):
        password = solution.generate_password(length)
        assert len(password) == length
        assert solution.has_all_categories(password)


@pytest.mark.parametrize("length", [0, 1, 3, -5])
def test_generate_password_rejects_short_length(solution, length):
    with pytest.raises(ValueError):
        solution.generate_password(length)


def test_generate_password_rejects_alphabet_without_categories(solution):
    with pytest.raises(ValueError):
        solution.generate_password(8, alphabet="abc")


def test_generate_password_accepts_full_alphabet(solution):
    password = solution.generate_password(12)
    assert solution.has_all_categories(password)


def test_passwords_are_not_constant(solution):
    assert len({solution.generate_password(16) for _ in range(20)}) > 1
