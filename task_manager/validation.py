"""Module for validating user inputs for task details."""

from datetime import datetime


def validate_task_title(title: str) -> tuple[bool, str]:
    if not isinstance(title, str) or not title.strip():
        return False, "Title cannot be empty."
    if len(title.strip()) < 3:
        return False, "Title must be at least 3 characters long."
    return True, ""


def validate_task_description(description: str) -> tuple[bool, str]:
    if not isinstance(description, str) or not description.strip():
        return False, "Description cannot be empty."
    return True, ""


def validate_due_date(due_date_str: str) -> tuple[bool, str]:
    if not isinstance(due_date_str, str) or not due_date_str.strip():
        return False, "Due date cannot be empty."
    try:
        datetime.strptime(due_date_str.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return (
            False,
            f"Invalid date '{due_date_str}'. Use YYYY-MM-DD (e.g., 2026-10-15).",
        )