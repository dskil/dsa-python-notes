"""№75 · Удалить гласные.

Источник: ``HSEtasks/strings/remove_vowels.py``. Тема: строки.

Английские гласные; для снятия регистра — ``casefold``.
"""

VOWELS = frozenset("aeiou")


def remove_vowels(text: str) -> str:
    return "".join(symbol for symbol in text if symbol.lower() not in VOWELS)


def main() -> None:
    print(remove_vowels("aeifkd"))


if __name__ == "__main__":
    main()
