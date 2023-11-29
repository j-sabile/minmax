minmax

utility - value of the current game state (0s or 1s)

zero sum games - sum of utilities is 0

upward tri - max
downwr tri - min
rectangles - terminals/utitlities

alpha - lower bound
beta  - upper bound

a = -inf
b =  inf

def maxValue(s,a,b):
    m = -inf
    for a, s in succ(s):
        v = values(s,a,b)
        m = max(m,v)
        if v >= B: return m
        a = max(A,m)
        return m


states = [None*9]
       = ["X", "0", None]

functions:
isTerminal(state)
successor(state)
maxValue(s,a,b)
minValue(s,a,b)



