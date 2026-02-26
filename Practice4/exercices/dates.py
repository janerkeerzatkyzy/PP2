#1
from datetime import datetime, timedelta

print(datetime.now() - timedelta(days=5))

#2
from datetime import datetime, timedelta

today = datetime.now()
print(today - timedelta(days=1))
print(today)
print(today + timedelta(days=1))

#3
from datetime import datetime

print(datetime.now().replace(microsecond=0))

#4
from datetime import datetime

t1 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
t2 = datetime.strptime(input(), "%Y-%m-%d %H:%M:%S")
print(int(abs((t2 - t1).total_seconds())))