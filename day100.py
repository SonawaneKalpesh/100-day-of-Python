import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: Task file is corrupted.")
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== YOUR TASKS =====")

    for task in tasks:
        status = "✓ Completed" if task["completed"] else "Pending"

        print(
            f'{task["id"]}. '
            f'{task["title"]} - {status}'
        )


def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to complete: "))

        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task is already completed.")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully.")
                return

        print("Task not found.")

    except ValueError:
        print("Please enter a valid task ID.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()