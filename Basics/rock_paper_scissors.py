import random
print('ROCK, PAPER, SCRISSORS')
wins = 0
losses = 0
ties = 0
print('Enter Your move (r)ock, (p)aper, (s)cissors. Type "exit" to exit')

for i in range(10):
        print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + " Ties.")
        num = random.randint(1,3)
        computerMove = ''
        playerMove = ''
        if num == 1:
            computerMove = 'rock'
            playerMove = input("Enter Your move: ")
            if playerMove == 'r':
                 print('Tie')
                 ties += 1
            elif playerMove == 'p':
                print('You win')
                wins += 1
            elif playerMove == 's':
                 print('You lose')
                 losses += 1
            else:
                 continue
        elif num == 2:
            computerMove = 'paper'
            playerMove = input("Enter Your move: ")
            if playerMove == 'r':
                 print('You lose')
                 losses += 1
            elif playerMove == 'p':
                print('Tie')
                ties += 1
            elif playerMove == 's':
                 print('You win')
                 wins += 1
            else:
                 continue
        else:
            computerMove = 'scissors'
            playerMove = input("Enter Your move: ")
            if playerMove == 'r':
                 print('You win')
                 wins += 1
            elif playerMove == 'p':
                print('You lose')
                losses += 1
            elif playerMove == 's':
                 print('Tie')
                 ties += 1
            else:
                 continue
        
print('Out of 10 rounds, You got:\n' + str(wins) + ' Wins\n' + str(ties) + ' Ties\n' + str(losses) + ' Losses')
        