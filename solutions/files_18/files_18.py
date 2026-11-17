"""№18 · Чтение файла с обработкой ошибок.

Источник: ``FilesTrain/Train18.py``. Тема: файлы.
"""

from pathlib import Path


class ReadError(Exception):
    """Базовое исключение чтения файла."""


class FileNotFoundReadError(ReadError):
    """Файла нет."""


class PermissionReadError(ReadError):
    """Нет прав на чтение."""


def read_text_checked(path: str | Path) -> str:
    """Вернуть содержимое файла или поднять ``ReadError`` с понятным текстом."""
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise FileNotFoundReadError(f"Файл не найден: {path}") from exc
    except PermissionError as exc:
        raise PermissionReadError(f"Недостаточно прав: {path}") from exc


def main() -> None:
    try:
        print(read_text_checked(input("Имя файла: ")))
    except ReadError as error:
        print(error)


if __name__ == "__main__":
    main()
