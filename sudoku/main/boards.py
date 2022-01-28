import numpy as np

default_board = np.array([[0,0,0,4,6,0,0,7,1],
                          [7,0,0,0,1,8,0,0,0],
                          [0,0,6,0,7,0,0,0,0],
                          [0,0,0,0,4,0,7,3,0],
                          [0,8,0,0,0,0,2,4,0],
                          [4,2,0,0,0,9,0,0,0],
                          [0,6,8,0,9,0,0,0,4],
                          [0,0,5,6,0,0,0,1,0],
                          [0,0,2,1,0,0,0,5,0]])

def manual():
    """Manually create a sudoku grid line by line"""
    board = np.zeros((9,9),dtype=int)
    for i in range(9):
        for k,c in enumerate(input(f'Input line {i}: ').replace(' ','')):
            board[i,k]=int(c)
    return board