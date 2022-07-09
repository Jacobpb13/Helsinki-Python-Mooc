# Programming exercise:
# Alphabetically in the middle

# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all lowercase.


# Write your solution here
letter1= str(input("enter a letter: "))
letter2= str(input("enter a letter: "))
letter3= str(input("enter a letter: "))

list = [letter1,letter2,letter3]
list.sort()
print(f"The letter in the middle is {list[1]}")