def wordsearch():
   board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
   w = "ABCCED"
   br = len(board)
   bc = len(board[0])
   visited = set()
   def ws(i, r, c):
      if(len(w) == i):
         return True
      if(r >= br    or
         c >= bc    or
         r < 0      or
         c < 0      or
         len(w) < i or
         w[i] != board[r][c] or
         (r,c) in visited
         ):
         return False

      visited.add((r,c))

      res = (ws(i + 1, r + 1, c) or
      ws(i + 1, r - 1, c) or
      ws(i + 1, r, c  + 1) or
      ws(i + 1, r, c  - 1))
      visited.remove((r,c))

      return res








   for i in range(br):
      for j in range(bc):
         if (ws(0, i, j)):
            return True

   return False



print(wordsearch())