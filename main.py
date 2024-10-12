import functions  # Importing custom module to handle task functions (reading and writing tasks)
import time  # Importing time module to add timestamps to tasks

# Main loop to interact with the user
while True:
    # Asking the user for a command input
    user_action = input("Type add, update, delete, list,(list done, list todo, list in progress) or exit: ")
    user_action = user_action.strip()  # Remove any leading/trailing spaces from the input

    # Handling the 'add' command to add a new task
    if user_action.startswith("add"):
        task = user_action[5:-1]  # Extract the task description (assuming 'add ' is 4 chars long)

        tasks = functions.get_tasks()  # Read the current list of tasks from the file
        sum_of_tasks = len(tasks)  # Count the number of existing tasks
        now = time.strftime("%b %d, %Y %H:%M:%S")  # Get the current timestamp
        # Add the new task with a unique ID and set its status to 'todo'
        tasks[str(sum_of_tasks + 1)] = {"description": task, "status": "todo", "createdAt": now, "updatedAt": now}

        functions.write_tasks(tasks)  # Write the updated list of tasks to the file
        print(f"Task added successfully (ID: {sum_of_tasks + 1})")

    # Handling the 'list' command to display tasks (optional filters: todo, in-progress, done)
    elif user_action.startswith('list'):
        tasks = functions.get_tasks()  # Fetch the current list of tasks
        # Display the table headers
        print(f'{"No": >3}. {"Description": <35} {"Status": >15} {"Created at": >25} {"Updated at": >25}')

        # Listing only tasks that match the filter (todo, in-progress, done)
        if user_action[5:] == "todo":  # If 'list todo' was entered
            for index in tasks:
                task = tasks[index]
                if task["status"] == "todo":
                    # Print each task's details if its status is 'todo'
                    print(
                        f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        elif user_action[5:] == "in-progress":  # If 'list in-progress' was entered
            for index in tasks:
                task = tasks[index]
                if task["status"] == "in-progress":
                    print(
                        f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        elif user_action[5:] == "done":  # If 'list done' was entered
            for index in tasks:
                task = tasks[index]
                if task["status"] == "done":
                    print(
                        f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        else:  # List all tasks if no specific filter was provided
            for index in tasks:
                task = tasks[index]
                print(
                    f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')

    # Handling the 'update' command to update a task description
    elif user_action.startswith('update'):
        try:
            position = int(user_action[7])  # Get the task number to update

            tasks = functions.get_tasks()  # Fetch the current list of tasks

            new_task = user_action[10:-1]  # Get the new task description
            task = tasks[str(position)]  # Get the task being updated
            status = task["status"]  # Preserve the existing task status
            createdAt = task["createdAt"]  # Preserve the original creation time
            now = time.strftime("%b %d, %Y %H:%M:%S")  # Get the current time as the updated time
            # Update the task with the new description while preserving other fields
            tasks[str(position)] = {"description": new_task, "status": status, "createdAt": createdAt, "updatedAt": now}

            functions.write_tasks(tasks)  # Save the updated tasks to the file
        except ValueError:
            print("Your command is not valid.")  # Handle invalid input (e.g., non-integer task number)
            continue

    # Handling the 'delete' command to remove a task
    elif user_action.startswith('delete'):
        try:
            index = int(user_action.split()[1])  # Extract the task number from the command
            tasks = functions.get_tasks()  # Fetch the current list of tasks

            if str(index) not in tasks:
                print(f"Task {index} does not exist.")  # If the task doesn't exist, show an error message
                continue

            tasks.pop(str(index))  # Remove the task from the list

            # Rebuild the task list with updated task numbers after deletion
            updated_tasks = {}
            for i, (task_id, task) in enumerate(tasks.items(), start=1):
                updated_tasks[str(i)] = task

            functions.write_tasks(updated_tasks)  # Save the updated task list
            print(f"Task {index} was removed.")  # Confirm the task has been deleted
        except (ValueError, IndexError):
            print("Invalid delete command. Usage: delete <task_number>")

    # Handling 'mark-in-progress' command to change task status to 'in-progress'
    elif user_action.startswith('mark-in-progress'):
        try:
            position = int(user_action.split()[1])  # Get the task number to mark as 'in-progress'
            tasks = functions.get_tasks()  # Fetch the current list of tasks

            if str(position) not in tasks:
                print(f"Task {position} does not exist.")  # Error message if task doesn't exist
                continue

            task = tasks[str(position)]
            task["status"] = "in-progress"  # Update the task's status
            task["updatedAt"] = time.strftime("%b %d, %Y %H:%M:%S")  # Update the 'updatedAt' timestamp

            functions.write_tasks(tasks)  # Save the updated tasks
            print(f"Task {position} marked as 'in-progress'.")
        except (ValueError, IndexError):
            print("Invalid command. Usage: mark-in-progress <task_number>")

    # Handling 'mark-done' command to mark a task as 'done'
    elif user_action.startswith('mark-done'):
        try:
            position = int(user_action.split()[1])  # Get the task number to mark as 'done'
            tasks = functions.get_tasks()  # Fetch the current list of tasks

            if str(position) not in tasks:
                print(f"Task {position} does not exist.")  # Error message if task doesn't exist
                continue

            task = tasks[str(position)]
            task["status"] = "done"  # Update the task's status to 'done'
            task["updatedAt"] = time.strftime("%b %d, %Y %H:%M:%S")  # Update the 'updatedAt' timestamp

            functions.write_tasks(tasks)  # Save the updated tasks
            print(f"Task {position} marked as 'done'.")
        except (ValueError, IndexError):
            print("Invalid command. Usage: mark-done <task_number>")

    # Exit command to break the loop
    elif user_action.startswith('exit'):
        break  # Exit the program when 'exit' is typed

    # Handling invalid commands
    else:
        print("Command is not valid.")  # Show an error for unrecognized commands

print("Bye!")  # Print a message when the program exits
