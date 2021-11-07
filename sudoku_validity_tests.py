from sudoku_utils import filled

# Rows validity 
def rowsTest(board):
  for i in board:
    l = [j for j in i if j!=0];
    if (not (len(l)==len(set(l)))):
      return False
  return True

# Columns validity 
def columnsTest(board):
  for i in range(9):
    l = []
    for j in board:
      if (j[i]!=0):
        l.append(j[i])
    if (not (len(l)==len(set(l)))):
      return False
  return True

# Squares validity 
def squaresTestHelper(board, x,y):
  l = []
  for i in range(x-3, x):
    for j in range(y-3, y):
      if (board[i][j]!=0):
        l.append(board[i][j])
  return (len(l)==len(set(l)))

def squaresTest(board):
  val = True
  for i in range(0,9,3):
    for j in range(0,9,3):
      if (not squaresTestHelper(board, i,j)):
        return False;
  return True;

# All validity tests 
def allTests(board):
  return (squaresTest(board) and rowsTest(board) and columnsTest(board))

# Final test (completely filled board + all tests passed) 
def finalTest(board):
  return (filled(board) and allTests(board))
