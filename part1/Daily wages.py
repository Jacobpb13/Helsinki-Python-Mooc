# Programming exercise:
# Daily wages
# Please write a program which asks for the hourly wage, hours worked, and the day of the week. 
# The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# Write your solution here
hourly = float(input("hourly wage "))
hours = int(input("hours worked "))
days = (input("day of week "))
if days != 'Sunday':
    print(f"Daily wages: {hours*hourly} euros")
if days =='Sunday':
    print(f"Daily wages: {hours*hourly*2} euros")
