matrix = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
]

def matrix():
   matrix = [
      [0, 0, 1],
      [0, 0, 1],
      [0, 0, 0]
   ]
   matrix_r = len(matrix)
   matrix_c = len(matrix[0])
   visited = set()
   def dfs(r,c):
      if(r<0 or c<0 or
         r>= matrix_r or c>= matrix_c or
         matrix[r][c] !=0 or
            (r,c) in visited):
         return 0
      if(r == matrix_r - 1 and c == matrix_c - 1):
         return 1
      visited.add((r,c))
      count = 0

      count += dfs(r+1,c)
      count += dfs(r-1,c)
      count += dfs(r  ,c+1)
      count += dfs(r  ,c-1)

      visited.pop()
      return count


   return (dfs(0,0))

print(matrix())