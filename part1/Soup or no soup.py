# Programming exercise:
# Soup or no soup
# Please write a program which asks for the user's name. 
# If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. 
# The price of a single portion is 5.90.

# Write your solution here
price = 5.9
name = input("whats your name? ")
if name != 'Jerry':
    portions = int(input("How many portions of soup? "))
    print(f"The total cost is {price*portions}")
print("Next please!")