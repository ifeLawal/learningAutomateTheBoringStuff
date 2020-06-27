# steps for tic tac toe terminal
# initiate empty 2D board
# create a game loop 
# in game loop check for player turn
# check user input to confirm if ther slot is available
# if a move has been made check for the win state
# if a player has won stop the game and let the players know
# if the board is filled let the players know it is a tie

# things to consider
# are we passing the array to the check winner function

# there are two ending states for a game
# win and tied

# create a board at the start of the game
# print out the board

# during user inputs we have to check
# 1 that a valid position was passed : aka it's a number and a dimension on the
# 2d array
# 2 that the position is empty
# once an input on the board is made, check the game state


import random, numpy as np

trueFalseArr = [True, False]

# return tuple with (winner or '' string if no winner, if game is tied)
def checkGameState(board):

    # check horizontal wins
    for x in range(len(board)):
        if(board[x][0] != '_' and all(marker == board[x][0] for marker in board[x])):
            print('horizontal win')
            return board[x][0], False
    
    # transpose 2Dimensional array so the vertical matches are in one array
    numpy_array = np.array(board)
    transpose = numpy_array.T
    # check vertical wins
    for x in range(len(transpose)):
        if(transpose[x][0] != '_' and all(marker == transpose[x][0] for marker in transpose[x])):
            print('vertical win')
            return transpose[x][0], False

    # check diagonal wins
    if(board[0][0] != '_' and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        print('diagonal win')
        return board[0][0], False

    if(board[0][2] != '_' and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        print('diagonal win')
        return board[0][0], False
    
    # check for gameTied
    for x in range(len(board)):
        if(any(marker == '_' for marker in board[x])):
            return '', False
    
    return '', True
    
def createBoard():
    twoDimensionalBoard = [['_','_','_'],['_','_','_'],['_','_','_']]
    return twoDimensionalBoard

def requestInputAndCheckIfValid():
    userMove = 'failure'
    for x in range(0, 4):  # try 4 times
            try:
                userMove = int(input())
            except (NameError, SyntaxError), e:
                if(x > 3): 
                    print("1 more chance for a valid number between 0 and 2")
                else: 
                    print('Please enter an integer')
                continue
            if userMove > 2 or userMove < 0:
                if(x > 3): 
                    print("1 more chance for a valid number between 0 and 2")
                else: 
                    print('Please enter an integer between 0 and 2')
            else:
                break

    return userMove

def printBoard(board):
    for x in range(len(board)):
        print(board[x])

def playGame():
    winner = ''
    gameIsTied = False
    # randomize who starts first
    playerXTurn = trueFalseArr[random.randint(0,1)]
    # welcome players
    print("Welcome to Tic Tac Toe in Python. \nHere is the board!")
    # create and print board in terminal
    ticTacToeBoard = createBoard()
    printBoard(ticTacToeBoard)
    while(not(gameIsTied) and winner == ''):
        # check for keyboard interrupt to stop the game
        try:
            # notify players of whose turn it is
            if(playerXTurn):
                print("It's player X's turn!")
            else:
                print("It's player O's turn!")

            # take user input to place a marker on the board
            print('To place your marker, choose your row')
            rowInput = requestInputAndCheckIfValid()
            if(rowInput == 'failure'):
                raise KeyboardInterrupt
            print('Choose your column')
            columnInput = requestInputAndCheckIfValid()
            if(columnInput == 'failure'):
                raise KeyboardInterrupt
            print(rowInput, columnInput)
            if(ticTacToeBoard[rowInput][columnInput] != '_'):
                print('That position already has a value')
                continue
            else:
                ticTacToeBoard[rowInput][columnInput] = 'X' if playerXTurn else 'O'
                printBoard(ticTacToeBoard)
                winner, gameIsTied = checkGameState(ticTacToeBoard)
            
            # if no winner swap turns
            if(winner == '' and not(gameIsTied)):
                playerXTurn = not(playerXTurn)
            elif(gameIsTied):
                print("This game was tied! Well done to both players")
            else:
                playerWon = 'X' if playerXTurn else 'O'
                print("Player %s won this game. \nThanks for playing!" % (playerWon))
            
        except KeyboardInterrupt:
            print("\nThanks for checking out Tic Tac Toe in Python!")
            break

    
playGame()
