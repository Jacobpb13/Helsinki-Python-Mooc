# Programming exercise:
# Alphabetically last

# Python comparison operators can also be used on strings. 
# String a is smaller than string b if it comes alphabetically before b. 
# Notice however that the comparison is only reliable if:

# --the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# --only the standard English alphabet of a to z, or A to Z, is used.

# Please write a program which asks the user for two words. 
# The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.


# Write your solution here
word1 = input("input a word: ")
word2 = input("input a word: ")

if word1>word2:
    print(f"{word1} comes alphabetically last.")
elif word2>word1:
    print(f"{word2} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice.")
