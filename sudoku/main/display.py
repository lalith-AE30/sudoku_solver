import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display(board):
    clear()
    for i,r in enumerate(board):
        for j,c in enumerate(r):
            if c==0:
                print(end='  ')
            else: print(c,end=' ')
            if j%3==2: print(end='| ')
        print()
        if i%3==2: print('------+-------+-------+')