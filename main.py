from sudoku_utils import getEmptyLocations, printBoard 
from sudoku_solver import backtrackingSolve 
from sudoku_board_generator import generateBoard

def solve(board): 
  emptyLocations = getEmptyLocations(board) 
  backtrackingSolve(board, emptyLocations)

board = generateBoard()
print("Unsolved board:") 
printBoard(board) 
print()
print("Solving...")
solve(board)
print() 
print("Solved board:") 
printBoard(board)



