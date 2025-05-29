task = input("Enter your task: ")
priority = input("What is the priority level? (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Provide a customized reminder using match-case
match priority:
    case "high":
        message = f"Reminder: Your HIGH priority task is '{task}'."
    case "medium":
        message = f"Reminder: Your MEDIUM priority task is '{task}'."
    case "low":
        message = f"Reminder: Your LOW priority task is '{task}'."
    case _:
        message = f"Reminder: Your task '{task}' has an UNKNOWN priority."

# Check if the task is time-bound and append the urgency message
if time_bound == "yes":
    message += " It requires immediate attention today!"

# Print the final reminder
print(message)