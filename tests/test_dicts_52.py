"""Тесты задачи №52."""

import pytest


def test_update_and_check(solution):
    data = {"x": 10, "y": 40}
    assert solution.update_and_check(data, "x", -20) == {"x": -10, "y": 40}
    assert solution.update_and_check(data, "z", 5) == {"x": -10, "y": 40, "z": 5}


def test_safe_get(solution):
    assert solution.safe_get({"a": 1}, "a") == 1
    assert solution.safe_get({"a": 1}, "b") == 0
    assert solution.safe_get({}, "b", default=7) == 7


def test_invert(solution):
    assert solution.invert({"x": 10, "y": 40}) == {10: "x", 40: "y"}


@pytest.mark.parametrize("data", [{}, {"k": 1}])
def test_invert_roundtrip(solution, data):
    assert solution.invert(solution.invert(data)) == data
