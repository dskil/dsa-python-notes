"""№76 · RLE-сжатие строки.

Источник: ``HSEtasks/strings/compress_string.py``. Тема: строки.

Пример: ``'aasssbb'`` -> ``'a2s3b2'``.
"""


def compress_string(word: str) -> str:
    if not word:
        return ""
    chunks: list[str] = []
    previous = word[0]
    count = 1
    for symbol in word[1:]:
        if symbol == previous:
            count += 1
        else:
            chunks.append(previous if count == 1 else f"{previous}{count}")
            previous, count = symbol, 1
    chunks.append(previous if count == 1 else f"{previous}{count}")
    return "".join(chunks)


def decompress_string(encoded: str) -> str:
    """Обратная операция: ``'a2s3'`` -> ``'aasss'``."""
    result: list[str] = []
    symbol = ""
    digits = ""
    for char in encoded:
        if char.isdigit():
            digits += char
        else:
            if symbol:
                result.append(symbol * int(digits or 1))
            symbol, digits = char, ""
    if symbol:
        result.append(symbol * int(digits or 1))
    return "".join(result)


def main() -> None:
    print(compress_string("aasssbb"))


if __name__ == "__main__":
    main()
