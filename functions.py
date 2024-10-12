import os  # Importing the 'os' module to work with file system paths
import json  # Importing 'json' module to read and write JSON data

FILEPATH = "tasks.json"  # Defining the path for the tasks file


def get_tasks(filepath=FILEPATH):
    """
    Read a JSON file and return the list of tasks.
    If the file does not exist, create an empty JSON file.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        # If the file doesn't exist, create an empty JSON file
        with open(filepath, 'w') as file_local:
            json.dump({}, file_local)  # Write an empty JSON object (dictionary)
        print(f"{filepath} has been created.")  # Notify that the file was created

    try:
        # Attempt to open and read the JSON file
        with open(filepath, 'r') as file_local:
            tasks_local = json.load(file_local)  # Load the tasks from the file
    except (json.JSONDecodeError, ValueError):
        # If the file is corrupted or contains invalid JSON, initialize empty tasks
        tasks_local = {}
        print(f"Invalid JSON in {filepath}, re-initializing with empty tasks.")

    return tasks_local  # Return the loaded tasks (or an empty dictionary)


def write_tasks(tasks_arg, filepath=FILEPATH):
    """
    Write the tasks list to the JSON file.
    """
    # Open the file in write mode and save the updated tasks
    with open(filepath, 'w') as file_local:
        json.dump(tasks_arg, file_local)  # Write the tasks list to the file


if __name__ == "__main__":
    # This code only runs when the file is executed directly (not imported)
    print("Hello")  # Print a greeting message
    print(get_tasks())  # Print the current tasks (or initialize the file if it doesn't exist)
