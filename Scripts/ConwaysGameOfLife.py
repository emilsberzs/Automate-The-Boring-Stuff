#Conway's Game OF Life
import random, time, copy
WIDTH = 6
HEIGHT = 6

#List of list for all cells
nextCells = []
for x in range(WIDTH):
    column = [] #Create new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #Add a living cell
        else:
            column.append(' ') #Add a dead cell
    nextCells.append(column) #Add column of cells

while True: #Main loop
    print('\n\n\n\n\n') #Separates each step with new line
    currentCells = copy.deepcopy(nextCells)

    #Print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space
        print() #Newline at the end of the row

    #Calculate the next steps cells based on current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring coordinates:
            #'%WIDTH' Ensures leftCoord is always between 0 and WIDTH-1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            # Set cell based on Conways Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                #Dead cells with 3 neighbors come alive:
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(2) # 1 Second pause to reduce flickering
       


