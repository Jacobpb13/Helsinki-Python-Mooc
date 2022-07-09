# Programming exercise:
# Age check

# Please write a program which asks for the user's age. 
# If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

# Write your solution here
age = int(input("what is your age? "))
if age<5 and age>=0 :
    print("I suspect you can't write quite yet")
elif age<0:
    print("That must be a mistake")
else:
    print(f"Ok, you're {age} years old")