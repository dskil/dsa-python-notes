"""№56 · Общие буквы двух строк (множества).

Источник: ``Train56.py``. Тема: словари.
"""


def common_letters(text1: str, text2: str) -> str:
    """Общие различные буквы в порядке первого появления в ``text1``."""
    in_second = set(text2)
    seen: set[str] = set()
    result: list[str] = []
    for letter in text1:
        if letter in in_second and letter not in seen:
            seen.add(letter)
            result.append(letter)
    return "".join(result)


def main() -> None:
    print(common_letters("программирование", "разработка"))


if __name__ == "__main__":
    main()
