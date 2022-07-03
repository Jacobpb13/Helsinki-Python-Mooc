# Programming exercise:
# Greater than or equal to

# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.

# Write your solution here
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

if num1>num2:
    print(f"The greater number was {num1}")
elif num2>num1:
    print(f"The greater number was {num2}")
else:
    print("The numbers are equal!")