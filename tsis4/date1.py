import datetime

current_date = datetime.date.today()
new_date = current_date - datetime.timedelta(days=5)

print("Current date:", current_date)
print("New date:", new_date)


import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


import datetime

current_datetime = datetime.datetime.now()
new_datetime = current_datetime.replace(microsecond=0)

print("Current datetime:", current_datetime)
print("New datetime:", new_datetime)


import datetime

date1 = datetime.datetime(2022, 1, 1, 0, 0, 0)
date2 = datetime.datetime(2022, 1, 1, 0, 0, 10)

difference = date2 - date1
difference_seconds = difference.total_seconds()

print("Difference in seconds:", difference_seconds)