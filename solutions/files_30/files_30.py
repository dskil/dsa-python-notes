"""№30 · Информация об изображении через Pillow.

Источник: ``Train30.py``. Тема: файлы.

Зависимость ``Pillow`` опциональна: без неё функция поднимает понятную ошибку,
а сам тест помечается как пропущенный.
"""

from pathlib import Path


def get_image_info(filename: str | Path) -> tuple[int, int, str]:
    """(ширина, высота, режим) изображения. ValueError, если это не картинка."""
    try:
        from PIL import Image  # noqa: PLC0415 - импорт ленивый, Pillow опционален
    except ImportError as exc:  # pragma: no cover - зависит от окружения
        raise RuntimeError("Установи Pillow: pip install pillow") from exc

    try:
        with Image.open(Path(filename)) as image:
            width, height = image.size
            return width, height, image.mode
    except FileNotFoundError:
        raise
    except Exception as exc:
        raise ValueError(f"Не изображение: {filename}") from exc


def main() -> None:
    try:
        print(get_image_info("image.jpg"))
    except (FileNotFoundError, RuntimeError) as error:
        print(error)


if __name__ == "__main__":
    main()
