tasks = []

print("Welcome to your To-Do List!")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        # Add a task
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"'{task}' has been added!")
    
    elif choice == "2":
        # View all tasks
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your list is empty!")
    
    elif choice == "3":
        # Remove a task
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("\nEnter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"'{removed_task}' has been removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("Your list is empty!")

    elif choice == "4":
        # Quit the program
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")        