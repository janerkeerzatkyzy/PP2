#1
def squares_up_to(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
print(*squares_up_to(n))

#2
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(map(str, evens(n))))

#3
def div_3_4(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

n = int(input())
print(*div_3_4(n))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input())
b = int(input())

for x in squares(a, b):
    print(x)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
print(*countdown(n))