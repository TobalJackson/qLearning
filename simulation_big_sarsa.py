#!/usr/bin/env python3
from pprint import pprint
import random
import os

R = [[0, 20, 10, 0, 35, 0, 0, 0, 0], 
     [0, 0, 0, 10, 35, 0, 0, 0, 0], 
     [0, 0, 0, 20, 35, 0, 0, 0, 0], 
     [0, 0, 0, 0, 35, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 20, 10, 0, 35], 
     [0, 0, 0, 0, 0, 0, 0, 10, 35], 
     [0, 0, 0, 0, 0, 0, 0, 20, 35], 
     [0, 0, 0, 0, 0, 0, 0, 0, 35], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

Q = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

actions = {0:[1, 2, 4], 
            1:[3, 4], 
            2:[3, 4], 
            3:[4], 
            4:[5, 6, 8], 
            5:[7, 8], 
            6:[7, 8], 
            7:[8], 
            8:None}

iState = 0 
randomDeath=0.0
epsilon = 0.9 
gamma = 0.8
alpha = 0.5

def getActions(state):
    if random.random() < randomDeath:
        if state != 4:
            return [8]
        else:
            return actions.get(state)
            #return [len(actions) - 1]
    else:
        return actions.get(state)

def getRewardValue(state, action):
    return R[state][action]

def getCurrentQ(state, action):
    return Q[state][action]

def updateQ(state, action):
    reward = getRewardValue(state, action)
    if action == len(actions) - 1:
        Q[state][action] = reward 
    else:
        Q[state][action] = Q[state][action] + alpha*(reward + (gamma * getCurrentQ(action, getMaxAction(action))) - Q[state][action])
    
def getMaxAction(state):
    maxQ = 0
    act = 0
    action = getActions(state)
    for a in action:
        if Q[state][a] > maxQ:
            maxQ = Q[state][a]
            act = a
    count = Q[state].count(maxQ)
    if count > 1:
        candidates = []
        for a in action:
            if Q[state][a] == maxQ:
                candidates.append(a)
        return random.choice(candidates)
    else:
        return act

def getNextAction(state, verbose=False):
    actions = getActions(state)
    candidates = []
    for a in actions:
        if Q[state][a] == 0:
            candidates.append(a)
    if len(candidates) > 0:
        if verbose:
            print("(Explore!)")
        return random.choice(candidates)
    elif random.random() < epsilon:
        if verbose:
            print("(Explore!)")
        return random.choice(getActions(state))
    else:
        return getMaxAction(state)

def runTrials(maxIt=20000, verbose=False, eps=1.0, gam=0.8, alph=1.0, ranDeath=0.4):
    global epsilon
    global gamma
    global randomDeath
    global alpha
    global Q


    newQ = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    Q = newQ
    epsilon = eps
    alpha = alph
    iterations = 0
    gamma = gam
    maxIterations = maxIt    
    randomDeath = ranDeath

    while iterations < maxIterations:
        state = iState
        if verbose:
            print("Iteration: {}\n".format(iterations))
        while state != len(actions) - 1:
            action = getNextAction(state, verbose)
            if verbose:
                print("State: {}".format(state+1))
                print("Action: {}".format(action+1))
                print("Epsilon: {}".format(epsilon))
            updateQ(state, action)
            state = action
            if verbose:
                pprint(Q)
                print()
        if verbose:
            os.system('clear')
        epsilon = 1.0 - (iterations/maxIterations)
        alpha = alpha - (alpha * (iterations/maxIterations))
        iterations = iterations + 1
    print("\nIterations: {}, Gamma: {}, randomDeath: {}".format(iterations, gamma, randomDeath))
    X = Q 
    for x in range(0, len(Q)):
        for y in range(0, len(Q[x])):
            X[x][y] = int(Q[x][y])
    state_disp = 1
    for x in X:
        print("{}: ".format(state_disp), end="")
        state_disp = state_disp + 1
        for y in x:
            print("{:4}".format(y), end = "")
        print()
    return X

def playGame(X):
    global Q

    iterations = 0
    maxIterations = 10000
    avgScore = 0
    Q = X
    pathTaken = [Q[0].index(max(Q[0]))+1, 
                Q[1].index(max(Q[1]))+1,
                Q[2].index(max(Q[2]))+1,
                Q[3].index(max(Q[3]))+1,
                Q[4].index(max(Q[4]))+1,
                Q[5].index(max(Q[5]))+1,
                Q[6].index(max(Q[6]))+1,
                Q[7].index(max(Q[7]))+1]
    while iterations < maxIterations:
        score = 0
        state = 0
        if iterations == maxIterations - 1:
            pathTaken = []
        while state != len(actions) - 1:
            action = getMaxAction(state)
            points = getRewardValue(state, action)
            score = score + points
            if iterations == maxIterations - 1:
                pathTaken.append(action + 1)
            state = action
        iterations = iterations + 1
        avgScore = avgScore + score / maxIterations
    print("Gameplay Iterations: {}\nAverage Score: {:.2f}\nPath Taken: {}".format(maxIterations, avgScore, pathTaken))


#runTrials(gam=0.1)
#runTrials(gam=0.2)
#runTrials(gam=0.5)
#runTrials(gam=0.8)
#runTrials(gam=0.85)
#runTrials(gam=0.9)
#runTrials(gam=0.95)
#runTrials(gam=0.99)
#runTrials(gam=1)


playGame(runTrials(gam=0.1))
playGame(runTrials(gam=0.5))
playGame(runTrials(gam=0.8))
playGame(runTrials(gam=0.85))
playGame(runTrials(gam=0.86))
playGame(runTrials(gam=0.9))
playGame(runTrials(gam=0.95))
playGame(runTrials(gam=0.99))
playGame(runTrials(gam=1))

