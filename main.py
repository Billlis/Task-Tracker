import functions
import time


while True:
    user_action = input("Type add, update, delete, list,(list done, list todo, list in progress) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        task = user_action[5:-1]

        tasks = functions.get_tasks()
        sum_of_tasks = len(tasks)
        now = time.strftime("%b %d, %Y %H:%M:%S")
        tasks[str(sum_of_tasks+1)]={"description": task, "status": "todo", "createdAt": now, "updatedAt": now}

        functions.write_tasks(tasks)
        print(f"Task added successfully (ID: {sum_of_tasks+1})")

    elif user_action.startswith('list'):
        tasks = functions.get_tasks()
        print(f'{"No": >3}. {"Description": <35} {"Status": >15} {"Created at": >25} {"Updated at": >25}')
        if user_action[5:]=="todo":
            for index in tasks:
                task=tasks[index]
                if task["status"]=="todo":
                    print(f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        elif user_action[5:]=="in-progress":
            for index in tasks:
                task = tasks[index]
                if task["status"] == "in-progress":
                    print(f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        elif user_action[5:]=="done":
            for index in tasks:
                task = tasks[index]
                if task["status"] == "done":
                    print(f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')
        else:
            for index in tasks:
                task=tasks[index]
                print(f'{index: >3}. {task["description"]: <35} {task["status"]: >15} {task["createdAt"]: >25} {task["updatedAt"]: >25}')

    elif user_action.startswith('update'):
        try:
            position = int(user_action[7])

            tasks = functions.get_tasks()

            new_task = user_action[10:-1]
            task=tasks[str(position)]
            status=task["status"]
            createdAt=task["createdAt"]
            now = time.strftime("%b %d, %Y %H:%M:%S")
            tasks[str(position)] = {"description": new_task, "status": status, "createdAt": createdAt, "updatedAt": now}

            functions.write_tasks(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('delete'):
        index = int(user_action[7:])

        tasks = functions.get_tasks()

        sum_of_tasks = len(tasks)
        if sum_of_tasks >= index >0:
            for i in range(index, sum_of_tasks):
                tasks[str(i)]=tasks[str(i+1)]
            tasks.pop(str(sum_of_tasks))
            functions.write_tasks(tasks)
            message = f"Task {index} was removed from the list."
            print(message)
        else:
            print("There is no item with that number.")


    elif user_action.startswith('mark-in-progress'):
        try:
            position = int(user_action[-1])
            tasks = functions.get_tasks()
            task = tasks[str(position)]
            description = task["description"]
            createdAt = task["createdAt"]
            now = time.strftime("%b %d, %Y %H:%M:%S")
            tasks[str(position)] = {"description": description, "status": "in-progress", "createdAt": createdAt, "updatedAt": now}
            functions.write_tasks(tasks)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('mark-done'):
        try:
            position = int(user_action[-1])
            tasks = functions.get_tasks()
            task = tasks[str(position)]
            description = task["description"]
            createdAt = task["createdAt"]
            now = time.strftime("%b %d, %Y %H:%M:%S")
            tasks[str(position)] = {"description": description, "status": "done", "createdAt": createdAt,
                                    "updatedAt": now}
            functions.write_tasks(tasks)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")