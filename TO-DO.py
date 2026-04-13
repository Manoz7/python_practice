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


def view_tasks():
    print("The tasks are:")
    for task in tasks:
        print(task)

view_tasks()

def delete_tasks():
    tasks.pop()

delete_tasks()
view_tasks()