"""Module for validating user inputs for task details."""

from datetime import datetime


def validate_task_title(title: str) -> bool:
    """Validates that title is a non-empty string."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Task title cannot be empty.")
    return True


def validate_task_description(description: str) -> bool:
    """Validates description presence and length limit."""
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Task description cannot be empty.")

    if len(description) > 500:
        raise ValueError("Task description cannot exceed 500 characters.")

    return True


def validate_due_date(due_date_str: str) -> bool:
    """Validates that due date matches YYYY-MM-DD format."""
    if not isinstance(due_date_str, str) or not due_date_str.strip():
        raise ValueError("Due date cannot be empty.")

    try:
        datetime.strptime(due_date_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")