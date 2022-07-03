# Programming exercise:
# The elder

# Please write a program which asks for the names and ages of two persons. 
# The program should then print out the name of the elder.

# Write your solution here
name1=input("first name: ")
age1=int(input("first age: "))
name2=input("first name: ")
age2=int(input("first age: "))

if age1>age2:
    print(f"The elder is {name1}")
elif age2>age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")