# Programming exercise:
# Temperatures
# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. 
# If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Write your solution here
temp = int(input("temperature"))

celcius = float((temp-32)*(5/9))

if celcius>0:
    print(f"{temp} degrees Farhenheit equals {celcius} degrees Celsius")
if celcius<0:
    print(f"{temp} degrees Farhenheit equals {celcius} degrees Celsius")
    print("Brr! It's cold in here!")
if temp == 32:
    print(f"{temp} degrees Fahrenheit equals 0.0 degrees Celsius")