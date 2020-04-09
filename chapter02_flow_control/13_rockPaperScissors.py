# This is a rock, paper, scissor game
import random
import sys

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
gameOptions = ['ROCK','PAPER',"SCISSORS"]
userKey = {'r':0,'p':1,'s':2}
# print(userKey['p'])

# prompt player for his move and track the progress
# stop playing when the player says so
while True:
    print('%i Wins, %i Losses, %i Ties' % (wins, losses, ties))
    print('Enter your move: (r)ock (p)aper (s)cissers or (q)uit')         
    playerMove = input()
    if playerMove == 'q':
        sys.exit()
    elif playerMove != "r" and playerMove != "p" and playerMove != "s":
        print('Please enter a valid move.')
        continue
    playerMoveIndex = userKey[playerMove]
    npcThrows = random.randint(0,2)
    print('%s versus...\n%s'
        % (gameOptions[playerMoveIndex],gameOptions[npcThrows]))
    # check fo tied game
    if playerMoveIndex == npcThrows:
        print('It is a tie!')
        ties += 1
        continue
    # check for if player is playing paper or scissors
    elif playerMoveIndex >= 1:
        # since 0 rock 1 paper 2 scissors
        # 1 below always wins 1 paper beats 0 rock | 2 scissors beats 1 paper
        # else you've lost 1 paper losses 2 rock | 2 scissors loses to 0 rock
        if playerMoveIndex - 1 == npcThrows:
            print('You win!')
            wins += 1
            continue
        else:
            print('You lose!')
            losses += 1
            continue
    # if not paper or scissors, then player threw rock
    # if npc threw paper player losses, else player wins
    else:
        if npcThrows == 1:
            print('You lose!')
            losses += 1
            continue
        else:
            print('You win!')
            wins += 1
            continue
