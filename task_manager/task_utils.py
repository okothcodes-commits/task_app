"""Module containing core business logic for task management."""

from .validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)


def add_task(
    tasks: list[dict], title: str, description: str, due_date: str
) -> bool:
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Validation Error: {e}")
        return False

    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(new_task)
    print("Task added successfully!")
    return True


def mark_task_as_complete(tasks: list[dict], task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"Notice: Task #{task_id} is already completed.")
                return False
            task["completed"] = True
            print("Task marked as complete!")
            return True

    print(f"Error: Task ID #{task_id} not found.")
    return False


def view_pending_tasks(tasks: list[dict]) -> list[dict]:
    pending = [t for t in tasks if not t.get("completed", False)]
    if not pending:
        print("No pending tasks.")
        return []

    for task in pending:
        print(f"[{task['id']}] {task['title']} | Due: {task['due_date']}")
        print(f"    Details: {task['description']}")
    return pending


def calculate_progress(tasks: list[dict]) -> float:
    if not tasks:
        return 0.0

    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("completed", False))
    return (completed / total) * 100