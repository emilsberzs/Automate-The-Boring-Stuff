def spam():
    global eggs
    eggs = 'spam' #Global variable

def bacon():
    eggs = 'bacon' #Local

def ham():
    print(eggs) #Prints Global

eggs = 42  #Global

spam()  #Prints 'spam'
print(eggs) #Still prints spam, as spam() was last to change it.

