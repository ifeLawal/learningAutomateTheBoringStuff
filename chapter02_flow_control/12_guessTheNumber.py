# This is a guess the number game.
import random
import sys

numGuesses = 0
theRandomNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# We're asking the player to keep guessing until they get the number
while True:
    print('Take a guess.')
    guess = int(input())
    numGuesses += 1
    if guess == theRandomNum:
        if numGuesses == 1:
            print('Good job! You guessed my number in 1 guess!')
        else:
            print('Good job! You guessed my number in %i guesses!' % numGuesses)
        sys.exit()
    elif guess < theRandomNum:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')

