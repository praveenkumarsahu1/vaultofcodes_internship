import json
import os

TASKS_FILE = "tasks.json"


class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            category=data.get("category", ""),
            completed=data.get("completed", False)
        )


def save_tasks(tasks):
    """Save list of Task objects to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)


def load_tasks():
    """Load tasks from JSON file and return a list of Task objects."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def print_tasks(tasks):
    """Display all tasks in a user-friendly format."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n------ Task List ------")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task.completed else "✗ Pending"
        print(f"{i}. {task.title} [{task.category}] - {status}")
        print(f"   Description: {task.description}")
    print("------------------------\n")


def add_task(tasks):
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    category = input("Enter task category (Work/Personal/Urgent/etc.): ").strip()

    if title == "":
        print("Task title cannot be empty!")
        return

    new_task = Task(title, description, category)
    tasks.append(new_task)
    print("Task added successfully!\n")


def mark_task_completed(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1].mark_completed()
            print("Task marked as completed!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def delete_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            print(f'Task "{deleted.title}" deleted successfully!\n')
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def edit_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to edit: "))
        if 1 <= index <= len(tasks):
            task = tasks[index - 1]
            print("\nLeave a field empty to keep it unchanged.")
            new_title = input(f"New title (current: {task.title}): ").strip()
            new_desc = input(f"New description (current: {task.description}): ").strip()
            new_cat = input(f"New category (current: {task.category}): ").strip()

            if new_title:
                task.title = new_title
            if new_desc:
                task.description = new_desc
            if new_cat:
                task.category = new_cat

            print("Task updated successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def filter_by_category(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    category = input("Enter category to filter (e.g., Work/Personal/Urgent): ").strip()
    filtered = [t for t in tasks if t.category.lower() == category.lower()]

    if not filtered:
        print(f"\nNo tasks found in category '{category}'.\n")
    else:
        print(f"\nTasks in category '{category}':")
        print_tasks(filtered)


def main():
    tasks = load_tasks()

    while True:
        print("===== Personal To-Do List Application =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Edit Task")
        print("4. Mark Task Completed")
        print("5. Delete Task")
        print("6. Filter Tasks by Category")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            filter_by_category(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("Tasks saved. Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select from 1 to 7.\n")


if __name__ == "__main__":
    main()
