# Алгоритмы на Python — тренажёр с проверкой

[![tests](https://github.com/dskil/dsa-python-notes/actions/workflows/tests.yml/badge.svg)](https://github.com/dskil/dsa-python-notes/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Алгоритмический тренажёр на Python: **86 задач**, у каждой — условие,
готовое решение и собственный набор тестов. Одна задача — одна папка,
один тестовый файл, одна команда для проверки. Прогресс считается локально.

```text
$ dsa-trainer run 47

tests/test_recursion_47.py ......................           [100%]
15 passed in 0.16s

Задача №47 решена ✓ (Ханойские башни)
```

## Быстрый старт для человека, который хочет порешать

Не нужно ничего устанавливать в систему: достаточно Python 3.10+ и git.
Одна команда показывает условие задачи и сразу прогоняет её тесты:

```bash
git clone https://github.com/dskil/dsa-python-notes.git
cd dsa-python-notes
pip install -r requirements-dev.txt

python tools/start.py 33      # условие задачи №33 + запуск её тестов
python tools/start.py         # первая нерешённая задача
python tools/start.py --list  # каталог задач со статусами
```

Цикл работы максимально короткий:

1. `python tools/start.py 33` — прочитал условие, увидел красный тест.
2. Открыл `solutions/recursion_33/recursion_33.py`, написал функцию.
3. Снова `python tools/start.py 33` — зелёное = решено.

Полная инструкция (как читать вывод pytest, что делать с ошибками,
работа в Git Bash) — [docs/HOW_TO_PLAY.md](docs/HOW_TO_PLAY.md).

Если поставил пакет через `pip install -e .`, те же вещи доступны как
`dsa-trainer list` / `show` / `run` / `stats`.

## Что внутри

| Что | Где |
|---|---|
| 86 задач с условиями | [`src/dsa_trainer/catalog.json`](src/dsa_trainer/catalog.json) и [`docs/tasks.md`](docs/tasks.md) |
| Решения (папка на задачу) | [`solutions/`](solutions) |
| Тесты и граничные случаи | [`tests/`](tests) |
| CLI-каталог с прогрессом | [`src/dsa_trainer/cli.py`](src/dsa_trainer/cli.py) |
| Генератор документации | [`tools/build_catalog.py`](tools/build_catalog.py) |

Темы: строки, битовые операции, числа, списки, файлы, рекурсия, словари,
множества, исключения.

## Быстрый старт

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -e .
pytest -q
```

Без установки пакета (CLI тогда запускается как модуль):

```bash
python -m pytest -q

# Windows PowerShell
$env:PYTHONPATH = "src"
python -m dsa_trainer list

# Linux / macOS
PYTHONPATH=src python -m dsa_trainer list
```

## CLI

```bash
dsa-trainer list                 # весь каталог со статусами
dsa-trainer list --todo          # только незакрытые
dsa-trainer list --topic "Рекурсия"
dsa-trainer show 47              # условие задачи
dsa-trainer run 47               # pytest только по этой задаче (и отметка о решении)
dsa-trainer run 47 -- -x         # любые флаги pytest после --
dsa-trainer stats                # прогресс по темам
dsa-trainer reset -y             # очистить журнал
```

Прогресс пишется в `.dsa_progress.json` (файл в `.gitignore`); путь можно
переопределить переменной окружения `DSA_PROGRESS_FILE`.

## Как устроена проверка

Тесты задачи лежат в `tests/test_<slug>.py`. Фикстура `solution` из
`tests/conftest.py` по имени файла находит папку `solutions/<slug>/`,
импортирует `<slug>.py` и отдаёт тестам модуль решения.

Проверки бывают двух видов:

1. **Сценарии через `assert_case`** — список вход->ожидание прямо в тесте
   (так устроено большинство задач, например
   [`tests/test_strings_69.py`](tests/test_strings_69.py)):

   ```python
   CASES = {
       "module": "solution",
       "cases": [
           {"input": {"word": "aabaa"}, "output": 2},
           {"input": {"word": ""}, "output": 0},
           {"input": {"word": 5}, "raises": "TypeError"},
       ],
   }


   @pytest.mark.parametrize("case", CASES["cases"], ids=case_ids(CASES["cases"]))
   def test_border(solution, case):
       assert_case(solution, "longest_prefix_suffix", CASES, case)
   ```

2. **Свойства и сверка с эталоном** — например, `merge_sort` сравнивается
   с `sorted()`, а `count_paths` — с брутфорсом; элементы списков не должны
   меняться после вызова.

Поддерживаются: ожидание исключения (`raises`, в том числе собственного,
например `solution.ValidationError`), строгий тип (`invalid`: кортеж ≠ список),
и обычное сравнение результата.

## Как добавить задачу

1. Выбери номер и slug: `99` → `strings_99`.
2. Зарегистрируй задачу в `src/dsa_trainer/catalog.json`:

   ```json
   {
     "id": 99,
     "slug": "strings_99",
     "topic": "Строки",
     "title": "Короткое имя задачи",
     "description": "Условие, сигнатуры функций и краевые случаи.",
     "status": "todo",
     "source": "HSEtasks/strings/example.py"
   }
   ```

3. Создай модуль решения `solutions/strings_99/strings_99.py`.
4. Создай тесты `tests/test_strings_99.py`.
5. `dsa-trainer run 99`, затем `python tools/build_catalog.py --write`.

## Хочу решать сам

Хочется тренажёра «с нуля», без готовых решений? Один из вариантов:

```bash
python tools/make_todo.py --all          # заменю тела всех функций на ...
python tools/make_todo.py 31 32 47       # или только выбранные задачи
```

Скрипт кладёт рядом `*.py.bak` — вернуть решение: переименуй обратно.
После правок запускай `dsa-trainer run <номер>`.

## Принципы

- **Одна задача — один модуль** с типизированными функциями и `main()`.
  Решения импортируются тестами; `print` в `main()` — только демо-пример.
- **Тесты проверяют поведение, а не реализацию**: возвращаемое значение,
  исключения, отсутствие мутации аргументов.
- **Граничные случаи важнее «примера из условия»**: пустой вход,
  отрицательные числа, один элемент, отсутствие решения.
- **Каталог — источник правды.** `docs/tasks.md` генерируется из
  `catalog.json`; `tests/test_catalog.py` следит, чтобы каталог, папки
  решений и файлы тестов не разъехались.
- **Никаких зависимостей в рантайме.** Только стандартная библиотека
  (Pillow — опционально, для задачи №30).

## Структура

```text
src/dsa_trainer/
  __init__.py      # публичный API: all_tasks(), get_task()...
  __main__.py      # python -m dsa_trainer
  catalog.py       # загрузка и поиск задач по catalog.json
  progress.py      # журнал решённых задач
  cli.py           # команды list / show / run / stats / reset
  catalog.json     # данные всех задач
solutions/
  recursion_47/recursion_47.py
  strings_01/strings_01.py
  ...
tests/
  conftest.py      # фикстуры и assert_case
  test_catalog.py  # консистентность каталога
  test_cli.py      # команды CLI
  test_<slug>.py   # тесты конкретной задачи
tools/
  build_catalog.py # генератор docs/tasks.md
  smoke_cli.py     # сквозная проверка CLI (--full добавляет pytest)
  make_todo.py     # превращает решения в заготовки для самостоятельного решения
docs/tasks.md      # таблица задач и журнал условий
```

## Разработка

```bash
pip install pre-commit
pre-commit install

ruff check . && ruff format --check .
pytest -q
python tools/build_catalog.py --check
python tools/smoke_cli.py --full
```

CI (`.github/workflows/tests.yml`) гоняет lint и тесты на Linux, macOS
и Windows для Python 3.10 и 3.12; `docs.yml` следит, чтобы
`docs/tasks.md` не отставал от каталога.

## Тесты

```text
pytest -q
705 passed, 1 skipped in 2.98s
```

Тестов больше, чем задач: каждая задача покрывает не только пример из
условия, но и краевые случаи, а отдельные тесты охраняют каталог, CLI,
генератор документации и `tools/make_todo.py`.

## Откуда задачи

Большинство задач выросли из учебных скриптов (`Train1`–`Train60`, задачи
по строкам, числам, файлам и рекурсии). Поле `source` хранит исходный файл;
в описаниях отмечены найденные баги исходников — в тренажёре на них
нет «правильного ответа по копипасту», их нужно исправить. Полный список
исправлений — в [CHANGELOG.md](CHANGELOG.md).

## Статус проекта

Проект поддерживается: новый задачи добавляются, `docs/tasks.md` и
`CHANGELOG.md` обновляются в том же PR. Версия — `0.1.0`.

## Лицензия

[MIT](LICENSE) © [dskil](https://github.com/dskil).

## Благодарности

Проект собран из личных тренировочных скриптов и курсовых задач; идея
CLI-каталога и статусов — вдохновлена `exercism`/`codewars`, но здесь
всё живёт в одном репозитории и без серверной части.

