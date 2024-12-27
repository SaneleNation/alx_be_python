#This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task.

#User inputs the task,priority and time-bound.
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#Generate a response based on user inputs if certain conditions are met.
match priority :
    case "high":
        chosen_task = "is a high priority task"
    case "medium":
        chosen_task = "is a medium priority task"
    case "low":
        chosen_task = "is a low priority task"
    case _:
        print("Not a valid priority option")

if time_bound == "yes":
    print("Reminder:",task,chosen_task,"that requires immediate attention today!" )
else:
    print("Note:",task,chosen_task,".Consider completing it when you have free time.")
