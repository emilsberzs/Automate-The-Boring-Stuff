import random

print('I am thinking of number between 1 and 20 \nTake a guess.')
myNumber = random.randint(1,20)
guesses = 0
while True:
    number = int(input())
    if number < myNumber:
        print("Too Low, try again")
        guesses += 1
        continue
    elif number > myNumber:
        print('Too high, try again')
        guesses += 1
        continue
    else:
        print('Well done, You guessed my number in ' + str(guesses) + ' guesses.')
        break