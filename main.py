# from functions import get_tasks, write_tasks
import functions

while True:
    user_action = input("Type add, update, delete, list,(list done, list todo, list in progress) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        task = user_action[4:]

        tasks = functions.get_tasks()

        tasks.append(task + '\n')

        functions.write_tasks(tasks)
        print("Task added successfully (ID: 1)")
        #NA GINEI ALLAGI TO ID
    elif user_action.startswith('list'):

        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('update'):
        try:
            number = int(user_action[7:])
            print(number)

            number = number - 1

            tasks = functions.get_tasks()

            new_task = input("Enter new task: ")
            tasks[number] = new_task + '\n'

            functions.write_tasks(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])

            tasks = functions.get_tasks()
            index = number - 1
            task_to_remove = tasks[index].strip('\n')
            tasks.pop(index)

            functions.write_tasks(tasks)

            message = f"Task {task_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print("Bye!")
