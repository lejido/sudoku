from sudoku_validity_tests import finalTest, allTests

# Backtracking algorithm 

def backtrackingSolve(board, emptyLocations):
  if (finalTest(board)):
    return 
  row = emptyLocations[0][0]
  col = emptyLocations[0][1]
  for i in range(1,10):
    board[row][col] = i
    if (allTests(board)):
      backtrackingSolve(board, emptyLocations[1:])
    if(finalTest(board)):
      return 
  board[row][col] = 0
  return 
