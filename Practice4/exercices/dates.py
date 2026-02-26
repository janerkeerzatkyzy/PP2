#1
from datetime import datetime
x = datetime.now()
print(x)

#2
from datetime import datetime, timedelta

now = datetime.now()

print(now + timedelta(days=1)) 
print(now - timedelta(days=1))  
print(now + timedelta(hours=3))
print(now - timedelta(minutes=30))

#3
from datetime import date

a = date(2026, 2, 27)
b = date(2026, 3, 1)

print(a < b)   # True
print(a == b)  # False