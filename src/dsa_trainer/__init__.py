"""Тренажёр по алгоритмам на Python: каталог задач, автопроверка и CLI."""

from __future__ import annotations

from .catalog import Task, all_tasks, get_task, resolve_task_id
from .progress import attempts_path, completed_ids, load_progress, mark_solved

__version__ = "0.1.0"

__all__ = [
    "Task",
    "all_tasks",
    "get_task",
    "resolve_task_id",
    "attempts_path",
    "load_progress",
    "mark_solved",
    "completed_ids",
    "__version__",
]
