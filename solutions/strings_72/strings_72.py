"""№72 · Найти подстроку (наивный поиск + встроенный).

Источник: ``HSEtasks/strings/find_substring.py``. Тема: строки.
"""


def find_substring_naive(text: str, pattern: str) -> int:
    """Первый индекс ``pattern`` в ``text`` или -1 (O(n·m))."""
    if not pattern:
        return 0
    for start in range(len(text) - len(pattern) + 1):
        if text[start : start + len(pattern)] == pattern:
            return start
    return -1


def find_substring(text: str, pattern: str) -> int:
    """Встроенная ``str.find`` — алгоритм Two-Way, амортизированно O(n)."""
    return text.find(pattern)


def main() -> None:
    print(find_substring("абакадабра", "кад"))


if __name__ == "__main__":
    main()
