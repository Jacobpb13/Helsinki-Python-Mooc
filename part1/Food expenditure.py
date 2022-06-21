# Programming exercise:
# Food expenditure
# Please write a program which estimates a user's typical food expenditure.

# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

# Write your solution here
cafe = int(input("how many times do you eat at canteen? "))
cost = float(input("how much does it cost each time? "))
food_price = float(input("how much do you spend on groceries weekly? "))

print("Average food expenditure:")
print(f"Daily: {(food_price/7)+((cafe*cost)/7)} euros")
print(f"Weekly: {food_price+(cafe*cost)} euros")