task = input("Enter task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case "high":
        print(f"Reminder: '{task}' is high priority that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is medium priority that should be addressed soon" 
              )
        else:
            print(f"Reminder: '{task}' is medium priority and can be addressed later")
    case "low":
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time. ")
