# Programming exercise:
# Nephews

# Please write a program which asks for the user's name. 
# If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.

# In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

# Write your solution here
name = input("whats your name? ")
list1 = ['Huey', 'Dewey', 'Louie']
list2 = ['Morty', 'Ferdie']

if name in list1:
    print("I think you might be one of Donald Duck's nephews.")
elif name in list2:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")