# Programming exercise:
# Grades and points

# Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

# Write your solution here
points = int(input("how many points: "))
if points<0 or points>100:
    print("Grade:impossible!")
elif 0<points<=49:
    print("Grade: fail")
elif 49<points<=59:
    print("Grade: 1")
elif 59<points<=69:
    print("Grade: 2")
elif 69<points<=79:
    print("Grade: 3")
elif 79<points<=89:
    print("Grade: 4")
elif 89<points<=100:
    print("Grade: 5")