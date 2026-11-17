"""Тесты задачи №12."""

import string

import pytest
from conftest import assert_case, case_ids

MAKE_LOGIN = {
    "module": "solution",
    "cases": [
        {"input": {"length": 0}, "raises": "ValueError"},
        {"input": {"length": -1}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", MAKE_LOGIN["cases"], ids=case_ids(MAKE_LOGIN["cases"]))
def test_make_login_rejects_bad_length(solution, case):
    assert_case(solution, "make_login", MAKE_LOGIN, case)


@pytest.mark.parametrize("length", [1, 8, 32])
def test_make_login_shape(solution, length):
    login = solution.make_login(length)
    assert len(login) == length
    assert set(login) <= set(string.ascii_lowercase + string.digits)


def test_make_login_uses_custom_alphabet(solution):
    assert set(solution.make_login(100, alphabet="ab")) <= {"a", "b"}


def test_make_login_is_random(solution):
    assert len({solution.make_login(16) for _ in range(20)}) > 1
