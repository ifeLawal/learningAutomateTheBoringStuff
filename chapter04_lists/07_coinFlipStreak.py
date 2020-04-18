# create a six heads or six tails checker
# part 1 create a list of 100 coin flips
# part 2 check if there is a streak of six heads or tails
# part 3 repeat experiment 10,000 times and spit out the percent of random coin flips with a streak
# optional part 4 consider optimizing six heads or tails checker code

import sys, random, time
headsOrTails = ['H', 'T']

def createListandReturnIfStreak():
    coinFlipList = []
    # create a list of 100 coin flips
    for i in range(100):
        flippedCoin = headsOrTails[random.randint(0, 1)]
        coinFlipList.append(flippedCoin)
    
    # count number of streaks
    streakCount = 0
    for i in range(99):
        if(coinFlipList[i] == coinFlipList[i+1]):
            streakCount += 1
        else:
            streakCount = 0
        if streakCount >= 6:
            return True
    return False

# run the 100 heads experiment as many times as passed
# return the percent of streaks
def calcPercentStreaks(amtExperimentRuns):
    amtStreaks = 0
    for i in range(amtExperimentRuns):
        if(createListandReturnIfStreak()):
            amtStreaks += 1
    return float(amtStreaks) / float(amtExperimentRuns)

print(calcPercentStreaks(10))