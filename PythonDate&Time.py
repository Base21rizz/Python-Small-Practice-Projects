from datetime import datetime

# Getting datetime Information

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(now)
timestamp = now.timestamp()
print(timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
