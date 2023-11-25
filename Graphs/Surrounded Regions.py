def answer():
   board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
   def dfs(r, c):
      if(r < 0 or c < 0 or
         r >= len(board) or c >= len(board) or
         board[r][c] == "X"
        ):
         return
      board[r][c] = "T"
      directions = [(1, 0), (0, -1), (0, 1), (0, -1)]
      for row_moment,column_moment in directions:
         dfs(r + row_moment, c + column_moment)

   #1. capture unsurrounded. DFS Change it to T.
   for r in range(len(board)):
      for c in range(len(board[0])):
         if (r == 0 or r == len(board) - 1 or
             c == 0 or c == len(board) - 1 or
             board[r][c] == "X"):
            dfs(r, c)

   #2. capture surrounded.
   for r in range(len(board)):
      for c in range(len(board[0])):
         if(board[r][c] == 'O'):
            board[r][c] = 'X'
   #3. capture unsurrounded T to 0
   for r in range(len(board)):
      for c in range(len(board[0])):
         if(board[r][c] == 'T'):
            board[r][c] = 'O'
   print(board)





answer()