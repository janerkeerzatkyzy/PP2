#1
import math

deg = float(input("Input degree: "))
rad = deg * math.pi / 180
print(f"Output radian: {rad:.6f}")

#2
h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

area = (b1 + b2) / 2 * h
print(f"Expected Output: {area}")

#3
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s * s) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:g}")

#4
base = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

area = base * h
print(f"Expected Output: {area}")