"""№28 · Фильтрация лога: строки уровня ERROR.

Источник: ``Train28.py``. Тема: файлы.
"""

from pathlib import Path


def filter_level(lines: list[str], level: str = "ERROR") -> list[str]:
    """Строки, где второй токен (после даты/времени) равен ``[level]``."""
    result: list[str] = []
    for line in lines:
        parts = line.split()
        if len(parts) > 2 and parts[2].strip("[]") == level:
            result.append(line)
    return result


def main() -> None:
    log_path = Path("app.log")
    log_path.write_text(
        "2024-01-01 10:00:00 [INFO] Started\n2024-01-01 10:00:01 [ERROR] Boom\n",
        encoding="utf-8",
    )
    errors = filter_level(log_path.read_text(encoding="utf-8").splitlines())
    Path("error.log").write_text("\n".join(errors) + "\n", encoding="utf-8")
    print(len(errors))


if __name__ == "__main__":
    main()
