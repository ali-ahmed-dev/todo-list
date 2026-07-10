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


print("Welcome to the To-Do List App!")
while True:
    print("\n1.View tasks\n2. Add a task\n3. Exit")
    choice = input("choose an option (1-3): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")