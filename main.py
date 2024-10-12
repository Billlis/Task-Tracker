import functions
import time


while True:
    user_action = input("Type add, update, delete, list,(list done, list todo, list in progress) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        task = user_action[4:]

        tasks = functions.get_tasks()
        sum_of_tasks = len(tasks)
        now = time.strftime("%b %d, %Y %H:%M:%S")
        tasks[str(sum_of_tasks+1)]={"description": task, "status": "todo", "createdAt": now, "updatedAt": ""}

        functions.write_tasks(tasks)
        print(f"Task added successfully (ID: {sum_of_tasks+1})")

    elif user_action.startswith('list'):
        tasks = functions.get_tasks()
        if user_action[5:]=="todo":
            for index in tasks:
                task=tasks[index]
                if task["status"]=="todo":
                    print(index, task["description"])
        elif user_action[5:]=="in progress":
            for index in tasks:
                task = tasks[index]
                if task["status"] == "in progress":
                    print(index, task["description"])
        elif user_action[5:]=="done":
            for index in tasks:
                task = tasks[index]
                if task["status"] == "done":
                    print(index, task["description"])
        else:
            for index in tasks:
                task=tasks[index]
                print(index, task["description"])

    elif user_action.startswith('update'):
        try:
            number = int(user_action[7:])
            print(number)

            tasks = functions.get_tasks()

            new_task = input("Enter new task: ")
            task=tasks[str(number)]
            status=task["status"]
            createdAt=task["createdAt"]
            now = time.strftime("%b %d, %Y %H:%M:%S")
            tasks[str(number)] = {"description": new_task, "status": status, "createdAt": createdAt, "updatedAt": now}

            functions.write_tasks(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('delete'):
        try:
            index = int(user_action[7:])

            tasks = functions.get_tasks()

            sum_of_tasks = len(tasks)
            for i in range(index, sum_of_tasks):
                tasks[str(i)]=tasks[str(i+1)]
            tasks.pop(str(sum_of_tasks))
            functions.write_tasks(tasks)

            message = f"Task {index} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")
