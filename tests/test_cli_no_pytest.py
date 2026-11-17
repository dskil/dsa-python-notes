"""Тесты круговой совместимости CLI и каталога."""

from __future__ import annotations

import dsa_trainer.cli as cli
from dsa_trainer.cli import main


def test_cli_run_without_pytest_reports_cleanly(capsys, monkeypatch):
    """Без pytest ``run`` не должен падать трейсбеком."""
    monkeypatch.setattr(cli, "pytest", None)
    assert main(["run", "2"]) == 2
    assert "pytest не установлен" in capsys.readouterr().err
