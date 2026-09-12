"""
To-Do List App - A simple command-line task manager with JSON persistence.
"""

import json
from pathlib import Path


TASKS_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    """
    Load tasks from the JSON file.

    Returns:
        list[dict]: A list of task dictionaries. Returns an empty list if the
        file is missing or corrupt.
    """
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read tasks file. Starting with an empty list.")
        return []


def save_tasks(tasks: list[dict]) -> None:
    """
    Save tasks to the JSON file.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError as e:
        print(f"Error saving tasks: {e}")


def view_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks with their completion status.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    if not tasks:
        print("No tasks in the list.")
        return

    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")


def get_task_index(tasks: list[dict], prompt: str) -> int | None:
    """
    Prompt the user to select a valid task index.

    Args:
        tasks (list[dict]): The list of task dictionaries.
        prompt (str): The prompt to display.

    Returns:
        int | None: The valid zero-based index, or None if invalid.
    """
    view_tasks(tasks)
    if not tasks:
        return None

    try:
        index = int(input(prompt)) - 1
        if index < 0 or index >= len(tasks):
            raise IndexError
        return index
    except (ValueError, IndexError):
        print("Invalid task number.")
        return None


def add_task(tasks: list[dict]) -> None:
    """
    Prompt the user to add a new task.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    description = input("Enter a new task: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return

    tasks.append({"description": description, "completed": False})
    print(f"Task added: {description}")
    save_tasks(tasks)


def edit_task(tasks: list[dict]) -> None:
    """
    Prompt the user to edit an existing task.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    task_index = get_task_index(tasks, "Enter the task number to edit: ")
    if task_index is None:
        return

    new_description = input("Enter the new description: ").strip()
    if not new_description:
        print("Task description cannot be empty.")
        return

    tasks[task_index]["description"] = new_description
    print(f"Task updated to: {new_description}")
    save_tasks(tasks)


def remove_task(tasks: list[dict]) -> None:
    """
    Prompt the user to remove a task.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    task_index = get_task_index(tasks, "Enter the task number to remove: ")
    if task_index is None:
        return

    removed = tasks.pop(task_index)
    print(f"Task removed: {removed['description']}")
    save_tasks(tasks)


def complete_task(tasks: list[dict]) -> None:
    """
    Prompt the user to mark a task as complete.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    task_index = get_task_index(tasks, "Enter the task number to mark as complete: ")
    if task_index is None:
        return

    tasks[task_index]["completed"] = True
    print(f"Task marked as complete: {tasks[task_index]['description']}")
    save_tasks(tasks)


def search_tasks(tasks: list[dict]) -> None:
    """
    Prompt the user to search tasks by keyword.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.")
        return

    results = [task for task in tasks if keyword in task["description"].lower()]
    if not results:
        print("No tasks found with that keyword.")
        return

    print("Search results:")
    for index, task in enumerate(results, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")


def sort_tasks(tasks: list[dict]) -> None:
    """
    Prompt the user to sort tasks by completion status or alphabetically.

    Args:
        tasks (list[dict]): The list of task dictionaries.
    """
    print("\n1. Sort by completion status\n2. Sort alphabetically")
    choice = input("Choose sorting option (1-2): ").strip()

    if choice == "1":
        sorted_list = sorted(tasks, key=lambda t: t["completed"])
    elif choice == "2":
        sorted_list = sorted(tasks, key=lambda t: t["description"].lower())
    else:
        print("Invalid option.")
        return

    print("Sorted tasks:")
    for index, task in enumerate(sorted_list, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")


def main() -> None:
    """Run the interactive To-Do List application."""
    tasks = load_tasks()

    print("Welcome to the To-Do List App!")

    while True:
        print(
            "\n1. View tasks\n"
            "2. Add a task\n"
            "3. Edit a task\n"
            "4. Remove a task\n"
            "5. Complete a task\n"
            "6. Search tasks\n"
            "7. Sort tasks\n"
            "8. Exit"
        )
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            sort_tasks(tasks)
        elif choice == "8":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()