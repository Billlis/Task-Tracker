# Task Manager

This is a simple command-line task management tool that allows you to add, update, delete, and list tasks. Each task has a status (e.g., "todo", "in-progress", "done") and a timestamp indicating when it was created and last updated. The tasks are stored in a JSON file (`tasks.json`).

## Features

- **Add a task:** Add a new task to the task list.
- **List tasks:** View tasks by status or all tasks at once.
- **Update a task:** Change the description of a task.
- **Delete a task:** Remove a task by its ID.
- **Mark a task as in-progress:** Change a task's status to "in-progress".
- **Mark a task as done:** Change a task's status to "done".
- **Persistence:** Tasks are stored in a JSON file (`tasks.json`), which is automatically created if it doesn't exist.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/task-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd task-manager
   ```

### Usage

To run the task manager, simply run the Python script:

```bash
python main.py
```

Once the program starts, you can interact with it using the following commands:

- `add <task_description>`: Adds a new task with the given description.
- `list`: Lists all tasks.
- `list todo`: Lists tasks with a "todo" status.
- `list in-progress`: Lists tasks with an "in-progress" status.
- `list done`: Lists tasks marked as "done".
- `update <task_id> <new_description>`: Updates the description of a task.
- `delete <task_id>`: Deletes the task with the given ID.
- `mark-in-progress <task_id>`: Marks the task as "in-progress".
- `mark-done <task_id>`: Marks the task as "done".
- `exit`: Exits the program.

### Example

```bash
Type add, update, delete, list,(list done, list todo, list in progress) or exit: add "Write a README file"
Task added successfully (ID: 1)

Type add, update, delete, list,(list done, list todo, list in progress) or exit: list
 No. Description                           Status         Created at             Updated at             
  1. Write a README file                   todo           Oct 12, 2024 12:34:56  Oct 12, 2024 12:34:56

Type add, update, delete, list,(list done, list todo, list in progress) or exit: mark-done 1
Task 1 marked as 'done'.

Type add, update, delete, list,(list done, list todo, list in progress) or exit: list done
 No. Description                           Status         Created at             Updated at             
  1. Write a README file                   done           Oct 12, 2024 12:34:56  Oct 12, 2024 12:37:22
```

### File Structure

```
.
├── functions.py       # Contains helper functions for managing tasks (get_tasks, write_tasks)
├── main.py            # Main script for running the task manager
├── tasks.json         # JSON file where tasks are stored
└── README.md          # This README file
```

### Code Explanation

- **`functions.py`**: Handles reading and writing tasks from/to the JSON file (`tasks.json`).
- **`main.py`**: Contains the logic for user interaction, including adding, updating, deleting, and listing tasks.

### Error Handling

- If the JSON file (`tasks.json`) does not exist, the program will create it automatically.
- If the JSON file is corrupted or contains invalid data, the program will reset it and start with an empty task list.

### Contributions

Feel free to fork this project and submit pull requests. Any contributions, such as bug fixes or new features, are welcome!

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
