"""Тесты задачи №84."""


def test_merge_dicts(solution):
    first = {"a": 1, "b": 2}
    assert solution.merge_dicts(first, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}
    assert first == {"a": 1, "b": 2}


def test_increment(solution):
    data: dict = {}
    assert solution.increment(data, "k") == 1
    assert solution.increment(data, "k", 5) == 6
    assert data == {"k": 6}


def test_key_with_max_value(solution):
    assert solution.key_with_max_value({"x": 10, "y": 40}) == "y"
    assert solution.key_with_max_value({"a": 1, "b": 1}) == "b"
    assert solution.key_with_max_value({}) is None
