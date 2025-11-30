# Personal To-Do List Application

A simple Python-based task management program using JSON file handling.

## Introduction

The Personal To-Do List Application is a command-line tool developed in Python to help users manage their daily tasks. It allows adding, viewing, editing, deleting, and completing tasks. All data is stored in a JSON file, making the application lightweight and easy to use.

## Objective

* To build a basic task management system.
* To apply Python concepts like OOP, functions, and file handling.
* To store tasks using JSON without any database.

## Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Mark tasks as completed
* Delete tasks
* Filter tasks by category
* Tasks are saved automatically in a JSON file

## Technologies Used

* Python 3
* JSON File Handling
* Object-Oriented Programming
* Command-Line Interface

## Project Structure

```
todo_app/
 ├── todo.py
 ├── tasks.json
 └── README.md
```

## How to Run

1. Install Python 3.x
2. Open the terminal and navigate to the project folder

   ```
   cd path/to/todo_app
   ```
3. Run the program

   ```
   python todo.py
   ```

## Usage

After running the program, a menu appears with the following options:

1. Add Task
2. View All Tasks
3. Edit Task
4. Mark Task as Completed
5. Delete Task
6. Filter Tasks by Category
7. Exit

Enter the number to perform the corresponding operation.

## Data Storage
The application stores tasks in a file named `tasks.json` in the following format:

{
    "title": "Sample Task",
    "description": "Task description",
    "category": "Work",
    "completed": false
}

## Future Enhancements
* Add a graphical user interface
* Add due dates and reminders
* Add task priority levels
* Export tasks to CSV or PDF
* Multi-user login support

## Conclusion
This project demonstrates the use of Python for building a simple console-based to-do list application. It strengthens understanding of OOP, file handling, and application design.
