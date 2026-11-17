"""Тесты задачи №29."""

from pathlib import Path

CASES = {"module": "solution", "cases": []}


def test_revenue_by_product(solution, tmp_path: Path):
    path = tmp_path / "sales.csv"
    path.write_text("product,quantity,price\nalpha,2,10\nbeta,1,5\nalpha,1,7\n", encoding="utf-8")
    assert solution.revenue_by_product(path) == {"alpha": 27, "beta": 5}


def test_empty_csv(solution, tmp_path: Path):
    path = tmp_path / "empty.csv"
    path.write_text("product,quantity,price\n", encoding="utf-8")
    assert solution.revenue_by_product(path) == {}
