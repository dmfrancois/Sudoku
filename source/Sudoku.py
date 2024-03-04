import math
import time

board = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],

    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],

    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,0,0,0,5]
]

board2 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(board):
    # Cell size
    size = math.sqrt(len(board))
    for i in range(len(board)):
        if i % size == 0 and i != 0: print("---------------------")
        letters = []
        for j in range(len(board[0])):
            if j != 0 and j % size == 0:
                letters.append("|")
            letters.append(str(board[i][j]))
        print(" ".join(letters))


def isValid(board, r, c, e):

    # Cell size
    size = math.sqrt(9)

    not_in_row = e not in board[r]
    not_in_column = e not in [board[i][c] for i in range(len(board))]
    not_in_cell = e not in [board[i][j] for i in range(int(r//size*size), int(r//size*size+size)) for j in range(int(c//size*size), int(c//size*size+size))]

    return not_in_row and not_in_column and not_in_cell

def solve(board, r=0, c=0):
    if r==len(board):
        return True
    elif c==len(board):
        return solve(board, r+1, 0)
    elif board[r][c] != 0:
        return solve(board, r, c+1)
    else:
        for k in range(1, 10):
            if isValid(board, r, c, k):
                board[r][c] = k
                if solve(board, r, c+1):
                    return True
                board[r][c] = 0
        return False

printBoard(board2)
start = time.time()
solve(board2)
print("\nTime to solve: " + str(time.time()-start))
printBoard(board2)









