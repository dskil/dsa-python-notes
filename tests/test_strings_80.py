"""Тесты задачи №80."""


def test_double(solution):
    assert solution.double(21) == 42


def test_docstring_of(solution):
    assert solution.docstring_of(solution.double) == "This Func doubles arg"
    assert solution.docstring_of(lambda x: x) == ""


def test_describe(solution):
    assert solution.describe(solution.double).startswith("double: This Func doubles arg")
