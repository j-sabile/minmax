# Jerico Sabile

def maxValue(state, alpha, beta):
    m = float("-inf")
    for succesorState in successor(state):
        v = minValue(succesorState, alpha, beta)
        m = max(m, v)
        if v >= alpha: return m
        a = max(alpha, m)
        return m

def minValue(state, alpha ,beta):
    m = float("inf")
    for succesorState in successor(state):
        v = maxValue(succesorState, alpha, beta)
        m = min(m, v)
        if v <= beta: return m
        a = min(beta, m)
        return m

def successor(state):
    temp = []
    for i in range(len(state)):
        if state[i] != "": continue
        

def isTerminal(state):
    if state[0] == state[1] == state[2]: return winner(state[0])
    elif state[3] == state[4] == state[5]: return winner(state[3])
    elif state[6] == state[7] == state[8]: return winner(state[6])
    elif state[0] == state[3] == state[6]: return winner(state[0])
    elif state[1] == state[4] == state[7]: return winner(state[1])
    elif state[2] == state[5] == state[8]: return winner(state[2])
    elif state[0] == state[4] == state[8]: return winner(state[0])
    elif state[2] == state[4] == state[6]: return winner(state[2])
    return "No Winner"

def winner(move):
    if move == "X": return -1
    return 1   



# ! test case
# X O X
# O X O
# O O 
state = ["X","O","X","O","X","O","O","O","O"]

alpha = float("-inf")
beta = float("inf")
print(maxValue(state, alpha, beta))