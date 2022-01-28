import numpy
import display
import copy

def isSafe(b,r,c,n):
    """Check if number is safe to place at given position."""
    if (b[:,c]==n).sum():
        return False
    if (b[r,:]==n).sum():
        return False
    if (b[3*(r//3):3*(r//3)+3,3*(c//3):3*(c//3)+3]==n).sum():
        return False
    return True

def empty_cells(board):
    """Return an array with position and possible numbers."""
    empty_cells = []
    for r,rv in enumerate(board):
        for c,cv in enumerate(rv):
            if cv==0:
                empty_cells.append((r,c,[n for n in range(1,10) if isSafe(board,r,c,n)]))
    empty_cells = numpy.array(empty_cells,dtype=object)
    return empty_cells

def solve(board):
    """Solve board sequentially"""
    empty = empty_cells(board)
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
        display.display(board)
        
        if (numpy.array([len(x[2]) for x in empty_cells(board)])==0).sum():
            continue
        
        i+=1
    return board


def solve_fast(board):
    """Solve board without displaying in-between steps."""
    empty = empty_cells(board)
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
