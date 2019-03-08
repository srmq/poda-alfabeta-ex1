'''
Created on Mar 7, 2019

@author: Sergio Queiroz <srmq@cin.ufpe.br>
'''
from enum import Enum
import sys

termStateValues = {'c' : 10, 'd' : 6, 'f' : 100, 'g' : 8, 
                   'j' : 1, 'k' : 2, 'm' : 20, 'n' : 4}

MinimaxType = Enum('MinimaxType', 'MAX MIN')

BIG_NUM = sys.maxsize//2 - 1

def isTerminal(state):
    return state in termStateValues

def resultadosAcoes(state):
    resultsByState = {'init' : ['a', 'h'], 
                   'a' : ['b', 'e'], 
                   'h' : ['i', 'l'], 
                   'b' : ['c', 'd'], 
                   'e' : ['f', 'g'],
                   'i' : ['j', 'k'],
                   'l' : ['m', 'n']}
    if isTerminal(state):
        return [];
    else:
        return resultsByState[state]

def minimax(state, stateType):
    if isTerminal(state):
        return termStateValues[state]
    if stateType == MinimaxType.MAX:
        return maxValue(state)
    elif stateType == MinimaxType.MIN:
        return minValue(state)
    
def maxValue(state):
    v = -BIG_NUM
    successors = resultadosAcoes(state)
    for s in successors:
        v = max(v, minimax(s, MinimaxType.MIN))
    return v

def minValue(state):
    v = BIG_NUM
    successors = resultadosAcoes(state)
    for s in successors:
        v = min(v, minimax(s, MinimaxType.MAX))
    return v

    

print(minimax('init', MinimaxType.MAX))
