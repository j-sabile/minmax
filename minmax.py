# Jerico Sabile

MIN = "min"
MAX = "max"
X = "X"
O = "O"
isAIFirstMove = True

def value(state, alpha, beta, type):
    print("IN VALUE", state)
    value = isTerminal(state)
    if value == True: return 0
    elif (value == X and type == MIN) or (value == O and type == MAX): return 1
    elif (value == X and type == MAX) or (value == O and type == MIN): return -1
    elif type == MAX: return maxValue(state, alpha, beta)
    elif type == MIN: return minValue(state, alpha, beta)

def maxValue(state, alpha, beta):
    print("IN MAX VALUE", state, alpha, beta)
    m = float("-inf")
    for succesorState in successor(state, getMove(MAX)):
        v = value(succesorState, alpha, beta, MIN)
        m = max(m, v)
        if v >= beta: return m
        alpha = max(alpha, m)
        print("RETURNING m =", m)
    return m

def minValue(state, alpha ,beta):
    print("IN MIN VALUE", state)
    m = float("inf")
    for succesorState in successor(state, getMove(MIN)):
        v = value(succesorState, alpha, beta, MAX)
        m = min(m, v)
        if v <= alpha: return m
        beta = min(beta, m)
        print("RETURNING m =", m)
    return m

def successor(state, move):
    print("IN SUCCESSOR")
    temp = []
    for i in range(len(state)):
        if state[i] != "": continue
        newTemp = state.copy()
        newTemp[i] = move
        temp.append(newTemp)
    print("RETURNING", temp)
    return temp

def isTerminal(state):
    if state[0] == state[1] == state[2]: return state[0]
    elif state[3] == state[4] == state[5]: return state[3]
    elif state[6] == state[7] == state[8]: return state[6]
    elif state[0] == state[3] == state[6]: return state[0]
    elif state[1] == state[4] == state[7]: return state[1]
    elif state[2] == state[5] == state[8]: return state[2]
    elif state[0] == state[4] == state[8]: return state[0]
    elif state[2] == state[4] == state[6]: return state[2]
    elif state[0] != "" and state[1] != "" and state[2] != "" and state[3] != "" and state[4] != "" and state[5] != "" and state[6] != "" and state[7] != "" and state[8] != "": return True
    return False

def winner(move):
    if move == X: return -1
    return 1   

def getMove(type):
    if (type == MAX and isAIFirstMove) or (type == MIN and not isAIFirstMove): return X
    elif (type == MAX and not isAIFirstMove) or (type == MIN and isAIFirstMove): return O


alpha = float("-inf")
beta = float("inf")

# ! test case
# X X O
# O O 
# X O X
state = [X,"",O,"",O,"",X,O,X]
print(maxValue(state, alpha, beta))
