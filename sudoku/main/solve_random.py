from solve import isSafe,empty_cells
from display import display
import copy
import numpy

def solve(board):
    """Solve board with random sequence of empty cells"""
    empty = empty_cells(board)
    numpy.random.shuffle(empty)
    bempty = copy.deepcopy(empty)
    i=0
    while i<len(empty):
        r,c = empty[i,:2]

        if len(empty[i,2])==0:
            board[r,c]=0
            empty[i:]=copy.deepcopy(bempty[i:])
            i-=1
            continue

        cur = empty[i,2].pop()
        if not isSafe(board,r,c,cur):
            continue
        board[r,c]=cur
        display(board)
        
        if (numpy.array([len(x[2]) for x in empty_cells(board)])==0).sum():
            continue
        
        i+=1
    return board


def solve_fast(board):
    """Solve board with shuffled cells without displaying in-between steps."""
    empty = empty_cells(board)
    numpy.random.shuffle(empty)
    bempty = empty_cells(board)
    i=0
    while i<len(empty):
        r,c = empty[i,:2]

        if len(empty[i,2])==0:
            board[r,c]=0
            empty[i:]=copy.deepcopy(bempty[i:])
            i-=1
            continue

        cur = empty[i,2].pop()
        if not isSafe(board,r,c,cur):
            continue
        board[r,c]=cur

        i+=1
    return board