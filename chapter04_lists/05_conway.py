# 4 parts to the conway code
# part 1: checking/storing what is next to the position you are checking
# part 2: evaluating what is next to the position in regards to conway
# part 3: updating the duplicate list
# part 4: printing what the 2 dimensional field looks like

import copy, random, time

field = [[]]
aliveOrNot = ['#', '']

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
        
# check the viable neighbor spots if wrap around is not allowed
# return true if the spot exists, false if it does not
# return this in list form
def findViableNeighbors(list,x,y):
    viableNeighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            if(x+i < 0 or y+j < 0 or x+i > len(list) or y+j > len(list[0])):
                viableNeighbors.append(False)
            else:
                viableNeighbors.append(True)
    return viableNeighbors

# check for index out of bounds for a wrap around conway
def findOutOfBoundsNeighbors(list, x, y):
    viableNeighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                list[x+i][y+j]
                viableNeighbors.append(True)
            except IndexError:
                viableNeighbors.append(False)
    return viableNeighbors

createField(field,4,5)
print(field)
viableNeighbors = findOutOfBoundsNeighbors(field,4,5)
print(viableNeighbors)

# part 1
def checkPosition(list, position):
    while True:
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

