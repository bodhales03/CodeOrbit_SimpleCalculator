# Simple To-Do List CLI App

tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # View tasks
    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    # Remove a task
    elif choice == "3":
        try:
            number = int(input("Enter task number: "))
            tasks.pop(number - 1)
            print("Task removed!")
        except (ValueError, IndexError):
            print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")