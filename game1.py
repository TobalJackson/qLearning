#!/usr/bin/env python3
import os

choices = ['A', 'B', 'C']
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

    print("\nLives Left: {} ...\nChoose!:".format(turns))
    print(choices)
    var = input()

    os.system('clear')
    getPoints(var)
    printScore()

    if var in ('B', 'b'):
        state = False


def getPoints(x):
    global score
    global choices
    
    if x in ('A', 'a'):
        score = score + 10
        print("Score: +10")
    if x in ('B', 'b'):
        score = score + 30
        print("Score: +30")
    if x in ('C', 'c'):
        score = score + 20
        print("Score: +20")

    choices.remove(x.upper())


def printScore():
    print("Total Score: {}".format(score))



while(turns > 0):
    while(state == True):
        runGame()
    turns = turns - 1
    state = True
    choices = ['A', 'B', 'C']
    if turns != 0:
        print("\nYou've died! Use what you've learned to achieve a higher score!")
    else:
        print("GAME OVER")
