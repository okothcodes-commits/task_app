"""Main script to run the Task Management CLI."""

from task_manager import (
    add_task,
    calculate_progress,
    mark_task_as_complete,
    view_pending_tasks,
)


def main():
    tasks: list[dict] = []

    while True:
        print("\n==============================")
        print("    TASK MANAGEMENT SYSTEM    ")
        print("==============================")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Pending Tasks")
        print("4. Calculate Progress")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            print("\n--- ADD TASK ---")
            title = input("Enter title: ")
            desc = input("Enter description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, desc, due)

        elif choice == "2":
            if not tasks:
                print("Notice: No tasks available.")
                continue
            task_id = input("Enter Task ID to complete: ").strip()
            if task_id.isdigit():
                mark_task_as_complete(tasks, int(task_id))
            else:
                print("Validation Error: Please enter a valid number.")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            calculate_progress(tasks)

        elif choice == "5":
            print("\nExiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid Choice: Select a number between 1 and 5.")


if __name__ == "__main__":
    main()