"""Общие фикстуры и хелперы тренажёра.

Главная фикстура — ``solution``: она находит папку текущей задачи
(``tests/test_<slug>.py`` -> ``solutions/<slug>/``), импортирует
``<slug>.py`` и возвращает модуль, из которого тесты берут функции.

Граничные случаи живут в ``tests/cases.json`` рядом с тестами задачи::

    {
      "count_even": {
        "module": "solution",          # какой файл в папке решения загружать
        "cases": [
          {"input": {"values": [2, 3, 4]}, "output": 2},
          {"input": {"values": []}, "output": 0},
          {"input": {"values": []}, "raises": "ValueError"}
        ]
      }
    }

- ``input`` — словарь ``{имя_аргумента: значение}``;
- ``output`` — ожидаемый результат;
- ``raises`` — ожидаемое исключение по имени (можно ``"solution.ValidationError"``
  для исключения, объявленного в модуле решения);
- ``invalid`` — разрешить не-JSON результат и сравнить тип строго
  (кортеж != список и т. п.).

Проверку запускает ``assert_case``: он даёт внятное сообщение при падении
и не умирает на задачах, где возвращается ``None``.
"""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

TASKS_DIR = ROOT / "tasks"
SOLUTIONS_DIR = ROOT / "solutions"


def task_slug(request: pytest.FixtureRequest) -> str:
    """Имя текущей задачи: ``tests/test_strings_01.py`` -> ``strings_01``."""
    return request.module.__name__.removeprefix("test_")


def load_cases_file() -> dict[str, Any]:
    data = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))
    for spec in data.values():
        spec.setdefault("module", "solution")
        spec.setdefault("cases", [])
        for case in spec["cases"]:
            case.setdefault("invalid", False)
    return data


def import_module_from(folder: Path, module_name: str) -> Any:
    """Импортировать ``<module_name>.py`` из папки задачи.

    Папка на время импорта добавляется в ``sys.path``, чтобы решение могло
    импортировать соседние файлы, но пути разных задач не конфликтовали.
    """
    folder = folder.resolve()
    if not folder.exists():
        pytest.skip(f"Папка решения ещё не создана: {folder}")

    sys.path.insert(0, str(folder))
    try:
        existing = sys.modules.get(module_name)
        if existing is not None and Path(getattr(existing, "__file__", "") or "").parent == folder:
            return importlib.reload(existing)
        sys.modules.pop(module_name, None)
        return importlib.import_module(module_name)
    finally:
        try:
            sys.path.remove(str(folder))
        except ValueError:
            pass


@pytest.fixture(scope="module")
def solution(request: pytest.FixtureRequest) -> Any:
    """Модуль решения текущей задачи (``solutions/<slug>/<slug>.py``)."""
    return import_module_from(SOLUTIONS_DIR / task_slug(request), task_slug(request))


@pytest.fixture(scope="module")
def cases(request: pytest.FixtureRequest) -> dict[str, Any]:
    """Сценарии текущей задачи из ``tests/cases.json``."""
    return load_cases_file()


def parametrize_cases(name: str, spec: dict[str, Any], solution: Any) -> Any:
    """Собрать ``pytest.mark.parametrize`` по сценариям функции ``name``."""
    module = spec_module(spec, solution)
    if not callable(getattr(module, name, None)):
        pytest.fail(f"В модуле решения нет функции {name}()")
    return pytest.mark.parametrize(
        "case",
        [pytest.param(case, id=case_id(case)) for case in spec["cases"]],
    )


def spec_module(spec: dict[str, Any], solution: Any) -> Any:
    """Модуль, в котором объявлена функция из ``spec``."""
    if spec["module"] == "solution":
        return solution
    return import_module_from(Path(solution.__file__).parent, spec["module"])


def case_id(case: dict[str, Any]) -> str:
    try:
        text = json.dumps(case.get("input", {}), ensure_ascii=False)
    except TypeError:
        text = repr(case.get("input"))
    if len(text) > 64:
        text = "..." + text[-61:]
    suffix = f" -> raises {case['raises']}" if "raises" in case else ""
    return text + suffix


def case_ids(cases: list[dict[str, Any]]) -> list[str]:
    return [case_id(case) for case in cases]


def run_cases(solution: Any, name: str, spec: dict[str, Any]) -> list[Any]:
    """Прогнать все сценарии функции ``name`` (для описательных проверок)."""
    return [assert_case(solution, name, spec, case) for case in spec["cases"]]


def assert_case(solution: Any, name: str, spec: dict[str, Any], case: dict[str, Any]) -> Any:
    """Вызвать функцию решения по сценарию и проверить результат."""
    module = spec_module(spec, solution)
    function = getattr(module, name, None)
    if function is None:
        pytest.fail(f"В модуле решения нет функции {name}()")
    payload = dict(case.get("input") or {})
    shown = _safe_json(payload)

    if expected_error := case.get("raises"):
        with pytest.raises(_find_exception(expected_error, solution)):
            function(**payload)
        return None

    result = function(**payload)
    expected = case.get("output")

    if case.get("invalid"):
        assert result == expected and type(result) is type(expected), (
            f"{name}({shown}) -> {result!r} ({type(result).__name__}), "
            f"ожидалось {expected!r} ({type(expected).__name__})"
        )
        return result

    assert result == expected, f"{name}({shown}) -> {result!r}, ожидалось {expected!r}"
    if isinstance(expected, (list, dict, str, int, float, bool)) or expected is None:
        try:
            json.dumps(result)
        except TypeError:
            pytest.fail(f"{name}({shown}): результат {result!r} не JSON-сериализуем")
    return result


def _safe_json(value: Any) -> str:
    try:
        return json.dumps(value, ensure_ascii=False, default=repr)
    except TypeError:
        return repr(value)


def _find_exception(name: str, solution: Any) -> type[BaseException]:
    module_path, _, attribute = name.rpartition(".")
    if not module_path:
        module_path, attribute = "builtins", name
    if module_path == "solution":
        module = solution
    else:
        try:
            module = importlib.import_module(module_path)
        except ImportError:
            pytest.fail(f"Неизвестный модуль исключения в cases.json: {name}")
    exception = getattr(module, attribute, None)
    if not (isinstance(exception, type) and issubclass(exception, BaseException)):
        pytest.fail(f"Неизвестное исключение в cases.json: {name}")
    return exception
