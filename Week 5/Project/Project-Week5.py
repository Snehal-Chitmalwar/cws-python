# Project 2
# Simple Task Manager
my_task_dict = {}  # initialize a dictionary to store task information
while True:
    # Menu itetms initialized below
    Item1 = "1. Create a task"
    Item2 = "2. Update a task"
    Item3 = "3. Delete a task"
    Item4 = "4. View all tasks"
    Item5 = "5. Exit"
    print(f"Menu:\n{Item1}\n{Item2}\n{Item3}\n{Item4}\n{Item5}")
    # ask user to select menu item
    Selected_Item = int(input("Please choose an option(1-5):"))
    if Selected_Item == 1:
        # Create a task and store it in a dictionary
        TaskCount = int(input("Enter Task no.:"))
        taskID = int(input("Enter task ID:"))
        taskTitle = input("Enter task title:")
        taskDesc = input("Enter task description:")
        taskDeadline = input("Enter task deadline:")
        my_task_dict[TaskCount] = [taskID,
                                   taskTitle, taskDesc, taskDeadline]
        # display the created task
        print(f"The task has been created and added to your Task Manager:")
        for k, v in my_task_dict.items():
            if k == TaskCount:
                print(
                    f"{k}.Task ID: {v[0]}\n  Task Title: {v[1]}\n  Task Description: {v[2]}\n  Task Deadline: {v[3]}")
    elif Selected_Item == 2:
        # Update task
        exitflag = False
        # ask user for the task number he wish to make update in
        taskToUpdate = int(input("Enter the task no. you wish to update:"))
        # check if requested task is present in a dictionary to update
        if my_task_dict.get(taskToUpdate) != None:
            while exitflag != True:
                # display update menu for the details of task selected from which user wish to update
                taskItemToUpdate = int(input(
                    "Please select the task item you wish to update from: \n1. Task ID\n2. Task Title\n3. Task Description\n4. Task Deadline\n5. Exit\n"))
                if taskItemToUpdate == 5:  # exit from the update loop
                    exitflag = True
                else:
                    for k, v in my_task_dict.items():
                        for i in range(len(v)):
                            if taskItemToUpdate == i+1 and k == taskToUpdate:
                                v[i] = input("Enter the detail to be updated:")
            for k, v in my_task_dict.items():
                if k == taskToUpdate:
                    print(
                        f"The Task No.{k} is updated successfully in the Task Manager.\nTask ID: {v[0]}\nTask Title: {v[1]}\nTask Description: {v[2]}\nTask Deadline: {v[3]}")
        else:
            print(
                "The task number you have entered is not present in Task Manager. Please try again.")
    elif Selected_Item == 3:
        # ask the task number from user to delete from dictionary
        taskToDelete = int(input("Enter the task no. you wish to delete:"))
        my_task_dict.pop(taskToDelete)
        print(
            f"The task no.{taskToDelete} is deleted from Task Manager successfully.")
    elif Selected_Item == 4:
        # view all tasks in a dictionary
        for k, v in my_task_dict.items():
            print(
                f"{k}.Task ID: {v[0]}\n  Task Title: {v[1]}\n  Task Description: {v[2]}\n  Task Deadline: {v[3]}")
    elif Selected_Item == 5:
        # exit from main menu
        print("Have a good day!!")
        break
    else:
        print("Please enter the items in Menu only.")
