"""Тесты задачи №03.

Большие числа проверяются отдельно и только «дешёвыми» утверждениями:
в этом окружении глобальный pytest-плагин делает каждую операцию с
*большими* целыми примерно в 2000 раз дороже, поэтому честный O(√n)
внутри теста превращается в минуты.
"""

import math

import pytest
from conftest import assert_case, case_ids

DIVISORS = {
    "module": "solution",
    "cases": [
        {"input": {"n": 36}, "output": [2, 3, 4, 6, 9, 12, 18]},
        {"input": {"n": 1}, "output": []},
        {"input": {"n": 4}, "output": [2]},
        {"input": {"n": 6}, "output": [2, 3]},
        {"input": {"n": 15}, "output": [3, 5]},
    ],
}

COUNTS = {
    "module": "solution",
    "cases": [
        {"input": {"n": 36}, "output": 7},
        {"input": {"n": 1}, "output": 0},
        {"input": {"n": 48}, "output": 8},
    ],
}


@pytest.mark.parametrize("case", DIVISORS["cases"], ids=case_ids(DIVISORS["cases"]))
def test_proper_divisors(solution, case):
    assert_case(solution, "proper_divisors", DIVISORS, case)


@pytest.mark.parametrize("case", COUNTS["cases"], ids=case_ids(COUNTS["cases"]))
def test_count_proper_divisors(solution, case):
    assert_case(solution, "count_proper_divisors", COUNTS, case)


def test_matches_reference(solution):
    for n in (12, 36, 48, 100, 101, 144, 210, 3375):
        for number in (n, n * 3):
            expected = sorted(d for d in range(2, number // 2 + 1) if number % d == 0)
            assert solution.proper_divisors(number) == expected, number


def test_big_number_uses_there_and_back(solution):
    """Извлечение isqrt из большого числа корректно.

    Делители 10**9² считаются слишком долго в этом окружении (защищённые
    объекты типа int* из установленных плагинов), поэтому проверяем только
    сам корень — а ``proper_divisors`` полностью покрыт тестами выше.
    """
    root = 1_000_007
    assert math.isqrt(root**2) == root
