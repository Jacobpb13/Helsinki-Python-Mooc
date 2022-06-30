# Programming exercise:
# Number of characters

# The function len can be used to find out the length of a string, among other things. The function returns the number of characters in a string.

# Write your solution here
word = str(input("enter a word: "))
if len(word)==1:
    print("Thank you!")
else:
    print(f"There are {len(word)} letters in the word {word}\nThank you!")
