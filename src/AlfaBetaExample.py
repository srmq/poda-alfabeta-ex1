'''
Created on Mar 8, 2019

@author: Sergio Queiroz <srmq@cin.ufpe.br>
'''
from enum import Enum
import sys

termStateValues = {'c' : 10, 'd' : 6, 'f' : 100, 'g' : 8, 
                   'j' : 1, 'k' : 2, 'm' : 20, 'n' : 4, 
                   'p' : 100, 'q' : 150, 'r' : 120}

MinimaxType = Enum('MinimaxType', 'MAX MIN')

BIG_NUM = sys.maxsize//2 - 1

actionsForState = dict.fromkeys(['init', 'a', 'b', 'e', 'l', 'i'], ['Left', 'Right'])
actionsForState.update(dict.fromkeys(['h', 'o'], ['Left', 'Middle', 'Right']))

def resultado(state, action):
    resultMap = {('init', 'Left') : 'a', ('init', 'Right') : 'h',
                 ('a', 'Left') : 'b', ('a', 'Right') : 'e',
                 ('h', 'Left') : 'l', ('h', 'Middle') : 'i', ('h', 'Right') : 'o',
                 ('b', 'Left') : 'c', ('b', 'Right') : 'd',
                 ('e', 'Left') : 'f', ('e', 'Right') : 'g',
                 ('l', 'Left') : 'm', ('l', 'Right') : 'n',
                 ('i', 'Left') : 'j', ('i', 'Right') : 'k',
                 ('o', 'Left') : 'p', ('o', 'Middle') : 'q', ('o', 'Right') : 'r'}
    return resultMap[(state, action)]


def isTerminal(state):
    return state in termStateValues

def minimax(state, stateType, alpha = -BIG_NUM, beta = BIG_NUM):
    if isTerminal(state):
        return termStateValues[state]
    if stateType == MinimaxType.MAX:
        return maxValue(state, alpha, beta)
    elif stateType == MinimaxType.MIN:
        return minValue(state, alpha, beta)
    
def maxValue(state, alpha, beta):
    v = -BIG_NUM
    successors = map(lambda action : resultado(state, action), actionsForState[state])
    for s in successors:
        v = max(v, minimax(s, MinimaxType.MIN, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minValue(state, alpha, beta):
    v = BIG_NUM
    successors = map(lambda action : resultado(state, action), actionsForState[state])
    for s in successors:
        v = min(v, minimax(s, MinimaxType.MAX, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v

    

print(minimax('init', MinimaxType.MAX))
