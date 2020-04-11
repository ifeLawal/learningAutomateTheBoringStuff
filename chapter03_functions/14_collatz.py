import time

def collatz(number):
    if number % 2 == 0:
        # if number is even
        print(number // 2)
        # return the floor division aka divide and cut off decimal nunbers
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    print('Enter number:')
    userNum = int(input())
    while userNum != 1:
        userNum = collatz(userNum)
        time.sleep(0.1) # pause for 1/10 of a second

except ValueError:
    print('Type in a valid number')