# To-Do List App

A command-line To-Do List application built in Python. Supports adding, viewing,
completing, and deleting tasks, with tasks saved permanently to a JSON file so
they persist between runs.

## Features
- Add a new task
- View all tasks with completion status
- Mark a task as completed
- Delete a task
- Tasks automatically saved to `tasks.json` and loaded on startup
- Handles missing, empty, or corrupted `tasks.json` gracefully
- Input validation for menu choices and task numbers

## Tech
- Python 3.x
- Built-in `json` module only (no external libraries)

## How to Run
```
python main.py
```
(On some systems: `python3 main.py` or `py main.py`)

## Project Structure
```
todo_app/
├── main.py
├── tasks.json          (created automatically on first run)
├── README.md
└── screenshots/
```

## CRUD Mapping
| Operation | Function        |
|-----------|------------------|
| Create    | `add_task()`     |
| Read      | `view_tasks()`   |
| Update    | `complete_task()`|
| Delete    | `delete_task()`  |

## Algorithms

**Add Task:** read task name → store with `completed: False` → save to JSON.

**View Tasks:** load tasks → print each with its status.

**Complete Task:** select task number → set `completed: True` → save file.

**Delete Task:** select task number → remove from list → save file.

## Future Enhancements
- GUI using Tkinter
- Flask web version
- SQLite database
- Login system
- Due dates, reminders, priorities
- Search and filtering
