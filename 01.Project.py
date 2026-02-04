seconds_to_mins = 60
mins_to_hours = 60
hours_to_days = 24
days_to_years = 365

total_seconds = int(input("Enter length of time in seconds: "))

years = total_seconds // (seconds_to_mins * mins_to_hours * hours_to_days * days_to_years)
remaining_seconds = total_seconds % (seconds_to_mins * mins_to_hours * hours_to_days * days_to_years)

days = remaining_seconds // (seconds_to_mins * mins_to_hours * hours_to_days)
remaining_seconds %= (seconds_to_mins * mins_to_hours * hours_to_days)

hours = remaining_seconds // (seconds_to_mins * mins_to_hours)
remaining_seconds %= (seconds_to_mins * mins_to_hours)

minutes = remaining_seconds // seconds_to_mins
seconds = remaining_seconds % seconds_to_mins

print(f"Number of years in the length of time: {years}")
print(f"Number of days in the length of time: {days}")
print(f"Number of hours in the length of time: {hours}")
print(f"Number of minutes in the length of time: {minutes}")
print(f"Number of seconds in the length of time: {seconds}")