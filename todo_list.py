import json

tasks = []
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def write_tasks_to_file():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def get_task_index(prompt):
    view_tasks()
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


def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['description']}")


def add_task():
    new_task = input("Enter a new task: ")
    tasks.append({"description": new_task, "completed": False})
    print(f"Task added: {new_task}")
    write_tasks_to_file()


def edit_task():
    task_index = get_task_index("Enter the task number to edit: ")
    if task_index is not None:
        new_description = input("Enter the new description: ")
        tasks[task_index]["description"] = new_description
        print(f"Task updated to: {new_description}")
        write_tasks_to_file()


def remove_task():
    task_index = get_task_index("Enter the task number to remove: ")
    if task_index is not None:
        removed_task = tasks.pop(task_index)
        print(f"Task removed: {removed_task['description']}")
        write_tasks_to_file()


def complete_task():
    task_index = get_task_index("Enter the task number to mark as complete: ")
    if task_index is not None:
        tasks[task_index]["completed"] = True
        print(f"Task marked as complete: {tasks[task_index]['description']}")
        write_tasks_to_file()


print("Welcome to the To-Do List App!")
while True:
    print("\n1.View tasks\n2. Add a task\n3. Edit a task\n4. Remove a task\n5. Complete a task\n6. Exit")
    choice = input("choose an option (1-6): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        complete_task()
    elif choice == "6":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")