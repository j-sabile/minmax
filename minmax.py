# Jerico Sabile


import tkinter as Tkinter
import random


MIN = "min"
MAX = "max"
X = "X"
O = "O"
E = ""
FONT = ("Arial",15)
TILESIZE = 4


def value(state, alpha, beta, type):
    value = isTerminal(state)
    if value == True: return 0
    elif (value == X and type == MIN) or (value == O and type == MIN): return 1
    elif (value == X and type == MAX) or (value == O and type == MAX): return -1
    elif type == MAX: return maxValue(state, alpha, beta)
    elif type == MIN: return minValue(state, alpha, beta)

def getAiMove(state):
    alpha = float("-inf")
    beta = float("inf")
    m = float("-inf")
    bestState = state
    for succesorState in successor(state, getMove(MAX)):
        v = value(succesorState, alpha, beta, MIN)
        if v > m:
            m = v
            bestState = succesorState
        if v >= beta: return succesorState
        alpha = max(alpha, m)
    return bestState

def maxValue(state, alpha, beta):
    m = float("-inf")
    for succesorState in successor(state, getMove(MAX)):
        v = value(succesorState, alpha, beta, MIN)
        m = max(m, v)
        if v >= beta: return m
        alpha = max(alpha, m)
    return m

def minValue(state, alpha ,beta):
    m = float("inf")
    for succesorState in successor(state, getMove(MIN)):
        v = value(succesorState, alpha, beta, MAX)
        m = min(m, v)
        if v <= alpha: return m
        beta = min(beta, m)
    return m

def successor(state, move):
    temp = []
    for i in range(len(state)):
        if state[i] != E: continue
        newTemp = state.copy()
        newTemp[i] = move
        temp.append(newTemp)
    return temp

def isTerminal(state):
    if state[0] != E and state[0] == state[1] == state[2]: return state[0]
    elif state[3] != E and state[3] == state[4] == state[5]: return state[3]
    elif state[6] != E and state[6] == state[7] == state[8]: return state[6]
    elif state[0] != E and state[0] == state[3] == state[6]: return state[0]
    elif state[1] != E and state[1] == state[4] == state[7]: return state[1]
    elif state[2] != E and state[2] == state[5] == state[8]: return state[2]
    elif state[0] != E and state[0] == state[4] == state[8]: return state[0]
    elif state[2] != E and state[2] == state[4] == state[6]: return state[2]
    elif state[0] != E and state[1] != E and state[2] != E and state[3] != E and state[4] != E and state[5] != E and state[6] != E and state[7] != E and state[8] != E: return True
    return False


def getMove(type):
    if (type == MAX and isAIFirstMove) or (type == MIN and not isAIFirstMove): return X
    elif (type == MAX and not isAIFirstMove) or (type == MIN and isAIFirstMove): return O


def printboard(board):
    for i in range(3):
        for j in range(3):
            print((f"{board[i*3+j]}\t").expandtabs(3), end="")
        print()

def loadGame():
    buttons[0] = Tkinter.Button(frame, text=puzzle[0], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(0))
    buttons[0].grid(row=0//3,column=0%3, sticky=Tkinter.NSEW)
    buttons[1] = Tkinter.Button(frame, text=puzzle[1], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(1))
    buttons[1].grid(row=1//3,column=1%3, sticky=Tkinter.NSEW)
    buttons[2] = Tkinter.Button(frame, text=puzzle[2], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(2))
    buttons[2].grid(row=2//3,column=2%3, sticky=Tkinter.NSEW)
    buttons[3] = Tkinter.Button(frame, text=puzzle[3], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(3))
    buttons[3].grid(row=3//3,column=3%3, sticky=Tkinter.NSEW)
    buttons[4] = Tkinter.Button(frame, text=puzzle[4], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(4))
    buttons[4].grid(row=4//3,column=4%3, sticky=Tkinter.NSEW)
    buttons[5] = Tkinter.Button(frame, text=puzzle[5], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(5))
    buttons[5].grid(row=5//3,column=5%3, sticky=Tkinter.NSEW)
    buttons[6] = Tkinter.Button(frame, text=puzzle[6], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(6))
    buttons[6].grid(row=6//3,column=6%3, sticky=Tkinter.NSEW)
    buttons[7] = Tkinter.Button(frame, text=puzzle[7], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(7))
    buttons[7].grid(row=7//3,column=7%3, sticky=Tkinter.NSEW)
    buttons[8] = Tkinter.Button(frame, text=puzzle[8], font=FONT, width=2*TILESIZE, height=TILESIZE, command=lambda:clickCell(8))
    buttons[8].grid(row=8//3,column=8%3, sticky=Tkinter.NSEW)

def clickCell(cellNum):
    global puzzle
    puzzle[cellNum] = getMove(MIN)
    if isFinished(): return 
    AITurn()

def AITurn():
    global puzzle
    puzzle = getAiMove(puzzle)
    if isFinished(): return 
    for i in range(9): 
        if puzzle[i] != E: buttons[i].config(text=puzzle[i], state=Tkinter.DISABLED)
        else: buttons[i].config(text=puzzle[i])

def isFinished():
    winner = isTerminal(puzzle)
    print(winner)
    if not winner: return
    if (winner == O and isAIFirstMove) or (winner == X and not isAIFirstMove): winner = "Congratulations! You have beaten the AI in Tic Tac Toe."
    elif (winner == X and isAIFirstMove) or (winner == O and not isAIFirstMove): winner = "Oops! The AI has won this time." 
    else: winner = "It's a tie! Great job holding your ground against the AI!"
    status.config(text=winner)
    for i in buttons: i.config(state=Tkinter.DISABLED)

buttons = [None, None, None, None, None, None, None, None, None]

# GUI
root = Tkinter.Tk()
root.title("Tic Tac Toe")
frame = Tkinter.Frame(root)
frame.pack()
status = Tkinter.Label(root)
status.pack()

puzzle = [E,E,E,E,E,E,E,E,E]
loadGame()
isAIFirstMove = random.randint(0,1) == 0
if isAIFirstMove: AITurn()

root.mainloop()
