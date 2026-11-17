"""№27 · Временный файл через tempfile.

Источник: ``Train27.py``. Тема: файлы.
"""

import tempfile
from pathlib import Path


def write_and_read_temp(payload: bytes = b"temp data") -> tuple[str, bytes, str]:
    """Записать байты во временный файл и прочитать обратно.

    Возвращает (имя файла, содержимое, hex). После чтения файл удаляется
    автоматически — это и есть смысл ``NamedTemporaryFile``.
    """
    with tempfile.NamedTemporaryFile() as file:
        file.write(payload)
        file.seek(0)
        content = file.read()
        return file.name, content, content.hex()


def main() -> None:
    name, content, hex_view = write_and_read_temp()
    print(Path(name).name != "")
    print(content.decode("utf-8"))
    print(hex_view)


if __name__ == "__main__":
    main()
