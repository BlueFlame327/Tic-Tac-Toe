import time as t

def makeBoard():
  board = [" "] * 9
  return board

def printBoard(board):
  print("   0   1   2")
  print("0  {} | {} | {}".format(board[0], board[1], board[2]))
  print("  -----------")
  print("1  {} | {} | {}".format(board[3], board[4], board[5]))
  print("  -----------")
  print("2  {} | {} | {}".format(board[6], board[7], board[8]))

def getUserInput(player, board):
  print("It is player {}'s turn!".format(player))
  row = int(input("Choose a row (0, 1, or 2)  "))
  while(row < 0 or row > 2):
    t.sleep(1)
    print("That input is either less than 0 or greater than 2, or it is not a number. Please enter a number that is greater than 0 and less than 2.")
    t.sleep(1)
    row = int(input("Choose a row (0, 1, or 2)  "))
  column = int(input("Choose a column (0, 1, or 2)  "))
  while(column < 0 or column > 2):
    t.sleep(1)
    print("That input is either less than 0 or greater than 2, or it is not a number. Please enter a number that is greater than 0 and less than 2.")
    t.sleep(1)
    row = int(input("Choose a column (0, 1, or 2)  "))
  index = row * 3 + column
  if player == 1:
    board[index] = "x"
  else:
    board[index] = "o"
  return board

