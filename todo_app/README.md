# Personal To-Do List Application

A simple and lightweight task management program built using Python and JSON file handling.

## 📌 Introduction

The Personal To-Do List Application is a command-line based tool that helps users add, view, edit, delete, and manage their daily tasks. All tasks are stored locally in a JSON file, making the application easy to use and fully offline.

## 🎯 Objectives

* To build a basic task organizer using Python
* To practice OOP concepts, functions, and file handling
* To store user tasks in a JSON file without using a database

## ✨ Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Mark tasks as completed
* Delete tasks
* Filter tasks by category
* Automatic saving of tasks to `tasks.json`

## 🛠 Technologies Used

* Python 3
* JSON File Handling
* Object-Oriented Programming
* Command-Line Interface

## 📁 Project Structure

```
todo_app/
 ├── todo.py        # Main Python program
 ├── tasks.json     # Auto-created file for storing tasks
 └── README.md      # Project documentation
```

## ▶️ How to Run

1. Install Python 3
2. Open the terminal and navigate to the project folder

   ```
   cd path/to/todo_app
   ```
3. Run the program

   ```
   python todo.py
   ```

## 📦 Data Storage

All tasks are saved inside `tasks.json` in this format:

```
{
    "title": "Example Task",
    "description": "Sample description",
    "category": "Work",
    "completed": false
}
```

## 🚀 Future Enhancements

* Add GUI using Tkinter
* Integrate due dates & reminders
* Implement task priority levels
* Export tasks to CSV/PDF
* Add multi-user login

## ✔ Conclusion

This project provides a simple and effective way to manage personal tasks while practicing core Python programming concepts like OOP and file handling.
