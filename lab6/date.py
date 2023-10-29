# Import the datetime module
import datetime

# Get today's date
date_today = datetime.date.today()

# Subtract 5 days from today's date
new_date = date_today - datetime.timedelta(days=5)

# Print the new date
print(new_date)

# Get today's date again
today = datetime.date.today()

# Calculate yesterday and tomorrow
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

# Print the dates
print(f"Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")

# Get the current date and time
current_datetime = datetime.datetime.now()

# Remove the microseconds from the current date and time
current_datetime = current_datetime.replace(microsecond=0)

# Print the current date and time
print(current_datetime)

# Define two specific datetime objects
date1 = datetime.datetime(2023, 10, 19)
date2 = datetime.datetime(2023, 10, 20)

# Calculate the time difference between the two dates in seconds
difference = (date2 - date1).total_seconds()

# Print the time difference in seconds
print(difference)

