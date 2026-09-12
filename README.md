# 📝 To-Do List App

A simple **command-line To-Do List application built with Python**.

This project was created as an **educational project** to practice fundamental programming concepts, file handling, JSON persistence, input validation, testing, and clean code structure.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-12%20Passed-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.1-orange)
![Educational](https://img.shields.io/badge/Project-Educational-purple)

---

## 📌 Features

* View all tasks with completion status.
* Add new tasks.
* Edit existing task descriptions.
* Remove tasks.
* Mark tasks as completed.
* Search tasks by keyword.
* Sort tasks by completion status or alphabetically.
* Persistent storage using a local JSON file.
* Graceful handling of corrupt or missing JSON files.
* Type hints and comprehensive docstrings.
* Input validation for task numbers and menu choices.
* Automated unit tests using Python's built-in `unittest` framework.
* Uses only Python's **standard library**.
* Clean Git history with incremental commits.

---

## 🧠 Educational Purpose

The main purpose of this project is to practice and demonstrate several Python concepts in a small, complete application.

### Concepts practiced

* Functions
* Conditional statements
* Loops
* Dictionaries and lists
* String handling
* Exception handling
* JSON data storage
* File I/O
* `pathlib`
* Modular function design
* Input validation
* Unit testing
* Type hints and docstrings
* Git and GitHub workflow

The project also demonstrates how a simple application can evolve through multiple development stages instead of being written as one large final version.

---

## 💾 Data Storage

Tasks are stored locally in:

    tasks.json

The file is automatically created when a task is first added.

Example structure:

    [
        {
            "description": "Buy groceries",
            "completed": false
        },
        {
            "description": "Finish project",
            "completed": true
        }
    ]

`tasks.json` is intentionally excluded from Git because it contains local user data.

---

## 🧪 Tests

The project includes **12 automated unit tests** using Python's built-in `unittest` framework.

The tests cover:

* Loading tasks from a missing file
* Saving and loading tasks (round-trip)
* Handling corrupt JSON files
* Adding tasks (valid and empty input)
* Editing task descriptions
* Removing tasks
* Marking tasks as complete
* Rejecting invalid task numbers (out-of-range and non-integer)
* Viewing an empty task list
* Searching tasks by keyword

Run the tests with:

    python -m unittest discover -s tests -t . -v

Current result:

    Ran 12 tests in 0.038s

    OK

---

## ▶️ Usage

### 1. Clone the repository

    git clone https://github.com/ali-ahmed-dev/todo-list.git

### 2. Enter the project directory

    cd todo-list

### 3. Run the application

    python todo_list.py

You will see:

    Welcome to the To-Do List App!

    1. View tasks
    2. Add a task
    3. Edit a task
    4. Remove a task
    5. Complete a task
    6. Search tasks
    7. Sort tasks
    8. Exit

    Choose an option (1-8):

---

## 📁 Project Structure

    todo-list/
    │
    ├── todo_list.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_todo_list.py
    ├── .gitignore
    ├── LICENSE
    └── README.md

`tasks.json` is generated locally when the application runs and is excluded from the repository.

---

## 🛠️ Requirements

* Python 3.x
* No external Python packages are required.

The application uses only Python's standard library.

---

## 📜 Version

**Current Version: 1.0.1**

This version includes:

* Full CRUD operations (Create, Read, Update, Delete)
* Task completion tracking
* Search and sort functionality
* Persistent JSON storage
* Graceful error handling for JSON files
* Type hints and docstrings
* 12 unit tests covering all core functionality
* Basic project documentation

---

## 📈 Development History

The project was developed incrementally through separate Git commits:

    Initial commit: basic to-do list with JSON storage
            ↓
    feat: add edit, remove, and complete task functionality
            ↓
    feat: add search and sort functionality
            ↓
    docs: add MIT license
            ↓
    refactor: add type hints, docstrings, and improve error handling
            ↓
    test: add 12 unit tests for core functionality

This development history is intentionally preserved to show the actual evolution of the project.

---

## 🚀 Future Improvements

Potential future enhancements include:

* Add task priorities and due dates
* Add colorized terminal output
* Support multiple task lists
* Command-line arguments using `argparse`
* Export tasks to CSV or Markdown

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

**Author**: [Ali Ahmed Al-Zaidi](https://github.com/ali-ahmed-dev)

---
**Built as part of my Python learning journey.**
