#to do list

tasks = []

while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("Tasks:")
        for task in tasks:
            print("-", task)


    elif choice == "3":
        break

    else:
        print("Invalid choice")

