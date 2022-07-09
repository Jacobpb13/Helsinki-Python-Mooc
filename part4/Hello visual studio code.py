
while True:
    editor=input("Editor: ")
    if editor.lower()=="word" or editor.lower()=="notepad":
        print("Awful")
    elif editor.lower()=="vim" or editor.lower()=="atom" or editor.lower()=="emacs":
        print("Not good")
    elif editor.lower()=="visual studio code":
        print("An excellent choice!")
        break