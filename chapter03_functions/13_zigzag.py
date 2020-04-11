import time, sys

spaceAmt = 3
increase = False
asteriskAmt = 8

def printAsterisk():
    print("*"*asteriskAmt)

try:
    while True:
        print(" " * spaceAmt, end="")
        printAsterisk() # print asterisk
        time.sleep(0.1) # Pause for 1/10 of a second.
        
        if(not increase):
            if(spaceAmt <= 0):
                # change direction:
                increase = True
            else:
                # decrease the number of spaces:
                spaceAmt -= 1
        else:
            if(spaceAmt >= 3):
                # change direction
                increase = False
            else:
                # increase the number of spaces
                spaceAmt += 1
except KeyboardInterrupt:
    sys.exit()

