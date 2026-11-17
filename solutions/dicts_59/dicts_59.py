"""№59 · Группировка по ключу (sort + groupby / defaultdict).

Источник: пустой ``Train59.py`` — задача на словари. Тема: словари.
"""

from collections import defaultdict
from collections.abc import Iterable


def group_lengths(words: Iterable[str]) -> dict[int, list[str]]:
    """Сгруппировать слова по длине, внутри группы — в исходном порядке."""
    groups: dict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def main() -> None:
    print(group_lengths(["мышь", "слон", "кот", "ёж"]))


if __name__ == "__main__":
    main()
