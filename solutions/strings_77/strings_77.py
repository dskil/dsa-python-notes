"""№77 · Сколько предложений в тексте.

Источник: ``HSEtasks/strings/count_sentences.py``. Тема: строки.

Предложение заканчивается на ``.``, ``!`` или ``?``; несколько подряд
идущих знаков считаются одним концом предложения.
"""


def count_sentences(text: str) -> int:
    count = 0
    previous_was_punctuation = False
    for symbol in text:
        if symbol in ".!?":
            if not previous_was_punctuation:
                count += 1
            previous_was_punctuation = True
        elif symbol.isalnum():
            previous_was_punctuation = False
    return count


def main() -> None:
    print(count_sentences("привет!!!!! как дела? норм."))


if __name__ == "__main__":
    main()
