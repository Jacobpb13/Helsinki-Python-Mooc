# Programming exercise:
# Leap year

# Generally, any year that is divisible by four is a leap year. 
# However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

# Write your solution here
leap_year = int(input("Enter the year: "))

if leap_year % 4 == 0 and leap_year % 100 != 0:
    print("That year is a leap year.")
elif leap_year % 400 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")