"""
To-Do List App
Concepts: Lists, File Handling
Skills: CRUD operations (Create, Read, Update, Delete)
Persistence: JSON (tasks.json)
"""

import json
import os

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json. Returns a list of dicts: {"task": str, "completed": bool}"""
    if not os.path.exists(FILENAME):
        # First run — no file yet, start empty
        return []
    try:
        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if not content:
                # File exists but is empty
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # File exists but is corrupted / not valid JSON
        print("Warning: tasks.json was corrupted. Starting with an empty list.")
        return []
    except OSError as e:
        print(f"Warning: could not read tasks.json ({e}). Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the list of task dicts to tasks.json"""
    try:
        with open(FILENAME, "w") as f:
            json.dump(tasks, f, indent=2)
    except OSError as e:
        print(f"Error: could not save tasks ({e})")


def add_task(tasks):
    task_text = input("Enter new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["completed"] else "[ ]"
        print(f"{i}. {status} {t['task']}")
    print()


def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark completed: "))
        index = num - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        index = num - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    menu = """
===== TO-DO LIST APP =====
1. View tasks
2. Add task
3. Complete task
4. Delete task
5. Exit
===========================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
