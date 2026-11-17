"""Тесты задачи №49 (сортировка слиянием).

Слияние имеет собственный модуль в задаче №48, поэтому здесь проверяем
только ``merge_sort``; ``merge`` вызывается через него.
"""

import pytest
from conftest import assert_case, case_ids

SORT = {
    "module": "solution",
    "cases": [
        {"input": {"items": [1, 2, 3, 7, 8, 4]}, "output": [1, 2, 3, 4, 7, 8]},
        {"input": {"items": []}, "output": []},
        {"input": {"items": [1]}, "output": [1]},
        {"input": {"items": [3, 3, 1, 1]}, "output": [1, 1, 3, 3]},
        {"input": {"items": [-5, 0, -1]}, "output": [-5, -1, 0]},
    ],
}

MERGE = {
    "module": "solution",
    "cases": [
        {"input": {"left": [1, 4], "right": [2, 3]}, "output": [1, 2, 3, 4]},
        {"input": {"left": [], "right": [1]}, "output": [1]},
        {"input": {"left": [1], "right": []}, "output": [1]},
    ],
}


@pytest.mark.parametrize("case", SORT["cases"], ids=case_ids(SORT["cases"]))
def test_merge_sort(solution, case):
    assert_case(solution, "merge_sort", SORT, case)


@pytest.mark.parametrize("case", MERGE["cases"], ids=case_ids(MERGE["cases"]))
def test_merge(solution, case):
    assert_case(solution, "merge", MERGE, case)


def test_does_not_mutate_input(solution):
    items = [3, 1, 2]
    solution.merge_sort(items)
    assert items == [3, 1, 2]
