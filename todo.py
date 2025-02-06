import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("To-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("\nEnter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!\n")
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_no = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_no < len(tasks):
                    removed_task = tasks.pop(task_no)
                    save_tasks(tasks)
                    print(f"Task '{removed_task}' removed!\n")
                else:
                    print("Invalid task number!\n")
            except ValueError:
                print("Please enter a valid number!\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
