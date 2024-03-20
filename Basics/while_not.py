name = ''
while not name:
    print('Enter Your name:')
    name = input()
print("How many guests?")
numOfGuests = int(input())
if numOfGuests:
     print("Ok, we will have space for " + str(numOfGuests) + " guests")