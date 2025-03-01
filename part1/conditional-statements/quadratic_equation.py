from math import sqrt

a: int = int(input("Value of a: "))
b: int = int(input("Value of b: "))
c: int = int(input("Value of c: "))

result1: float = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
result2: float = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)

print(f"The roots are {result1} and {result2}")
