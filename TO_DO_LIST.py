to_do_list = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task (Mark as complete/incomplete)")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not to_do_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['task']} [{status}]")

def add_task():
    task_name = input("Enter the task: ")
    task = {'task': task_name, 'completed': False}
    to_do_list.append(task)
    print(f"Task '{task_name}' added to your list.")

def update_task():
    view_tasks()
    if to_do_list:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(to_do_list):
            task = to_do_list[task_num - 1]
            task['completed'] = not task['completed']
            status = "complete" if task['completed'] else "incomplete"
            print(f"Task '{task['task']}' marked as {status}.")
        else:
            print("Invalid task number.")

def delete_task():
    view_tasks()
    if to_do_list:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(to_do_list):
            removed_task = to_do_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")

def to_do_list_app():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

to_do_list_app()
