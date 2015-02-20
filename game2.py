#!/usr/bin/env python3
import os

choices = ['A', 'B', 'C', 'D', 'E']
state = True
global score 
score = 0
global turns
turns = 2
os.system('clear')
print("Score: 0 \nTotal Score: 0")
def runGame():
    global state
    global turns
    print("\nTurns Left: {} ...\nChoose!:".format(turns))
    print(choices)
    var = input()

    os.system('clear')
    getPoints(var)
    printScore()

    if var == 'B':
        state = False


def getPoints(x):
    global score
    global choices
    
    if x == 'A':
        score = score + 10
        print("Score: +10")
    if x == 'B':
        score = score + 30
        print("Score: +30")
    if x == 'C':
        score = score + 20
        print("Score: +20")
    if x == 'D':
        if len(choices) <= 2:
            score = score + 100
            print("REWARD! Score: +100!")
        else:
            score = score - 100
            print("PAIN! Too many choices left... Score: -100")
    if x == 'E':
        score = score + 50
        print("Score: +50")

    choices.remove(x)



def printScore():
    print("Total Score: {}".format(score))



while(turns > 0):
    while(state == True):
        runGame()
    turns = turns - 1
    state = True
    choices = ['A', 'B', 'C', 'D', 'E']
    if turns != 0:
        print("\nYou've died! Use what you've learned to achieve a higher score!")
    else:
        print("GAME OVER")
