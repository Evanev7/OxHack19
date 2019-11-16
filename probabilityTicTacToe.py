import random

grid_x = 15
grid_y = 15

global true_zeros = [[False for i in range(grid_y)] for j in range(grid_x)]
global true_zeros_list = []
global false_zeros = [[False for i in range(grid_y)] for j in range(grid_x)]
global false_zeros_list = []
global true_crosses = [[False for i in range(grid_y)] for j in range(grid_x)]
global true_crosses_list = []
global false_crosses = [[False for i in range(grid_y)] for j in range(grid_x)]
global false_crosses_list = []

def newProbabilityDist (x, y):
    return [[random.randrange(0, 9) for i in range(x)] for j in range(y)]

probability_dist = newProbabilityDist(grid_x, grid_y)

def drawZero (x, y):
    if true_zeros[x][y]:
        return "O"
    elif false_zeros[x][y]:
        return "o"
    else:
        return "_"

def drawCross (x, y):
    if true_crosses[x][y]:
        return "X"
    elif false_crosses[x][y]:
        return "x"
    else:
        return "_"

def drawGrid():
    for i in range(15):
        line = ""
        for j in range(15):
            line += ("|(" + drawCross(i, j, true_crosses, false_crosses ) + " " + drawZero(i, j, true_zeros, false_zeros ) + " " + str(probability_dist[i][j]) + ")|")
        print(line)
        print("_"*135)
        
def zerosTurn():
    probs = []
    for zero in true_zeros:
        probs += probability_dist[zero.first][zero.second]
    s = sum (probs)
    p.map(lambda x : x / s)
    next_zero = choice(true_zeros, 1, p = probs)[0]
    num, true_zeros_list, false_zeros_list = getZerosInput()
    
        
drawGrid(true_zeros, false_zeros, true_crosses, false_crosses, probability_dist)
