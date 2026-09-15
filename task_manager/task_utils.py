"""Module containing core business logic for task management."""

from .validation import (
    validate_due_date,
    validate_task_description,
    validate_task_title,
)


def add_task(
    tasks: list[dict], title: str, description: str, due_date: str
) -> bool:
    is_valid_title, title_err = validate_task_title(title)
    if not is_valid_title:
        print(f"Validation Error: {title_err}")
        return False

    is_valid_desc, desc_err = validate_task_description(description)
    if not is_valid_desc:
        print(f"Validation Error: {desc_err}")
        return False

    is_valid_date, date_err = validate_due_date(due_date)
    if not is_valid_date:
        print(f"Validation Error: {date_err}")
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
    print(f"Success: Added Task #{task_id} '{new_task['title']}'.")
    return True


def mark_task_as_complete(tasks: list[dict], task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"Notice: Task #{task_id} is already completed.")
                return False
            task["completed"] = True
            print(f"Success: Task #{task_id} marked as complete.")
            return True

    print(f"Error: Task ID #{task_id} not found.")
    return False


def view_pending_tasks(tasks: list[dict]) -> list[dict]:
    pending = [t for t in tasks if not t["completed"]]
    print("\n--- PENDING TASKS ---")
    if not pending:
        print("No pending tasks. Everything is done!")
        return []

    for task in pending:
        print(f"[{task['id']}] {task['title']} | Due: {task['due_date']}")
        print(f"    Details: {task['description']}")
    return pending


def calculate_progress(tasks: list[dict]) -> float:
    print("\n--- PROGRESS REPORT ---")
    if not tasks:
        print("No tasks available to track.")
        return 0.0

    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    rate = (completed / total) * 100

    print(f"Total: {total} | Completed: {completed} | Pending: {total - completed}")
    print(f"Completion Rate: {rate:.1f}%")
    return rate