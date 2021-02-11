import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

try:
    print(round((-b + math.sqrt(b**2-(4 * a * c))) / (2 * a), 2))
    print(round((-b - math.sqrt(b**2-(4 * a * c))) / (2 * a), 2))
except ValueError:
    print("There is an error somewhere in your input")
