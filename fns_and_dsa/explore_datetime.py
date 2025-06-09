from datetime import datetime, timedelta
current_date = datetime.now()
def display_current_datetime():
    print(f"The current date is: '{current_date}'")
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The formatted date is: '{formatted_date}'")

    #future dates
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_dates = current_date + timedelta(days=number_of_days)
    return print(f"Future date: '{future_dates.strftime('%y-%m-%d')}'")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()