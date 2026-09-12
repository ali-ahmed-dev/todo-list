# 📝 To-Do List App

A simple **command-line To-Do List application built with Python**.

This project was created as an **educational project** to practice fundamental programming concepts, file handling, JSON persistence, input validation, and clean code structure.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
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
* Input validation for task numbers and menu choices.
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
* Modular function design
* Input validation
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

**Current Version: 1.0.0**

This version includes:

* Full CRUD operations (Create, Read, Update, Delete)
* Task completion tracking
* Search and sort functionality
* Persistent JSON storage
* Input validation
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

This development history is intentionally preserved to show the actual evolution of the project.

---

## 🚀 Future Improvements

Potential future enhancements include:

* Add unit tests
* Add type hints and docstrings
* Handle JSON file errors gracefully
* Add task priorities and due dates
* Add colorized terminal output
* Support multiple task lists
* Command-line arguments using `argparse`

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

**Built as part of my Python learning journey.**

---
