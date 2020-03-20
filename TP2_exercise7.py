print("----------WELCOME----------")
DAY = 86400
HOUR = 3600
MIN = 60
entered_seconds = int(input("Please enter the seconds:"))

days = entered_seconds // DAY
days_rest = entered_seconds % DAY
hours = days_rest // HOUR
hours_rest = days_rest % HOUR
minutes = hours_rest // MIN
seconds = hours_rest % MIN

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

