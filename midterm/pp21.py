from datetime import datetime 
a = "2026-12-26"
b = datetime.strptime(a, "%Y-%m-%d")
c= list(map(str,input().split()))
for i in c:
    d = datetime.strptime(i, "%Y-%m-%d")
    e = b - d
    print(e.days)
