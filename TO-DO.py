tasks = []

def add_tasks():
    choose = 'y'   # start with yes

    while choose.lower() == 'y':
        task = input("Add a task: ")
        
        if task:
            tasks.append(task)
        else:
            print("Enter something!!")

        choose = input("Do you want to add another task? (Y/N): ")

add_tasks()
print(tasks)

# def view_tasks():
#     for i in tasks:
#         print(tasks[i])

# view_tasks()