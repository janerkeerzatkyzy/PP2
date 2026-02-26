#1
from datetime import datetime, timedelta

current_time = datetime.now()
result_time = current_time - timedelta(days=5)

print(result_time)

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(today)
print(yesterday)
print(tomorrow)

#3
from datetime import datetime

current_time = datetime.now()
no_microseconds = current_time.replace(microsecond=0)

print(no_microseconds)

#4
from datetime import datetime

first_text = input()
second_text = input()

first_time = datetime.strptime(first_text, "%Y-%m-%d %H:%M:%S")
second_time = datetime.strptime(second_text, "%Y-%m-%d %H:%M:%S")

difference_seconds = abs((second_time - first_time).total_seconds())
print(int(difference_seconds))