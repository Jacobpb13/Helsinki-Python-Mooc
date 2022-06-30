# Programming exercise:
# Typecasting

# When programming in Python, often we need to change the data type of a value.
# For example, a floating point number can be converted into an integer with the function int:

# Write your solution here
number = float(input("enter a number: "))
print(f"Integer part:{int(number)}")
print(f"Decimal part:{number%1}")