def main():
    tasks = []
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            print()
            n_tasks = int(input("How many task you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done":False})
                print("Task added!")
        elif choice == '2':
            print("\nTasks:") 
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}.{task["task"]} - {status}")
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0<= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        elif choice == '4':
            task_index = int(input("Enter the task number to edit: "))-1
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_index]["task"] = new_task
                print("Task updated!")
            else:
                print("Invalid choice.Please try again.")
        elif choice == '5':
            print("Existing the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()       
                