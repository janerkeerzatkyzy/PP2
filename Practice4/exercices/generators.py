#1
def gen_numbers(n):
    for i in range(n + 1):
        yield i

g = gen_numbers(3)

print(next(g))
print(next(g))
print(next(g))
print(next(g)) 

#2
def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

print(*powers_of_two(5))  # 1 2 4 8 16 32