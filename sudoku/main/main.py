import display
import solve
import solve_random
import boards

def main():
    solver = solve.solve
    q1 = input(
    """Choose sequence for empty cells:
    1. Sequential
    2. Shuffled
    """)
    display.clear()
    q2 = input('Display solving steps? (y/n)').upper()
    if q1==1 and q2=='Y': solver = solve.solve
    if q1==1 and q2=='N': solver = solve.solve_fast
    if q1==2 and q2=='Y': solver = solve_random.solve
    if q1==2 and q2=='N': solver = solve_random.solve_fast
    display.display(solver(boards.manual()))

    input()

if __name__=='__main__':
    main()