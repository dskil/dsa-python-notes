"""Тесты задачи №15."""

import string

CASES = {"module": "solution", "cases": []}


def test_has_categories_and_length(solution):
    for _ in range(200):
        password = solution.generate_password()
        assert len(password) == 10
        assert any(ch.isdigit() for ch in password)
        assert any(ch in string.punctuation for ch in password)
