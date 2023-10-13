import collections
def sudoku():
   board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


   r = collections.defaultdict(set)
   c = collections.defaultdict(set)
   s = collections.defaultdict(set)

   for i in range(0,9):
      for j in range(0,9):
         if(board[i][j] == '.'):
            continue
         if(board[i][j] in r[i] or
            board[i][j] in c[j] or
            board[i][j] in s[(i//3,j//3)]):
            print("invalid")
            return False
         else:
            r[i].add(  board[i][j])
            c[j].add(  board[i][j])
            s[i//3,j//3].add( board[i][j])
   print("true")
   return True


sudoku()