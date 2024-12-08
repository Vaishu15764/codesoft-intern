import datetime

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False, "added": datetime.datetime.now()})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return

    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status} (Added: {task['added'].strftime('%Y-%m-%d %H:%M')})")

def mark_done():
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks()
    task_index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid choice.")
