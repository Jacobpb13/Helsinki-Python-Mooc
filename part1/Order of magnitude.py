# Programming exercise:
# Order of magnitude
# Please write a program which asks the user for an integer number. 
# The program should then print out the magnitude of the number according to the following examples.

# Write your solution here
number = int(input("enter a number: "))
if number<10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    
if 10<number and number<100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    
if 100<number and number<1000:
    print("This number is smaller than 1000")

print("Thank you!")