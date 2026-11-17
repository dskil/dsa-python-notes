"""Тесты задачи №83."""


def test_add_to_tuple(solution):
    fruits = ("Apple", "Banana")
    assert solution.add_to_tuple(fruits, "Kiwi") == ("Apple", "Banana", "Kiwi")
    assert fruits == ("Apple", "Banana")


def test_safe_index(solution):
    assert solution.safe_index(("a", "b"), "b") == 1
    assert solution.safe_index(("a", "b"), "z") == -1
