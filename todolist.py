# Basic To-Do List Application

tasks = []  # empty list to store tasks

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please try again.")
