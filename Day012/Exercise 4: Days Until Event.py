from datetime import datetime, timedelta

event_name = input("Enter the event name: ")
date_str = input("Enter the date (YYYY-MM-DD): ")

try:
    event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    
    if event_date < today:
        print("Event already passed")
    else:
        days_until = (event_date - today).days
        print(f"There are {days_until} days until {event_name}.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
