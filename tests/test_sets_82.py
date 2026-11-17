"""Тесты задачи №82."""

import pytest


@pytest.mark.parametrize(
    "operation",
    ["union", "intersection", "symmetric_difference", "difference"],
)
def test_matches_set_operators(solution, operation):
    first = {1, 2, 3}
    second = {3, 4}
    expected = {
        "union": first | second,
        "intersection": first & second,
        "symmetric_difference": first ^ second,
        "difference": first - second,
    }[operation]
    assert getattr(solution, operation)(first, second) == expected
