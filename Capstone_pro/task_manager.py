
from datetime import date

def task_schduler():
    jobs=int(input("Enter the number of task you want to manage"))
    
    task_dict={}
    for i in range(jobs):
        task_name=input(f"Enter the name of the task {i+1}")
        task_priority=int(input("Enter the priority of the task (1-10)"))
        task_duration=int(input("Enter the duration of the task in minutes"))
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))

        try:
            user_date = date(year, month, day)
            print("You entered:", user_date)
        except ValueError:
            print("Invalid date! Please enter a valid year, month, and day.")

        print(f"Task {task_name} scheduled with priority {task_priority} and duration {task_duration} minutes")
        task_dict[task_name]={"priority":task_priority, "duration":task_duration, "deadline":user_date}
    return task_dict  # Return the dictionary of tasks with their details for further scheduling


def schedule_task(task_dict):
    # Implement scheduling logic here
    # Sort the tasks by priority and deadline in ascending order
    # The task with the highest priority should be executed first
    # The task with the earliest deadline should be executed first
    # You can use a combination of priority and deadline to break ties
    # Example:
    sorted_by_values = dict(sorted(task_dict.items(), key=lambda item: (item[1]['priority'], item[1]['deadline'])))

    print(sorted_by_values)
    

    print("the task with the highest priority")
    for item in sorted_by_values:
        
        print(f"Task: {item}")


value=task_schduler() 
schedule_task(value)
