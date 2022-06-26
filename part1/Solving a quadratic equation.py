# Programming exercise:
# Solving a quadratic equation
# In the Python math module there is the function sqrt, which calculates the square root of a number.

#write your solution here
from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

discriminant = b**2 - (4 * a * c)

root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

print(f"The roots are {root1} and {root2}")