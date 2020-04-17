# 4 parts to the conway code
# part 1: checking/storing how many alive and dead cells are next to the x and y position you are checking
# part 2: evaluating the amount of alive and dead cells next to the position in regards to conway rules
# part 3: updating a duplicate list
# part 4: once you go through all the x and y positions, copy the duplicate into the current field
# part 5: print what the 2 dimensional field looks like

import copy, random, time, sys

field = [[]]
alive = '#'
dead = ' '
aliveOrNot = ['#', ' ']

# part 0 create a field list with alive and dead cells
def createField(list, xLength, yLength):
    # check if there is something in the list, if there is delete everything
    if(len(list) > 0):
        del list[:]
    for i in range(xLength):
        # attach a new row to the field
        list.append([])
        for j in range(yLength):
            # fill this new row with cell states
            cellState = random.choice(aliveOrNot) # choose state of cell
            list[i].append(cellState) # append to the row
        
# part 1
# check the viable neighbor spots if wrap around is not allowed
# check if the neighbor spot exists, if it does store the state of the cell in the list
# if the neighbor spot does not exist, treat it like a dead cell
# return the list of neighbor cell states
def findNeighborStatesNoWrap(list,x,y):
    neighborStates = []
    for i in range(-1,2):
        for j in range(-1,2):
            # check if x and  y field positions are between 0 and less than list length
            if(x+i >= 0 and y+j >= 0 and x+i < len(list) and y+j < len(list[0])):
                # if the position is not itself i and j = 0, append what the state of the cell is
                if(not(i == 0 and j == 0)):
                    neighborStates.append(list[x+i][y+j])
            else:
                neighborStates.append(' ')
    return neighborStates

# part 1
# check for index out of bounds at the far right edge and below edge
# for a wrap around conway field. If the neighbor is not out of bounds
# store the state of the neighbor cell
# return what the neighbor states as a list
def findNeighborStatesWrap(list, x, y):
    viableNeighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                # if the position is not itself i and j are zero, append what the state of the cell is
                if(not(i == 0 and j == 0)):
                    viableNeighbors.append(list[x+i][y+j])
            except IndexError:
                viableNeighbors.append(' ')
    return viableNeighbors

# part 4 print field on a 1 by 1 line so it looks good
def printField(field):
    print('\n\n')
    for i in range(len(field)):
        print(field[i])

# part 2 check the conway rules using the neighbor states and current cell state
# return what the state of the cell should be based on the rules
def conwayRules(neighbors, stateOfCell):
    if(stateOfCell == alive):
        if(neighbors.count(alive) == 2 or neighbors.count(alive) == 3):
            return alive
    elif(stateOfCell == dead):
        if(neighbors.count(alive) == 3):
            return alive
    return dead

def playConwaysGame(field):
    while True:
        try:
            fieldTemp = copy.deepcopy(field)
            for i in range(len(field)):
                for j in range(len(field[0])):
                    currentCellState = fieldTemp[i][j]
                    neighbors = findNeighborStatesWrap(fieldTemp, i, j)
                    field[i][j] = conwayRules(neighbors, currentCellState)
            printField(field)
            time.sleep(0.5)
        except KeyboardInterrupt:
            sys.exit()

createField(field,5,5)
printField(field)
print()
playConwaysGame(field)

# part 1
# given the field and position, check the viable neighbors
# return a list of alive and dead cells
def checkPosition(list, position):
    for x in range(len(field)):
    # loop through the field from top to down
        for y in range(len(field[0])):
        # loop through the field from left to right
            viableNeighbors = [
                checktopLeft(field,x,y),
                checktop(field,x,y),
                checktopRight(field,x,y)
            ]
        break


# check the viable neighbor spots using a try except function seeing if the index exists
# starting from the top left and working clockwise
def checktopLeft(list, x, y):
    try:
        list[x-1][y-1]
        return True
    except IndexError:
        return False

def checktop(list, x, y):
    try:
        list[x-1][y]
        return True
    except IndexError:
        return False

def checktopRight(list, x, y):
    try:
        list[x-1][y+1]
        return True
    except IndexError:
        return False

def checkright(list, x, y):
    try:
        list[x][y+1]
        return True
    except IndexError:
        return False

def checkbottomRight(list, x, y):
    try:
        list[x+1][y+1]
        return True
    except IndexError:
        return False

def checkbottom(list, x, y):
    try:
        list[x+1][y]
        return True
    except IndexError:
        return False

def checkbottomLeft(list, x, y):
    try:
        list[x+1][y-1]
        return True
    except IndexError:
        return False

def checkleft(list, x, y):
    try:
        list[x][y-1]
        return True
    except IndexError:
        return False

