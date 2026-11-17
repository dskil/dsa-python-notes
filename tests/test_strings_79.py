"""Тесты задачи №79."""

import pytest
from conftest import assert_case, case_ids

GREETING = {
    "module": "solution",
    "cases": [
        {"input": {"first": "Genry", "second": "Harry"}, "output": "Hello Harry, Genry"},
        {"input": {"first": "a", "second": "b"}, "output": "Hello b, a"},
    ],
}

PRICE = {
    "module": "solution",
    "cases": [
        {
            "input": {"name": "Alex", "price": 49},
            "output": "Привет Alex, вам необходимо заплатить 49.00",
        },
        {
            "input": {"name": "Ира", "price": 1.005},
            "output": "Привет Ира, вам необходимо заплатить 1.00",
        },
    ],
}

ALIGN = {
    "module": "solution",
    "cases": [
        {"input": {"text": "Python", "width": 10}, "output": "Python    "},
        {"input": {"text": "Python", "width": 10, "align": "right"}, "output": "    Python"},
        {"input": {"text": "Python", "width": 10, "align": "center"}, "output": "  Python  "},
        {"input": {"text": "Python", "width": 2}, "output": "Python"},
        {"input": {"text": "x", "width": 1, "align": "bad"}, "raises": "ValueError"},
    ],
}


@pytest.mark.parametrize("case", GREETING["cases"], ids=case_ids(GREETING["cases"]))
def test_email_greeting(solution, case):
    assert_case(solution, "email_greeting", GREETING, case)


@pytest.mark.parametrize("case", PRICE["cases"], ids=case_ids(PRICE["cases"]))
def test_price_line(solution, case):
    assert_case(solution, "price_line", PRICE, case)


@pytest.mark.parametrize("case", ALIGN["cases"], ids=case_ids(ALIGN["cases"]))
def test_align(solution, case):
    assert_case(solution, "align", ALIGN, case)
