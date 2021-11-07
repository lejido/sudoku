# Print board 
def printBoard(board): 
  for i in board: 
    print(i)

# Get locations of empty "coordinates" 
def getEmptyLocations(board): 
  locations = [] 
  for i in range(9): 
    for j in range(9): 
      if (board[i][j]==0): 
        locations.append([i,j])
  return locations

# Is board completely filled 
def filled(board):
  count = 0
  for i in board:
    for j in range(len(i)):
      if (i[j]!=0):
        count = count+1
  return (count==81)


