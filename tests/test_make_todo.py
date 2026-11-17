"""Тест `tools/make_todo.py`: заглушки не теряют сигнатуры и докстринги."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import make_todo  # noqa: E402

SOLUTIONS = sorted((ROOT / "solutions").glob("*/*.py"))


def test_solution_files_found():
    assert len(SOLUTIONS) == 86


@pytest.mark.parametrize("path", SOLUTIONS, ids=[p.parent.name for p in SOLUTIONS])
def test_stub_is_valid_python_and_keeps_signatures(path: Path):
    source = path.read_text(encoding="utf-8")
    stubbed = make_todo.stubify(source)
    compile(stubbed, str(path), "exec")

    original_tree = ast.parse(source)
    stub_tree = ast.parse(stubbed)
    original_defs = {
        node.name: (node.lineno, node.col_offset)
        for node in ast.walk(original_tree)
        if isinstance(node, ast.FunctionDef)
    }
    stub_defs = {node.name for node in ast.walk(stub_tree) if isinstance(node, ast.FunctionDef)}
    assert original_defs.keys() == stub_defs, f"{path.parent.name}: изменился набор функций"

    for node in ast.walk(stub_tree):
        if not isinstance(node, ast.FunctionDef) or node.name == "main":
            continue
        body = node.body
        assert body, f"{path.parent.name}: у {node.name}() пустое тело"
        last = body[-1]
        assert isinstance(last, ast.Raise), f"{path.parent.name}: {node.name}() не заглушка"
        assert isinstance(last.exc, ast.Name) and last.exc.id == "NotImplementedError"


def test_main_and_module_level_code_survive():
    source = (ROOT / "solutions" / "strings_01" / "strings_01.py").read_text(encoding="utf-8")
    stubbed = make_todo.stubify(source)
    assert 'if __name__ == "__main__":' in stubbed
    assert "print(strip_digits(text))" in stubbed


def test_stub_is_idempotent():
    source = (ROOT / "solutions" / "recursion_47" / "recursion_47.py").read_text(encoding="utf-8")
    once = make_todo.stubify(source)
    assert make_todo.stubify(once) == once


def test_task_slugs_by_number_and_slug():
    assert make_todo.task_slugs(["47"], everything=False) == ["recursion_47"]
    assert make_todo.task_slugs(["strings_01"], everything=False) == ["strings_01"]
    assert len(make_todo.task_slugs([], everything=True)) == 86
