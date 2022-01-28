
# Sudoku solver

This project implements the brute force search for solving a sudoku puzzle. It has two
different orderings for the empty cells; a sequential ordering and a shuffled ordering.

The sequential ordering has cells filled row by row which can be seen when it is solving.
It solves a board in 2 min on average

The shuffled ordering, as the name suggests shuffles the order of the empty cells which get filled.
Though the puzzle will still be solved if it can be solved sequentially, it is much slower (it can
take hours when compared to the sequential ordering which completes in about 2 min on average).

This suggests that the sequential ordering has additional features which make it faster,
I am not sure what it is (probably something to do with it filling rows), but there certainly
a difference in performance between the methods.



## Usage

Install dependencies by running
```pip install -r requirements.txt```
from the root directory.

Run the program by running
```
cd main
py main.py
```

## References

Wikpedia: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking
