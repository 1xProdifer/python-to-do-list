import json
import os

file_path = "tasks.json"
    
def home():
    print("Welcome to the app, Enjoy Tracking your tasks")
    while True:
        try:
            user_choice = int(input("""
                                What would you like to do:
                                1. Add a task
                                2. Delete a Task
                                3. View all the tasks
                                4. Complete a task
                                (Only enter the number corrosponding to the option): """))
        except:
            print('Value error: Please Only Write the number corrosponding to the option')
            continue
        
        if user_choice == 1:
            addTask()
        elif user_choice == 2:
            deleteTask()
        elif user_choice == 3:
            viewTask()
        elif user_choice == 4:
            completeTask()
        
        else:
            print("Invalid choice Please try again!!")
            continue
        
def addTask():

    user_task = input("Please Write down the task you want to save: ")
    
    # creates a file if it doesnt exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)    
    
    with open(file_path, 'r') as f:
        tasks = json.load(f) # reads the file
    
    # if tasks are there then
    if tasks:
        last_id = max(task["ID"] for task in tasks) # get the highest id
        next_id = last_id + 1
    else:
        next_id = 1 
    
        #Dictory the task
    task_data = {
        "Task": user_task,
        "Done": False,
        "ID" : next_id
    }      
      
    tasks.append(task_data)
    
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)
            
def deleteTask():
    # Make sure file exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    # Load tasks
    with open(file_path, 'r') as f:
        tasks = json.load(f)

    if not tasks:
        print("There are no available tasks to delete.")
        return

    try:
        user_input = int(input("""\nWould you like to:
1. Delete a specific task
2. Delete all tasks
Please enter the corresponding number: """))
    except:
        print("Please enter a valid option.")
        return

    if user_input == 1:
        print("\nHere are your current tasks:")
        for task in tasks:
            print(f"ID: {task['ID']} | Task: {task['Task']} | Done: {task['Done']}")

        try:
            task_to_delete = int(input("Enter the ID of the task you would like to delete: "))
        except:
            print("Invalid ID.")
            return

        matching_ids = [task for task in tasks if task["ID"] == task_to_delete]
        if not matching_ids:
            print("No task found with that ID.")
            return

        tasks = [task for task in tasks if task["ID"] != task_to_delete]
        with open(file_path, 'w') as f:
            json.dump(tasks, f, indent=4)

        print("Task deleted successfully.")

    elif user_input == 2:
        with open(file_path, 'w') as f:
            json.dump([], f)
        print("All tasks have been deleted.")

    else:
        print("Invalid option selected.")

            
def viewTask():
    
    #creates the file
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([],f)
        
    # loads the file to be read with the variable tasks
    with open(file_path,'r') as f:
        tasks = json.load(f) 
              
        if tasks:

            try:   
                user_input = int(input("""Would you like to -: 
                    1. Look at all the tasks (Completed and uncompleted).
                    2. Look at all the completed tasks.
                    3. Look at all the uncompleted tasks.
                    Please write the number corrosponding to the option you would like to perform: """))
            except:
                print("Invalid input, please type the correct option number")
                return
            
            if user_input == 1:
                for task in tasks:
                    all_tasks = (f"\n ID {task['ID']} | Task: {task['Task']} | Done: {task['Done']}")
                    print(all_tasks)
                    print('-------------------------')
            
            elif user_input == 2:
                completed_tasks = [task for task in tasks if task['Done'] == True]
                
                if completed_tasks:
                    for task in completed_tasks:
                        print(f"\n ID: {task['ID']} | Task: {task['Task']} | Done: {task['Done']} \n")
                else:
                    print('no tasks are listed as completed')
                    
            elif user_input == 3:
                uncompleted_tasks = [task for task in tasks if task['Done'] == False]
                
                if uncompleted_tasks:
                    for task in uncompleted_tasks:
                        print(f"\n ID: {task['ID']} | Task: {task['Task']} | Done: {task['Done']} \n")
                else:
                    print('No uncompleted tasks are available to display')
        else:
            print("There are currently no tasks that you have added. Please add a task to view them")
    
def completeTask():
    
    # Creates the file
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([],f)
    
    # loads the file to be read
    with open(file_path,'r') as f:
        tasks = json.load(f)
    
    if tasks:
        print("Please look at all the Tasks below")
        for task in tasks:
            all_tasks = (f"\n ID: {task['ID']} | Task: {task['Task']} | Done: {task['Done']} \n")
            print(all_tasks)
        
        while True:     
            try:
                user_input = int(input("""\n Would you like to-:
                                       1. Mark a specific task completed
                                       2. Mark all tasks completed
                                       Please Write the number corrosponding to the options: """))
            except:
                print('Invalid Input, Please write a number')
                continue
            
            if user_input == 1:
                try:
                    task_id = int(input("Enter the ID of the task to mark as completed: "))
                except:
                    print("Invalid input.")
                    continue

                found = False
                for task in tasks:
                    if task_id == task['ID']:
                        found = True
                        break
                
                if found:
                    task['Done'] = True   
                    with open(file_path, 'w') as f:
                        json.dump(tasks ,f, indent=4)
                    print('Task has been marked Completed (True)')
                    break      
            
            elif user_input == 2:
                for task in tasks:
                    task['Done'] = True
                with open(file_path, 'w') as f:
                    json.dump(tasks, f, indent=4)  
                print('ALL tasks are marked Completed') 
                break       
    else:
        print('There are no tasks available. Please add a task. ')

