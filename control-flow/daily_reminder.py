task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
    case  "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a medium priority task. You can complete it when you have some time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done later.")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
