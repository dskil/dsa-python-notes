"""№29 · CSV: выручка по товарам.

Источник: ``Train29.py``. Тема: файлы.
"""

import csv
from collections import defaultdict
from pathlib import Path


def revenue_by_product(path: str | Path) -> dict[str, int]:
    """Всего выручки на товар из CSV с колонками product, quantity, price."""
    totals: dict[str, int] = defaultdict(int)
    with Path(path).open("r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            totals[row["product"]] += int(row["quantity"]) * int(row["price"])
    return dict(totals)


def main() -> None:
    source = Path("sales.csv")
    source.write_text("product,quantity,price\nalpha,2,10\nbeta,1,5\nalpha,1,7\n", encoding="utf-8")
    print(revenue_by_product(source))


if __name__ == "__main__":
    main()
