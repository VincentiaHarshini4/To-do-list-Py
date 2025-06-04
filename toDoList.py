import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks to show.\n")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
        print()

def add_task(tasks):
    task_text = input("Enter new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("❌ Task cannot be empty!\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done.\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {deleted['task']}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def main():
    print("\n📝 Welcome to the To-Do List CLI App!")
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
